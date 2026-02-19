from frameworks.wulf import ViewModel

class DailyQuestsTimerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(DailyQuestsTimerTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DailyQuestsTimerTooltipModel, self)._initialize()