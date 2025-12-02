import typing
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from frameworks.wulf import ViewSettings
from grinch.skeletons.battle_controller import IGrinchController
from grinch.gui.impl.gen.view_models.views.lobby.banner_entry_point.grinch_banner_entry_point_model import GrinchBannerEntryPointModel, State
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.pub import ViewImpl
from helpers import dependency
if typing.TYPE_CHECKING:
    from grinch.gui.game_control.grinch_controller import GrinchController
    from grinch_progression.gui.game_control.grinch_progression_controller import GrinchProgressionController
_BANNER_STATE_TO_TOOLTIP_STATE = {EventBannerState.INACTIVE: State.FROZEN, EventBannerState.INTRO: State.INTRO, 
   EventBannerState.IN_PROGRESS: State.INPROGRESS}

class EventBannerTooltipView(ViewImpl):
    __slots__ = ('_bannerState', '_timerValue', '_performanceRisk', '_isBattlesFinished',
                 '_isCompleted')
    _grinchCtrl = dependency.descriptor(IGrinchController)
    _grinchProgressionCtrl = dependency.descriptor(IGrinchProgressionController)

    def __init__(self, bannerState, timerValue, performanceRisk, isBattlesFinished, isCompleted):
        settings = ViewSettings(R.views.grinch.lobby.tooltips.EventBannerTooltip())
        settings.model = GrinchBannerEntryPointModel()
        super(EventBannerTooltipView, self).__init__(settings)
        self._bannerState = bannerState
        self._timerValue = timerValue
        self._performanceRisk = performanceRisk
        self._isBattlesFinished = isBattlesFinished
        self._isCompleted = isCompleted

    @property
    def viewModel(self):
        return super(EventBannerTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(EventBannerTooltipView, self)._onLoading(*args, **kwargs)
        if self._isBattlesFinished:
            state = State.BATTLESFINISHED
        elif self._isCompleted:
            state = State.COMPLETED
        else:
            state = _BANNER_STATE_TO_TOOLTIP_STATE.get(self._bannerState, State.INPROGRESS)
        with self.getViewModel().transaction() as (model):
            model.setPerformanceRisk(self._performanceRisk)
            model.setState(state)
            model.setDate(self._grinchCtrl.getStartDate())
            model.setEndDate(self._grinchCtrl.getAllSeasonsEndDate())
            claimStats = self._grinchProgressionCtrl.getClaimStats()
            model.setShowClaimableRewards(self._grinchProgressionCtrl.showClaimableRewards())
            model.setFinishedLevelsCount(claimStats.claimedCount)
            model.setMaxProgressionStep(self._grinchProgressionCtrl.getMaxChapterStep())
            model.setNextTimeEnable(self._timerValue)