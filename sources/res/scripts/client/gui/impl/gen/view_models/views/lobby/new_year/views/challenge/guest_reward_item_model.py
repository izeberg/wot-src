from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class GuestRewardItemModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(GuestRewardItemModel, self).__init__(properties=properties, commands=commands)

    def getIntCD(self):
        return self._getNumber(9)

    def setIntCD(self, value):
        self._setNumber(9, value)

    def getHasNewActivity(self):
        return self._getBool(10)

    def setHasNewActivity(self, value):
        self._setBool(10, value)

    def getIconSmall(self):
        return self._getString(11)

    def setIconSmall(self, value):
        self._setString(11, value)

    def getIconBig(self):
        return self._getString(12)

    def setIconBig(self, value):
        self._setString(12, value)

    def _initialize(self):
        super(GuestRewardItemModel, self)._initialize()
        self._addNumberProperty('intCD', 0)
        self._addBoolProperty('hasNewActivity', False)
        self._addStringProperty('iconSmall', '')
        self._addStringProperty('iconBig', '')