from __future__ import absolute_import
from AvatarInputHandler.kill_cam_modes import LookAtKillerMode

class WTLookAtKillerMode(LookAtKillerMode):

    def _canSwitchToAllyVehicle(self):
        return False