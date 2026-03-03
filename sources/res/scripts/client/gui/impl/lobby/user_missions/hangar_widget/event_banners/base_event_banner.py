from abc import ABCMeta
from helpers import time_utils
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState

class BaseEventBanner(object):
    __metaclass__ = ABCMeta
    NAME = ''

    def __init__(self):
        super(BaseEventBanner, self).__init__()
        self._isVisible = False

    @property
    def bannerState(self):
        return EventBannerState.INACTIVE

    @property
    def isMode(self):
        return False

    @property
    def hasRewards(self):
        return False

    @property
    def borderColor(self):
        return ''

    @property
    def title(self):
        return ''

    @property
    def iconsPath(self):
        return ''

    @property
    def videosPath(self):
        return ''

    @property
    def introDescription(self):
        return ''

    @property
    def inProgressDescription(self):
        return ''

    @property
    def timerText(self):
        return ''

    @property
    def timerValue(self):
        return 0

    @property
    def eventStartDate(self):
        return 0

    @property
    def eventEndDate(self):
        return 0

    @property
    def playAppearAnim(self):
        return False

    @property
    def showTimerBeforeEventEnd(self):
        hoursBeforeEnd = 72
        return hoursBeforeEnd * time_utils.ONE_HOUR

    @property
    def isVisible(self):
        return self._isVisible

    def createToolTipContent(self, event):
        return

    def onClick(self):
        pass

    def onAppearAnimationPlayed(self):
        pass

    def prepare(self):
        pass

    def onAppear(self):
        self._isVisible = True

    def onDisappear(self):
        self._isVisible = False