from constants import MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL
from gui.impl.backport.backport_tooltip import _BackportTooltipContent
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.event_model import EventStatus
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.daily.daily_helpers import modifyPostbattleConditions
from gui.impl.lobby.daily.tooltips.mode_selector_tooltip import ModeSelectorTooltip
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from gui.shared.missions.packers.events import getEventUIDataPacker
from gui.server_events.event_items import TokenQuest
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.tooltips.lootbox_tooltip import LootboxTooltip
from helpers import dependency
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.new_year_info_view_model import Tabs
from new_year.gui.game_control.ny_controller import getNYQuests
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.quests.ny_quests_view_model import NyQuestsViewModel
from new_year.gui.impl.lobby.new_year.sub_model_presenter import HistorySubModelPresenter
from new_year.gui.impl.lobby.new_year.quests.ny_quest_helper import getCurrentWeek, modifyTokenQuestConditions
from new_year.gui.impl.new_year.new_year_bonus_packer import getNewYearBonusPacker
from new_year.interactive_state_machine.constants import PersonaTypes
from new_year.ny_constants import NY_IS_QUESTS_CELEB_VOICEOVERS_ENABLED, NY_SEEN_QUESTS, InternalViewState, ViewAliases
from new_year.skeletons.new_year import INewYearController, INewYearMetricsLogger
from new_year.skeletons.i_sm_queue import IStateMachineQueue
from new_year_account_settings import getNYSetting, setNYSettings
from new_year_common.items.components.ny_constants import CurrentNYConstants
from shared_utils import findFirst
from skeletons.gui.game_control import IUnseenEventsCounter
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
_INT_MAX_VALUE = 2147483647

class NyQuestsView(HistorySubModelPresenter):
    __slots__ = ('__tooltipData', '__subviewTabIdx', '__minLevel', '__maxLevel', '__dailyQuests',
                 '__weeklyQuests', '__battleTypes')
    _INTERNAL_VIEW_STATE = InternalViewState.GRIMVAGEN_MAIN
    eventsCache = dependency.descriptor(IEventsCache)
    itemsCache = dependency.descriptor(IItemsCache)
    __nyCtrl = dependency.descriptor(INewYearController)
    __unseenEventsManager = dependency.descriptor(IUnseenEventsCounter)
    __uiLogger = dependency.descriptor(INewYearMetricsLogger)
    __stateMachineQueue = dependency.descriptor(IStateMachineQueue)

    def __init__(self, viewModel, parentView, *args, **kwargs):
        super(NyQuestsView, self).__init__(viewModel, parentView, *args, **kwargs)
        self.__tooltipData = {}
        self.__subviewTabIdx = 0
        self.__minLevel = MAX_VEHICLE_LEVEL
        self.__maxLevel = MIN_VEHICLE_LEVEL
        self.__dailyQuests, self.__weeklyQuests = getNYQuests(self.eventsCache)
        self.__battleTypes = None
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def initialize(self, *args, **kwargs):
        self.__stateMachineQueue.handleCloseUp(PersonaTypes.CELEB_WOMAN, True)
        super(NyQuestsView, self).initialize(*args, **kwargs)
        self._update()

    def finalize(self):
        self.__subviewTabIdx = 0
        self.__tooltipData = {}
        self.__battleTypes = None
        self.__stateMachineQueue.handleCloseUp(PersonaTypes.CELEB_WOMAN, False)
        super(NyQuestsView, self).finalize()
        self.__uiLogger.logQuestsScreenClosed(self.__nyCtrl.isQuestsCelebVoiceoverEnabled())
        return

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.daily.tooltips.ModeSelectorTooltip():
            return ModeSelectorTooltip(event.contentID, self.__battleTypes)
        else:
            if contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                tooltipData = self.__getBackportTooltipData(event)
                if tooltipData is not None:
                    return _BackportTooltipContent(tooltipData)
                return
            if contentID == R.views.gui_lootboxes.lobby.gui_lootboxes.tooltips.LootboxTooltip():
                tooltipData = self.__getBackportTooltipData(event)
                if tooltipData and tooltipData.specialArgs and tooltipData.specialArgs[0] is not None:
                    lootBoxIdStr = tooltipData.specialArgs[0].getID()
                    lootBox = self.itemsCache.items.tokens.getLootBoxByID(int(lootBoxIdStr))
                    return LootboxTooltip(lootBox)
            return super(NyQuestsView, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        return (
         (
          self.viewModel.onTypeSelect, self.__onTypeSelect),
         (
          self.viewModel.onInfoClick, self.__onInfoClick),
         (
          self.viewModel.changePersonVoicesEnabled, self.__updateCelebVoicesEnabled),
         (
          self.__nyCtrl.onStateChanged, self.__updateNYState),
         (
          self.__nyCtrl.onDataUpdated, self._update))

    def __getBackportTooltipData(self, event):
        missionParam = event.getArgument('tooltipId', '')
        missionParams = missionParam.rsplit(':', 1)
        if len(missionParams) != 2:
            return self.__tooltipData.get(missionParam)
        missionId, tooltipId = missionParams
        tooltipsData = self.__tooltipData.get(missionId, {})
        return tooltipsData.get(tooltipId)

    def _update(self, *args, **kwargs):
        self.__dailyQuests, self.__weeklyQuests = getNYQuests(self.eventsCache)
        self.__tooltipData.clear()
        with self.viewModel.transaction() as (vm):
            vm.setCurrentTabIdx(self.__subviewTabIdx)
            vm.setIsPersonVoicesEnabled(self.__nyCtrl.isQuestsCelebVoiceoverEnabled())
            self.__updateBattleTypes(vm.getBattleTypes())
            self.__updateQuests(vm.getQuests())
            self.__updateQuestsCountdown(vm)
            self.__updateLevels(vm)
            self.__updateCelebText(vm)

    def __updateNYState(self):
        if not self.__nyCtrl.isEnabled():
            from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
            from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_HANGAR)), EVENT_BUS_SCOPE.LOBBY)

    def __updateQuests(self, questsInModelToUpdate):
        questsInModelToUpdate.clear()
        quests = self.__dailyQuests if self.__subviewTabIdx == 0 else self.__weeklyQuests
        seenQuests = set(getNYSetting(NY_SEEN_QUESTS))
        updatedSeenQuests = []
        self.__minLevel = MAX_VEHICLE_LEVEL
        self.__maxLevel = MIN_VEHICLE_LEVEL
        for questID, quest in sorted(quests.iteritems(), key=lambda (_, q): not isinstance(q, TokenQuest)):
            questVehDescr = quest.vehicleReqs.getConditions().find('vehicleDescr')
            if questVehDescr is not None:
                levels = questVehDescr.getData()['levels'][0][1]
                self.__minLevel = min(self.__minLevel, *levels)
                self.__maxLevel = max(self.__maxLevel, *levels)
            packer = getEventUIDataPacker(quest, bonusPackerGetter=getNewYearBonusPacker)
            questModel = packer.pack()
            isQuestSeen = questID in seenQuests
            if not isQuestSeen:
                updatedSeenQuests.append(questID)
            questModel.setIsFirstView(not isQuestSeen)
            self.__tooltipData[questID] = packer.getTooltipData()
            if questVehDescr is None:
                modifyTokenQuestConditions(quest, questModel)
            else:
                modifyPostbattleConditions(quest, questModel)
            questModel.setStatus(EventStatus.DONE if quest.isCompleted() else EventStatus.ACTIVE)
            questModel.setDescription(quest.getDescription())
            questsInModelToUpdate.addViewModel(questModel)
            self.eventsCache.questsProgress.markQuestProgressAsViewed(questID)

        if self.__minLevel > self.__maxLevel:
            self.__minLevel = MIN_VEHICLE_LEVEL
            self.__maxLevel = MAX_VEHICLE_LEVEL
        self.__updateSeenQuests(updatedSeenQuests)
        seenQuests.update(updatedSeenQuests)
        setNYSettings(NY_SEEN_QUESTS, list(seenQuests))
        questsInModelToUpdate.invalidate()
        return

    def __updateSeenQuests(self, seenQuests):
        for questID in seenQuests:
            self.__unseenEventsManager.seenEvent(questID, 1)

    def __updateQuestsCountdown(self, model):
        questItems = self.__dailyQuests.items() if self.__subviewTabIdx == 0 else self.__weeklyQuests.items()
        model.setCountDown(int(self.__extractResetTime(questItems)))

    def __extractResetTime(self, questItems):
        result = _INT_MAX_VALUE
        for _, quest in questItems:
            result = min(result, quest.getFinishTimeLeft())

        return result

    def __updateLevels(self, model):
        model.setMinLevel(self.__minLevel)
        model.setMaxLevel(self.__maxLevel)

    @staticmethod
    def __updateCelebText(model):
        model.setPersonTextNumber(getCurrentWeek())

    @args2params(int)
    def __onTypeSelect(self, typeId):
        if typeId is not None:
            self.__subviewTabIdx = int(typeId)
            self._update()
        return

    def __onInfoClick(self):
        self._goToByViewAlias(ViewAliases.INFO_VIEW, None, True, startTab=Tabs.QUESTS, previousViewAlias=ViewAliases.QUESTS_VIEW, saveHistory=True)
        return

    def __updateBattleTypes(self, battleTypes):
        battleTypes.clear()
        allQuests = sorted(self.eventsCache.getAllQuests().iteritems())
        _, nyQuest = findFirst(lambda (questID, _): questID.startswith(CurrentNYConstants.NY_DAILY_QUESTS_PREFIX), allQuests, ('',
                                                                                                                               None))
        if nyQuest is not None:
            bonusTypes = nyQuest.preBattleCond.getConditions().find('bonusTypes').getValue()
            for bonusType in bonusTypes:
                battleTypes.addString(str(bonusType))

        self.__battleTypes = battleTypes
        battleTypes.invalidate()
        return

    def __updateCelebVoicesEnabled(self):
        with self.viewModel.transaction() as (ts):
            isEnabled = not self.__nyCtrl.isQuestsCelebVoiceoverEnabled()
            ts.setIsPersonVoicesEnabled(isEnabled)
            setNYSettings(NY_IS_QUESTS_CELEB_VOICEOVERS_ENABLED, isEnabled)
        self.__uiLogger.logQuestsVoiceoverSwitch(isEnabled)