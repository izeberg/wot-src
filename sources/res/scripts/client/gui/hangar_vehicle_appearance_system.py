from __future__ import absolute_import
import typing, BigWorld, CGF, Vehicular
from gui.hangar_vehicle_appearance import ActivateContext
from vehicle_appearance.component import VehicleAppearanceComponent
if typing.TYPE_CHECKING:
    from gui.hangar_vehicle_appearance import HangarVehicleAppearance

class HangarAppearanceSystem(CGF.System):
    Activate = CGF.ActivateReaction(CGF.ReactRo(VehicleAppearanceComponent), CGF.Rw(BigWorld.CollisionComponent), CGF.OptRo(Vehicular.GeneralWheelsAnimator), CGF.OptRo(Vehicular.DirtComponent))
    Reactions = CGF.Reactions(Activate)

    def update(self):
        for reactions in self.reaction(self.Activate):
            self.__activateAppearance(reactions)

    def __activateAppearance(self, reactions):
        appearanceCmp = reactions[0]
        appearance = appearanceCmp.appearance
        if appearance is not None:
            appearance.onActivate(ActivateContext(*reactions[1:]))
        return