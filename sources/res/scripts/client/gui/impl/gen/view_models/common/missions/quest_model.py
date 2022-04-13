from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel
from gui.impl.gen.view_models.common.missions.event_model import EventModel

class QuestModel(EventModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(QuestModel, self).__init__(properties=properties, commands=commands)

    @property
    def preBattleCondition(self):
        return self._getViewModel(7)

    @property
    def bonusCondition(self):
        return self._getViewModel(8)

    @property
    def postBattleCondition(self):
        return self._getViewModel(9)

    def getBonuses(self):
        return self._getArray(10)

    def setBonuses(self, value):
        self._setArray(10, value)

    def getTotalCount(self):
        return self._getNumber(11)

    def setTotalCount(self, value):
        self._setNumber(11, value)

    def getCompletedCount(self):
        return self._getNumber(12)

    def setCompletedCount(self, value):
        self._setNumber(12, value)

    def _initialize(self):
        super(QuestModel, self)._initialize()
        self._addViewModelProperty('preBattleCondition', ConditionGroupModel())
        self._addViewModelProperty('bonusCondition', ConditionGroupModel())
        self._addViewModelProperty('postBattleCondition', ConditionGroupModel())
        self._addArrayProperty('bonuses')
        self._addNumberProperty('totalCount', 0)
        self._addNumberProperty('completedCount', 0)