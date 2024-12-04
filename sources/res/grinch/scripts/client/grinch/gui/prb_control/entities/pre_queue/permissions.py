from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from grinch.skeletons.battle_controller import IGrinchController
from helpers import dependency

class GrinchPermissions(PreQueuePermissions):
    grinchCtrl = dependency.descriptor(IGrinchController)

    def canCreateSquad(self):
        canCreateSquad = super(GrinchPermissions, self).canCreateSquad()
        return canCreateSquad and self.grinchCtrl.isAvailable()