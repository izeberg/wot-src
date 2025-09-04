from frameworks.wulf import Array, ViewModel

class TankmanInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(TankmanInfoModel, self).__init__(properties=properties, commands=commands)

    def getSkills(self):
        return self._getArray(0)

    def setSkills(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSkillsType():
        return unicode

    def _initialize(self):
        super(TankmanInfoModel, self)._initialize()
        self._addArrayProperty('skills', Array())