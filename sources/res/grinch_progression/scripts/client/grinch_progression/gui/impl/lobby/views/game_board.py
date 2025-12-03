import logging
from functools import partial
import typing, adisp
from ClientSelectableCameraObject import ClientSelectableCameraObject
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from frameworks.wulf import Array
from frameworks.wulf import WindowFlags
from grinch.gui.grinch_gui_constants import ABILITY_COMMANDS
from grinch.skeletons.battle_controller import IGrinchController
from grinch_progression.account_helpers.account_settings import getCompletedQuests, setCompletedQuests, getCurrentVehicle, setCurrentVehicle
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.ability_model import AbilityModel
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.enums import RewardState, RewardRarity
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.game_board_view_model import GameBoardViewModel
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.rewards_model import RewardsModel
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.tank_card_model import TankCardModel, VehicleStates
from grinch_progression.gui.impl.lobby.tooltips.ability_tooltip_view import AbilityTooltipView
from grinch_progression.gui.impl.lobby.tooltips.chapter_info_tooltip_view import ChaptersTooltipView
from grinch_progression.gui.impl.lobby.views.bonus_packer import updateRewardBonuses
from grinch_progression.gui.impl.lobby.views.hints_helper import HintsHelper
from grinch_progression.gui.impl.lobby.views.quests_helper import VehicleRoleStr, vehicleRoleStrToModel, getDailyModifiersQuest, getWeekendQuests, getSpecialQuestQuests
from grinch_progression.gui.impl.lobby.views.quests_packer import getGrinchUIDataPacker
from grinch_progression.gui.impl.sounds import GAME_BOARD_SOUND_SPACE
from grinch_progression.gui.shared.event_dispatcher import showGameBoardProgressionInfoView
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from grinch_progression_common import getAvailableForClaimingSteps
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.Waiting import Waiting
from gui.impl.gen import R
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.common.view_mixins import LobbyHeaderVisibility
from gui.impl.pub import WindowImpl
from gui.impl.pub.view_component import ViewComponent
from gui.server_events.events_helpers import EventInfoModel
from gui.shared import g_eventBus, events
from gui.shared.event_dispatcher import showModeSelectorWindow, showLobbyMenu
from gui.shared.utils.key_mapping import getReadableKey
from gui.shared.utils.scheduled_notifications import SimpleNotifier, Notifiable
from helpers import dependency, time_utils
from shared_utils import nextTick
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
if typing.TYPE_CHECKING:
    from typing import Optional, Any, List, Tuple
    from grinch_progression.gui.impl.gen.view_models.views.lobby.views.enums import VehicleRole
    from grinch.gui.game_control.grinch_controller import GrinchController
    from grinch_progression.gui.game_control import GrinchProgressionController
    from gui.shared.items_cache import ItemsCache
    from frameworks.wulf import ViewEvent
    from season_common import GameSeason
    from Vehicle import Vehicle
_logger = logging.getLogger(__name__)
_TANK_NAME_TO_VEH_ROLE = {'Ch48_BZ_75_grinch': VehicleRoleStr.ASSAULT, 
   'F88_AMX_13_105_grinch': VehicleRoleStr.CARRIER, 
   'G89_Leopard1_grinch': VehicleRoleStr.SUPPORT}
_TANK_ORDER = [
 VehicleRoleStr.CARRIER, VehicleRoleStr.SUPPORT, VehicleRoleStr.ASSAULT]

def getTankRoleStr(vehicleName):
    return _TANK_NAME_TO_VEH_ROLE.get(vehicleName, VehicleRoleStr.CARRIER)


_AMMO_START_IDX = 0
_AMMO_COUNT = 1
_EQUIPMENT_START_IDX = _AMMO_START_IDX + _AMMO_COUNT
_EQUIPMENT_COUNT = len(ABILITY_COMMANDS)
_TOTAL_PANEL_SLOTS = _AMMO_COUNT + _EQUIPMENT_COUNT
_INVALID_STEP_ID = -1

class GameBoardWindow(WindowImpl):

    def __init__(self, layer, **kwargs):
        super(GameBoardWindow, self).__init__(content=GameBoardView(), wndFlags=WindowFlags.WINDOW, layer=layer)


class GameBoardView(ViewComponent, LobbyHeaderVisibility, Notifiable):
    LAYOUT_ID = R.views.grinch_progression.mono.lobby.game_board()
    _COMMON_SOUND_SPACE = GAME_BOARD_SOUND_SPACE
    __gpController = dependency.descriptor(IGrinchProgressionController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __grinchCtrl = dependency.descriptor(IGrinchController)
    __eventsCache = dependency.descriptor(IEventsCache)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, *args, **kwargs):
        super(GameBoardView, self).__init__(self.LAYOUT_ID, GameBoardViewModel, *args, **kwargs)
        self.__hintHelper = HintsHelper()
        self.__isMovingToInfo = False
        self.__sortedVehicles = None
        ClientSelectableCameraObject.deselectAll()
        return

    @property
    def viewModel(self):
        return super(GameBoardView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.grinch_progression.mono.lobby.tooltips.ability_tooltip():
            intCD = event.getArgument('intCD')
            keyString = event.getArgument('keyString')
            return AbilityTooltipView(int(intCD), keyString)
        if contentID == R.views.grinch_progression.mono.lobby.tooltips.chapters_info_tooltip():
            return ChaptersTooltipView()
        return super(GameBoardView, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        return super(GameBoardView, self)._getEvents() + (
         (
          self.viewModel.onViewLoaded, self.__onViewLoaded),
         (
          self.viewModel.onChangeTank, self.__onChangeTank),
         (
          self.viewModel.onShowGameBoardInfo, self.__onShowGameBoardInfo),
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onOpenLobbyMenu, self.__onOpenLobbyMenu),
         (
          self.viewModel.onCompletedMissionShown, self.__onCompletedMissionShown),
         (
          self.viewModel.onClaimReward, self.__onClaimReward),
         (
          self.__eventsCache.onSyncCompleted, self.__update),
         (
          self.__itemsCache.onSyncCompleted, self.__update),
         (
          g_currentVehicle.onChanged, self.__onVehicleChanged),
         (
          self.__gpController.onDataUpdated, self.__onDataUpdated))

    def _onLoading(self, *args, **kwargs):
        super(GameBoardView, self)._onLoading(*args, **kwargs)
        Waiting.show('loadHangarSpace')
        self.__gpController.setIsFirstEntry(False)
        g_currentPreviewVehicle.selectNoVehicle()
        self.__sortedVehicles = self._getSortedVehicles()
        self.__selectVehicle()
        self.addNotificator(SimpleNotifier(self.__getTimer, self.__timerUpdate))
        self.startNotification()
        self.__update()

    def _onLoaded(self, *args, **kwargs):
        super(GameBoardView, self)._onLoaded(*args, **kwargs)
        self.suspendLobbyHeader(self.uniqueID)

    def _subscribe(self):
        super(GameBoardView, self)._subscribe()
        g_clientUpdateManager.addCallbacks({'cache.vehsLock': self.__onVehicleLockUpdated})

    def _unsubscribe(self):
        super(GameBoardView, self)._unsubscribe()
        g_clientUpdateManager.removeObjectCallbacks(self)

    def _finalize(self):
        if not self.__isMovingToInfo:
            nextTick(partial(self.__hintHelper.setFightButtonFlag, False))()
        self.__hintHelper.clear()
        self.resumeLobbyHeader(self.uniqueID)
        super(GameBoardView, self)._finalize()

    def __update(self, *args, **kwargs):
        currentPoints = self.__gpController.getPoints()
        prevPoints = self.__gpController.getPreviousPointsCount()
        claimStats = self.__gpController.getClaimStats()
        tankProgression = claimStats.claimedPoints + self.__gpController.getPoints()
        with self.viewModel.transaction() as (model):
            self.__updateHeader()
            model.setPoints(currentPoints)
            model.setPrevPoints(prevPoints)
            model.setTankProgression(tankProgression)
            if g_currentVehicle.intCD:
                model.setSelectedVehicleIntCD(g_currentVehicle.intCD)
            self.__updateMissions(model)
            self.__updateRewards(model)
            self.__updateTanksCards(model)
            self.__updateIsLastDay(model)
        if prevPoints != currentPoints:
            self.__gpController.setPreviousPointsCount(currentPoints)

    def __getTimer(self):
        timeLeft = self.__grinchCtrl.getClosestStateChangeTime() - time_utils.getCurrentLocalServerTimestamp()
        if timeLeft > 0:
            return timeLeft + 1
        return 0

    def __timerUpdate(self):
        self.__updateHeader()

    def __updateHeader(self):
        chapterId = self.__gpController.getCurrentChapter()
        now = time_utils.getCurrentLocalServerTimestamp()
        chapterSeason = self.__getSeasonByChapterID(chapterId)
        if not chapterSeason:
            _logger.warning('chapterSeason empty')
            return
        lastActiveSeason = self.__grinchCtrl.getCurrentSeason() or self.__grinchCtrl.getPreviousSeason()
        if not lastActiveSeason:
            _logger.warning('lastActiveSeason empty')
            return
        with self.viewModel.transaction() as (model):
            model.setEventEndDate(self.__grinchCtrl.getAllSeasonsEndDate())
            if now < chapterSeason.getStartDate():
                model.setEventStartDate(chapterSeason.getStartDate())
            elif lastActiveSeason:
                model.setEventStartDate(lastActiveSeason.getStartDate())

    def __updateIsLastDay(self, model):
        now = time_utils.getServerUTCTime()
        endDate = self.__grinchCtrl.getAllSeasonsEndDate()
        isLastDay = endDate - now <= time_utils.ONE_DAY
        model.setIsLastDay(isLastDay)

    def _getSortedVehicles(self):
        vehicles = [ (intCD, self.__itemsCache.items.getItemByCD(intCD)) for intCD in self.__gpController.getGrinchVehicles()
                   ]
        return sorted(vehicles, key=lambda (_, veh): _TANK_ORDER.index(getTankRoleStr(veh.name.split(':')[1])))

    def __updateTanksCards(self, model):
        tankCardsModel = model.getTankCards()
        tankCardsModel.clear()
        for intCD, vehicle in self.__sortedVehicles:
            vehicle = self.__itemsCache.items.getItemByCD(intCD)
            vehicleName = vehicle.name.split(':')[1]
            tankCardModel = TankCardModel()
            tankCardModel.setIntCD(intCD)
            tankCardModel.setResourceKey(vehicleName)
            tankCardModel.setVehicleState(self.__getVehicleState(vehicle))
            tankCardModel.setBonusPoints(self.__getModiferValue(vehicle))
            roleStr = getTankRoleStr(vehicleName)
            tankCardModel.setRole(vehicleRoleStrToModel(roleStr))
            abilitiesModel = tankCardModel.getAbilities()
            abilitiesModel.clear()
            role = vehicleRoleStrToModel(roleStr)
            abilitiesModel.addViewModel(self.__getGunAbilityModel(vehicle, _AMMO_START_IDX, role))
            for index, eqId in enumerate(vehicle.getBuiltInEquipmentIDs()):
                abilitiesModel.addViewModel(self.__getEquipmentAbilityModel(eqId, index + 1, role))

            tankCardsModel.addViewModel(tankCardModel)
            abilitiesModel.invalidate()

        tankCardsModel.invalidate()

    def __getVehicleState(self, vehicle):
        if vehicle.isInBattle:
            return VehicleStates.INBATTLE
        if vehicle.isInUnit:
            return VehicleStates.INPLATOON
        return VehicleStates.DEFAULT

    def __getGunAbilityModel(self, vehicle, index, role):
        abilityModel = AbilityModel()
        shell = vehicle.gun.descriptor.shots[0].shell
        abilityModel.setResourceKey(shell.name)
        abilityModel.setIntCD(vehicle.gun.intCD)
        abilityModel.setKeyString(self.__getKeyString(index))
        abilityModel.setRole(role)
        return abilityModel

    def __getEquipmentAbilityModel(self, eqId, index, role):
        abilityModel = AbilityModel()
        equipment = self.__itemsCache.items.getItemByCD(eqId)
        abilityModel.setResourceKey(equipment.name)
        abilityModel.setIntCD(eqId)
        abilityModel.setKeyString(self.__getKeyString(index))
        abilityModel.setRadius(equipment.descriptor.radius or 0)
        abilityModel.setDuration(equipment.descriptor.duration or 0)
        abilityModel.setDebuffDuration(equipment.descriptor.debuffDuration or 0)
        abilityModel.setRole(role)
        abilityModel.setPosition(index)
        return abilityModel

    def __updateMissions(self, model):
        missionsModel = model.getMissions()
        missionsModel.clear()
        if not g_currentVehicle.intCD:
            return
        quests = []
        quests.extend(getWeekendQuests(role=VehicleRoleStr.ASSAULT))
        quests.extend(getWeekendQuests(role=VehicleRoleStr.CARRIER))
        quests.extend(getWeekendQuests(role=VehicleRoleStr.SUPPORT))
        quests.extend(getSpecialQuestQuests())
        completedQuests = getCompletedQuests()
        for quest in quests:
            seenQuestID = quest.getID()
            missionCompletedVisited = seenQuestID in completedQuests
            if quest.isCompleted():
                if missionCompletedVisited:
                    continue
                else:
                    completedQuests.add(seenQuestID)
            mModel = getGrinchUIDataPacker(quest).pack()
            missionsModel.addViewModel(mModel)

        missionsModel.invalidate()
        model.setMissionRefreshTime(EventInfoModel.getDailyProgressResetTimeDelta())

    def __updateRewards(self, model):
        curChapterID = self.__gpController.getCurrentChapter()
        remainingPoints = self.__gpController.getPoints()
        rewardsModel = model.getRewards()
        rewardsModel.clear()
        stepsToOpen = getAvailableForClaimingSteps(self.__gpController.getActiveChapters(), self.__gpController.getUserProgression(), remainingPoints)
        chapterValue = self.__gpController.getCurrentChapterData()
        steps = chapterValue['steps']
        for stepId, step in enumerate(steps, 1):
            bonusDict = step['bonus']
            rewardModel = RewardsModel()
            rewardModel.setStep(stepId)
            rewardModel.setIndex(stepId - 1)
            rewardModel.setPrice(step['price'])
            updateRewardBonuses(bonusDict, rewardModel)
            if self.__gpController.isStepClaimed(self.__gpController.getCurrentChapter(), stepId):
                rewardModel.setState(RewardState.CLAIMED)
            elif stepId in stepsToOpen.get(curChapterID, tuple()):
                rewardModel.setState(RewardState.AVAILABLE)
            else:
                rewardModel.setState(RewardState.NOTAVAILABLE)
            rewardsModel.addViewModel(rewardModel)

        self._addRepeatableReward(rewardsModel)
        rewardsModel.invalidate()

    def _addRepeatableReward(self, rewardsModel):
        rewardModel = RewardsModel()
        rewardModel.setStep(self.__gpController.getMaxChapterStep())
        rewardModel.setIndex(self.__gpController.getMaxChapterStep())
        rewardModel.setRarity(RewardRarity.COMMON)
        price = self.__gpController.getFinalStepPrice()
        rewardModel.setAmount(self.__gpController.getPoints())
        rewardModel.setName('random')
        rewardModel.setPrice(price)
        rewardModel.setId('finalStep')
        claimStats = self.__gpController.getClaimStats()
        areAllRewardsClaimed = self.__gpController.getMaxChapterStep() == claimStats.claimedCount
        enoughPointsToClaim = self.__gpController.getPoints() >= price
        rewardModel.setState(RewardState.AVAILABLE if areAllRewardsClaimed and enoughPointsToClaim else RewardState.NOTAVAILABLE)
        rewardsModel.addViewModel(rewardModel)

    def __onClose(self):
        showModeSelectorWindow()
        self.__hintHelper.setFightButtonFlag(False)

    def __onOpenLobbyMenu(self):
        showLobbyMenu()

    def __onChangeTank(self, args):
        intCD = args.get('intCD')
        if intCD:
            self.__selectVehicle(int(intCD))
            self.__updateMissions(self.viewModel)

    def __onShowGameBoardInfo(self):
        self.__isMovingToInfo = True
        showGameBoardProgressionInfoView()

    def __onVehicleChanged(self):
        if g_currentVehicle.intCD:
            with self.viewModel.transaction() as (model):
                model.setSelectedVehicleIntCD(g_currentVehicle.intCD)

    def __getKeyString(self, idx):
        if _AMMO_START_IDX <= idx < _EQUIPMENT_START_IDX:
            _logger.debug('[GameBoardView] Index is of an ammo slot, ammo slots should not have keybindings.')
            return ''
        relativeEquipmentIndex = idx - _EQUIPMENT_START_IDX
        command = ABILITY_COMMANDS[relativeEquipmentIndex]
        return getReadableKey(command)

    def __getModiferValue(self, vehicle):
        for quest in getDailyModifiersQuest():
            if quest.vehicleReqs.isAvailable(vehicle) and not quest.isCompleted():
                return quest.getRawBonuses().get('tokens', {}).get(self.__gpController.token, {}).get('count', 0)

        return 0

    def __selectVehicle(self, intCD=None):
        if not intCD:
            intCD = getCurrentVehicle()
        if not intCD:
            intCD, _ = self.__sortedVehicles[0]
        g_currentVehicle.selectVehicleByCD(intCD)
        setCurrentVehicle(intCD)

    def __onVehicleLockUpdated(self, _):
        with self.viewModel.transaction() as (model):
            self.__updateTanksCards(model)

    def __onDataUpdated(self):
        self.__update()

    def __onCompletedMissionShown(self, args):
        seenQuestID = args.get('questId')
        completedQuests = getCompletedQuests()
        completedQuests.add(seenQuestID)
        setCompletedQuests(completedQuests)
        self.__updateMissions(self.viewModel)

    @args2params(int)
    def __onClaimReward(self, step):
        self.onClaimReward(step)

    @adisp.adisp_process
    def onClaimReward(self, step):
        chapterId = self.__gpController.getCurrentChapter()
        result = yield self.__gpController.claimReward(chapterId, step)
        if not result.success:
            return
        with self.viewModel.transaction() as (model):
            self.__updateRewards(model)
            self.__updateHeader()

    def __getSeasonByChapterID(self, chapterId):
        for season in self.__grinchCtrl.getAllSeasons():
            if season.getNumber() == chapterId:
                return season

        return

    def destroy(self):
        if Waiting.isVisible():
            Waiting.hide('loadHangarSpace')
        super(GameBoardView, self).destroy()

    def __onViewLoaded(self):
        Waiting.hide('loadHangarSpace')
        g_eventBus.handleEvent(events.ViewReadyEvent(self.layoutID))