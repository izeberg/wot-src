from frameworks.wulf import Array, ViewModel

class ModifiersHangarViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ModifiersHangarViewModel, self).__init__(properties=properties, commands=commands)

    def getModifiersDomains(self):
        return self._getArray(0)

    def setModifiersDomains(self, value):
        self._setArray(0, value)

    @staticmethod
    def getModifiersDomainsType():
        return unicode

    def _initialize(self):
        super(ModifiersHangarViewModel, self)._initialize()
        self._addArrayProperty('modifiersDomains', Array())