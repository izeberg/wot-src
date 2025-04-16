from AvatarInputHandler.control_modes import PostMortemControlMode

class FallTanksPostMortemCtrlMode(PostMortemControlMode):

    def _isPostmortemDelayEnabled(self):
        return False