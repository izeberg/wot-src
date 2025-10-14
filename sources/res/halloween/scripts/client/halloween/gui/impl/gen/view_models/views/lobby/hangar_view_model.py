from frameworks.wulf import ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel

class HangarViewModel(ViewModel):
    __slots__ = ('onEscPressed', 'onAboutClick', 'onExitClick', 'onViewLoaded', 'onSlide',
                 'onPreview', 'onTasksClick', 'onPacksClick', 'onComparisonClick')

    def __init__(self, properties=9, commands=9):
        super(HangarViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def mainGiftVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getMainGiftVehicleType():
        return VehicleTitleViewModel

    def getIsLoadedSetup(self):
        return self._getBool(1)

    def setIsLoadedSetup(self, value):
        self._setBool(1, value)

    def getSelectedSlide(self):
        return self._getNumber(2)

    def setSelectedSlide(self, value):
        self._setNumber(2, value)

    def getSlidesCount(self):
        return self._getNumber(3)

    def setSlidesCount(self, value):
        self._setNumber(3, value)

    def getIsVehicleLocked(self):
        return self._getBool(4)

    def setIsVehicleLocked(self, value):
        self._setBool(4, value)

    def getLockedMissionIndex(self):
        return self._getNumber(5)

    def setLockedMissionIndex(self, value):
        self._setNumber(5, value)

    def getIsVehicleInBattle(self):
        return self._getBool(6)

    def setIsVehicleInBattle(self, value):
        self._setBool(6, value)

    def getIsCompleted(self):
        return self._getBool(7)

    def setIsCompleted(self, value):
        self._setBool(7, value)

    def getIsInfoPageEnabled(self):
        return self._getBool(8)

    def setIsInfoPageEnabled(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(HangarViewModel, self)._initialize()
        self._addViewModelProperty('mainGiftVehicle', VehicleTitleViewModel())
        self._addBoolProperty('isLoadedSetup', False)
        self._addNumberProperty('selectedSlide', 0)
        self._addNumberProperty('slidesCount', 0)
        self._addBoolProperty('isVehicleLocked', False)
        self._addNumberProperty('lockedMissionIndex', 0)
        self._addBoolProperty('isVehicleInBattle', False)
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('isInfoPageEnabled', False)
        self.onEscPressed = self._addCommand('onEscPressed')
        self.onAboutClick = self._addCommand('onAboutClick')
        self.onExitClick = self._addCommand('onExitClick')
        self.onViewLoaded = self._addCommand('onViewLoaded')
        self.onSlide = self._addCommand('onSlide')
        self.onPreview = self._addCommand('onPreview')
        self.onTasksClick = self._addCommand('onTasksClick')
        self.onPacksClick = self._addCommand('onPacksClick')
        self.onComparisonClick = self._addCommand('onComparisonClick')