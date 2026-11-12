from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.surprise_machine.robot_tv_rewards_view_model import RobotTvRewardsViewModel
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses, splitBonuses
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from new_year.gui.bonuses.bonuses_packers import getRobotTvRewardsBonusPacker
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.tooltips.lootbox_tooltip import LootboxTooltip, ExtendedLootboxTooltip
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from new_year.gui.shared.ny_machine_helper import stripOpenedLootboxTokens
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer, WindowStatus
from gui.shared.utils.graphics import isRendererPipelineDeferred
from gui.shared.view_helpers.blur_manager import CachedBlur
from skeletons.gui.shared.utils import IHangarSpace
from gui.impl.pub import ViewImpl, WindowImpl
from skeletons.gui.shared import IItemsCache
from helpers import dependency
from gui.impl.gen import R

class RobotTvRewardsView(ViewImpl):
    __slots__ = ('__tooltips', )
    __itemsCache = dependency.descriptor(IItemsCache)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        settings = ViewSettings(layoutID=R.views.new_year.lobby.new_year.RobotTvRewardsView(), flags=ViewFlags.VIEW, model=RobotTvRewardsViewModel())
        self.__tooltips = {}
        super(RobotTvRewardsView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RobotTvRewardsView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(RobotTvRewardsView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        tooltipData = self.getTooltipData(event)
        if contentID == R.views.gui_lootboxes.lobby.gui_lootboxes.tooltips.LootboxTooltip() and tooltipData:
            lootBox = self.__itemsCache.items.tokens.getLootBoxByID(int(tooltipData.get('lootBoxID')))
            if lootBox.isExtendedTooltip():
                return ExtendedLootboxTooltip(lootBox)
            return LootboxTooltip(lootBox)
        return super(RobotTvRewardsView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        tID = event.getArgument('tooltipId')
        return self.__tooltips.get(tID, None)

    def setTokensUsed(self, count):
        self.viewModel.setTokensUsed(count)

    def fillRewards(self, rewardsListOfDicts):
        vmList = self.viewModel.getRewards()
        vmList.clear()
        rawBonuses = []
        for rewards in rewardsListOfDicts:
            if not rewards:
                continue
            cleaned = stripOpenedLootboxTokens(rewards)
            for bType, bVal in cleaned.iteritems():
                rawBonuses.extend(getNonQuestBonuses(bType, bVal))

        merged = splitBonuses(mergeBonuses(rawBonuses))
        self.__tooltips.clear()
        packBonusModelAndTooltipData(merged, vmList, tooltipData=self.__tooltips, packer=getRobotTvRewardsBonusPacker())
        vmList.invalidate()

    def _onLoading(self, *args, **kwargs):
        super(RobotTvRewardsView, self)._onLoading(*args, **kwargs)
        self.viewModel.setHasBlur(isRendererPipelineDeferred())

    def _finalize(self):
        self.viewModel.getRewards().clear()
        super(RobotTvRewardsView, self)._finalize()


class RobotTvRewardsViewWindow(WindowImpl):
    __slots__ = ('__blur', )

    def __init__(self, parent=None):
        super(RobotTvRewardsViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=RobotTvRewardsView(), parent=parent, layer=WindowLayer.OVERLAY)
        self.__blur = None
        self.onStatusChanged += self.__onStatusChanged
        return

    def _finalize(self):
        self.onStatusChanged -= self.__onStatusChanged
        if self.__blur is not None:
            self.__blur.fini()
            self.__blur = None
        super(RobotTvRewardsViewWindow, self)._finalize()
        return

    def __onStatusChanged(self, newState):
        if newState != WindowStatus.LOADED or self.__blur is not None:
            return
        if not isRendererPipelineDeferred():
            return
        else:
            self.__blur = CachedBlur(enabled=True, ownLayer=self.layer - 1, blurAnimRepeatCount=4)
            return