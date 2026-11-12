import typing, SoundGroups
from debug_utils import LOG_ERROR
from gui.impl.gui_decorators import args2params
from helpers import dependency
from helpers.time_utils import getCurrentTimestamp
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import IndicatorType
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_item_leaderboard_point import NyPetItemLeaderboardPoint
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_model import IndicatorType as PetNeedType, NyPetModel, State
from new_year.gui.impl.lobby.new_year.ny_leaderboard_recount_view import NyLeaderboardRecountViewWindow
from new_year.gui.impl.lobby.new_year.sub_model_presenter import SubModelPresenter
from new_year.helpers.server_settings import getNewYearGeneralConfig, getNewYearRaidConfig
from new_year.ny_constants import PERCENT
from new_year.skeletons.new_year import ITamagotchiDataProvider, INewYearController, INewYearTamagotchiController, IRaccoonAnimationController
from new_year.gui.impl.new_year.sounds import RaccoonMood
from new_year_common.items.components.ny_constants import RaidState
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from new_year.tamagotchi.dto.player_info import PlayerInfo
    from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel

class NyPetIndicatorsBlock(SubModelPresenter):
    __slots__ = ()
    _INTERNAL_VIEW_STATE = None
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _itemsCache = dependency.descriptor(IItemsCache)
    _nyController = dependency.descriptor(INewYearController)
    _tamagotchiController = dependency.descriptor(INewYearTamagotchiController)
    _raccoonCtrl = dependency.descriptor(IRaccoonAnimationController)
    _MOOD_TO_SOUND = {State.FUN: RaccoonMood.FUN, 
       State.NORMAL: RaccoonMood.NORMAL, 
       State.SAD: RaccoonMood.SAD}

    @property
    def viewModel(self):
        return self.getViewModel()

    def initialize(self, *args, **kwargs):
        self.__buildCards()
        self.updateViewModel()
        super(NyPetIndicatorsBlock, self).initialize(*args, **kwargs)

    def finalize(self):
        super(NyPetIndicatorsBlock, self).finalize()
        self.__resetIndicators()
        self.clear()

    def updateViewModel(self):
        pInfo = self._dataProvider.playerInfo
        with self.viewModel.transaction() as (model):
            self.__fillHeader(model, pInfo)
            self.__fillNeeds(model)
            for indicatorName, points in pInfo.indicators.iteritems():
                indicatorType = IndicatorType(indicatorName)
                vm = self.getIndicator(indicatorType, model)
                self.applyIndicatorData(indicatorName, vm, points)

    @staticmethod
    def getIndicator(indType, tx):
        for indicator in (tx.foodIndicator, tx.funIndicator, tx.activityIndicator):
            if indicator.getType() == indType:
                return indicator

        LOG_ERROR('invalid indicator type - ', indType.value)
        return

    @staticmethod
    def getUnlockLevel(indicatorName):
        return getNewYearGeneralConfig().getRaccoonIndicatorLevelOpen(indicatorName)

    @classmethod
    def isIndicatorLocked(cls, indicatorName):
        return cls._dataProvider.isIndicatorLocked(indicatorName)

    @classmethod
    def applyUnlockState(cls, vm, indicatorName):
        unlockLevel = cls.getUnlockLevel(indicatorName)
        vm.setAtmosphereLevelToUnlock(unlockLevel)
        vm.setIsLocked(cls.isIndicatorLocked(indicatorName))

    @classmethod
    def applyIndicatorData(cls, name, vm, points):
        config = cls._dataProvider.config.indicators[name]
        vm.setMaxPoint(config.maxPoints)
        vm.setItemScalePoint(config.item.scalePoint)
        cls.applyUnlockState(vm, name)
        if points < 0 and not cls.isIndicatorLocked(name):
            points = 0
        vm.setCurPoint(min(max(points, 0), config.maxPoints))
        vm.setItemCount(cls._dataProvider.getIndicatorCurrency(name))
        vm.setBonus(cls._dataProvider.getIndicatorDeb(name))
        vm.setScaleDowngradeTime(cls._dataProvider.getIndicatorStateDecayTime(name))
        vm.setScaleEmptyTime(cls._dataProvider.getIndicatorDecayTime(name))
        levels = vm.getScaleLevels()
        levels.clear()
        for lvl in config.levels[1::]:
            levels.addNumber(lvl.points)

        levels.invalidate()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onResetWasOverflowed, self.__onResetWasOverflowed),
         (
          self._itemsCache.onSyncCompleted, self.__onSyncCompleted),
         (
          self._dataProvider.onSimulationEnd, self.__onSimulationEnd),
         (
          self._dataProvider.onItemsActivateRequested, self.__onItemsActivateRequested),
         (
          self._dataProvider.onItemsActivated, self.__onItemsActivated),
         (
          self._dataProvider.onRaidReadyUpdated, self.__onRaidReadyUpdated),
         (
          self._dataProvider.onTamagotchiRaidViewEnabledChanged, self.__onTamagotchiRaidViewEnabledChanged),
         (
          self._dataProvider.onPlayerInfoUpdated, self.__onPlayerInfoUpdated),
         (
          self._tamagotchiController.onRaidDataUpdated, self.__onRaidDataUpdated))

    def __buildCards(self):
        with self.viewModel.transaction() as (model):
            model.foodIndicator.setType(IndicatorType.FOOD)
            model.funIndicator.setType(IndicatorType.FUN)
            model.activityIndicator.setType(IndicatorType.ACTIVITY)

    def __fillHeader(self, model, player):
        self.__fillHeaderBonus(model)
        raidState = self._tamagotchiController.getRaidState()
        self.__fillHeaderRaidInfo(model)
        mood = self.__resolvePetMood(raidState, player)
        self.__applyPetMood(model, mood)
        self.__syncRaidTvPresentation(raidState)

    def __fillHeaderBonus(self, model):
        maxBonus = self._nyController.getMaxBonusValue() * PERCENT
        currBonus = self._nyController.getActiveSettingBonusValue() * PERCENT + self._dataProvider.getDeb()
        model.setCurBonus(min(currBonus, maxBonus))
        model.setMaxBonus(maxBonus)

    def __fillHeaderRaidInfo(self, model):
        model.setRaidViewEnabled(self._dataProvider.isTamagotchiRaidViewEnabled)
        model.setIsRaidReady(self._dataProvider.isReadyForRaid())
        raidBoost = getNewYearRaidConfig().get('raidBoost', {})
        model.setRaidRemainingTime(self._dataProvider.getRaidRemainingTime())
        model.setCanUseRaidSpeedup(self._tamagotchiController.getRaidBoostAmount() > 0)
        model.setBoostAmount(self._tamagotchiController.getRaidBoostAmount())
        model.setMaxBoostLimit(raidBoost.get('limit', 0))

    def __resolvePetMood(self, raidState, player):
        if raidState == RaidState.FINISHED:
            return State.LOOT
        if raidState == RaidState.ACTIVE:
            return State.RAID
        return State(player.state.lower())

    def __applyPetMood(self, model, mood):
        if model.getState() != mood:
            self._applyRaccoonSoundMood(mood)
        model.setState(mood)
        if mood in self._MOOD_TO_SOUND:
            self._raccoonCtrl.updateMoodState(mood)

    def __syncRaidTvPresentation(self, raidState):
        if raidState == RaidState.ACTIVE:
            self._raccoonCtrl.setRaidActive(True)
        elif raidState == RaidState.FINISHED:
            self._raccoonCtrl.endRaidTvPresentation()
        else:
            self._raccoonCtrl.setRaidActive(False)

    def __fillNeeds(self, model):
        needs = model.getPetNeeds()
        needs.clear()
        raidState = self._tamagotchiController.getRaidState()
        if raidState in (RaidState.ACTIVE, RaidState.FINISHED):
            pass
        elif self._dataProvider.isReadyForRaid():
            needs.addString(PetNeedType.RAID.value)
        else:
            for name in self._dataProvider.getNeeds():
                needs.addString(name)

        needs.invalidate()

    def __onSyncCompleted(self, *_, **__):
        self._dataProvider.syncOpenedIndicators()
        self.updateViewModel()

    def __onRaidDataUpdated(self, *_):
        self._dataProvider.setRaidReady()
        self.updateViewModel()

    def __onRaidReadyUpdated(self, *_):
        self.updateViewModel()

    def __onTamagotchiRaidViewEnabledChanged(self, value):
        self.viewModel.setRaidViewEnabled(value)

    def __onPlayerInfoUpdated(self, isSuccess):
        if not isSuccess:
            self.updateViewModel()

    def __onSimulationEnd(self):
        self.updateViewModel()

    @args2params(IndicatorType)
    def __onResetWasOverflowed(self, type):
        self.getIndicator(type, self.viewModel).setWasOverflowed(False)

    def __onItemsActivateRequested(self, *_, **__):
        self.__toggleIndicatorsWaiting(True)

    def __onItemsActivated(self, isSuccess, itemId, count, isRecalculation):
        self.__toggleIndicatorsWaiting(False)
        if not isSuccess and isRecalculation:
            NyLeaderboardRecountViewWindow(parent=self.getParentWindow()).load()
            return
        with self.viewModel.transaction() as (tx):
            for name, indicator in self._dataProvider.config.indicators.iteritems():
                if indicator.item.id != itemId:
                    continue
                self._raccoonCtrl.activateItem(name)
                indicatorType = IndicatorType(name)
                model = self.getIndicator(indicatorType, tx)
                model.setWasOverflowed(self._dataProvider.playerInfo.indicators[name] >= indicator.maxPoints)
                if not self._dataProvider.isLeaderboardFinished:
                    points = model.getItemLeaderboardPoint()
                    item = NyPetItemLeaderboardPoint()
                    item.setId(getCurrentTimestamp())
                    item.setValue(count * indicator.item.leaderboardPoint)
                    item.setType(indicatorType)
                    points.addViewModel(item)
                    points.invalidate()

    def __toggleIndicatorsWaiting(self, state):
        with self.viewModel.transaction() as (tx):
            tx.foodIndicator.setIsLoading(state)
            tx.funIndicator.setIsLoading(state)
            tx.activityIndicator.setIsLoading(state)

    def __resetIndicators(self):
        with self.viewModel.transaction() as (tx):
            for indicatorName, _ in self._dataProvider.playerInfo.indicators.iteritems():
                array = self.getIndicator(IndicatorType(indicatorName), tx).getItemLeaderboardPoint()
                array.clear()
                array.invalidate()

    def _applyRaccoonSoundMood(self, mood):
        nextState = self._MOOD_TO_SOUND.get(mood)
        if nextState is None:
            return
        else:
            SoundGroups.g_instance.setState(RaccoonMood.GROUP, nextState)
            return