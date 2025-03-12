from frameworks.wulf import ViewModel

class RulesEntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(RulesEntryPointTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RulesEntryPointTooltipModel, self)._initialize()