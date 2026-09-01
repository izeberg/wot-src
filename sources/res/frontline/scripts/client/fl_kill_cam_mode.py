from AvatarInputHandler.kill_cam_modes import LookAtKillerMode

class FLLookAtKillerMode(LookAtKillerMode):

    def _canSwitchToAllyVehicle(self):
        return False