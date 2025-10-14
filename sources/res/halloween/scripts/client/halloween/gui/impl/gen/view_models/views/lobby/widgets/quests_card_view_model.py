from frameworks.wulf import ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class QuestsCardViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(QuestsCardViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def bonus(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusType():
        return BonusItemViewModel

    def getConditionName(self):
        return self._getString(1)

    def setConditionName(self, value):
        self._setString(1, value)

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)

    def getIsCompleted(self):
        return self._getBool(4)

    def setIsCompleted(self, value):
        self._setBool(4, value)

    def getIsHidden(self):
        return self._getBool(5)

    def setIsHidden(self, value):
        self._setBool(5, value)

    def getCurrentProgress(self):
        return self._getNumber(6)

    def setCurrentProgress(self, value):
        self._setNumber(6, value)

    def getMaximumProgress(self):
        return self._getNumber(7)

    def setMaximumProgress(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(QuestsCardViewModel, self)._initialize()
        self._addViewModelProperty('bonus', BonusItemViewModel())
        self._addStringProperty('conditionName', '')
        self._addStringProperty('name', '')
        self._addStringProperty('description', '')
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('isHidden', False)
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('maximumProgress', 0)