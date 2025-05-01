from helpers import dependency
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from historical_battles.skeletons.gui.game_event_controller import IGameEventController

class HistoricalBattlesQueueCtx(QueueCtx):
    gameEventController = dependency.descriptor(IGameEventController)

    def __init__(self, subdivionId):
        front = self.gameEventController.frontController.getSelectedFront()
        super(HistoricalBattlesQueueCtx, self).__init__(entityType=front.getFrontQueueType(), waitingID='prebattle/join')
        self._subdivionID = subdivionId

    @property
    def subdivionID(self):
        return self._subdivionID