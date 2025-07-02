from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class RankedPermissions(PreQueuePermissions):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def canSendInvite(self):
        return True

    def canCreateSquad(self):
        if not self.__rankedController.hasSuitableVehicles():
            return False
        return super(RankedPermissions, self).canCreateSquad()