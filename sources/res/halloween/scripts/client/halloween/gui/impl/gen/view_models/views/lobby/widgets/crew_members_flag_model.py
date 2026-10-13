from frameworks.wulf import ViewModel

class CrewMembersFlagModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=1, commands=1):
        super(CrewMembersFlagModel, self).__init__(properties=properties, commands=commands)

    def getIsHidden(self):
        return self._getBool(0)

    def setIsHidden(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(CrewMembersFlagModel, self)._initialize()
        self._addBoolProperty('isHidden', False)
        self.onClick = self._addCommand('onClick')