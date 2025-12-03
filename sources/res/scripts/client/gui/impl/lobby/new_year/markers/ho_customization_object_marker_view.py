from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.markers.ny_customization_object_marker_model import NyCustomizationObjectMarkerModel, MarkerType
from gui.impl.lobby.new_year.markers.ho_hangar_marker_view import HOHangarMarkerView
from helpers import dependency
from new_year.ny_constants import SyncDataKeys, NYObjects, MarkerObjects
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.new_year import INewYearController, IFriendServiceController

class HOCustomizationObjectMarkerView(HOHangarMarkerView):
    _nyController = dependency.descriptor(INewYearController)
    _friendService = dependency.descriptor(IFriendServiceController)
    _settingsCore = dependency.descriptor(ISettingsCore)
    _OBJECT_TYPE = None

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops_marker.ho_customization_object_marker())
        settings.model = NyCustomizationObjectMarkerModel()
        settings.args = args
        settings.kwargs = kwargs
        super(HOCustomizationObjectMarkerView, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _getEvents(self):
        events = super(HOCustomizationObjectMarkerView, self)._getEvents()
        return events + (
         (
          self._nyController.onDataUpdated, self._onDataUpdated),
         (
          self._friendService.onFriendHangarEnter, self._updateMarker),
         (
          self._friendService.onFriendHangarExit, self._updateMarker),
         (
          self._objectObserver.onObjectStateChanged, self._onObjectUpdate),
         (
          self.viewModel.onLevelUpdate, self.__onLevelUpdate))

    def _onLoading(self, *args, **kwargs):
        super(HOCustomizationObjectMarkerView, self)._onLoading(*args, **kwargs)
        self._updateMarker()

    def _onObjectUpdate(self, objectName):
        self.viewModel.setIsAbleForUpgrade(objectName == self._OBJECT_TYPE)
        if self.__isMaxLevelState():
            self.viewModel.setIsMaxLevelState(True)
        self.viewModel.setIsCameraOnUnderSpace(objectName == NYObjects.TOWN)

    def __isMaxLevelState(self):
        return self._nyController.customizationObjects.getLevel(self._OBJECT_TYPE) == NyCustomizationObjectMarkerModel.MAX_LEVEL

    def __onLevelUpdate(self):
        self._nyController.setCustomizationObjectLevelUp()

    def _onDataUpdated(self, keys, _):
        checkKeys = {
         SyncDataKeys.OBJECTS_LEVELS}
        if set(keys) & checkKeys and not self._friendService.isInFriendHangar:
            self._updateMarker()

    def _setMarkerVisible(self, isVisible):
        with self.viewModel.transaction() as (model):
            if model.getIsVisible() != isVisible:
                model.setIsVisible(isVisible)
                if isVisible:
                    self._updateMarker()

    def _updateMarker(self, *args, **kwargs):
        with self.viewModel.transaction() as (model):
            model.setObjectType(self._OBJECT_TYPE)
            currentLevel = self._nyController.customizationObjects.getLevel(self._OBJECT_TYPE)
            model.setCurrentLevel(currentLevel)
            model.setMarkerType((self._friendService.isInFriendHangar or MarkerType).DEFAULT if 1 else MarkerType.FRIEND)


class HOFirMarkerView(HOCustomizationObjectMarkerView):
    _OBJECT_TYPE = MarkerObjects.FIR


class HOFairMarkerView(HOCustomizationObjectMarkerView):
    _OBJECT_TYPE = MarkerObjects.FAIR


class HOInstallationMarkerView(HOCustomizationObjectMarkerView):
    _OBJECT_TYPE = MarkerObjects.INSTALLATION