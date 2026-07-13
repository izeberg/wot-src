from frameworks.wulf import ViewModel

class ChallengesShieldsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(ChallengesShieldsTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ChallengesShieldsTooltipModel, self)._initialize()