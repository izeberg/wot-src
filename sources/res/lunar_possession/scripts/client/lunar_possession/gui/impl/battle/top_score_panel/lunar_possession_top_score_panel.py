from frameworks.wulf import ViewFlags, ViewSettings
from gui.shared import EVENT_BUS_SCOPE
from lunar_possession.gui.impl.gen.view_models.views.battle.top_score_panel.lunar_possession_top_score_panel_model import LunarPossessionTopScorePanelModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from lunar_possession.gui.shared.events import TeamScoreEvents
from helpers import dependency
from account_helpers.settings_core import ISettingsCore, settings_constants
from account_helpers.settings_core.settings_constants import GRAPHICS
from lunar_possession_common.component_helpers import isSpiritCarrier
from lunar_possession.gui.shared.events import BuffEvents
from skeletons.gui.battle_session import IBattleSessionProvider

class LunarPossessionTopScorePanelView(ViewImpl):
    __slots__ = ()
    _settingsCore = dependency.descriptor(ISettingsCore)
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        settings = ViewSettings(R.views.lunar_possession.battle.top_score_panel.LunarPossessionTopScorePanel(), ViewFlags.VIEW, LunarPossessionTopScorePanelModel())
        super(LunarPossessionTopScorePanelView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LunarPossessionTopScorePanelView, self).getViewModel()

    def _getListeners(self):
        return (
         (
          TeamScoreEvents.TEAM_SCORE_UPDATE, self.updateScore, EVENT_BUS_SCOPE.BATTLE),
         (
          BuffEvents.VEHICLE_GET_BUFF, self.updateTeamSpiritCarrier, EVENT_BUS_SCOPE.BATTLE),
         (
          BuffEvents.VEHICLE_LOSE_BUFF, self.updateTeamSpiritCarrier, EVENT_BUS_SCOPE.BATTLE))

    def _subscribe(self):
        super(LunarPossessionTopScorePanelView, self)._subscribe()
        self._settingsCore.onSettingsChanged += self.__onSettingsChanged

    def _unsubscribe(self):
        super(LunarPossessionTopScorePanelView, self)._unsubscribe()
        self._settingsCore.onSettingsChanged -= self.__onSettingsChanged

    def __onSettingsChanged(self, diff):
        if GRAPHICS.COLOR_BLIND in diff:
            with self.viewModel.transaction() as (model):
                model.setIsColorblindMode(diff[GRAPHICS.COLOR_BLIND])

    def updateTeamSpiritCarrier(self, event):
        arenaDP = self.guiSessionProvider.getArenaDP()
        vehicleID = event.vehicleID
        isAlly = arenaDP.isAlly(vehicleID)
        hasSpiritBuff = isSpiritCarrier(vehicleID)
        isAllyTeamSpiritCarrier = isAlly and hasSpiritBuff
        self.viewModel.setIsAllyTeamSpiritCarrier(isAllyTeamSpiritCarrier)

    def updateScore(self, event):
        allyScore, enemyScore, targetScore = event.teamScore
        self.fillModel(allyScore, enemyScore, targetScore)

    def fillModel(self, alliesPoints, enemiesPoints, maxPoints):
        with self.viewModel.transaction() as (model):
            model.setCurrentPoints(alliesPoints)
            model.setEnemyPoints(enemiesPoints)
            model.setMaxPoints(maxPoints)
            isColorBlind = self._settingsCore.getSetting(settings_constants.GRAPHICS.COLOR_BLIND)
            model.setIsColorblindMode(isColorBlind)