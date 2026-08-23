from frameworks.wulf import Array, ViewModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_model import JmNodeModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_popover_model import JmNodePopoverModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_quest_card_model import JmQuestCardModel

class JmMapViewModel(ViewModel):
    __slots__ = ('onQuestProgressShown', 'onQuestCompletedShown', 'onSelectNode', 'onChangeCurrentNode',
                 'onExplore', 'onExploreAnimationFinished', 'onInterruptForScreenShow',
                 'onCurrentNodeSynced', 'onPreviewLore', 'onRewardPreview', 'onBannerOpen')
    VEHICLE_REWARD = 'vehicles'
    TOKEN_REWARD = 'jm_lock_token'

    def __init__(self, properties=16, commands=11):
        super(JmMapViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def nodePopover(self):
        return self._getViewModel(0)

    @staticmethod
    def getNodePopoverType():
        return JmNodePopoverModel

    def getNodes(self):
        return self._getArray(1)

    def setNodes(self, value):
        self._setArray(1, value)

    @staticmethod
    def getNodesType():
        return JmNodeModel

    def getCurrentNodeId(self):
        return self._getString(2)

    def setCurrentNodeId(self, value):
        self._setString(2, value)

    def getQuestCards(self):
        return self._getArray(3)

    def setQuestCards(self, value):
        self._setArray(3, value)

    @staticmethod
    def getQuestCardsType():
        return JmQuestCardModel

    def getTimeTillNewQuests(self):
        return self._getNumber(4)

    def setTimeTillNewQuests(self, value):
        self._setNumber(4, value)

    def getIsLastGameDay(self):
        return self._getBool(5)

    def setIsLastGameDay(self, value):
        self._setBool(5, value)

    def getCoinTokenCount(self):
        return self._getNumber(6)

    def setCoinTokenCount(self, value):
        self._setNumber(6, value)

    def getUnlockTokenCount(self):
        return self._getNumber(7)

    def setUnlockTokenCount(self, value):
        self._setNumber(7, value)

    def getIsInteractivityLocked(self):
        return self._getBool(8)

    def setIsInteractivityLocked(self, value):
        self._setBool(8, value)

    def getTimeTillEnd(self):
        return self._getNumber(9)

    def setTimeTillEnd(self, value):
        self._setNumber(9, value)

    def getIsCompleted(self):
        return self._getBool(10)

    def setIsCompleted(self, value):
        self._setBool(10, value)

    def getIsQuestCompletedShow(self):
        return self._getBool(11)

    def setIsQuestCompletedShow(self, value):
        self._setBool(11, value)

    def getMovingFailed(self):
        return self._getBool(12)

    def setMovingFailed(self, value):
        self._setBool(12, value)

    def getBannerShown(self):
        return self._getBool(13)

    def setBannerShown(self, value):
        self._setBool(13, value)

    def getExploreAnimationNodeId(self):
        return self._getString(14)

    def setExploreAnimationNodeId(self, value):
        self._setString(14, value)

    def getExploreAnimationUnpause(self):
        return self._getString(15)

    def setExploreAnimationUnpause(self, value):
        self._setString(15, value)

    def _initialize(self):
        super(JmMapViewModel, self)._initialize()
        self._addViewModelProperty('nodePopover', JmNodePopoverModel())
        self._addArrayProperty('nodes', Array())
        self._addStringProperty('currentNodeId', '')
        self._addArrayProperty('questCards', Array())
        self._addNumberProperty('timeTillNewQuests', 0)
        self._addBoolProperty('isLastGameDay', False)
        self._addNumberProperty('coinTokenCount', 0)
        self._addNumberProperty('unlockTokenCount', 0)
        self._addBoolProperty('isInteractivityLocked', False)
        self._addNumberProperty('timeTillEnd', 0)
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('isQuestCompletedShow', False)
        self._addBoolProperty('movingFailed', False)
        self._addBoolProperty('bannerShown', False)
        self._addStringProperty('exploreAnimationNodeId', '')
        self._addStringProperty('exploreAnimationUnpause', '')
        self.onQuestProgressShown = self._addCommand('onQuestProgressShown')
        self.onQuestCompletedShown = self._addCommand('onQuestCompletedShown')
        self.onSelectNode = self._addCommand('onSelectNode')
        self.onChangeCurrentNode = self._addCommand('onChangeCurrentNode')
        self.onExplore = self._addCommand('onExplore')
        self.onExploreAnimationFinished = self._addCommand('onExploreAnimationFinished')
        self.onInterruptForScreenShow = self._addCommand('onInterruptForScreenShow')
        self.onCurrentNodeSynced = self._addCommand('onCurrentNodeSynced')
        self.onPreviewLore = self._addCommand('onPreviewLore')
        self.onRewardPreview = self._addCommand('onRewardPreview')
        self.onBannerOpen = self._addCommand('onBannerOpen')