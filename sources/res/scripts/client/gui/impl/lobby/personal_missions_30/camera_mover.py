import logging
from gui.subhangar.subhangar_state_groups import CameraMover
_logger = logging.getLogger(__name__)

class PersonalMissions3CameraMover(CameraMover):

    def __init__(self, callback=None):
        self.callback = callback

    def moveCamera(self, _, __):
        if self.callback:
            self.callback()
        else:
            _logger.error('PersonalMissions3CameraMover callback is None')