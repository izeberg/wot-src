from AvatarInputHandler.control_modes import PostMortemControlMode

class LunarPossessionPostMortemCtrlMode(PostMortemControlMode):

    def _isPostmortemDelayEnabled(self):
        return False