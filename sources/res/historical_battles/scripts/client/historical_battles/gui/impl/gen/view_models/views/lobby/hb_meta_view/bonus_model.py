from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class BonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)

    def getAmount(self):
        return self._getNumber(8)

    def setAmount(self, value):
        self._setNumber(8, value)

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addNumberProperty('amount', 0)