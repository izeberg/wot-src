from __future__ import absolute_import
import CGF
from StagedJetBoostersController import StagedJetBoostersController

class StagedJetBoostersComponentSystem(CGF.System):
    Activated = CGF.ActivateReaction(CGF.ReactRw(StagedJetBoostersController))
    Deactivated = CGF.DeactivateReaction(CGF.ReactRw(StagedJetBoostersController))
    Reactions = CGF.Reactions(Activated, Deactivated)

    def update(self):
        for controller in self.reaction(self.Deactivated):
            if controller.isValid and not controller.isComponentDestroyed():
                controller.detachInput()

        for controller in self.reaction(self.Activated):
            controller.attachInput()
            controller.createInputLogger()