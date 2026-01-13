from __future__ import absolute_import
import BattleReplay
from ReplayEvents import g_replayEvents
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater

class ReplayPausedViewUpdater(ViewUpdater):

    def __init__(self, *args, **kwargs):
        super(ReplayPausedViewUpdater, self).__init__(*args, **kwargs)
        self.isPaused = False

    def initialize(self):
        super(ReplayPausedViewUpdater, self).initialize()
        g_replayEvents.onPause += self.__onReplayPaused
        g_replayEvents.onTimeWarpFinish += self.__onReplayTimeWarpFinished

    def finalize(self):
        super(ReplayPausedViewUpdater, self).finalize()
        g_replayEvents.onPause -= self.__onReplayPaused
        g_replayEvents.onTimeWarpFinish -= self.__onReplayTimeWarpFinished

    def __onReplayTimeWarpFinished(self):
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying:
            self.__onReplayPaused(replayCtrl.isPaused, True)

    def __onReplayPaused(self, isPaused, forced=False):
        if forced or self.isPaused != isPaused:
            self.isPaused = isPaused
            self.view.onReplayPaused(isPaused)