from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.daily.widget_quest_model import WidgetQuestModel

class DailyQuestsWidgetViewModel(ViewModel):
    __slots__ = ('onQuestClick', 'onDisappear', 'onNyQuestsClick')

    def __init__(self, properties=9, commands=3):
        super(DailyQuestsWidgetViewModel, self).__init__(properties=properties, commands=commands)

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)

    @staticmethod
    def getQuestsType():
        return WidgetQuestModel

    def getPremiumQuests(self):
        return self._getArray(1)

    def setPremiumQuests(self, value):
        self._setArray(1, value)

    @staticmethod
    def getPremiumQuestsType():
        return WidgetQuestModel

    def getSerialEnterQuests(self):
        return self._getArray(2)

    def setSerialEnterQuests(self, value):
        self._setArray(2, value)

    @staticmethod
    def getSerialEnterQuestsType():
        return WidgetQuestModel

    def getCountdown(self):
        return self._getNumber(3)

    def setCountdown(self, value):
        self._setNumber(3, value)

    def getVisible(self):
        return self._getBool(4)

    def setVisible(self, value):
        self._setBool(4, value)

    def getIndicateCompleteQuests(self):
        return self._getArray(5)

    def setIndicateCompleteQuests(self, value):
        self._setArray(5, value)

    @staticmethod
    def getIndicateCompleteQuestsType():
        return bool

    def getIsAllNyQuestsComplete(self):
        return self._getBool(6)

    def setIsAllNyQuestsComplete(self, value):
        self._setBool(6, value)

    def getIsNyEnabled(self):
        return self._getBool(7)

    def setIsNyEnabled(self, value):
        self._setBool(7, value)

    def getIsNyCardVisible(self):
        return self._getBool(8)

    def setIsNyCardVisible(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(DailyQuestsWidgetViewModel, self)._initialize()
        self._addArrayProperty('quests', Array())
        self._addArrayProperty('premiumQuests', Array())
        self._addArrayProperty('serialEnterQuests', Array())
        self._addNumberProperty('countdown', 0)
        self._addBoolProperty('visible', False)
        self._addArrayProperty('indicateCompleteQuests', Array())
        self._addBoolProperty('isAllNyQuestsComplete', False)
        self._addBoolProperty('isNyEnabled', False)
        self._addBoolProperty('isNyCardVisible', False)
        self.onQuestClick = self._addCommand('onQuestClick')
        self.onDisappear = self._addCommand('onDisappear')
        self.onNyQuestsClick = self._addCommand('onNyQuestsClick')