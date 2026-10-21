import BigWorld, CommandMapping
from AvatarInputHandler.control_modes import PostMortemControlMode

class PortalPostMortemControlMode(PostMortemControlMode):

    def _isPostmortemDelayEnabled(self):
        return False

    def handleKeyEvent(self, isDown, key, mods, event=None):
        cmdMap = CommandMapping.g_instance
        guiCtrlEnabled = BigWorld.player().isForcedGuiControlMode()
        if cmdMap.isFired(CommandMapping.CMD_CM_POSTMORTEM_NEXT_VEHICLE, key) and isDown and not guiCtrlEnabled:
            return True
        if cmdMap.isFired(CommandMapping.CMD_CM_POSTMORTEM_SELF_VEHICLE, key) and isDown and not guiCtrlEnabled:
            return True
        return super(PortalPostMortemControlMode, self).handleKeyEvent(isDown, key, mods, event)