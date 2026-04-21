from __future__ import absolute_import
from last_stand.gui.scaleform.genConsts.LS_CM_HANDLER_TYPE import LS_CM_HANDLER_TYPE
from last_stand.gui.scaleform.daapi.view.lobby.tank_setup.context_menu.consumable import LSHangarConsumableSlotContextMenu

def getContextMenuHandlers():
    return (
     (
      LS_CM_HANDLER_TYPE.TANK_SETUP_LS_HANGAR_CONSUMABLE_SLOT, LSHangarConsumableSlotContextMenu),)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()