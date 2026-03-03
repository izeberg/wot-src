from __future__ import absolute_import
from fall_tanks.gui.battle_control.controllers.consumables import opt_devices_ctrl

def createOptDevicesCtrl(setup):
    return opt_devices_ctrl.FallTanksOptDevicesController(setup)


__all__ = ('createOptDevicesCtrl', )