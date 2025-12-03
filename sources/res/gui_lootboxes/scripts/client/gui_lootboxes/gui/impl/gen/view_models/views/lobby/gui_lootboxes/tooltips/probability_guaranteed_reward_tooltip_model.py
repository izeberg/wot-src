from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class ProbabilityGuaranteedRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ProbabilityGuaranteedRewardTooltipModel, self).__init__(properties=properties, commands=commands)

    def getGuaranteedFrequencies(self):
        return self._getArray(0)

    def setGuaranteedFrequencies(self, value):
        self._setArray(0, value)

    @staticmethod
    def getGuaranteedFrequenciesType():
        return int

    def _initialize(self):
        super(ProbabilityGuaranteedRewardTooltipModel, self)._initialize()
        self._addArrayProperty('guaranteedFrequencies', Array())