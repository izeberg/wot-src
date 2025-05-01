from frameworks.wulf import ViewModel

class LockedSubscriptionBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LockedSubscriptionBonusTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsActiveSubscription(self):
        return self._getBool(0)

    def setIsActiveSubscription(self, value):
        self._setBool(0, value)

    def getIsQuestDone(self):
        return self._getBool(1)

    def setIsQuestDone(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(LockedSubscriptionBonusTooltipModel, self)._initialize()
        self._addBoolProperty('isActiveSubscription', False)
        self._addBoolProperty('isQuestDone', False)