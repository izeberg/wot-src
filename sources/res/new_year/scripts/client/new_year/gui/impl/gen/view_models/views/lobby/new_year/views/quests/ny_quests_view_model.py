from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class NyQuestsViewModel(ViewModel):
    __slots__ = ('onTypeSelect', 'onStartStopPersonVoice', 'changePersonVoicesEnabled',
                 'onInfoClick')

    def __init__(self, properties=10, commands=4):
        super(NyQuestsViewModel, self).__init__(properties=properties, commands=commands)

    def getCurrentTabIdx(self):
        return self._getNumber(0)

    def setCurrentTabIdx(self, value):
        self._setNumber(0, value)

    def getFirstSeenNewBonusMissions(self):
        return self._getBool(1)

    def setFirstSeenNewBonusMissions(self, value):
        self._setBool(1, value)

    def getQuests(self):
        return self._getArray(2)

    def setQuests(self, value):
        self._setArray(2, value)

    @staticmethod
    def getQuestsType():
        return DailyQuestModel

    def getCountDown(self):
        return self._getNumber(3)

    def setCountDown(self, value):
        self._setNumber(3, value)

    def getMinLevel(self):
        return self._getNumber(4)

    def setMinLevel(self, value):
        self._setNumber(4, value)

    def getMaxLevel(self):
        return self._getNumber(5)

    def setMaxLevel(self, value):
        self._setNumber(5, value)

    def getPersonTextNumber(self):
        return self._getNumber(6)

    def setPersonTextNumber(self, value):
        self._setNumber(6, value)

    def getIsPersonVoicesNowPlaying(self):
        return self._getBool(7)

    def setIsPersonVoicesNowPlaying(self, value):
        self._setBool(7, value)

    def getIsPersonVoicesEnabled(self):
        return self._getBool(8)

    def setIsPersonVoicesEnabled(self, value):
        self._setBool(8, value)

    def getBattleTypes(self):
        return self._getArray(9)

    def setBattleTypes(self, value):
        self._setArray(9, value)

    @staticmethod
    def getBattleTypesType():
        return unicode

    def _initialize(self):
        super(NyQuestsViewModel, self)._initialize()
        self._addNumberProperty('currentTabIdx', 0)
        self._addBoolProperty('firstSeenNewBonusMissions', False)
        self._addArrayProperty('quests', Array())
        self._addNumberProperty('countDown', 0)
        self._addNumberProperty('minLevel', 0)
        self._addNumberProperty('maxLevel', 0)
        self._addNumberProperty('personTextNumber', 1)
        self._addBoolProperty('isPersonVoicesNowPlaying', False)
        self._addBoolProperty('isPersonVoicesEnabled', False)
        self._addArrayProperty('battleTypes', Array())
        self.onTypeSelect = self._addCommand('onTypeSelect')
        self.onStartStopPersonVoice = self._addCommand('onStartStopPersonVoice')
        self.changePersonVoicesEnabled = self._addCommand('changePersonVoicesEnabled')
        self.onInfoClick = self._addCommand('onInfoClick')