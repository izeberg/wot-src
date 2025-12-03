import typing
from GrinchAccountSettings import isBannerSeen, setBannerSeen
from grinch.gui.Scaleform.genConsts.GRINCH_HANGAR_ALIASES import GRINCH_HANGAR_ALIASES
from grinch.gui.grinch_gui_constants import SELECTOR_BATTLE_TYPES
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from grinch.gui.impl.lobby.banner_entry_point.event_banner_tooltip import EventBannerTooltipView
from grinch.gui.impl.lobby.banner_entry_point import grinch_banner_entry_point
from grinch.gui.impl.lobby.mode_selector.grinch_mode_selector_item import PERFORMANCE_MAP
from grinch.gui.game_control.performance_analyzer import IPerformanceAnalyzer
from grinch.skeletons.battle_controller import IGrinchController
from grinch.gui.impl.gen.view_models.views.lobby.banner_entry_point.grinch_banner_entry_point_model import PerformanceRiskEnum
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from gui.shared.utils.SelectorBattleTypesUtils import isKnownBattleType
from gui.shared.utils.scheduled_notifications import Notifiable
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService
from helpers import dependency, time_utils
from gui.impl import backport
from gui.impl.gen import R
if typing.TYPE_CHECKING:
    from grinch.gui.game_control.grinch_controller import GrinchController

class GrinchEventBanner(BaseEventBanner, Notifiable):
    NAME = GRINCH_HANGAR_ALIASES.GRINCH_ENTRY_POINT
    _grinchCtrl = dependency.descriptor(IGrinchController)
    _grinchProgressionCtrl = dependency.descriptor(IGrinchProgressionController)
    _eventsService = dependency.descriptor(IEventsService)
    _performanceAnalyzer = dependency.descriptor(IPerformanceAnalyzer)

    def __init__(self):
        self._isVisible = True
        super(GrinchEventBanner, self).__init__()
        self._state = EventBannerState.INACTIVE
        self._timerValue = 0
        self._playAppearAnim = False
        self._isBattlesFinished = False
        self._isCompleted = False
        self._performanceRisk = PerformanceRiskEnum.LOWRISK

    @property
    def bannerState(self):
        return self._state

    @property
    def isMode(self):
        return True

    @property
    def borderColor(self):
        return '#37DEC4'

    @property
    def timerValue(self):
        return self._timerValue

    @property
    def eventStartDate(self):
        return self._grinchCtrl.getStartDate()

    @property
    def eventEndDate(self):
        return self._grinchCtrl.getAllSeasonsEndDate()

    @property
    def inProgressDescription(self):
        if self._grinchProgressionCtrl.showClaimableRewards():
            return backport.text(R.strings.hangar_event_banners.event.GrinchEntryPoint.claimableRewards.description())
        return super(GrinchEventBanner, self).inProgressDescription

    @property
    def playAppearAnim(self):
        return self._playAppearAnim

    def createToolTipContent(self, event):
        return EventBannerTooltipView(self._state, self._timerValue, self._performanceRisk, self._isBattlesFinished, self._isCompleted)

    def onClick(self):
        if self._state == EventBannerState.INACTIVE and not self._grinchProgressionCtrl.showClaimableRewards() and not self._timerValue:
            return
        self._grinchCtrl.selectMode()

    def prepare(self):
        self._performanceRisk = PERFORMANCE_MAP.get(self._performanceAnalyzer.getPerformanceGroup(), PerformanceRiskEnum.LOWRISK)
        self._playAppearAnim = not isBannerSeen()
        self._timerValue = 0
        self._isBattlesFinished = self._grinchCtrl.getCurrentSeason() is None and self._grinchCtrl.getNextSeason() is None
        self._isCompleted = False
        timeToStart = self._grinchCtrl.getStartDate()
        now = time_utils.getCurrentLocalServerTimestamp()
        deltaToStart = timeToStart - now
        if self._grinchProgressionCtrl.showClaimableRewards():
            self._state = EventBannerState.IN_PROGRESS
            return
        else:
            if self._grinchCtrl.isEnabled() and now < timeToStart:
                self._timerValue = deltaToStart
                self._state = EventBannerState.INACTIVE
                return
            if self._isBattlesFinished:
                self._state = EventBannerState.INACTIVE
                return
            if not self._grinchCtrl.isAvailable():
                self._state = EventBannerState.INACTIVE
                return
            if not isKnownBattleType(SELECTOR_BATTLE_TYPES.GRINCH):
                self._state = EventBannerState.INTRO
                return
            self._timerValue = self._getTimeLeft()
            self._isCompleted = self._grinchProgressionCtrl.isPostProgression()
            self._state = EventBannerState.IN_PROGRESS
            return

    def onAppear(self):
        if self._isVisible:
            return
        if not isBannerSeen():
            setBannerSeen()
        super(GrinchEventBanner, self).onAppear()
        self._grinchCtrl.onPrimeTimeStatusUpdated += self._onUpdate

    def onDisappear(self):
        if not self._isVisible:
            return
        super(GrinchEventBanner, self).onDisappear()
        self._grinchCtrl.onPrimeTimeStatusUpdated -= self._onUpdate
        self.clearNotification()

    def _onUpdate(self, *args, **kwargs):
        self.clearNotification()
        if grinch_banner_entry_point.isGrinchBannerEntryPointAvailable():
            EventBannersContainer().onBannerUpdate(self)
        else:
            self._eventsService.updateEntries()

    def _getTimeLeft(self):
        if not self._grinchCtrl.isEnabled() or self._grinchCtrl.getCurrentSeason() is None:
            return 0
        now = time_utils.getCurrentLocalServerTimestamp()
        return self._grinchCtrl.getAllSeasonsEndDate() - now