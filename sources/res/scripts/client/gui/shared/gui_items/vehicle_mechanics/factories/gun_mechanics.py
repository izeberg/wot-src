from __future__ import absolute_import
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from items.vehicle_mechanics_types import VehicleMechanicKeys

class GunMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        return [
         (
          guiItem.isAutoShoot(vehDescr), VehicleMechanicKeys.AUTO_SHOOT_GUN),
         (
          guiItem.isDualGun(vehDescr), VehicleMechanicKeys.DUAL_GUN),
         (
          guiItem.hasMechanic(VehicleMechanicKeys.DUAL_ACCURACY, vehDescr), VehicleMechanicKeys.DUAL_ACCURACY),
         (
          guiItem.isTwinGun(vehDescr), VehicleMechanicKeys.TWIN_GUN),
         (
          guiItem.isClipGun(vehDescr), VehicleMechanicKeys.MAGAZINE_GUN),
         (
          guiItem.isLowChargeShotGun(vehDescr), VehicleMechanicKeys.LOW_CHARGE_SHOT),
         (
          guiItem.isAutoReloadableWithBoost(vehDescr), VehicleMechanicKeys.AUTO_LOADER_GUN_BOOST),
         (
          guiItem.isAutoReloadable(vehDescr) and not guiItem.isAutoReloadableWithBoost(vehDescr),
          VehicleMechanicKeys.AUTO_LOADER_GUN),
         (
          guiItem.isDamageMutable(), VehicleMechanicKeys.DAMAGE_MUTABLE),
         (
          any(shell.descriptor.hasStun for shell in guiItem.defaultAmmo), VehicleMechanicKeys.STUN)]

    @classmethod
    def _getMechanicsParams(cls, guiItem, vehDescr):
        return guiItem.getDescriptor(vehDescr).mechanicsParams