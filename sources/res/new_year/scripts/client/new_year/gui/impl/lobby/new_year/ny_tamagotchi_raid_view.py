from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl, WindowImpl
from gui.server_events.bonuses import getNonQuestBonuses
from helpers import dependency, time_utils
from helpers.time_utils import getServerUTCTime
from new_year.gui.impl.new_year.new_year_bonus_packer import packBonusModelAndTooltipData, getNewYearBonusPacker
from new_year.gui.impl.lobby.new_year.tooltips.ny_pet_raid_boost_tooltip import NyPetRaidBoostTooltip
from new_year.gui.impl.new_year.sounds import NY_RAID_SOUND_SPACE
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipt_model import ReceiptModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.ny_tamagotchi_raid_view_model import NyTamagotchiRaidViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipts_panel import TabId
from new_year.gui.impl.lobby.new_year.ny_tamagotchi_raid_bonus_packer import packRaidBonusModelAndTooltipData
from new_year.gui.impl.lobby.new_year.ny_raid_reward_helpers import prepareRaidRewardResult
from new_year.gui.impl.lobby.new_year.ny_raid_receipt_helpers import prepareReceiptStates, calcReceiptState, getVisibleReceipts, getFirstDisabledIndex, getTotalItemsCount, hasEnoughResourcesForComponents, getTabData, DEFAULT_FIRST_DISABLED_INDEX
from new_year.gui.shared.gui_items.processors.ny_processor import ReceiveTamagotchiRaidRewardProcessor, StartTamagotchiRaidProcessor, UseTamagotchiRaidSpeedupProcessor
from new_year.helpers.ny_helpers import collectRaidReservedResources, isRaidComponentEnabled
from new_year.helpers.server_settings import getNewYearServerSettings, getNewYearRaidConfig
from new_year_account_settings import getNYSetting, setNYSettings
from new_year_common.settings import NyRaidConsts
from account_helpers.settings_core.settings_constants import NewYearStorageKeys
from new_year.ny_constants import NY_TAMAGOTCHI_RAID_REPEAT_ONBOARDING_COUNT
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
from new_year.gui.shared.event_dispatcher import showNYPetRaidRewardWindow
from new_year.skeletons.new_year import INewYearController, INewYearTamagotchiController, ITamagotchiDataProvider, INewYearMetricsLogger
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
from new_year_common.items.components.ny_constants import RaidState
from skeletons.festivity_factory import IFestivityFactory
from skeletons.gui.shared import IItemsCache
from adisp import adisp_process
from new_year.gui.impl.lobby.new_year.tooltips.ny_common_tooltip import NyCommonTooltip, getCommonTooltipArgsFromEvent
from shared_utils import first
_FAILURE_NOT_ENOUGH_RESOURCES_CODE = -1

class NyTamagotchiRaidView(ViewImpl):
    __slots__ = ('__selectedBonuses', '__tooltipData', '__isReceiptsTabsOpened', '__raidComponents',
                 '__isBoostMode', '__closeCallback', '__receiptData', '__receiptsOffset')
    _COMMON_SOUND_SPACE = NY_RAID_SOUND_SPACE
    _RECEIPT_CARDS_LIMIT = 100
    __itemsCache = dependency.descriptor(IItemsCache)
    __festivityFactory = dependency.descriptor(IFestivityFactory)
    __nyController = dependency.descriptor(INewYearController)
    __tamagotchiController = dependency.descriptor(INewYearTamagotchiController)
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __uiLogger = dependency.descriptor(INewYearMetricsLogger)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, isBoostMode, layoutID, closeCallback):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = NyTamagotchiRaidViewModel()
        self.__selectedBonuses = [None, None, None]
        self.__tooltipData = {}
        self.__isReceiptsTabsOpened = False
        self.__raidComponents = None
        self.__isBoostMode = isBoostMode
        self.__closeCallback = closeCallback
        self.__receiptData = {}
        self.__receiptsOffset = 0
        super(NyTamagotchiRaidView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(NyTamagotchiRaidView, self).getViewModel()

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyPetRaidBoostTooltip():
            return NyPetRaidBoostTooltip()
        else:
            if contentID == R.views.new_year.lobby.new_year.tooltips.CommonTooltip():
                return NyCommonTooltip(*getCommonTooltipArgsFromEvent(event))
            lootboxesViews = R.views.dyn('gui_lootboxes')
            if lootboxesViews.isValid() and contentID == lootboxesViews.lobby.gui_lootboxes.tooltips.LootboxTooltip():
                tooltipData = self.getTooltipData(event)
                if tooltipData is not None:
                    return tooltipData.tooltip(*tooltipData.specialArgs)
                return
            return super(NyTamagotchiRaidView, self).createToolTipContent(event, contentID)

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(NyTamagotchiRaidView, self).createToolTip(event)

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onRaidStart, self.__onRaidStart),
         (
          self.viewModel.onRecipiePreview, self.__onRecipiePreview),
         (
          self.viewModel.onUpdateSelected, self.__onUpdateSelected),
         (
          self.viewModel.onReceiveReward, self.__onReceiveReward),
         (
          self.viewModel.onOpenReceiptsTabs, self.__onOpenReceiptsTabs),
         (
          self.viewModel.onCloseReceiptsTabs, self.__onCloseReceiptsTabs),
         (
          self.viewModel.onAccelerationRaid, self.__onRaidSpeedup),
         (
          self.viewModel.onSetOnboardingEnd, self.__onSetOnboardingEnd),
         (
          self.viewModel.onOnboardingRestart, self.__onRaidOnboardingRestart),
         (
          self.__tamagotchiController.onRaidDataUpdated, self.__onRaidDataUpdated),
         (
          self.__nyController.onPetRaidVisibilityUpdated, self.__onPetRaidVisibilityUpdated),
         (
          self.__dataProvider.onRaidReadyUpdated, self.__onRaidReadyUpdated),
         (
          self.__itemsCache.onSyncCompleted, self.__onSyncCompleted),
         (
          self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChanged),
         (
          self.viewModel.receiptsPanel.onSelectTab, self.__onSelectTab),
         (
          self.viewModel.receiptsPanel.onLoadReceipts, self.__onLoadReceipts))

    def _onLoading(self, *args, **kwargs):
        super(NyTamagotchiRaidView, self)._onLoading(*args, **kwargs)
        self.viewModel.setIsBoostMode(self.__isBoostMode)
        self.__fillRaidData()
        self.__fillRegularInventoryItems()
        self.viewModel.setIsTamagotchiForRaidReady(self.__dataProvider.isReadyForRaid())
        self.__updateReceiptsTabs()
        isFirstOnboardingEnter = self.__settingsCore.serverSettings.getNewYearStorage().get(NewYearStorageKeys.NY_TAMAGOTCHI_RAID_FIRST_ONBOARDING, True)
        self.viewModel.setIsFirstOnboardingEnter(isFirstOnboardingEnter)

    def __fillBoostData(self):
        raidBoost = getNewYearRaidConfig().get('raidBoost', {})
        self.viewModel.setBoostAmount(self.__tamagotchiController.getRaidBoostAmount())
        self.viewModel.setMaxBoostLimit(raidBoost.get('limit', 0))
        self.viewModel.setBoostTime(raidBoost.get('boostTime', 0))
        self.viewModel.setBoostsToAdd(raidBoost.get('amount', 0))
        self.viewModel.setBoostAccrualTime(raidBoost.get('accrualTime', 0) + 3 * time_utils.ONE_HOUR)

    def __fillRaidData(self):
        raidData = self.__tamagotchiController.getRaidData()
        self.__fillRaidHeader(raidData)
        self.__fillSelectedItems(raidData)
        self.__updatePreviewTimeFromSelected()

    def __fillRaidHeader(self, raidData):
        self.__fillRaidTime(raidData)
        self.__fillRewardState()
        self.__fillBoostData()

    def __fillRewardState(self):
        raidState = self.__tamagotchiController.getRaidState()
        self.viewModel.setIsHasUnreceivedReward(raidState == RaidState.FINISHED)

    def __fillRaidTime(self, raidData):
        elapsedTime, remainingTime = self.__getRaidTimeData(raidData)
        self.viewModel.setTimeLeft(elapsedTime)
        self.viewModel.setRemainingTime(remainingTime)

    def __getRaidTimeData(self, raidData):
        startTime = raidData.get('startTime', 0)
        remainingTime = self.__dataProvider.getRaidRemainingTime()
        durationDiff = int(raidData.get('primaryDuration', 0) - raidData.get('duration', 0))
        elapsedTime = 0 if startTime == 0 else getServerUTCTime() - startTime + durationDiff
        return (elapsedTime, remainingTime)

    def __fillSelectedItems(self, raidData):
        self.__fillComponentItems(self.viewModel.getSelectedItems(), selectedIDs=raidData.get('componentIDs', []), isEnabled=True, sortByWeight=False)

    def __fillRegularInventoryItems(self):
        reservedResources = collectRaidReservedResources(self.__getRaidComponentsConfig(), self.__selectedBonuses)
        self.__fillComponentItems(self.viewModel.getItems(), reservedResources=reservedResources, sortByWeight=True)

    def __fillComponentItems(self, model, selectedIDs=None, reservedResources=None, isEnabled=None, sortByWeight=False):
        model.clear()
        components = self.__getRaidComponentsConfig()
        if selectedIDs is not None:
            components = [ (componentId, components[componentId]) for componentId in selectedIDs if componentId in components ]
        else:
            components = components.iteritems()
            if sortByWeight:
                components = sorted(components, key=self.__getComponentWeightSortKey, reverse=True)
            for componentId, componentData in components:
                bonus = componentData.get('bonus', {})
                bonuses = self.__getComponentBonuses(bonus)
                packRaidBonusModelAndTooltipData(bonuses, model, componentId=componentId, isEnabled=isRaidComponentEnabled(bonus, reservedResources=reservedResources) if isEnabled is None else isEnabled, tooltipsData=self.__tooltipData)

        model.invalidate()
        return

    @staticmethod
    def __getComponentWeightSortKey(component):
        componentId, componentData = component
        return (componentData.get('weight', 0.0), -componentId)

    @staticmethod
    def __getComponentBonuses(bonus):
        bonuses = []
        for name, value in bonus.iteritems():
            bonuses.extend(getNonQuestBonuses(name, value))

        return bonuses

    def __onClose(self):
        if self.__closeCallback is not None:
            self.__closeCallback()
        self.destroyWindow()
        return

    def __onRaidDataUpdated(self):
        if not self.__dataProvider.isRaidActive() and self.__isBoostMode:
            self.__onClose()
            return
        self.__fillRaidData()
        self.viewModel.setIsTamagotchiForRaidReady(self.__dataProvider.isReadyForRaid())

    def __onPetRaidVisibilityUpdated(self, isPetRaidEnabled):
        if not isPetRaidEnabled:
            self.__onClose()

    def __onSyncCompleted(self, *_, **__):
        self.__fillRegularInventoryItems()
        if self.__isReceiptsTabsOpened:
            self.__refreshReceiptsData()

    def __onSetOnboardingEnd(self):
        self.__settingsCore.serverSettings.saveInNewYearStorage({NewYearStorageKeys.NY_TAMAGOTCHI_RAID_FIRST_ONBOARDING: False})
        self.viewModel.setIsFirstOnboardingEnter(False)

    @adisp_process
    @args2params(int, int, int)
    def __onRaidStart(self, firstItem, secondItem, thirdItem):
        raidInput = [firstItem, secondItem, thirdItem]
        if not self.__hasEnoughResourcesForSelectedComponents(raidInput):
            self.__raidStartError(True)
            return
        if not self.__dataProvider.isReadyForRaid():
            self.__raidStartError(False)
            return
        result = yield StartTamagotchiRaidProcessor(raidInput).request()
        if result.success:
            TamagotchiSysMsgHandler.sendRaidStarted()
            self.__onClose()
        else:
            self.__raidStartError(result.auxData == _FAILURE_NOT_ENOUGH_RESOURCES_CODE)

    def __raidStartError(self, isNotEnoughResources=True):
        self.__selectedBonuses = []
        self.__fillSelectedItems({'componentIDs': []})
        self.__fillRegularInventoryItems()
        self.viewModel.setIsTamagotchiForRaidReady(self.__dataProvider.isReadyForRaid())
        TamagotchiSysMsgHandler.sendRaidStartError(isNotEnoughResources)

    @args2params(int)
    def __onRecipiePreview(self, receiptId):
        if receiptId == -1:
            self.__updatePreviewTimeFromSelected()
            return
        receiptData = self.__getRaidDataForReceipt(receiptId)
        self.viewModel.setPreviewTime(self.__getReceiptDuration(receiptId, receiptData))

    def __onUpdateSelected(self, args):
        firstItem = args.get('firstItem')
        secondItem = args.get('secondItem')
        thirdItem = args.get('thirdItem')
        self.__selectedBonuses = (firstItem, secondItem, thirdItem)
        self.__fillSelectedItems({'componentIDs': self.__selectedBonuses})
        self.__fillRegularInventoryItems()
        self.__updatePreviewTimeFromSelected()

    def __updatePreviewTimeFromSelected(self):
        if all(item is not None and item != 'empty' for item in self.__selectedBonuses):
            duration = self.__getDurationForSelectedComponents(self.__selectedBonuses)
            self.viewModel.setPreviewTime(duration)
        else:
            self.viewModel.setPreviewTime(0)

    def __getDurationForSelectedComponents(self, componentIDs):
        selectedComponents = set(componentIDs)
        raidMetaData = self.__tamagotchiController.getRaidMetaData()
        disclosedReceipts = raidMetaData.get('disclosedReceipts', {})
        for category in ('public', 'secret'):
            for receiptId, receiptData in disclosedReceipts.get(category, {}).iteritems():
                if receiptData.get('disabled', False):
                    continue
                if set(receiptData.get('slots', ())) != selectedComponents:
                    continue
                return self.__getReceiptDuration(receiptId, receiptData)

        return 0

    def __getReceiptDuration(self, receiptId, receiptData):
        if receiptData is None:
            return 0
        else:
            limit = receiptData.get('limit')
            receiptLimits = self.__tamagotchiController.getRaidMetaData().get('receiptLimits', {})
            if limit is not None and receiptLimits.get(receiptId, 0) >= limit:
                return 0
            reward = first(receiptData.get('rewards', ()))
            if reward is not None:
                return reward.get('duration', 0)
            return 0

    def __hasEnoughResourcesForSelectedComponents(self, selectedIDs):
        components = self.__getRaidComponentsConfig()
        return hasEnoughResourcesForComponents(components, selectedIDs)

    @adisp_process
    def __onReceiveReward(self):
        result = yield ReceiveTamagotchiRaidRewardProcessor().request()
        if result is not None and result.success:
            self.__onClose()
            prepareRaidRewardResult(result)
            showNYPetRaidRewardWindow(next(iter(result.auxData['bonus'])) or {})
        else:
            TamagotchiSysMsgHandler.sendRaidRewardError()
        return

    def __onRaidReadyUpdated(self, isReady):
        self.viewModel.setIsTamagotchiForRaidReady(isReady)

    def __onServerSettingsChanged(self, _):
        self.__fillBoostData()
        if self.__isReceiptsTabsOpened:
            self.__refreshReceiptsData()

    def __onOpenReceiptsTabs(self):
        self.__isReceiptsTabsOpened = True
        self.__updateReceiptsTabs()

    def __onCloseReceiptsTabs(self):
        self.__isReceiptsTabsOpened = False
        self.__updateReceiptsTabs()
        self.__updatePreviewTimeFromSelected()

    @adisp_process
    def __onRaidSpeedup(self):
        result = yield UseTamagotchiRaidSpeedupProcessor().request()
        if result is not None and result.userMsg:
            TamagotchiSysMsgHandler.sendRaidAccelerationError()
        if self.__isBoostMode:
            self.__onClose()
        return

    def __updateReceiptsTabs(self):
        self.viewModel.setIsReceiptsTabsOpened(self.__isReceiptsTabsOpened)
        self.__clearReceiptsPanel()
        if not self.__isReceiptsTabsOpened:
            return
        self.__loadReceiptsForTab(self.__dataProvider.currentRaidTab)

    def __getRaidComponentsConfig(self):
        if self.__raidComponents is None:
            raidConfig = getNewYearServerSettings().get(NyRaidConsts.CONFIG_NAME, {})
            self.__raidComponents = raidConfig.get('components', {})
        return self.__raidComponents

    def __onRaidOnboardingRestart(self):
        count = getNYSetting(NY_TAMAGOTCHI_RAID_REPEAT_ONBOARDING_COUNT) + 1
        setNYSettings(NY_TAMAGOTCHI_RAID_REPEAT_ONBOARDING_COUNT, count)
        self.__uiLogger.logRaidRepeatOnboardingClick(count)

    @args2params(TabId)
    def __onSelectTab(self, selectedTab):
        if selectedTab != self.__dataProvider.currentRaidTab:
            self.__receiptsOffset = 0
        self.__dataProvider.currentRaidTab = selectedTab
        self.__clearReceiptsPanel()
        if not self.__isReceiptsTabsOpened:
            return
        self.__loadReceiptsForTab(selectedTab)

    @args2params(int)
    def __onLoadReceipts(self, offset):
        limit = self._RECEIPT_CARDS_LIMIT
        self.__fillVisibleReceipts(offset, limit)

    def __clearReceiptsPanel(self):
        panel = self.viewModel.receiptsPanel
        panel.setItemsAmount(0)
        panel.setItemsOffset(0)
        panel.getKnownReceipts().clear()
        panel.getDiscoveredReceipts().clear()
        panel.getReceiptHistory().clear()
        self.viewModel.receiptsPanel.setFirstDisabledReceiptIndex(DEFAULT_FIRST_DISABLED_INDEX)

    def __loadReceiptsForTab(self, tab):
        raidMetaData = self.__tamagotchiController.getRaidMetaData()
        tabData = getTabData(tab, raidMetaData, self.viewModel)
        if tabData is None:
            return
        else:
            self.__receiptData = tabData
            self.__prepareTabReceiptStates()
            self.__receiptData['totalItems'] = self.__getTotalItemsCount()
            panel = self.viewModel.receiptsPanel
            panel.setSelectedTab(tab)
            panel.setItemsAmount(self.__receiptData['totalItems'])
            self.__fillVisibleReceipts(self.__receiptsOffset, self._RECEIPT_CARDS_LIMIT)
            return

    def __refreshReceiptsData(self):
        if self.__receiptData is None:
            return
        else:
            self.__prepareTabReceiptStates()
            self.__receiptData['totalItems'] = self.__getTotalItemsCount()
            panel = self.viewModel.receiptsPanel
            panel.setItemsAmount(self.__receiptData['totalItems'])
            self.__fillVisibleReceipts(self.__receiptsOffset, self._RECEIPT_CARDS_LIMIT)
            return

    def __prepareTabReceiptStates(self):
        receiptLimits = self.__receiptData.get('receiptLimits', {})
        if self.__dataProvider.currentRaidTab == TabId.HISTORY:
            disclosedReceipts = self.__receiptData.get('disclosedReceipts', {})
            for category in ('public', 'secret'):
                self.__prepareReceiptStates(disclosedReceipts.get(category, {}), receiptLimits)

        else:
            self.__prepareReceiptStates(self.__receiptData.get('receipts', {}), receiptLimits)

    def __prepareReceiptStates(self, receipts, receiptLimits):
        componentsConfig = self.__getRaidComponentsConfig()
        isRaidReady = self.__dataProvider.isRaidReady
        raidState = self.__tamagotchiController.getRaidState()
        prepareReceiptStates(receipts, receiptLimits, isRaidReady, raidState, componentsConfig)

    def __getTotalItemsCount(self):
        return getTotalItemsCount(self.__dataProvider.currentRaidTab, self.__receiptData)

    def __getDisclosedReceipts(self):
        if 'disclosedReceipts' in self.__receiptData:
            return self.__receiptData['disclosedReceipts']
        return self.__tamagotchiController.getRaidMetaData().get('disclosedReceipts', {})

    def __getRaidDataForReceipt(self, receiptID):
        disclosedReceipts = self.__getDisclosedReceipts()
        public = disclosedReceipts.get('public', {})
        secret = disclosedReceipts.get('secret', {})
        return public.get(receiptID) or secret.get(receiptID)

    def __getReceiptState(self, slotIDs):
        componentsConfig = self.__getRaidComponentsConfig()
        isRaidReady = self.__dataProvider.isRaidReady
        raidState = self.__tamagotchiController.getRaidState()
        return calcReceiptState(isRaidReady, raidState, slotIDs, None, 0, componentsConfig)

    def __fillReceiptComponent(self, model, componentID):
        componentData = self.__getRaidComponentsConfig().get(componentID)
        if componentData is None:
            return
        else:
            bonus = componentData.get('bonus', {})
            bonuses = self.__getComponentBonuses(bonus)
            packRaidBonusModelAndTooltipData(bonuses, model, componentId=componentID, isEnabled=True, tooltipsData=self.__tooltipData)
            return

    def __fillVisibleReceipts(self, offset, limit):
        model = self.__receiptData.get('model')
        if model is None:
            return
        else:
            model.clear()
            self.__receiptsOffset = offset
            currentRaidTab = self.__dataProvider.currentRaidTab
            items, endIdx = getVisibleReceipts(currentRaidTab, self.__receiptData, offset, limit)
            firstDisabledIndex = getFirstDisabledIndex(items, currentRaidTab)
            for receiptItem in items:
                self.__fillReceiptCard(model, receiptItem)

            model.invalidate()
            self.__receiptData['offset'] = endIdx
            self.viewModel.receiptsPanel.setFirstDisabledReceiptIndex(firstDisabledIndex)
            self.viewModel.receiptsPanel.setItemsOffset(endIdx)
            return

    def __fillReceiptCard(self, model, receiptItem):
        receiptModel = ReceiptModel()
        if self.__dataProvider.currentRaidTab == TabId.HISTORY:
            receiptData = receiptItem
            receiptModel.setStartTime(receiptData.get('startTime', -1))
            self.__fillReceiptHistoryEntry(receiptModel, receiptData)
        else:
            receiptId, receiptData = receiptItem
            usageCount = self.__receiptData['receiptLimits'].get(receiptId, 0)
            self.__fillReceipt(receiptModel, receiptData, usageCount)
        model.addViewModel(receiptModel)

    def __fillReceipt(self, model, receiptData, usageCount):
        receiptComponents = model.getReceiptComponents()
        receiptComponents.clear()
        slotIDs = receiptData.get('slots', ())
        for slotID in slotIDs:
            self.__fillReceiptComponent(receiptComponents, slotID)

        receiptComponents.invalidate()
        receiptRewards = model.getReceiptRewards()
        receiptRewards.clear()
        rewards = receiptData.get('rewards', [])
        if rewards:
            bonuses = self.__getComponentBonuses(rewards[0].get('bonus', {}))
            packBonusModelAndTooltipData(bonuses, receiptRewards, getNewYearBonusPacker(), tooltipsData=self.__tooltipData)
        receiptRewards.invalidate()
        limit = receiptData.get('limit')
        if limit is not None:
            model.setLimit(limit)
        model.setId(receiptData.get('id', 0))
        model.setIsDisabled(receiptData.get('disabled', False))
        model.setWeight(receiptData.get('weight', 0.0))
        model.setUsageCount(usageCount)
        state = receiptData.get('state')
        if state is not None:
            model.setState(state)
        return

    def __fillReceiptHistoryEntry(self, model, receiptData):
        receiptID = receiptData.get('receiptID')
        if receiptID is not None:
            raidData = self.__getRaidDataForReceipt(receiptID)
            if raidData is not None:
                self.__fillReceipt(model, raidData, 0)
                return
        self.__fillEmptyReceipt(model, receiptData)
        return

    def __fillEmptyReceipt(self, model, receiptData):
        model.setStartTime(receiptData.get('startTime', -1))
        components = receiptData.get('components', ())
        self.__fillComponents(model.getReceiptComponents(), components)
        self.__fillRewards(model.getReceiptRewards(), receiptData.get('bonus'))
        state = self.__getReceiptState(components)
        model.setState(state)

    def __fillComponents(self, model, components):
        model.clear()
        for componentID in components:
            self.__fillReceiptComponent(model, componentID)

        model.invalidate()

    def __fillRewards(self, model, bonus):
        model.clear()
        if bonus:
            bonuses = self.__getComponentBonuses(bonus)
            packBonusModelAndTooltipData(bonuses, model, getNewYearBonusPacker(), tooltipsData=self.__tooltipData)
        model.invalidate()


class NyTamagotchiRaidViewWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, isBoostMode=False, parent=None, closeCallback=None):
        super(NyTamagotchiRaidViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=NyTamagotchiRaidView(isBoostMode, R.views.new_year.lobby.new_year.NyTamagotchiRaidView(), closeCallback), parent=parent)