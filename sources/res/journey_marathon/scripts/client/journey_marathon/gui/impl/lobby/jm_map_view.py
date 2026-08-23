from __future__ import absolute_import
import logging, typing
from items.components.c11n_constants import Rarity
from shared_utils import findFirst, first
from frameworks.wulf import Array, ViewFlags, ViewSettings, WindowFlags, WindowStatus
from frameworks.wulf.view.array import fillStringsArray
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.collection.collections_helpers import composeBonuses
from gui.impl.backport import BackportTooltipWindow
from gui.impl.gen import R
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.pub import ViewImpl, WindowImpl
from gui.shared.event_dispatcher import showVehicleHubOverview
from gui.shared.gui_items import getItemTypeID
from gui.shared.utils.decorators import adisp_process
from helpers import dependency
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.impl import IGuiLoader
from journey_marathon.gui.impl.lobby.jm_lsm_states import JmMapState
from journey_marathon.gui.impl.lobby.tooltips.jm_key_tooltip_view import JmKeyTooltipView
from journey_marathon.gui.impl.lobby.tooltips.jm_locked_tooltip_view import JmLockedTooltipView
from journey_marathon.gui.impl.lobby.tooltips.jm_lore_tooltip_view import JmLoreTooltipView
from journey_marathon.gui.impl.lobby.tooltips.jm_rewards_tooltip_view import JmRewardsTooltipView
from journey_marathon.gui.shared.bonus_packers import getJMBonusPacker
from journey_marathon.gui.impl.lobby.attachement_reward import AttachmentRewardWindow
from journey_marathon.gui.impl.lobby.jm_final_reward_view import JmFinalRewardWindow
from journey_marathon.gui.sounds_constants import JM_MAP_SOUND_SPACE
from journey_marathon.jm_helpers.jm_account_settings import getJmLoreNodeShown, updateJmLoreNodeShown
from journey_marathon.gui.shared.jm_event_dispatcher import openJmShop, showCustomizationRarityAwardScreen, showLoreOverlay, showVehicleRewardScreen
from journey_marathon.gui.shared.processors import OpenJMNodesProcessor
from journey_marathon.jm_constants import JM_MAP_TOKENS_UPD_TYPES, JM_MAP_VIEW_DISABLED_FT_STATES, JM_MAP_VIEW_DISABLED_TIME_STATES, JM_NODE_PATHS_UPD_TYPES, JM_NODES_UPD_TYPES, JM_TIME_UPD_TYPES, JmNodesUpdType, JmTimeUpdType, JmTokensUpdType
from journey_marathon.jm_helpers import JmCurrNodeMover, getJmQuestsCompleteAnimShown, jmCtrl, makeJmMapViewQuestsProgressGetter, packJmPopover, setJmMapViewOpened, setJmMapViewQuestsProgress, setJmQuestsCompleteAnimShown
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_map_view_model import JmMapViewModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_model import JmNodeModel, NodeType
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_quest_card_model import JmQuestCardModel
from journey_marathon.skeletons.game_control import IJourneyMarathonController
if typing.TYPE_CHECKING:
    from typing import Any, Dict, Optional
    from journey_marathon.gui.game_control.jm_components import JmNodes, JmNode
    from journey_marathon.jm_constants import JmTokensUpdTypes, JmNodesUpdTypes, JmTimeUpdTypes
    TCommandArgs = Dict[(str, Any)]
    TBonusCache = Dict[(str, Any)]
_logger = logging.getLogger(__name__)

class JmMapWindow(WindowImpl):

    def __init__(self, layer, **__):
        super(JmMapWindow, self).__init__(content=JmMapView(), wndFlags=WindowFlags.WINDOW, layer=layer)


class JmMapView(ViewImpl):
    jmCtrl = dependency.descriptor(IJourneyMarathonController)
    __gui = dependency.descriptor(IGuiLoader)
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.map_view()
    _COMMON_SOUND_SPACE = JM_MAP_SOUND_SPACE

    def __init__(self, *args, **kwargs):
        super(JmMapView, self).__init__(ViewSettings(layoutID=self.LAYOUT_ID, flags=ViewFlags.VIEW, model=JmMapViewModel(), args=args, kwargs=kwargs))
        self.__bonusCache = {}
        self.__isNodeUpdateBlocked = False
        self.__pendingRewardWindowTypes = []
        self.__popoverNodeId = None
        self.__lastInterruptedNodeID = None
        self.__currNodeMover = JmCurrNodeMover()
        self.__popoverTooltips = {}
        self.__nodeTooltips = {}
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def _finalize(self):
        self.__bonusCache.clear()
        self.__isNodeUpdateBlocked = False
        if self.__pendingRewardWindowTypes:
            self.__gui.windowsManager.onWindowStatusChanged -= self.__onWindowStatusChanged
            del self.__pendingRewardWindowTypes[:]
        self.__popoverNodeId = None
        self.__lastInterruptedNodeID = None
        self.__currNodeMover.fini()
        self.__popoverTooltips.clear()
        self.__nodeTooltips.clear()
        self.jmCtrl.jmSysMessages.pushJmAnimPending()
        super(JmMapView, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        super(JmMapView, self)._onLoading(*args, **kwargs)
        self.__currNodeMover.init(self.viewModel)
        self.__updateAll()

    def _onShown(self):
        super(JmMapView, self)._onShown()
        setJmMapViewOpened()

    def createToolTip(self, event):
        if event.contentID != R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            return super(JmMapView, self).createToolTip(event)
        else:
            nodeId = event.getArgument('nodeId', None)
            tooltipId = event.getArgument('tooltipId', None)
            if nodeId is not None:
                tooltipData = self.__nodeTooltips.get(nodeId, {}).get(tooltipId)
            else:
                tooltipData = self.__popoverTooltips.get(tooltipId)
            if tooltipData is None:
                return
            window = BackportTooltipWindow(tooltipData, self.getParentWindow(), event)
            if window is None or window.windowStatus != WindowStatus.CREATED:
                return
            window.load()
            return window

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.journey_marathon.mono.lobby.tooltips.key_tooltip():
            return JmKeyTooltipView(event.getArgument('keyName', ''))
        else:
            if contentID in (
             JmLockedTooltipView.LAYOUT_ID,
             JmLoreTooltipView.LAYOUT_ID,
             JmRewardsTooltipView.LAYOUT_ID):
                nodeId = event.getArgument('nodeId')
                node = self.jmCtrl.jmNodes.getJmNodes().get(nodeId)
                if node is None:
                    _logger.error('Invalid nodeId when opening tooltip, nodeId=%s', nodeId)
                else:
                    if contentID == JmLockedTooltipView.LAYOUT_ID:
                        return JmLockedTooltipView(node)
                    if contentID == JmLoreTooltipView.LAYOUT_ID:
                        return JmLoreTooltipView(node)
                    if contentID == JmRewardsTooltipView.LAYOUT_ID:
                        nodeModel = findFirst(lambda n: n.getId() == nodeId, self.viewModel.getNodes(), None)
                        if nodeModel is not None:
                            return JmRewardsTooltipView(nodeModel.getBonuses())
            return super(JmMapView, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        ctrl = self.jmCtrl
        model = self.viewModel
        return (
         (
          ctrl.onJmFeatureStateChange, _onDisabledCloseView),
         (
          ctrl.onJmNodesChange, self.__updateNodes),
         (
          ctrl.onJmQuestsChange, self.__updateQuests),
         (
          ctrl.onJmTokensChange, self.__updateTokens),
         (
          ctrl.onJmTimeChange, self.__updateTime),
         (
          ctrl.onJmConfigChange, self.__onJmConfigChange),
         (
          ctrl.onJmConfigErrors, _onDisabledCloseView),
         (
          model.onExplore, self.__onExplore),
         (
          model.onInterruptForScreenShow, self.__onInterruptForScreenShow),
         (
          model.onExploreAnimationFinished, self.__onExploreAnimationFinished),
         (
          model.onQuestProgressShown, self.__onQuestProgressShown),
         (
          model.onQuestCompletedShown, self.__onQuestCompletedShown),
         (
          model.onSelectNode, self.__onSelectNode),
         (
          model.onChangeCurrentNode, self.__onChangeCurrentNode),
         (
          model.onCurrentNodeSynced, self.__onCurrentNodeSynced),
         (
          model.onPreviewLore, self.__onPreviewShow),
         (
          model.onRewardPreview, self.__onRewardPreview),
         (
          model.onBannerOpen, openJmShop))

    def __updateAll(self):
        with self.getViewModel().transaction() as (tx):
            _updateNodes(tx, JM_NODES_UPD_TYPES, self.__bonusCache, self.__nodeTooltips)
            _updateQuests(tx)
            _updateTokens(tx, JM_MAP_TOKENS_UPD_TYPES)
            _updateTime(tx, JM_TIME_UPD_TYPES)
            _updateBanner(tx)

    def __updateNodes(self, updTypes):
        if self.__isNodeUpdateBlocked:
            return
        with self.getViewModel().transaction() as (tx):
            _updateNodes(tx, updTypes, self.__bonusCache, self.__nodeTooltips)
            _updatePopover(tx, self.__popoverNodeId, updTypes, self.__popoverTooltips)

    def __updateQuests(self):
        with self.getViewModel().transaction() as (tx):
            _updateQuests(tx)

    def __updateTokens(self, updTypes, _):
        if not updTypes & JM_MAP_TOKENS_UPD_TYPES:
            return
        with self.getViewModel().transaction() as (tx):
            _updateTokens(tx, updTypes)
            if JmTokensUpdType.SHOP_BUNDLE in updTypes:
                _updateBanner(tx)

    def __updateTime(self, updTypes):
        with self.getViewModel().transaction() as (tx):
            _updateTime(tx, updTypes)

    @adisp_process('updating')
    def __onExplore(self, args):
        node = self.jmCtrl.jmNodes.getJmNodes().get(args.get('nodeId'))
        if node is None:
            _logger.error('Invalid args for exploring: args=%s', args)
            return
        else:
            nodeIds = [ str(node.id) for node in node.path if not node.isExplored ]
            self.__isNodeUpdateBlocked = True
            result = yield OpenJMNodesProcessor(nodeIds).request()
            if not result.success and result.userMsg:
                _logger.error('Request for open nodes %s not succeeded with message %s', nodeIds, result.userMsg)
            if result.success:
                self.viewModel.setExploreAnimationNodeId(nodeIds[(-1)])
            else:
                self.__isNodeUpdateBlocked = False
            return

    @args2params(str)
    def __onChangeCurrentNode(self, nodeId):
        self.__currNodeMover.moveJmCurrNode(nodeId)

    def __onCurrentNodeSynced(self):
        self.viewModel.setMovingFailed(False)

    @args2params(str)
    def __onSelectNode(self, nodeId):
        self.__popoverNodeId = nodeId
        with self.getViewModel().transaction() as (tx):
            packJmPopover(nodeId, tx.nodePopover, self.__popoverTooltips)

    def __onInterruptForScreenShow(self, args):
        self.__lastInterruptedNodeID = nodeID = args.get('nodeId')
        node = self.jmCtrl.jmNodes.getJmNodes().get(nodeID)
        if node is None:
            _logger.error('onInterruptForScreenShow called with invalid args: %s', args)
            self.viewModel.setExploreAnimationUnpause(nodeID)
            return
        else:
            windows = self.__pendingRewardWindowTypes
            if 'vehicles' in node.bonus:
                showVehicleRewardScreen(node.id)
                windows.append(JmFinalRewardWindow)
            attachments = _checkFullscreenForAttachmentBonuses(node.bonus)
            attachments.sort(key=_attachmentSortKey)
            for attachment in attachments:
                showCustomizationRarityAwardScreen(attachment)
                windows.append(AttachmentRewardWindow)

            if not windows:
                self.viewModel.setExploreAnimationUnpause(nodeID)
                return
            onWindowStatusChanged = self.__gui.windowsManager.onWindowStatusChanged
            if self.__onWindowStatusChanged in onWindowStatusChanged:
                return
            onWindowStatusChanged += self.__onWindowStatusChanged
            return

    def __onExploreAnimationFinished(self):
        self.__isNodeUpdateBlocked = False
        self.viewModel.setExploreAnimationNodeId('')
        self.__lastInterruptedNodeID = ''
        self.viewModel.setExploreAnimationUnpause('')
        self.jmCtrl.jmSysMessages.pushJmAnimPending()
        self.__updateNodes(JM_NODE_PATHS_UPD_TYPES)

    def __onWindowStatusChanged(self, uniqueID, newStatus):
        if newStatus != WindowStatus.DESTROYING or not self.__pendingRewardWindowTypes:
            return
        window = self.__gui.windowsManager.getWindow(uniqueID)
        if window is None:
            return
        else:
            for i, windowType in enumerate(self.__pendingRewardWindowTypes):
                if isinstance(window, windowType):
                    del self.__pendingRewardWindowTypes[i]
                    break

            if not self.__pendingRewardWindowTypes:
                self.__gui.windowsManager.onWindowStatusChanged -= self.__onWindowStatusChanged
                self.viewModel.setExploreAnimationUnpause(self.__lastInterruptedNodeID)
            return

    @args2params(str)
    def __onQuestProgressShown(self, questId):
        with self.getViewModel().transaction() as (tx):
            for questCard in tx.getQuestCards():
                if questCard.getId() == questId:
                    earnedProgress = questCard.getEarnedProgress()
                    if earnedProgress <= 0:
                        return
                    oldProgress = questCard.getCurrentProgress()
                    newProgress = oldProgress + earnedProgress
                    totalProgress = questCard.getTotalProgress()
                    questCard.setEarnedProgress(0)
                    questCard.setCurrentProgress(newProgress)
                    questCard.setIsCompleted(totalProgress == newProgress)
                    setJmMapViewQuestsProgress(questId, newProgress)
                    return

        _logger.error('Wrong questID when caching progress qID = %s', questId)

    def __onQuestCompletedShown(self):
        setJmQuestsCompleteAnimShown()
        self.viewModel.setIsQuestCompletedShow(False)

    def __onPreviewShow(self, event):
        loreNodeId = str(event.get('loreNodeId') or '')
        if loreNodeId:
            showLoreOverlay(str(loreNodeId))
            updateJmLoreNodeShown(loreNodeId)
            _updateLoreShownHint(self.viewModel.getNodes(), loreNodeId)
        else:
            _logger.error('invalid loreNodeId=%s', loreNodeId)

    def __onRewardPreview(self, args):
        nodeId = str(args.get('nodeId') or '')
        if nodeId not in self.__bonusCache:
            _logger.error('onPreviewShow invalid nodeId=%s', nodeId)
            return
        bonus = self.__bonusCache[nodeId]
        if bonus.getName() != 'vehicles':
            _logger.error('onPreviewShow invalid bonus=%s', bonus)
            return
        vehicle, _ = first(bonus.getVehicles())
        showVehicleHubOverview(vehicle.compactDescr)

    def __onJmConfigChange(self, diff):
        if 'shopLink' in diff:
            with self.getViewModel().transaction() as (tx):
                _updateBanner(tx)


def _updateNodes(tx, updTypes, bonusCache, tooltips):
    nodes = jmCtrl().jmNodes.getJmNodes()
    nodeModels = tx.getNodes()
    tx.setCurrentNodeId(nodes.getJmCurrNodeId())
    tx.setIsCompleted(nodes.getIsAllJmNodesExplored())
    if updTypes == {JmNodesUpdType.CURR_NODE}:
        _updateExploredPaths(nodeModels, nodes)
        return
    if JmNodesUpdType.CONFIG in updTypes:
        _updateNodesConfig(nodeModels, nodes, bonusCache, tooltips)
        _updateNodePaths(nodeModels, nodes)
        return
    _updateNodePaths(nodeModels, nodes)


def _updateNodesConfig(nodeModels, nodes, bonusCache, tooltips):
    bonusCache.clear()
    nodeModels.clear()
    tooltips.clear()
    loreShown = getJmLoreNodeShown()
    for node in nodes.values():
        model = JmNodeModel()
        nodeModels.addViewModel(model)
        model.setId(node.id)
        model.setPrice(node.price)
        model.setNodeType(node.type)
        model.setPosX(node.x)
        model.setPosY(node.y)
        model.setHasLore(node.hasLore)
        if node.hasLore:
            model.setLoreX(node.xLore)
            model.setLoreY(node.yLore)
            model.setLoreVisited(node.id in loreShown)
        fillStringsArray(node.nextNodes, model.getNextNodeIds())
        tooltips[node.id] = nodeTooltips = {}
        fillBonuses(node, model, bonusCache, nodeTooltips)

    nodeModels.invalidate()


def _updateNodePaths(nodeModels, nodes):
    for model in nodeModels:
        node = nodes[model.getId()]
        model.setIsExplored(node.isExplored)
        fillStringsArray([ node.id for node in node.path ], model.getPathFromCurrentNode())
        model.setCanAfford(node.path.canAfford)


def _updateExploredPaths(nodeModels, nodes):
    for model in nodeModels:
        node = nodes[model.getId()]
        if node.isExplored:
            fillStringsArray([ node.id for node in node.path ], model.getPathFromCurrentNode())


def _updateLoreShownHint(nodeModels, loreNodeId):
    for model in nodeModels:
        if model.getId() == loreNodeId:
            model.setLoreVisited(True)
            return


def _updatePopover(tx, nodeId, updTypes, tooltips):
    if JmNodesUpdType.CONFIG in updTypes and nodeId:
        packJmPopover(nodeId, tx.nodePopover, tooltips)


def fillBonuses(node, nodeModel, bonusCache, tooltips):
    composedBonuses = composeBonuses([node.bonus])
    sortedBonuses = jmCtrl().jmBonuses.sortJmNodesBonuses(composedBonuses)
    if node.type == NodeType.LARGE:
        bonusCache[node.id] = first(sortedBonuses)
    bonusModels = nodeModel.getBonuses()
    bonusModels.clear()
    packBonusModelAndTooltipData(sortedBonuses, bonusModels, tooltips, getJMBonusPacker())
    if _checkFullscreenForAttachmentBonuses(node.bonus) or 'vehicles' in node.bonus:
        nodeModel.setHasFullscreenReward(True)


def _updateQuests(tx):
    getProgress = makeJmMapViewQuestsProgressGetter()
    tx.setIsQuestCompletedShow(not getJmQuestsCompleteAnimShown())
    questInfos = jmCtrl().jmQuests.getJmCurrQuestInfos()
    questModels = tx.getQuestCards()
    questModels.clear()
    for questInfo in questInfos:
        model = JmQuestCardModel()
        questModels.addViewModel(model)
        model.setId(questInfo.id)
        model.setDescription(questInfo.descr)
        model.setIconKey(questInfo.iconKey + '_silver')
        model.setReward(questInfo.coinCount)
        if not questInfo.isCumulative:
            model.setIsCompleted(questInfo.isCompleted)
            continue
        lastSeenProgress = getProgress(questInfo.id)
        if lastSeenProgress > questInfo.currProgress:
            setJmMapViewQuestsProgress(questInfo.id, questInfo.currProgress)
            lastSeenProgress = questInfo.currProgress
        model.setIsCompleted(lastSeenProgress == questInfo.totalProgress)
        model.setCurrentProgress(lastSeenProgress)
        model.setTotalProgress(questInfo.totalProgress)
        model.setEarnedProgress(questInfo.currProgress - lastSeenProgress)

    questModels.invalidate()


def _updateTokens(tx, updTypes):
    jmTokens = jmCtrl().jmTokens
    if JmTokensUpdType.COINS in updTypes:
        _, __, coinTokenCnt = jmTokens.getJmCoinToken()
        tx.setCoinTokenCount(coinTokenCnt)
    if JmTokensUpdType.LOCK in updTypes:
        lockTokens = jmTokens.getJmLockTokens()
        lockToken = first(sorted(lockTokens))
        _, lockTokenCnt = lockTokens.get(lockToken, (None, 0))
        tx.setUnlockTokenCount(lockTokenCnt)
    return


def _updateTime(tx, updTypes):
    jmTime = jmCtrl().jmTime
    if JmTimeUpdType.STATE in updTypes:
        _onDisabledCloseView()
    if JmTimeUpdType.STAMPS in updTypes:
        tx.setTimeTillEnd(jmTime.getJmTimeLeft())
    if JmTimeUpdType.QUESTS_REROLL in updTypes:
        tx.setTimeTillNewQuests(jmTime.getJmTimeTillNewQuests())
        tx.setIsLastGameDay(not jmTime.hasMoreJmQuestRerolls())


def _updateBanner(tx):
    ctrl = jmCtrl()
    shopLink = ctrl.jmConfig.getJmShopLink()
    _, __, petTokenCount = ctrl.jmTokens.getJmShopBundleToken()
    showBanner = bool(petTokenCount <= 0 and shopLink)
    tx.setBannerShown(showBanner)


def _onDisabledCloseView():
    ctrl = jmCtrl()
    if ctrl.jmSwitcher.getJmFtState() in JM_MAP_VIEW_DISABLED_FT_STATES or ctrl.jmTime.getJmTimeState() in JM_MAP_VIEW_DISABLED_TIME_STATES or ctrl.jmConfig.getJmConfigErrors():
        lsm = getLobbyStateMachine()
        mapState = lsm.getStateByCls(JmMapState)
        mapState.goBack()


@dependency.replace_none_kwargs(c11n=ICustomizationService)
def _checkFullscreenForAttachmentBonuses(nodeBonuses, c11n=None):
    attachments = []
    for customization in nodeBonuses.get('customizations', []):
        custType = customization.get('custType')
        if custType == 'attachment':
            attachment = c11n.getItemByID(getItemTypeID(custType), customization.get('id'))
            if attachment.rarity in Rarity.UI_EFFECT:
                attachments.append(attachment)

    return attachments


def _attachmentSortKey(attachment, order=(
 Rarity.LEGENDARY, Rarity.EPIC)):
    return order.index(attachment.rarity)