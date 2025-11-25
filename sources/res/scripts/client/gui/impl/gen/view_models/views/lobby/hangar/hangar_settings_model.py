from gui.impl.gen.view_models.views.lobby.common.settings_model import SettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.all_vehicles_settings_model import AllVehiclesSettingsModel

class HangarSettingsModel(SettingsModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=1):
        super(HangarSettingsModel, self).__init__(properties=properties, commands=commands)

    @property
    def allVehicles(self):
        return self._getViewModel(1)

    @staticmethod
    def getAllVehiclesType():
        return AllVehiclesSettingsModel

    def _initialize(self):
        super(HangarSettingsModel, self)._initialize()
        self._addViewModelProperty('allVehicles', AllVehiclesSettingsModel())