from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class RewardAttachmentIconBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(RewardAttachmentIconBonusModel, self).__init__(properties=properties, commands=commands)

    def getIconName(self):
        return self._getString(9)

    def setIconName(self, value):
        self._setString(9, value)

    def getRarity(self):
        return self._getString(10)

    def setRarity(self, value):
        self._setString(10, value)

    def _initialize(self):
        super(RewardAttachmentIconBonusModel, self)._initialize()
        self._addStringProperty('iconName', '')
        self._addStringProperty('rarity', '')