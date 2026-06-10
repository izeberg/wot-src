from skeletons.gui.game_control import IGameController

class IEventController(IGameController):

    def isEnabled(self):
        raise NotImplementedError

    def getEventStartTime(self):
        raise NotImplementedError

    def getEventFinishTime(self):
        raise NotImplementedError