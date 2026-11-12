from frameworks.wulf import ViewModel

class NyBlockActivitiesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyBlockActivitiesTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(NyBlockActivitiesTooltipModel, self)._initialize()
        self._addNumberProperty('level', 0)