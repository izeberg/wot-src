from __future__ import absolute_import
import CommandMapping
from AvatarInputHandler import control_modes

class LSArcadeControlMode(control_modes.ArcadeControlMode):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        cmdMap = CommandMapping.g_instance
        if cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown:
            return False
        return super(LSArcadeControlMode, self).handleKeyEvent(isDown, key, mods, event)


class LSSniperControlMode(control_modes.SniperControlMode):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        cmdMap = CommandMapping.g_instance
        if cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown:
            return False
        return super(LSSniperControlMode, self).handleKeyEvent(isDown, key, mods, event)