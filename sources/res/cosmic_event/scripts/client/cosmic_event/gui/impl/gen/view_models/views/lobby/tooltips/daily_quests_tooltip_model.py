from frameworks.wulf import ViewModel

class DailyQuestsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(DailyQuestsTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DailyQuestsTooltipModel, self)._initialize()