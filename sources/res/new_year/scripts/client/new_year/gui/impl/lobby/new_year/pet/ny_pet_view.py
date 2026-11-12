import SoundGroups, typing, CGF
from account_helpers.AccountSettings import LOOT_BOXES_VIEWED_COUNT
from gui.impl.gui_decorators import args2params
from gui.impl.pub import PopOverWindow, WindowImpl
from new_year.gui.impl.lobby.new_year.ny_raid_reward_helpers import prepareRaidRewardResult
from new_year.gui.impl.lobby.new_year.tooltips.ny_pet_raid_boost_tooltip import NyPetRaidBoostTooltip
from new_year.gui.impl.lobby.new_year.tooltips.ny_pet_in_raid_tooltip import NyPetInRaidTooltip
from new_year.gui.impl.lobby.new_year.ny_pet_tv_screen_view import NyPetTvScreenView
from helpers.CallbackDelayer import CallbackDelayer
from new_year.ny_constants import NY_HAS_PET_ANIMATION, NY_TAMAGOTCHI_SEEN_TIPS
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.lootboxes_storage_view_model import ReturnPlace
from new_year_common.items.components.ny_constants import RaidState
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import IndicatorType
from new_year.gui.impl.lobby.new_year.popovers.ny_pet_item_activate_popover import NyPetItemActivatePopover
from new_year.gui.impl.lobby.new_year.tooltips.ny_common_tooltip import NyCommonTooltip, getCommonTooltipArgsFromEvent
from new_year.gui.impl.lobby.new_year.tooltips.ny_pet_bonus_tooltip import NyPetBonusTooltip
from new_year.gui.impl.lobby.new_year.tooltips.ny_pet_indicator_tooltip import NyPetIndicatorTooltip
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.main_view_model import SwitchStates
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_model import NyPetModel, SingleTipType
from new_year.gui.impl.lobby.new_year.pet.ny_pet_indicators_block import NyPetIndicatorsBlock
from new_year.gui.impl.lobby.new_year.ny_leaderboard_recount_view import NyLeaderboardRecountViewWindow
from new_year.gui.impl.lobby.new_year.tooltips.ny_pet_token_stepper_tooltip import NyPetTokenStepperTooltip
from new_year.skeletons.new_year import IRaccoonAnimationController, INewYearCurrencyController, INewYearEnvironmentSwitchController, INewYearTamagotchiController, ITamagotchiDataProvider, INewYearMetricsLogger
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyType
from new_year.gui.impl.lobby.new_year.sub_model_presenter import HistorySubModelPresenter
from new_year.gui.impl.lobby.new_year.pet.ny_pet_shop_view import NyPetShopView
from new_year.helpers.ny_fading_cover import NYFadingCover
from gui_lootboxes.gui.shared.event_dispatcher import showStorageView
from new_year.helpers.server_settings import getNewYearGeneralConfig, getNewYearRaidConfig
from cgf_components.hangar_camera_manager import HangarCameraManager
from cgf_components.view_camera_sync import CameraState
from new_year.gui.impl.new_year.navigation import NewYearNavigation
from new_year.gui.shared.gui_items.processors.ny_processor import ReceiveTamagotchiRaidRewardProcessor
from new_year.ny_constants import InternalViewState, EnvironmentState, NY_TAMAGOTCHI_REPEAT_ONBOARDING_COUNT
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
from new_year.gui.shared.event_dispatcher import showNYPetRaidRewardWindow, openTamagotchiRaidView
from skeletons.festivity_factory import IFestivityFactory
from skeletons.gui.game_control import IGuiLootBoxesController
from new_year.gui.impl.new_year.sounds import RaccoonStates, NewYearSoundEvents
from gui.impl.common.fade_manager import FadeManager
from skeletons.gui.shared.utils import IHangarSpace
from new_year_account_settings import getNYSetting, setNYSettings
from frameworks.wulf import WindowFlags, WindowLayer
from adisp import adisp_process
from helpers import dependency, time_utils
from collections import deque
from functools import partial
from gui.impl.gen import R
_TEXTURE_PATH = 'content/Hangars/h03_mt_ny_2026/environment/h03_NY27_RacconTV_Screen_AM.dds'

class ProgressSequenceSteps(object):

    def __init__(self):
        super(ProgressSequenceSteps, self).__init__()
        self._steps = []

    def init(self):
        pass

    def fini(self):
        pass

    @property
    def _step(self):
        return self._steps and self._steps[0]

    def process(self, progress):
        item = self._step
        while item:
            stepProgress, handler = item
            if progress <= stepProgress:
                break
            handler()
            if self._steps:
                self._steps.popleft()
            item = self._step

    def setSteps(self, steps):
        self._steps = deque(steps)


class NyPetView(HistorySubModelPresenter):
    __slots__ = ('__shopView', '__indicatorsBlock', '__fadeManager', '__fadeSteps',
                 '__indicatorFillActive', '__isFillSoundPlaying', '__displayView',
                 '__internalStateCbDelayer', '__isRestartedOnboarding', '__raidViewEnabled',
                 '__isDecreasedIndicatorsPoints', '__isRaidViewOpened', '__popoverWnd',
                 '__pendingRecountView', '__hasActivatedItemOutsideOnboarding')
    _INTERNAL_VIEW_STATE = InternalViewState.RACCOON
    __raccoonCtrl = dependency.descriptor(IRaccoonAnimationController)
    __guiLootBoxes = dependency.descriptor(IGuiLootBoxesController)
    __nyCurrencyController = dependency.descriptor(INewYearCurrencyController)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __nyEnvSwitcherController = dependency.descriptor(INewYearEnvironmentSwitchController)
    __festivityFactory = dependency.descriptor(IFestivityFactory)
    _tamagotchiController = dependency.descriptor(INewYearTamagotchiController)
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    __uiLogger = dependency.descriptor(INewYearMetricsLogger)

    def __init__(self, viewModel=None, parentView=None, **kwargs):
        super(NyPetView, self).__init__(viewModel, parentView, **kwargs)
        self.__shopView = None
        self.__indicatorsBlock = None
        self.__fadeManager = None
        self.__fadeSteps = ProgressSequenceSteps()
        self.__indicatorFillActive = {IndicatorType.FOOD: False, 
           IndicatorType.FUN: False, 
           IndicatorType.ACTIVITY: False}
        self.__isFillSoundPlaying = False
        self.__displayView = None
        self.__isRestartedOnboarding = False
        self.__internalStateCbDelayer = CallbackDelayer()
        self.__raidViewEnabled = False
        self.__isDecreasedIndicatorsPoints = False
        self.__isRaidViewOpened = False
        self.__popoverWnd = None
        self.__pendingRecountView = False
        self.__hasActivatedItemOutsideOnboarding = False
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @property
    def hangarCameraManager(self):
        return CGF.getManager(self.__hangarSpace.spaceID, HangarCameraManager)

    @property
    def __fadeStates(self):
        return (
         (
          0.85, self.__fadeManager.show),
         (
          0.97, partial(self.__updateInternalViewState, True)),
         (
          0.99, partial(self.__nyEnvSwitcherController.switchEnvironment, EnvironmentState.RACCOON.value)))

    def initialize(self, isLoadedFromHangar, *args, **kwargs):
        self.__fadeManager = FadeManager(layer=WindowLayer.VIEW, coverFactory=NYFadingCover)
        self.__initRaccoonFlyState(isLoadedFromHangar)
        raidBoost = getNewYearRaidConfig().get('raidBoost', {})
        SoundGroups.g_instance.setState(RaccoonStates.GROUP, RaccoonStates.MAIN)
        blockByRecalc = self._dataProvider.isOnboarding and self._dataProvider.isLeaderboardRecalcPeriod
        isOnboarding = self._dataProvider.isOnboarding and not blockByRecalc
        with self.viewModel.transaction() as (model):
            model.lootBox.setIsLootBoxesEnabled(self.__guiLootBoxes.isLootBoxesAvailable())
            model.setIsGuiLootBoxesVisible(self.__guiLootBoxes.isEnabled())
            model.setIsOnboarding(isOnboarding)
            model.setIsRestartedOnboarding(self.__isRestartedOnboarding)
            model.setHasPetAnimations(getNYSetting(NY_HAS_PET_ANIMATION))
            model.setWasLeaderboardFinished(self._dataProvider.isLeaderboardFinished)
            model.setIsPetRaidEnabled(self.__getPetRaidVisible())
            model.setBoostsToAdd(raidBoost.get('amount', 0))
            model.setBoostAccrualTime(raidBoost.get('accrualTime', 0) + 3 * time_utils.ONE_HOUR)
        if isOnboarding:
            TamagotchiSysMsgHandler.showSkipMsg()
        self.__indicatorsBlock = NyPetIndicatorsBlock(self.viewModel, self)
        self.__indicatorsBlock.initialize()
        self.__shopView = NyPetShopView(self.viewModel.shop, self)
        self.__shopView.initialize()
        self.__updateLootboxEntryPoint(self.__guiLootBoxes.getBoxesCount())
        self.__resolveAndShowSingleTip()
        if self._tamagotchiController.getRaidState() != RaidState.ACTIVE:
            self.__raccoonCtrl.setRaidActive(False)
        else:
            self.__completePendingTvRaidIfNeeded()
        self.__createDisplayView()
        self._dataProvider.onViewVisibilityChanged(True)
        self.__raidViewEnabled = self._dataProvider.isTamagotchiRaidViewEnabled
        self.__uiLogger.logPetScreenOpened()
        if blockByRecalc and isLoadedFromHangar:
            self.__pendingRecountView = True
        super(NyPetView, self).initialize(*args, **kwargs)
        if blockByRecalc and not isLoadedFromHangar:
            self.__showLeaderboardRecountView()

    def finalize(self):
        super(NyPetView, self).finalize()
        self.__pendingRecountView = False
        self.__popoverWnd = None
        self.viewModel.setIsOnboarding(False)
        self.__saveSeenTip()
        self.__forceStopFillSound()
        SoundGroups.g_instance.playSound2D(NewYearSoundEvents.OLDMAN_ONBOARDING_SKIP)
        self.__internalStateCbDelayer.clearCallbacks()
        self.__shopView.finalize()
        self.__indicatorsBlock.finalize()
        self.__destroyDisplayView()
        if self._tamagotchiController.getRaidState() != RaidState.ACTIVE:
            self.__raccoonCtrl.setRaidActive(False)
        self.__fadeManager.destroy()
        if self.__hangarSpace.spaceID is not None:
            self.__nyEnvSwitcherController.switchEnvironment(self.__nyEnvSwitcherController.userEnvState.value)
        self.__onOnboardingRestartFinish()
        self._dataProvider.onViewVisibilityChanged(False)
        return

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyPetIndicatorTooltip():
            indicatorType = self.__getIndicatorType(event)
            return NyPetIndicatorTooltip(NyPetIndicatorsBlock.getIndicator(indicatorType, self.viewModel))
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyPetBonusTooltip():
            return NyPetBonusTooltip(self.viewModel)
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyPetTokenStepperTooltip():
            indicatorType = self.__getIndicatorType(event)
            return NyPetTokenStepperTooltip(indicatorType)
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyPetRaidBoostTooltip():
            return NyPetRaidBoostTooltip()
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyPetInRaidTooltip():
            return NyPetInRaidTooltip()
        if contentID == R.views.new_year.lobby.new_year.tooltips.CommonTooltip():
            return NyCommonTooltip(*getCommonTooltipArgsFromEvent(event))
        return super(NyPetView, self).createToolTipContent(event, contentID)

    def createPopOver(self, event):
        if event.contentID == R.views.new_year.lobby.new_year.popovers.NyPetItemActivatePopover():
            indicatorType = self.__getIndicatorType(event)
            content = NyPetItemActivatePopover(self.viewModel, NyPetIndicatorsBlock.getIndicator(indicatorType, self.viewModel), indicatorType)
            self.__popoverWnd = window = PopOverWindow(event, content, self.getParentWindow(), WindowLayer.TOP_WINDOW)
            window.load()
            return window
        return super(NyPetView, self).createPopOver(event)

    def _getEvents(self):
        result = (
         (
          self._nyController.onNySettingsChanged, self.__onNySettingsChanged),
         (
          self._nyController.onPetRaidVisibilityUpdated, self.__onPetRaidVisibilityUpdated),
         (
          self.__nyEnvSwitcherController.onEnvironmentSwitched, self.__onEnvironmentSwitched),
         (
          self.__guiLootBoxes.onBoxesCountChange, self.__updateLootboxEntryPoint),
         (
          self.__guiLootBoxes.onAvailabilityChange, self.__onAvailabilityChange),
         (
          self.__guiLootBoxes.onStatusChange, self.__onLootBoxesStatusChange),
         (
          self.__raccoonCtrl.onRaidStateChanged, self.__onRaidStateChanged),
         (
          self.viewModel.onLootBoxEntryPointClick, self.__onLootBoxEntryPointClick),
         (
          self.viewModel.onShopClick, self.__onShopClick),
         (
          self.viewModel.onRaid, self.__onRaid),
         (
          self.viewModel.onRaidSpeedup, self.__onRaidSpeedup),
         (
          self.viewModel.onOnboardingFinish, self.__onOnboardingFinish),
         (
          self.viewModel.onPetStateAnimationsChange, self.__onPetStateAnimationsChange),
         (
          self.viewModel.onDeleteItemLeaderboardPoint, self.__onDeleteItemLeaderboardPoint),
         (
          self.viewModel.onProgressFillSound, self.__onIndicatorFillSound),
         (
          self.viewModel.onCloseSingleTip, self.__onCloseSingleTip),
         (
          self._dataProvider.onOnboardingSkipped, self.__onOnboardingSkipped),
         (
          self._dataProvider.onUpdateTipsRequested, self.__onUpdateTipsRequested),
         (
          self._dataProvider.onItemsActivated, self.__onItemsActivated),
         (
          self._dataProvider.onItemsActivateRequested, self.__onItemsActivateRequested),
         (
          self._dataProvider.onSeasonEnded, self.__onSeasonEnded),
         (
          self._dataProvider.onDecreasedIndicatorsPoints, self.__onDecreasedIndicatorsPoints),
         (
          self._dataProvider.onTamagotchiRaidViewEnabledChanged, self.__onTamagotchiRaidViewEnabledChanged),
         (
          self.viewModel.onOnboardingRestart, self.__onOnboardingRestart))
        if self.__hangarSpace.spaceID is not None and self.hangarCameraManager is not None:
            result += ((self.hangarCameraManager.onProgressChanged, self.__fadeSteps.process),)
        return result

    def __updateInternalViewState(self, skipFlight=False):
        previousState = NyPetView._INTERNAL_VIEW_STATE
        targetState = InternalViewState.RACCOON_TV if self._dataProvider.isRaidActive() else InternalViewState.RACCOON
        self.__destroyPopover()
        self.setInternalViewState(targetState, skipFlight)
        NyPetView._INTERNAL_VIEW_STATE = targetState
        if skipFlight or previousState == targetState:
            return
        if targetState == InternalViewState.RACCOON_TV:
            soundEvent = NewYearSoundEvents.PET_TV_ENTER
        elif previousState == InternalViewState.RACCOON_TV:
            soundEvent = NewYearSoundEvents.PET_TV_EXIT
        else:
            return
        SoundGroups.g_instance.playSound2D(soundEvent)

    def __delayedUpdateViewState(self, skipFlight=False):
        self.__updateInternalViewState(skipFlight or self.__isPetShopOpened())
        self.__internalStateCbDelayer.clearCallbacks()

    def __onRaidStateChanged(self, isActive):
        if not isActive:
            self.__internalStateCbDelayer.clearCallbacks()
            if NyPetView._INTERNAL_VIEW_STATE != InternalViewState.RACCOON_FLY:
                self.__updateInternalViewState(skipFlight=self.__isPetShopOpened())
            return
        self.__internalStateCbDelayer.clearCallbacks()
        self.__internalStateCbDelayer.delayCallback(self.__raccoonCtrl.raidAnimationDuration, self.__delayedUpdateViewState)
        self.__resolveAndShowSingleTip()

    def __isPetShopOpened(self):
        return self.__shopView is not None and self.__shopView.viewModel.getIsShopEnabled()

    def __getIndicatorType(self, event):
        return IndicatorType(event.getArgument('type'))

    def __initRaccoonFlyState(self, isLoadedFromHangar):
        if not isLoadedFromHangar:
            self.__updateInternalViewState(skipFlight=True)
            self.__nyEnvSwitcherController.switchEnvironment(EnvironmentState.RACCOON.value)
            return
        self.setSwitchState(SwitchStates.WITH_SWITCHING_OBJS)
        self.__fadeSteps.setSteps(self.__fadeStates)
        NyPetView._INTERNAL_VIEW_STATE = InternalViewState.RACCOON_FLY

    def __onNySettingsChanged(self):
        config = getNewYearGeneralConfig()
        if config is not None and not config.getPetVisible():
            NewYearNavigation.closeMainView()
        return

    def __onPetRaidVisibilityUpdated(self, isPetRaidEnabled):
        self.viewModel.setIsPetRaidEnabled(isPetRaidEnabled)

    def __getPetRaidVisible(self):
        config = getNewYearRaidConfig()
        if config is not None:
            return config.get('isEnabled', False)
        else:
            return False

    def setCameraState(self, cameraState):
        if cameraState == CameraState.INSTALLED:
            self.__tryShowPendingRecountView()

    def __onEnvironmentSwitched(self):
        self.__fadeManager.hide()

    def __tryShowPendingRecountView(self):
        if not self.__pendingRecountView or not self.isLoaded:
            return
        self.__showLeaderboardRecountView()

    def __showLeaderboardRecountView(self):
        self.__pendingRecountView = False
        NyLeaderboardRecountViewWindow(parent=self.getParentWindow(), shouldCloseMainView=True).load()

    def __updateLootboxEntryPoint(self, count, *_):
        lastViewed = self.__guiLootBoxes.getSetting(LOOT_BOXES_VIEWED_COUNT)
        with self.viewModel.lootBox.transaction() as (model):
            model.setBoxesCount(count)
            model.setHasNew(count > lastViewed)

    def __onAvailabilityChange(self, *_):
        self.viewModel.lootBox.setIsLootBoxesEnabled(self.__guiLootBoxes.isLootBoxesAvailable())

    def __onLootBoxesStatusChange(self):
        self.viewModel.setIsGuiLootBoxesVisible(self.__guiLootBoxes.isEnabled())

    def __onLootBoxEntryPointClick(self, *_):
        showStorageView(returnPlace=ReturnPlace.TO_PET)

    def __onShopClick(self):
        if self.__isRestartedOnboarding:
            self.__onOnboardingRestartFinish()
        self.__forceStopFillSound()
        self.__destroyPopover()
        self.__nyCurrencyController.setVisibleCurrencies(NyCurrencyType.CREDITS)
        self.__shopView.toggleVisibility(True)

    def __onRaid(self):
        if self._tamagotchiController.getRaidState() == RaidState.FINISHED:
            self.__claimRaidReward()
            return
        self.__openRaidView()

    @adisp_process
    def __claimRaidReward(self):
        result = yield ReceiveTamagotchiRaidRewardProcessor().request()
        if result is not None and result.success:
            prepareRaidRewardResult(result)
            showNYPetRaidRewardWindow(next(iter(result.auxData['bonus'])) or {}, parent=self.getParentWindow())
        else:
            TamagotchiSysMsgHandler.sendRaidRewardError()
        return

    def __onRaidSpeedup(self):
        if not self.viewModel.getIsPetRaidEnabled() or not self.viewModel.getCanUseRaidSpeedup():
            return
        self.__openRaidView(isBoostMode=True)

    def __openRaidView(self, isBoostMode=False):
        if self.__isRaidViewOpened:
            return
        if SingleTipType.RAIDAVAILABLE.value not in getNYSetting(NY_TAMAGOTCHI_SEEN_TIPS):
            self.__markTipAsSeen(SingleTipType.RAIDAVAILABLE)
        if self.viewModel.getIsOnboarding() or self.__isRestartedOnboarding:
            self.__onOnboardingFinish()
        self.__isRaidViewOpened = True
        self.__destroyPopover()
        self.__stopSingleTipVoiceover()
        self.__onCloseSingleTip()
        openTamagotchiRaidView(self.getParentWindow(), isBoostMode, self.__raidViewCloseCallback)

    def __destroyPopover(self):
        if self.__popoverWnd is None:
            return
        else:
            self.__popoverWnd.destroy()
            self.__popoverWnd = None
            return

    def __raidViewCloseCallback(self):
        self.__isRaidViewOpened = False
        self.__resolveAndShowSingleTip()

    def __completePendingTvRaidIfNeeded(self):
        if self._tamagotchiController.getRaidState() != RaidState.ACTIVE:
            return
        if self.__raccoonCtrl.isRaidStarted and not self.__raccoonCtrl.isRaidActive:
            self.__raccoonCtrl.beginTvRaidPresentation()

    def __createDisplayView(self):
        if self.__displayView is not None:
            return
        else:
            self.__displayView = NyPetTvScreenView()
            window = WindowImpl(WindowFlags.SURFACE, content=self.__displayView, layer=WindowLayer.VIEW, name=_TEXTURE_PATH, parent=self.getParentWindow())
            window.load()
            return

    def __destroyDisplayView(self):
        if self.__displayView is None:
            return
        else:
            self.__displayView.destroyWindow()
            self.__displayView = None
            return

    def __onOnboardingSkipped(self):
        SoundGroups.g_instance.playSound2D(NewYearSoundEvents.OLDMAN_ONBOARDING_SKIP)
        self.__forceStopFillSound()
        self.viewModel.setIsOnboarding(False)
        self._dataProvider.isOnboarding = False
        self.__onOnboardingRestartFinish()

    def __onItemsActivated(self, isSuccess, *_, **__):
        if isSuccess and not self.viewModel.getIsOnboarding() and not self.__isRestartedOnboarding:
            self.__hasActivatedItemOutsideOnboarding = True
        self.__resolveAndShowSingleTip()

    def __onItemsActivateRequested(self, *_, **__):
        if self._dataProvider.isOnboarding:
            SoundGroups.g_instance.playSound2D(NewYearSoundEvents.OLDMAN_ONBOARDING_SKIP)
            self._dataProvider.isOnboarding = False

    def __onUpdateTipsRequested(self, state):
        if state:
            self.__resolveAndShowSingleTip()
            return
        self.__saveSeenTip()

    def __onTamagotchiRaidViewEnabledChanged(self, value):
        if not value:
            return
        self.__raidViewEnabled = True
        self.__resolveAndShowSingleTip()

    def __onDecreasedIndicatorsPoints(self):
        self.__isDecreasedIndicatorsPoints = True
        self.__resolveAndShowSingleTip()

    def __resolveAndShowSingleTip(self):
        tip = self.__resolveSingleTip()
        if tip is None:
            return
        else:
            self.__forceStopFillSound()
            self.viewModel.setSingleTip(tip)
            return

    def __resolveSingleTip(self):
        if self.__isRaidViewOpened:
            return None
        else:
            seen = getNYSetting(NY_TAMAGOTCHI_SEEN_TIPS)
            if self.viewModel.getIsOnboarding() or self.__isRestartedOnboarding or self._dataProvider.isOnboarding or self.__shopView.viewModel.getIsShopEnabled():
                return None
            return self.__getRegularTip(seen) or self.__getRaidAvailableTip(seen)

    def __getRaidAvailableTip(self, seen):
        if not self.__raidViewEnabled or SingleTipType.RAIDAVAILABLE.value in seen:
            return None
        return SingleTipType.RAIDAVAILABLE

    @staticmethod
    def __markTipAsSeen(tip):
        seen = set(getNYSetting(NY_TAMAGOTCHI_SEEN_TIPS))
        seen.add(tip.value)
        setNYSettings(NY_TAMAGOTCHI_SEEN_TIPS, seen)

    def __getRaidIndicatorLowTip(self, seen):
        if not self.__isDecreasedIndicatorsPoints or SingleTipType.RAIDINDICATORLOW.value in seen:
            return None
        if not self._dataProvider.isRaidActive():
            return None
        else:
            self.__isDecreasedIndicatorsPoints = False
            return SingleTipType.RAIDINDICATORLOW

    def __getRegularTip(self, seen):
        pInfo = self._dataProvider.playerInfo
        raidIndicatorLowTip = self.__getRaidIndicatorLowTip(seen)
        if raidIndicatorLowTip is not None:
            return raidIndicatorLowTip
        else:
            if pInfo.indicators[IndicatorType.FUN.value] >= 0 and SingleTipType.FUNOPENED.value not in seen:
                return SingleTipType.FUNOPENED
            if pInfo.indicators[IndicatorType.ACTIVITY.value] >= 0 and SingleTipType.ACTIVITYOPENED.value not in seen:
                return SingleTipType.ACTIVITYOPENED
            if self.__hasActivatedItemOutsideOnboarding and not self._dataProvider.isLeaderboardFinished:
                if SingleTipType.LEADERBOARD.value in seen:
                    return
                for name, points in pInfo.indicators.iteritems():
                    lastLevel = self._dataProvider.config.indicators[name].levels[(-1)]
                    if points >= lastLevel.points:
                        return SingleTipType.LEADERBOARD

            return

    def __isIndicatorUnlocked(self, indicatorName):
        return not NyPetIndicatorsBlock.isIndicatorLocked(indicatorName)

    def __saveSeenTip(self):
        if self._dataProvider.isOnboarding or self.__isRestartedOnboarding:
            return
        with self.viewModel.transaction() as (tx):
            tip = tx.getSingleTip()
            tx.setSingleTip(SingleTipType.EMPTY)
        if tip == SingleTipType.EMPTY:
            return
        self.__markTipAsSeen(tip)

    def __onOnboardingRestartFinish(self):
        self.__isRestartedOnboarding = False
        self.viewModel.setIsRestartedOnboarding(False)

    def __onOnboardingFinish(self):
        self.__forceStopFillSound()
        self.viewModel.setIsOnboarding(False)
        self._dataProvider.isOnboarding = False
        if self.__isRestartedOnboarding:
            self.__onOnboardingRestartFinish()
        self.__resolveAndShowSingleTip()

    def __onOnboardingRestart(self):
        self.__isRestartedOnboarding = True
        self.viewModel.setIsRestartedOnboarding(True)
        count = getNYSetting(NY_TAMAGOTCHI_REPEAT_ONBOARDING_COUNT) + 1
        setNYSettings(NY_TAMAGOTCHI_REPEAT_ONBOARDING_COUNT, count)
        self.__uiLogger.logPetRepeatOnboardingClick(count)

    def __onPetStateAnimationsChange(self):
        with self.viewModel.transaction() as (tx):
            desired = not tx.getHasPetAnimations()
            tx.setHasPetAnimations(desired)
        self.__raccoonCtrl.setAnimationsEnabled(desired)

    def __onSeasonEnded(self, _):
        if self._dataProvider.isLeaderboardFinished:
            self.viewModel.setWasLeaderboardFinished(True)
            if self.viewModel.getSingleTip() is SingleTipType.LEADERBOARD:
                self.viewModel.setSingleTip(SingleTipType.EMPTY)

    @args2params(IndicatorType, int)
    def __onDeleteItemLeaderboardPoint(self, type, id):
        array = NyPetIndicatorsBlock.getIndicator(type, self.viewModel).getItemLeaderboardPoint()
        for index, item in enumerate(array):
            if item.getId() == id:
                array.remove(index)
                array.invalidate()
                return

    @args2params(IndicatorType, bool)
    def __onIndicatorFillSound(self, type, started):
        prevActive = self.__indicatorFillActive[type]
        if prevActive == started:
            return
        self.__indicatorFillActive[type] = started
        desiredPlaying = any(self.__indicatorFillActive.itervalues())
        if desiredPlaying != self.__isFillSoundPlaying:
            self.__playFillSound(desiredPlaying)
            self.__isFillSoundPlaying = desiredPlaying

    def __onCloseSingleTip(self):
        self.__saveSeenTip()
        self.__resolveAndShowSingleTip()

    def __stopSingleTipVoiceover(self):
        if self.viewModel.getSingleTip() is SingleTipType.EMPTY:
            return
        SoundGroups.g_instance.playSound2D(NewYearSoundEvents.OLDMAN_ONBOARDING_SKIP)

    def __forceStopFillSound(self):
        if self.__isFillSoundPlaying:
            self.__playFillSound(False)
            self.__isFillSoundPlaying = False
        for key in self.__indicatorFillActive.iterkeys():
            self.__indicatorFillActive[key] = False

    def __playFillSound(self, enable):
        soundEvent = RaccoonStates.PROGRESS_FILL_START if enable else RaccoonStates.PROGRESS_FILL_STOP
        SoundGroups.g_instance.playSound2D(soundEvent)