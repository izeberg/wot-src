from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class JmAttachmentBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(JmAttachmentBonusModel, self).__init__(properties=properties, commands=commands)

    def getRarity(self):
        return self._getString(9)

    def setRarity(self, value):
        self._setString(9, value)

    def _initialize(self):
        super(JmAttachmentBonusModel, self)._initialize()
        self._addStringProperty('rarity', '')