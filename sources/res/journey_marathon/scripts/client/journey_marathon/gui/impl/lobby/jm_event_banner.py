from __future__ import absolute_import
import logging
from frameworks.wulf import ViewSettings
from gui.impl.backport import text
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as BannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService
from gui.impl.pub import ViewImpl
from helpers.dependency import descriptor
from journey_marathon.gui.impl.gen.view_models.views.lobby.src.views.tooltips.banner_tooltip_model import BannerTooltipModel
from journey_marathon.gui.shared.jm_event_dispatcher import showJmMapView, showJmIntro
from journey_marathon.jm_constants import JmFtState, JmTimeState, JM_RUNNING_OUT_THRESHOLD, JM_BANNER_ENABLED_FT_STATES, JM_BANNER_ENABLED_TIME_STATES
from journey_marathon.jm_helpers import jmCtrl, getJmMapViewOpened, setJmBannerAppearAnimSeen, getJmBannerAppearAnimSeen
from skeletons.gui.impl import IGuiLoader
_logger = logging.getLogger(__name__)

class JmEventBanner(BaseEventBanner):
    __eventsService = descriptor(IEventsService)
    __guiLoader = descriptor(IGuiLoader)
    NAME = 'JmEventBanner'
    bannerState = property(lambda self: self.__state)
    title = property(lambda self: self.__title)
    inProgressDescription = property(lambda self: self.__descr)
    introDescription = property(lambda self: self.__descr)
    timerValue = property(lambda self: self.__timerValue)
    playAppearAnim = property(lambda self: self.__playAnim)
    showTimerBeforeEventEnd = property(lambda self: JM_RUNNING_OUT_THRESHOLD)
    borderColor = property(lambda self: '#FFB947')

    def __init__(self):
        super(JmEventBanner, self).__init__()
        self.__state = BannerState.INACTIVE
        self.__title = ''
        self.__descr = ''
        self.__timerValue = 0
        self.__playAnim = False
        self.__isEnabled = self.isEnabled()
        ctrl = jmCtrl()
        ctrl.onJmFeatureStateChange += self.__updateEntries
        ctrl.onJmTimeChange += self.__updateEntries

    def prepare(self):
        ctrl = jmCtrl()
        timeState = ctrl.jmTime.getJmTimeState()
        ftState = ctrl.jmSwitcher.getJmFtState()
        if ftState == JmFtState.PAUSED:
            bannerState = BannerState.INACTIVE
        elif not getJmMapViewOpened() and timeState in (JmTimeState.DURING, JmTimeState.RUNNING_OUT):
            bannerState = BannerState.INTRO
        elif timeState == JmTimeState.PRE:
            bannerState = BannerState.ANNOUNCE
        elif timeState == JmTimeState.POST:
            bannerState = BannerState.FINISHED
        else:
            bannerState = BannerState.IN_PROGRESS
        self.__state = bannerState
        animState = bannerState == BannerState.INTRO or bannerState == BannerState.INACTIVE
        self.__playAnim = animState and not getJmBannerAppearAnimSeen()
        self.__timerValue = ctrl.jmTime.getJmTimeLeft() if timeState == JmTimeState.RUNNING_OUT and ftState == JmFtState.ACTIVE else 0
        textRes = R.strings.hangar_event_banners.event.dyn(JmEventBanner.NAME)
        self.__title = text(textRes.title())
        self.__descr = text(textRes.introDescription()) if bannerState == BannerState.INTRO else text(textRes.inProgressDescription())
        tooltip = self.__guiLoader.windowsManager.getViewByLayoutID(JmBannerTooltip.LAYOUT_ID)
        if tooltip is not None:
            tooltip.updateJmBannerTooltip(self)
        return

    def onAppear(self):
        if not self._isVisible:
            super(JmEventBanner, self).onAppear()
            self.__subscribe()

    def onDisappear(self):
        if self._isVisible:
            super(JmEventBanner, self).onDisappear()
            self.__unsubscribe()

    def onClick(self):
        errors = jmCtrl().jmConfig.getJmConfigErrors()
        if errors:
            jmCtrl().jmSysMessages.pushMessJmActionUnavailable()
            _logger.error('Banner disabled because of these errors:\n%s', ('\n').join(errors))
            return
        if self.__state in (BannerState.INTRO, BannerState.IN_PROGRESS):
            if not getJmMapViewOpened():
                showJmIntro()
            showJmMapView()

    def createToolTipContent(self, event):
        return JmBannerTooltip()

    @staticmethod
    def isEnabled():
        ctrl = jmCtrl()
        return ctrl.jmSwitcher.getJmFtState() in JM_BANNER_ENABLED_FT_STATES and ctrl.jmTime.getJmTimeState() in JM_BANNER_ENABLED_TIME_STATES

    def updateJmBanner(self, *_):
        EventBannersContainer().onBannerUpdate(self)

    def onAppearAnimationPlayed(self):
        super(JmEventBanner, self).onAppearAnimationPlayed()
        setJmBannerAppearAnimSeen()

    def __subscribe(self):
        ctrl = jmCtrl()
        ctrl.onJmFeatureStateChange += self.updateJmBanner
        ctrl.onJmTimeChange += self.updateJmBanner

    def __unsubscribe(self):
        ctrl = jmCtrl()
        ctrl.onJmFeatureStateChange -= self.updateJmBanner
        ctrl.onJmTimeChange -= self.updateJmBanner

    def __updateEntries(self, *_):
        isEnabled = self.isEnabled()
        if self.__isEnabled != isEnabled:
            self.__isEnabled = isEnabled
            self.__eventsService.updateEntries()


class JmBannerTooltip(ViewImpl):
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.tooltips.banner_tooltip()

    def __init__(self):
        super(JmBannerTooltip, self).__init__(settings=ViewSettings(layoutID=self.LAYOUT_ID, model=BannerTooltipModel()))

    def updateJmBannerTooltip(self, banner):
        with self.getViewModel().transaction() as (tx):
            tx.setBannerState(banner.bannerState)
            tx.setTimeLeft(jmCtrl().jmTime.getJmTimeLeft())

    def _onLoading(self, *args, **kwargs):
        super(JmBannerTooltip, self)._onLoading(*args, **kwargs)
        banner = EventBannersContainer().getEventBanner(JmEventBanner.NAME)
        banner.updateJmBanner()
        self.updateJmBannerTooltip(banner)