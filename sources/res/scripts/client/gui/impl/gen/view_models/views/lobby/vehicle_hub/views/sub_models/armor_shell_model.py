from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel

class ArmorShellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ArmorShellModel, self).__init__(properties=properties, commands=commands)

    def getMechanics(self):
        return self._getArray(0)

    def setMechanics(self, value):
        self._setArray(0, value)

    @staticmethod
    def getMechanicsType():
        return VehicleMechanicModel

    def _initialize(self):
        super(ArmorShellModel, self)._initialize()
        self._addArrayProperty('mechanics', Array())