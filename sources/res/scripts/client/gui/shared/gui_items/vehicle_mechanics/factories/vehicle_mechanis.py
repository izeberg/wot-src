from __future__ import absolute_import
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from vehicles.mechanics.mechanic_constants import VehicleMechanic

class VehicleMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, _, vehDescr):
        return [
         (
          vehDescr.hasSiegeMode and not vehDescr.hasAutoSiegeMode, VehicleMechanic.SIEGE_MODE)]

    @classmethod
    def _getMechanicsParams(cls, _, vehDescr):
        return vehDescr.type.mechanicsParams