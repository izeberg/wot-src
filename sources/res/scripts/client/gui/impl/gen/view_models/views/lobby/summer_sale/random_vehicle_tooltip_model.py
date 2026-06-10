from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.summer_sale.vehicle_bonus_model import VehicleBonusModel

class RandomVehicleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RandomVehicleTooltipModel, self).__init__(properties=properties, commands=commands)

    def getVehicles(self):
        return self._getArray(0)

    def setVehicles(self, value):
        self._setArray(0, value)

    @staticmethod
    def getVehiclesType():
        return VehicleBonusModel

    def _initialize(self):
        super(RandomVehicleTooltipModel, self)._initialize()
        self._addArrayProperty('vehicles', Array())