from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.tooltips.bonus_item_view_model import BonusItemViewModel

class LootboxGroupModel(ViewModel):
    __slots__ = ()
    GUARANTEED = 'guaranteed'
    CURRENCY = 'currency'
    NY_ITEMS = 'ny_items'
    ATTACHMENTS = 'attachments'
    CUSTOMIZATIONS = 'customizations'
    HIGH_TIER_VEHICLES = 'high_tier_vehicles'
    LOW_TIER_VEHICLES = 'low_tier_vehicles'

    def __init__(self, properties=3, commands=0):
        super(LootboxGroupModel, self).__init__(properties=properties, commands=commands)

    def getProbability(self):
        return self._getReal(0)

    def setProbability(self, value):
        self._setReal(0, value)

    def getGroupName(self):
        return self._getString(1)

    def setGroupName(self, value):
        self._setString(1, value)

    def getBonusItems(self):
        return self._getArray(2)

    def setBonusItems(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBonusItemsType():
        return BonusItemViewModel

    def _initialize(self):
        super(LootboxGroupModel, self)._initialize()
        self._addRealProperty('probability', 0.0)
        self._addStringProperty('groupName', '')
        self._addArrayProperty('bonusItems', Array())