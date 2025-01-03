from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class ParagonsUnlockModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(ParagonsUnlockModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(8)

    def setId(self, value):
        self._setNumber(8, value)

    def getIsLocked(self):
        return self._getBool(9)

    def setIsLocked(self, value):
        self._setBool(9, value)

    def _initialize(self):
        super(ParagonsUnlockModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addBoolProperty('isLocked', False)