from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSGlobalChatController(IGameController):

    def isEnabled(self):
        raise NotImplementedError