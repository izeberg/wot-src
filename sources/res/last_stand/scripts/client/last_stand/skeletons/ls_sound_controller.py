from skeletons.gui.game_control import IGameController

class ILSSoundController(IGameController):

    def playSoundEvent(self, audioEvent):
        raise NotImplementedError