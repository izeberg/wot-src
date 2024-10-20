from gui.Scaleform.daapi.view.meta.PvePlayerLivesMeta import PvePlayerLivesMeta
from gui.battle_control import avatar_getter
from TeamInfoLivesComponent import TeamInfoLivesComponent

class PvePlayerLives(PvePlayerLivesMeta):

    def _populate(self):
        super(PvePlayerLives, self)._populate()
        teamLives = TeamInfoLivesComponent.getInstance()
        if teamLives is not None:
            teamLives.onTeamLivesUpdated += self._onTeamLivesUpdated
        self._updateRespawnInfo()
        return

    def _dispose(self):
        teamLives = TeamInfoLivesComponent.getInstance()
        if teamLives is not None:
            teamLives.onTeamLivesUpdated -= self._onTeamLivesUpdated
        super(PvePlayerLives, self)._dispose()
        return

    def _updateRespawnInfo(self):
        teamLives = TeamInfoLivesComponent.getInstance()
        if not teamLives:
            return
        playerVehicleID = avatar_getter.getPlayerVehicleID()
        lives = teamLives.getLives(playerVehicleID)
        usedLives = teamLives.getUsedLives(playerVehicleID)
        lockedLives = teamLives.getLockedLives(playerVehicleID)
        self.as_setCountLivesS(lives, usedLives, lockedLives)

    def _onTeamLivesUpdated(self):
        self._updateRespawnInfo()