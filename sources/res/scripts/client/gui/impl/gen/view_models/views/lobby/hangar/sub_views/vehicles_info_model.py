from frameworks.wulf import Map, ViewModel

class VehiclesInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(VehiclesInfoModel, self).__init__(properties=properties, commands=commands)

    def getVehicles(self):
        return self._getMap(0)

    def setVehicles(self, value):
        self._setMap(0, value)

    @staticmethod
    def getVehiclesType():
        return (unicode, unicode)

    def _initialize(self):
        super(VehiclesInfoModel, self)._initialize()
        self._addMapProperty('vehicles', Map(unicode, unicode))