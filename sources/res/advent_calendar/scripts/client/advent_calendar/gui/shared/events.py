from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class AdventCalendarEvent(HasCtxEvent):
    PROGRESSION_REWARD_VIEWED = 'progressionRewardViewed'
    CHANGE_BLUR_STATUS = 'changeBlurStatus'
    INTRO_CLOSE_STARTED = 'introCloseStarted'