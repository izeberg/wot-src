from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_stage_model import NyStageModel

class NyWeeklyRewardsViewModel(ViewModel):
    __slots__ = ('onClose', 'onInfoClick', 'onPreviewClick', 'onTabSelected')

    def __init__(self, properties=5, commands=4):
        super(NyWeeklyRewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getCurrentStage(self):
        return self._getNumber(0)

    def setCurrentStage(self, value):
        self._setNumber(0, value)

    def getFinalStageComplete(self):
        return self._getBool(1)

    def setFinalStageComplete(self, value):
        self._setBool(1, value)

    def getIsRecalc(self):
        return self._getBool(2)

    def setIsRecalc(self, value):
        self._setBool(2, value)

    def getStages(self):
        return self._getArray(3)

    def setStages(self, value):
        self._setArray(3, value)

    @staticmethod
    def getStagesType():
        return NyStageModel

    def getIsFromMainView(self):
        return self._getBool(4)

    def setIsFromMainView(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(NyWeeklyRewardsViewModel, self)._initialize()
        self._addNumberProperty('currentStage', 0)
        self._addBoolProperty('finalStageComplete', False)
        self._addBoolProperty('isRecalc', False)
        self._addArrayProperty('stages', Array())
        self._addBoolProperty('isFromMainView', True)
        self.onClose = self._addCommand('onClose')
        self.onInfoClick = self._addCommand('onInfoClick')
        self.onPreviewClick = self._addCommand('onPreviewClick')
        self.onTabSelected = self._addCommand('onTabSelected')