from frameworks.wulf import ViewModel

class FlProgressionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FlProgressionModel, self).__init__(properties=properties, commands=commands)

    def getCurrent(self):
        return self._getNumber(0)

    def setCurrent(self, value):
        self._setNumber(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(FlProgressionModel, self)._initialize()
        self._addNumberProperty('current', 0)
        self._addStringProperty('name', '')