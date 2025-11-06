from frameworks.wulf import ViewModel

class PetObjectTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PetObjectTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsStorageTooltipVisible(self):
        return self._getBool(0)

    def setIsStorageTooltipVisible(self, value):
        self._setBool(0, value)

    def getIs3dObjectTooltipVisible(self):
        return self._getBool(1)

    def setIs3dObjectTooltipVisible(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(PetObjectTooltipModel, self)._initialize()
        self._addBoolProperty('isStorageTooltipVisible', False)
        self._addBoolProperty('is3dObjectTooltipVisible', False)