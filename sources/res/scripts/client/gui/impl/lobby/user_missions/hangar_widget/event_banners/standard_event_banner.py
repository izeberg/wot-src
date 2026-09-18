from __future__ import absolute_import
import typing
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class StandardEventBanner(BaseEventBanner):

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

    def fillModel(self, model):
        super(StandardEventBanner, self).fillModel(model)
        model.setIsMode(self.isMode)
        model.setTitle(self.title)
        model.setHasRewards(self.hasRewards)
        model.setIntroDescription(self.introDescription)
        model.setInProgressDescription(self.inProgressDescription)
        model.setBannerState(self.bannerState)
        model.setIconsPath(self.iconsPath)
        model.setVideosPath(self.videosPath)
        model.setBorderColor(self.borderColor)
        model.setTimerText(self.timerText)
        model.setTimerValue(self.timerValue)
        model.setEventEndDate(self.eventEndDate)
        model.setEventStartDate(self.eventStartDate)