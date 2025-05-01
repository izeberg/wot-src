from skeletons.gui.game_control import IGameController

class IHBEventNotifications(IGameController):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError