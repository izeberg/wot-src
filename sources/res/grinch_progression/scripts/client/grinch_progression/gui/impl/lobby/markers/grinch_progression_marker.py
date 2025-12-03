import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from helpers import dependency
from grinch_progression.gui.impl.gen.view_models.views.lobby.markers.grinch_progression_marker_model import GrinchProgressionMarkerModel, MarkerState
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from grinch.skeletons.battle_controller import IGrinchController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared.utils import IHangarSpace
from gui.impl.lobby.new_year.markers.ho_hangar_marker_view import HOHangarMarkerView
from skeletons.new_year import IFriendServiceController
from gui.impl.new_year.navigation import NewYearNavigation
if typing.TYPE_CHECKING:
    from grinch_progression.gui.game_control import GrinchProgressionController
    from grinch.gui.game_control.grinch_controller import GrinchController
_MAX_SYNC_INITIATOR = 1000

class GrinchProgressionMarker(HOHangarMarkerView):
    __progressionCtrl = dependency.descriptor(IGrinchProgressionController)
    __grinchCtrl = dependency.descriptor(IGrinchController)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __friendService = dependency.descriptor(IFriendServiceController)
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.grinch_progression.mono.lobby.markers.grinch_progression_marker())
        settings.model = GrinchProgressionMarkerModel()
        settings.args = args
        settings.kwargs = kwargs
        self.__syncInitiator = 0
        super(GrinchProgressionMarker, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(GrinchProgressionMarker, self)._onLoading(*args, **kwargs)
        self.__updateMarker()

    def _getEvents(self):
        return (
         (
          self._objectObserver.onObjectStateChanged, self.__onObjectStateChanged),
         (
          self.__hangarSpace.onSpaceCreate, self._updateMarkerVisibility),
         (
          self.__friendService.onFriendHangarEnter, self._updateMarkerVisibility),
         (
          self.__friendService.onFriendHangarExit, self._updateMarkerVisibility),
         (
          self.__progressionCtrl.onDataUpdated, self.__updateMarker),
         (
          self.__grinchCtrl.onConfigChanged, self.__updateMarker),
         (
          self.__grinchCtrl.onSeasonStatusUpdated, self.__updateMarker),
         (
          self.__eventsCache.onSyncCompleted, self.__updateMarker))

    def _setMarkerVisible(self, isVisible):
        with self.viewModel.transaction() as (model):
            newValue = isVisible and self.__hangarSpace.spaceInited and not self.__friendService.isInFriendHangar and self.__grinchCtrl.isEnabled() and not self.__grinchCtrl.isFrozen()
            if model.getIsVisible() != newValue:
                model.setIsVisible(newValue)

    def __updateMarker(self, *args, **kwargs):
        self._updateMarkerVisibility()
        claimStats = self.__progressionCtrl.getClaimStats()
        if not self.__progressionCtrl.isPostProgression():
            points = claimStats.claimedPoints + self.__progressionCtrl.getPoints()
            maxPoints = self.__progressionCtrl.getMaxPointsForCurChapter()
            rewardsCount = self.__progressionCtrl.getNumberOfClaimableRewards()
        else:
            points = self.__progressionCtrl.getPoints()
            maxPoints = self.__progressionCtrl.getFinalStepPrice()
            rewardsCount = 1 if points >= maxPoints else 0
        with self.viewModel.transaction() as (model):
            model.setPoints(min(maxPoints, points))
            model.setPrevPoints(min(maxPoints, self.__progressionCtrl.getPointsSeenCount()))
            model.setCountdown(self.__grinchCtrl.getTimeTillNextBattlesStart())
            model.setNumberOfRewardsToClaim(rewardsCount)
            model.setPrevNumberOfRewardsToClaim(self.__progressionCtrl.getClaimableRewardsSeenCount())
            model.setMaxPoints(maxPoints)
            model.setIsPostProgression(self.__progressionCtrl.isPostProgression())
            model.setMarkerState(self.__getMarkerState())
        self.__progressionCtrl.setPointsSeenCount(points)
        self.__progressionCtrl.setClaimableRewardsSeenCount(rewardsCount)

    def __onObjectStateChanged(self, _):
        with self.viewModel.transaction() as (model):
            if NewYearNavigation.getCurrentObject() is None:
                if self.__syncInitiator >= _MAX_SYNC_INITIATOR:
                    self.__syncInitiator = 0
                else:
                    self.__syncInitiator += 1
                model.setSyncInitiator(self.__syncInitiator)
        return

    def __getMarkerState(self):
        season = self.__grinchCtrl.getCurrentSeason()
        if season and season.getCycleInfo():
            return MarkerState.ACTIVE
        if self.__grinchCtrl.getNextSeason():
            return MarkerState.LOCK
        return MarkerState.DONE