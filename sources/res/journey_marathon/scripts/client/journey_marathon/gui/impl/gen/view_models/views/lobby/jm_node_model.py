from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class NodeType(Enum):
    START = 'start'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    LOCKED = 'locked'


class JmNodeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(JmNodeModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getNextNodeIds(self):
        return self._getArray(1)

    def setNextNodeIds(self, value):
        self._setArray(1, value)

    @staticmethod
    def getNextNodeIdsType():
        return unicode

    def getNodeType(self):
        return NodeType(self._getString(2))

    def setNodeType(self, value):
        self._setString(2, value.value)

    def getIsExplored(self):
        return self._getBool(3)

    def setIsExplored(self, value):
        self._setBool(3, value)

    def getPosX(self):
        return self._getNumber(4)

    def setPosX(self, value):
        self._setNumber(4, value)

    def getPosY(self):
        return self._getNumber(5)

    def setPosY(self, value):
        self._setNumber(5, value)

    def getHasLore(self):
        return self._getBool(6)

    def setHasLore(self, value):
        self._setBool(6, value)

    def getLoreX(self):
        return self._getNumber(7)

    def setLoreX(self, value):
        self._setNumber(7, value)

    def getLoreY(self):
        return self._getNumber(8)

    def setLoreY(self, value):
        self._setNumber(8, value)

    def getLoreVisited(self):
        return self._getBool(9)

    def setLoreVisited(self, value):
        self._setBool(9, value)

    def getPrice(self):
        return self._getNumber(10)

    def setPrice(self, value):
        self._setNumber(10, value)

    def getBonuses(self):
        return self._getArray(11)

    def setBonuses(self, value):
        self._setArray(11, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getPathFromCurrentNode(self):
        return self._getArray(12)

    def setPathFromCurrentNode(self, value):
        self._setArray(12, value)

    @staticmethod
    def getPathFromCurrentNodeType():
        return unicode

    def getCanAfford(self):
        return self._getBool(13)

    def setCanAfford(self, value):
        self._setBool(13, value)

    def getHasFullscreenReward(self):
        return self._getBool(14)

    def setHasFullscreenReward(self, value):
        self._setBool(14, value)

    def _initialize(self):
        super(JmNodeModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addArrayProperty('nextNodeIds', Array())
        self._addStringProperty('nodeType')
        self._addBoolProperty('isExplored', False)
        self._addNumberProperty('posX', 0)
        self._addNumberProperty('posY', 0)
        self._addBoolProperty('hasLore', False)
        self._addNumberProperty('loreX', 0)
        self._addNumberProperty('loreY', 0)
        self._addBoolProperty('loreVisited', False)
        self._addNumberProperty('price', 0)
        self._addArrayProperty('bonuses', Array())
        self._addArrayProperty('pathFromCurrentNode', Array())
        self._addBoolProperty('canAfford', False)
        self._addBoolProperty('hasFullscreenReward', False)