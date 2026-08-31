import typing
from components_base.component import Component
if typing.TYPE_CHECKING:
    from typing import Any, Optional

class InputHandlerCommand(Component):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        return False