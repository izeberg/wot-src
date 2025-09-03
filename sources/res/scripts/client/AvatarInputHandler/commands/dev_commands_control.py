import BigWorld, Keys
from constants import HAS_DEV_RESOURCES, IS_DEVELOPMENT
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand

class DevCommandsControl(InputHandlerCommand):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if BigWorld.isKeyDown(Keys.KEY_CAPSLOCK) and isDown and HAS_DEV_RESOURCES:
            avatar = BigWorld.player()
            if key == Keys.KEY_X:
                avatar.base.setDevelopmentFeature(0, 'reload_mechanics', 0, '')
                return False
        return False


def createDevCommandsControl():
    if IS_DEVELOPMENT:
        return DevCommandsControl()
    return InputHandlerCommand()