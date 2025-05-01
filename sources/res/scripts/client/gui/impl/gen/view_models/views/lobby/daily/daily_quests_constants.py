from frameworks.wulf import ViewModel

class DailyQuestsConstants(ViewModel):
    __slots__ = ()
    DAILY_GROUP_ID = 0
    PREMIUM_GROUP_ID = 1
    EPIC_GROUP_ID = 2

    def __init__(self, properties=0, commands=0):
        super(DailyQuestsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DailyQuestsConstants, self)._initialize()