from account_helpers import AccountSettings
from account_helpers.AccountSettings import OTG_EVENT_BANNER_ANIMATION_SHOWN
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService
from gui.shared.system_factory import registerBannerEntryPointValidator
from helpers import dependency, time_utils
from one_time_gift.gui.impl.lobby.tooltips.otg_event_banner_tooltip import OTGBannerTooltipView
from one_time_gift.gui.messages import pushOTGNotAvailableErrorNotification
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
OTG_UMG_ENTRY_POINT = 'OneTimeGiftEntryPoint'

@dependency.replace_none_kwargs(ctrl=IOneTimeGiftController)
def isOTGBannerAvailable(ctrl=None):
    return ctrl.isEntryPointEnabled


def registerOneTimeGiftEventBanner():
    ebc = EventBannersContainer()
    if ebc.getEventBanner(OTG_UMG_ENTRY_POINT):
        return
    registerBannerEntryPointValidator(OTG_UMG_ENTRY_POINT, isOTGBannerAvailable)
    ebc.registerEventBanner(OneTimeGiftEventBanner)


def getOneTimeGiftEventBanner():
    return EventBannersContainer().getEventBanner(OTG_UMG_ENTRY_POINT)


class OneTimeGiftEventBanner(BaseEventBanner):
    NAME = OTG_UMG_ENTRY_POINT
    __eventsService = dependency.descriptor(IEventsService)
    __oneTimeGiftController = dependency.descriptor(IOneTimeGiftController)

    def __init__(self):
        super(OneTimeGiftEventBanner, self).__init__()
        self._state = ''
        self._eventStartDate = 0
        self._eventEndDate = 0
        self._timerValue = 0
        self._playAppearAnim = False

    @property
    def borderColor(self):
        return '#6298D4'

    @property
    def bannerState(self):
        return self._state

    @property
    def timerValue(self):
        return self._timerValue

    @property
    def eventStartDate(self):
        return self._eventStartDate

    @property
    def eventEndDate(self):
        return self._eventEndDate

    @property
    def isVisible(self):
        return self._isVisible

    @property
    def playAppearAnim(self):
        return self._playAppearAnim

    def createToolTipContent(self, event):
        return OTGBannerTooltipView()

    def onClick(self):
        if self._state in (EventBannerState.INTRO, EventBannerState.IN_PROGRESS):
            self.__oneTimeGiftController.onEntryPointClicked()
            return
        pushOTGNotAvailableErrorNotification()

    def prepare(self):
        self._state, self._eventStartDate, self._eventEndDate, self._timerValue = self.__getBannerState()
        self._playAppearAnim = False
        animationIsShown = AccountSettings.getUIFlag(OTG_EVENT_BANNER_ANIMATION_SHOWN)
        if not animationIsShown and self._state in (
         EventBannerState.INTRO, EventBannerState.IN_PROGRESS):
            self._playAppearAnim = True
            AccountSettings.setUIFlag(OTG_EVENT_BANNER_ANIMATION_SHOWN, True)

    def onAppear(self):
        if self._isVisible:
            return
        super(OneTimeGiftEventBanner, self).onAppear()
        self.__oneTimeGiftController.onSettingsChanged += self.update
        self.__oneTimeGiftController.onEntryPointUpdated += self.update
        self.__oneTimeGiftController.onPlayerOTGStatusChanged += self.update

    def onDisappear(self):
        if not self._isVisible:
            return
        super(OneTimeGiftEventBanner, self).onDisappear()
        self.__oneTimeGiftController.onSettingsChanged -= self.update
        self.__oneTimeGiftController.onEntryPointUpdated -= self.update
        self.__oneTimeGiftController.onPlayerOTGStatusChanged -= self.update

    def update(self, *_):
        if not isOTGBannerAvailable() or not self._isVisible:
            self.__eventsService.updateEntries()
        else:
            EventBannersContainer().onBannerUpdate(self)

    def __getBannerState(self):
        eventStartDate = 0
        eventEndDate = 0
        timerValue = 0
        state = EventBannerState.INACTIVE
        if self.__oneTimeGiftController.isEntryPointEnabled:
            eventStartDate = self.__oneTimeGiftController.getStartTime()
            eventEndDate = self.__oneTimeGiftController.getEndTime()
            if self.__oneTimeGiftController.isEntryPointActive:
                timerValue = eventEndDate - time_utils.getServerUTCTime()
                state = EventBannerState.IN_PROGRESS if self.__oneTimeGiftController.introShown else EventBannerState.INTRO
        return (state, eventStartDate, eventEndDate, timerValue)