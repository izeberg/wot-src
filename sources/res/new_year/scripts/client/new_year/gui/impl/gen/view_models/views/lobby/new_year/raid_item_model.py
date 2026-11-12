from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class RaidItemModel(RewardItemModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(RaidItemModel, self).__init__(properties=properties, commands=commands)

    def getIsEnabled(self):
        return self._getBool(14)

    def setIsEnabled(self, value):
        self._setBool(14, value)

    def getComponentID(self):
        return self._getNumber(15)

    def setComponentID(self, value):
        self._setNumber(15, value)

    def _initialize(self):
        super(RaidItemModel, self)._initialize()
        self._addBoolProperty('isEnabled', False)
        self._addNumberProperty('componentID', -1)