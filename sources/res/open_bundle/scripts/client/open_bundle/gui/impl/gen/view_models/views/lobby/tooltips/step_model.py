from frameworks.wulf import Array, ViewModel
from open_bundle.gui.impl.gen.view_models.views.lobby.bonus_model import BonusModel

class StepModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(StepModel, self).__init__(properties=properties, commands=commands)

    def getStepNumber(self):
        return self._getNumber(0)

    def setStepNumber(self, value):
        self._setNumber(0, value)

    def getFixedRewards(self):
        return self._getArray(1)

    def setFixedRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getFixedRewardsType():
        return BonusModel

    def _initialize(self):
        super(StepModel, self)._initialize()
        self._addNumberProperty('stepNumber', 0)
        self._addArrayProperty('fixedRewards', Array())