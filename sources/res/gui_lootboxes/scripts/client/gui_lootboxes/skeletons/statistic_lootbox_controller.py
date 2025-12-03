from skeletons.gui.game_control import IGameController

class IStatisticLootBoxController(IGameController):
    onStatusChanged = None

    @property
    def onBaseStatCollect(self):
        raise NotImplementedError

    def getFullStatistic(self):
        raise NotImplementedError

    def getMergeStatByLootboxIDs(self, lootboxIDs):
        raise NotImplementedError

    def getLootboxesExpireInfo(self):
        raise NotImplementedError

    def isNeedShowHint(self):
        raise NotImplementedError

    def getLootBoxesVersionInfo(self, lootboxID=None):
        raise NotImplementedError

    def isShowStatistic(self):
        raise NotImplementedError