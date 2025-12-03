import Windowing
from frameworks.wulf import ViewSettings, WindowLayer, Array, WindowFlags
from frameworks.wulf.view.array import fillStringsArray
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.views.reward.ho_pet_reward_view_model import HoPetRewardViewModel
from gui.impl.lobby.loot_box.loot_box_sounds import setOverlayHangarGeneral
from gui.impl.lobby.new_year.reward.reward_video_handler import PetRewardVideoStartStopHandler
from gui.impl.lobby.pet_system.states import PetStorageState
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.pet_system.pet_item_helper import PetItem, PromoPetItem
from helpers import dependency
from new_year.ny_constants import EnvironmentState
from pet_system_common import pet_constants
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.pet_system import IPetSystemController
from skeletons.new_year import INewYearController

class HOPetRewardView(ViewImpl):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __nyController = dependency.descriptor(INewYearController)
    __petController = dependency.descriptor(IPetSystemController)

    def __init__(self, *args):
        settings = ViewSettings(R.views.mono.holiday_ops.pet_reward_view())
        settings.model = HoPetRewardViewModel()
        settings.args = args
        super(HOPetRewardView, self).__init__(settings)
        self._videoStartStopHandler = PetRewardVideoStartStopHandler()

    def _initialize(self, *args):
        super(HOPetRewardView, self)._initialize(*args)
        setOverlayHangarGeneral(onState=True)
        Windowing.addWindowAccessibilitynHandler(self._onWindowAccessibilityChanged)
        with self.viewModel.transaction() as (model):
            model.setIsViewAccessible(Windowing.isWindowAccessible())

    def _finalize(self):
        setOverlayHangarGeneral(onState=False)
        Windowing.removeWindowAccessibilityHandler(self._onWindowAccessibilityChanged)
        self._videoStartStopHandler.onVideoDone()
        self._videoStartStopHandler = None
        super(HOPetRewardView, self)._finalize()
        return

    @property
    def viewModel(self):
        return super(HOPetRewardView, self).getViewModel()

    def _onLoading(self, petID):
        super(HOPetRewardView, self)._onLoading()
        self.update(petID)

    def _getEvents(self):
        events = super(HOPetRewardView, self)._getEvents()
        return events + (
         (
          self.viewModel.onGoToPetDen, self.__onGoToPetDen),
         (
          self.viewModel.onVideoStarted, self._onVideoStarted),
         (
          self.viewModel.onVideoStopped, self._onVideoStopped),
         (
          self.__nyController.onStateChanged, self.__onEventStateChanged),
         (
          self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChanged))

    def update(self, petID):
        bonusesStrList = PromoPetItem.getPetBenefits(petID)
        bonuses = Array()
        fillStringsArray(bonusesStrList, bonuses)
        environmentState = self.__nyController.getEnvironmentState()
        with self.viewModel.transaction() as (model):
            model.setPetNameID(PetItem.getDefaultNameId(petID))
            model.setBreedName(PetItem.getPetBreed(petID))
            model.setPromotionBonuses(bonuses)
            model.setIsDayHangar(environmentState == EnvironmentState.DAY)
            model.setIsPetDenAvailable(self.__petController.isEnabled)

    def updatePetDenAvailability(self):
        with self.viewModel.transaction() as (model):
            model.setIsPetDenAvailable(self.__petController.isEnabled)

    def __onGoToPetDen(self):
        PetStorageState.goTo()
        self.destroyWindow()

    def _onVideoStarted(self):
        environmentState = self.__nyController.getEnvironmentState()
        self._videoStartStopHandler.onVideoStart(environmentState == EnvironmentState.DAY)

    def _onVideoStopped(self):
        self._videoStartStopHandler.onVideoDone()

    def _onWindowAccessibilityChanged(self, isWindowAccessible):
        self._videoStartStopHandler.setIsNeedPause(not isWindowAccessible)
        self.viewModel.setIsViewAccessible(isWindowAccessible)

    def __onEventStateChanged(self):
        if not self.__nyController.isEnabled():
            self.destroyWindow()

    def __onServerSettingsChanged(self, diff):
        if pet_constants.PETS_SYSTEM_CONFIG in diff:
            if self.__petController.isEnabled:
                self.updatePetDenAvailability()
            else:
                self.destroyWindow()


class HOPetRewardWindow(LobbyNotificationWindow):

    def __init__(self, petID):
        super(HOPetRewardWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=HOPetRewardView(petID), layer=WindowLayer.OVERLAY)
        self.__args = (petID,)

    def isParamsEqual(self, *args):
        return self.__args == args