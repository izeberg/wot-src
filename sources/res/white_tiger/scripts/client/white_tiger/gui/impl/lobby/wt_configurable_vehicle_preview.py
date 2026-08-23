from helpers import dependency
from skeletons.prebattle_vehicle import IPrebattleVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_preview.configurable_vehicle_preview import ConfigurableVehiclePreview

class WTConfigurableVehiclePreview(ConfigurableVehiclePreview):
    __prebattleVehicle = dependency.descriptor(IPrebattleVehicle)

    def closeView(self):
        self.__prebattleVehicle.selectAny()
        super(WTConfigurableVehiclePreview, self).closeView()