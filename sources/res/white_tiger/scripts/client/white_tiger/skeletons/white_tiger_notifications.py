from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class IWhiteTigerNotifications(IGameController):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError