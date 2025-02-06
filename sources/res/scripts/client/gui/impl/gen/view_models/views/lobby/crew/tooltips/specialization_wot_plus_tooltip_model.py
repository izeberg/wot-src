from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class SpecializationWotPlusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SpecializationWotPlusTooltipModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleInfoModel

    def _initialize(self):
        super(SpecializationWotPlusTooltipModel, self)._initialize()
        self._addViewModelProperty('vehicle', VehicleInfoModel())