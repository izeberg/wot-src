from __future__ import absolute_import
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic

class EngineMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, _, vehDescr):
        return [
         (
          vehDescr.hasTurboshaftEngine, VehicleMechanic.TURBOSHAFT_ENGINE),
         (
          vehDescr.hasRocketAcceleration, VehicleMechanic.ROCKET_ACCELERATION),
         (
          hasVehicleDescrMechanic(vehDescr, VehicleMechanic.STAGED_JET_BOOSTERS),
          VehicleMechanic.STAGED_JET_BOOSTERS)]