import BigWorld
from gui import SystemMessages
from chat_shared import SYS_MESSAGE_TYPE
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.new_year.tooltips.ho_surprise_banner_tooltip import HOSurpriseBannerTooltip
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from gui.Scaleform.Waiting import Waiting
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService
from gui.shared.event_dispatcher import showSurpriseGiftWindow
from gui.shared.system_factory import registerBannerEntryPointValidator
from helpers import dependency
from messenger.proto.events import g_messengerEvents
from skeletons.new_year import INewYearController
SURPRISE_ENTRY_POINT = 'SurpriseEntryPoint'

@dependency.replace_none_kwargs(ctrl=INewYearController)
def isSurpriseBannerAvailable(ctrl=None):
    return ctrl.surpriseBannerHelper.isEntryPointAvailable()


def registerSurpriseBanner():
    if SurpriseBanner is not None:
        ebc = EventBannersContainer()
        if ebc.getEventBanner(SURPRISE_ENTRY_POINT):
            return
        registerBannerEntryPointValidator(SURPRISE_ENTRY_POINT, isSurpriseBannerAvailable)
        ebc.registerEventBanner(SurpriseBanner)
    return


class SurpriseBanner(BaseEventBanner):
    NAME = SURPRISE_ENTRY_POINT
    __nyController = dependency.descriptor(INewYearController)
    __eventsService = dependency.descriptor(IEventsService)

    def __init__(self):
        super(SurpriseBanner, self).__init__()
        self._state = ''
        self._eventStartDate = 0
        self._eventEndDate = 0
        self._timerValue = 0
        self._playAppearAnim = False
        self.__surpriseToken = ''

    @property
    def borderColor(self):
        return '#bd5417'

    @property
    def bannerState(self):
        return self._state

    @property
    def introDescription(self):
        return ' '

    @property
    def timerValue(self):
        return self._timerValue

    @property
    def eventStartDate(self):
        return self._eventStartDate

    @property
    def eventEndDate(self):
        return self._eventEndDate

    def createToolTipContent(self, event):
        return HOSurpriseBannerTooltip(isActiveState=self._state == EventBannerState.INTRO)

    def onClick(self):
        if self._state is not EventBannerState.INTRO:
            return
        Waiting.show('synchronize')
        BigWorld.player().requestSingleToken(self.__surpriseToken, lambda requestID, resultID, errorStr: self.__response(resultID, errorStr))

    def __response(self, code, _):
        if code != 0:
            SystemMessages.pushI18nMessage('#system_messages:newYear/surprise/claim_failed', type=SystemMessages.SM_TYPE.Error, priority='high')
            Waiting.hide('synchronize')

    def __onChatMessageReceived(self, *args):
        _, message = args
        tokenQuestRewards = None
        if message is not None and message.type == SYS_MESSAGE_TYPE.tokenQuests.index() and message.data is not None:
            tokenQuestRewards = message.data.get('detailedRewards', {}).get(self.__surpriseToken)
        if tokenQuestRewards is None:
            return
        else:
            Waiting.hide('synchronize')
            showSurpriseGiftWindow()
            return

    def prepare(self):
        self.__surpriseToken = self.__nyController.surpriseBannerHelper.surpriseToken
        self._state, self._eventStartDate, self._eventEndDate, self._timerValue = self.__nyController.surpriseBannerHelper.getBannerState()

    def onAppear(self):
        if self._isVisible:
            return
        super(SurpriseBanner, self).onAppear()
        g_messengerEvents.serviceChannel.onChatMessageReceived += self.__onChatMessageReceived
        self.__nyController.onStateChanged += self.__onUpdate
        self.__nyController.surpriseBannerHelper.onTimeStatusUpdated += self.__onUpdate

    def onDisappear(self):
        if not self._isVisible:
            return
        else:
            super(SurpriseBanner, self).onDisappear()
            self.__surpriseToken = None
            g_messengerEvents.serviceChannel.onChatMessageReceived -= self.__onChatMessageReceived
            self.__nyController.onStateChanged -= self.__onUpdate
            self.__nyController.surpriseBannerHelper.onTimeStatusUpdated -= self.__onUpdate
            return

    def __onUpdate(self, *_):
        if isSurpriseBannerAvailable():
            EventBannersContainer().onBannerUpdate(self)
        else:
            self.__eventsService.updateEntries()