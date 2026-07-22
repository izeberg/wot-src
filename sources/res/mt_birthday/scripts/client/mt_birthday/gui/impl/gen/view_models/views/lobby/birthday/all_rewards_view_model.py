from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.common.level_model import LevelModel

class AllRewardsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AllRewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getLevels(self):
        return self._getArray(0)

    def setLevels(self, value):
        self._setArray(0, value)

    @staticmethod
    def getLevelsType():
        return LevelModel

    def _initialize(self):
        super(AllRewardsViewModel, self)._initialize()
        self._addArrayProperty('levels', Array())