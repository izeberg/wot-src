from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class RespawnAmmunitionPanelViewModel(AmmunitionPanelViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(RespawnAmmunitionPanelViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(7)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def _initialize(self):
        super(RespawnAmmunitionPanelViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())