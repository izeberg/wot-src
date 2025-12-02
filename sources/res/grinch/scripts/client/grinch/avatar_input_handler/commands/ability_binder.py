import BigWorld, Keys, CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from grinch.gui.grinch_gui_constants import ABILITY_COMMANDS
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class AbilityBinderCommand(InputHandlerCommand):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if not isDown or not CommandMapping.g_instance.isFiredList(ABILITY_COMMANDS, key):
            return False
        if mods or BigWorld.isKeyDown(Keys.KEY_CAPSLOCK):
            return False
        ammoCtrl = self.guiSessionProvider.shared.ammo
        if ammoCtrl:
            ammoCtrl.handleAmmoChoice(key)
            return True
        return False