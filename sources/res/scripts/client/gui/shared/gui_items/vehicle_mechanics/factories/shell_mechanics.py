from __future__ import absolute_import
from typing import TYPE_CHECKING
from gui.shared.items_parameters.functions import getShellParamsSwitcherModifiedShells, getShellCalibrationShells, getBustleFeedModifiedShells
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic
if TYPE_CHECKING:
    from gui.shared.gui_items.vehicle_modules import Shell
    from items.vehicles import VehicleDescr
_SHELL_MODIFICATION_MECHANICS_GETTERS = {VehicleMechanic.SHELL_PARAMS_SWITCHER: getShellParamsSwitcherModifiedShells, 
   VehicleMechanic.SHELL_CALIBRATION: getShellCalibrationShells, 
   VehicleMechanic.BUSTLE_FEED: getBustleFeedModifiedShells}

def _hasShellMechanics(descriptor, shell, mechanic):
    getter = _SHELL_MODIFICATION_MECHANICS_GETTERS.get(mechanic)
    if getter is None or not hasVehicleDescrMechanic(descriptor, mechanic):
        return False
    return shell.intCD in getter(descriptor)


class ShellMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        return [
         (
          hasVehicleDescrMechanic(vehDescr, VehicleMechanic.LOW_CHARGE_SHOT), VehicleMechanic.LOW_CHARGE_SHOT),
         (
          _hasShellMechanics(vehDescr, guiItem, VehicleMechanic.SHELL_CALIBRATION), VehicleMechanic.SHELL_CALIBRATION),
         (
          _hasShellMechanics(vehDescr, guiItem, VehicleMechanic.BUSTLE_FEED), VehicleMechanic.BUSTLE_FEED),
         (
          _hasShellMechanics(vehDescr, guiItem, VehicleMechanic.SHELL_PARAMS_SWITCHER), VehicleMechanic.SHELL_PARAMS_SWITCHER)]