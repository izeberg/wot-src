from __future__ import absolute_import
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from vehicles.mechanics.mechanic_constants import VehicleMechanic

class ChassisMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, _):
        return [
         (
          guiItem.isHydraulicWheeledChassis(), VehicleMechanic.HYDRAULIC_WHEELED_CHASSIS),
         (
          guiItem.isHydraulicChassis(), VehicleMechanic.HYDRAULIC_CHASSIS),
         (
          guiItem.isTrackWithinTrack(), VehicleMechanic.TRACK_WITHIN_TRACK)]