from __future__ import absolute_import
import BigWorld, logging
from fort_rush.gui.battle_control.controllers.respawn_ctrl import ISpawnListener
from fort_rush.gui.scaleform.daapi.view.battle.crosshair.container import FortRushCrosshairPanelContainer
from fort_rush.gui.shared.events import RespawnCtrlEvent
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.Scaleform.daapi.view.battle.shared.indicators import createDamageIndicator
from gui.Scaleform.daapi.view.battle.shared import finish_sound_player
from gui.Scaleform.daapi.view.battle.classic.page import ClassicComponentsConfig, DynamicAliases as ClassicDynamicAliases
from gui.Scaleform.daapi.view.battle.shared.indicators import createPredictionIndicator
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig
from fort_rush.gui.fort_rush_gui_constants import BATTLE_CTRL_ID
from PlayerEvents import g_playerEvents
from constants import ARENA_PERIOD
from fort_rush.gui.impl.battle import showFortRushHud
from fort_rush.gui.scaleform.daapi.view.battle.markers2d.manager import FortRushMarkersManager
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_BATTLE_VIEW_ALIASES import FORT_RUSH_BATTLE_VIEW_ALIASES
from fort_rush.gui.scaleform.daapi.view.meta.FortRushBattlePageMeta import FortRushBattlePageMeta
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from shared_utils import CONST_CONTAINER
from fort_rush.gui.scaleform.daapi.view.battle.battle_hints import FortRushBattleHintComponent
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams
from fort_rush.gui.scaleform.daapi.view.battle.battle_hints import FortRushBattleHintsQueue, FortRushBattleHint
_logger = logging.getLogger(__name__)
COMMON_CLASSIC_CONFIG = ClassicComponentsConfig()
EXTENDED_CLASSIC_CONFIG = COMMON_CLASSIC_CONFIG + ComponentsConfig(config=(
 (
  BATTLE_CTRL_ID.ARENA_PERIOD, (ClassicDynamicAliases.FINISH_SOUND_PLAYER,)),
 (
  BATTLE_CTRL_ID.TEAM_BASES, (ClassicDynamicAliases.FINISH_SOUND_PLAYER,)),
 (
  BATTLE_CTRL_ID.BATTLE_FIELD_CTRL, (ClassicDynamicAliases.FINISH_SOUND_PLAYER,))), viewsConfig=(
 (
  ClassicDynamicAliases.FINISH_SOUND_PLAYER, finish_sound_player.FinishSoundPlayer),))

class DynamicAliases(CONST_CONTAINER):
    FORT_RUSH_BATTLE_HINT = 'fortRushBattleHint'


EXT_CONFIG = ComponentsConfig(config=(
 (
  BATTLE_CTRL_ID.BATTLE_HINTS, (DynamicAliases.FORT_RUSH_BATTLE_HINT,)),
 (
  BATTLE_CTRL_ID.HIT_DIRECTION,
  (
   BATTLE_VIEW_ALIASES.PREDICTION_INDICATOR,
   BATTLE_VIEW_ALIASES.HIT_DIRECTION)),
 (
  BATTLE_CTRL_ID.FORT_RUSH_GUI_CTRL,
  (
   FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW,
   FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_VEHICLE_SELECTOR))), viewsConfig=(
 (
  BATTLE_VIEW_ALIASES.PREDICTION_INDICATOR, createPredictionIndicator),
 (
  BATTLE_VIEW_ALIASES.HIT_DIRECTION, createDamageIndicator),
 (
  DynamicAliases.FORT_RUSH_BATTLE_HINT,
  lambda : FortRushBattleHintComponent(DynamicAliases.FORT_RUSH_BATTLE_HINT, BattleHintQueueParams('text', queueClass=FortRushBattleHintsQueue, hintClass=FortRushBattleHint, withFadeOut=False)))))
_EXTERNAL_COMPONENTS = (
 FortRushCrosshairPanelContainer, FortRushMarkersManager)

class FortRushBattlePage(FortRushBattlePageMeta, ISpawnListener):

    def __init__(self, components=None, external=_EXTERNAL_COMPONENTS, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS, **kwargs):
        self.__savedVisibleComponents = set()
        if components is None:
            components = COMMON_CLASSIC_CONFIG if self.sessionProvider.isReplayPlaying else EXTENDED_CLASSIC_CONFIG
        components = components + EXT_CONFIG
        super(FortRushBattlePage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        return

    def _populate(self):
        super(FortRushBattlePage, self)._populate()
        showFortRushHud()
        respawnCtrl = self.sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.FORT_RUSH_GUI_CTRL)
        if respawnCtrl:
            respawnCtrl.addRuntimeView(self)
        else:
            _logger.warning('[FORT_RUSH][BATTLE_PAGE] _populate: respawnCtrl is None')

    def _onBattleLoadingFinish(self):
        super(FortRushBattlePage, self)._onBattleLoadingFinish()
        self._setComponentsVisibility(hidden={BATTLE_VIEW_ALIASES.FRAG_CORRELATION_BAR})
        if self.__savedVisibleComponents:
            return
        if BigWorld.player().arena.period == ARENA_PERIOD.BATTLE:
            self.__setVisibilityInitBattlePeriod()

    def _startBattleSession(self):
        super(FortRushBattlePage, self)._startBattleSession()
        g_playerEvents.onArenaPeriodChange += self.__onArenaPeriodChange
        g_playerEvents.onRoundFinished += self.__onRoundFinished

    def _stopBattleSession(self):
        g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChange
        g_playerEvents.onRoundFinished -= self.__onRoundFinished
        super(FortRushBattlePage, self)._stopBattleSession()

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(FortRushBattlePage, self)._onRegisterFlashComponent(viewPy, alias)
        if alias in (
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW,
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_VEHICLE_SELECTOR):
            self._setComponentsVisibility(hidden={alias})

    def __onArenaPeriodChange(self, period, *_):
        if period == ARENA_PERIOD.BATTLE:
            self.__setVisibilityInitBattlePeriod()

    def __onRoundFinished(self, *_):
        hiddenComponents = set()
        self._setComponentsVisibility(hidden=hiddenComponents)

    def __setVisibilityInitBattlePeriod(self):
        visibleComponents = set()
        hiddenComponents = {
         BATTLE_VIEW_ALIASES.PREBATTLE_TIMER,
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW,
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_VEHICLE_SELECTOR}
        self._setComponentsVisibility(visible=visibleComponents, hidden=hiddenComponents)

    def _dispose(self):
        super(FortRushBattlePage, self)._dispose()
        g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChange

    def showSpawnPoints(self):
        if self.__savedVisibleComponents:
            return
        self._toggleFullStats(isShown=False)
        self.__savedVisibleComponents = set(self.as_getComponentsVisibilityS())
        availableComponents = self.__savedVisibleComponents
        desiredVisibleComponents = {
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW,
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_VEHICLE_SELECTOR,
         BATTLE_VIEW_ALIASES.MINIMAP,
         BATTLE_VIEW_ALIASES.PLAYERS_PANEL,
         BATTLE_VIEW_ALIASES.BATTLE_TIMER,
         BATTLE_VIEW_ALIASES.BATTLE_MESSENGER}
        visibleComponents = desiredVisibleComponents
        hiddenComponents = availableComponents - visibleComponents
        self._setComponentsVisibility(visible=visibleComponents, hidden=hiddenComponents)
        self.as_setRespawnModeS(True)
        self.app.enterGuiControlMode(FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW)
        g_eventBus.handleEvent(RespawnCtrlEvent(RespawnCtrlEvent.SHOW_SPAWN_POINTS), scope=EVENT_BUS_SCOPE.GLOBAL)
        self.__toggleExternalComponentsVisibility(externalComponents=self._external, isVisible=False)

    def closeSpawnPoints(self):
        if not self.__savedVisibleComponents:
            return
        self._toggleFullStats(isShown=False)
        hiddenComponents = {
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW,
         FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_VEHICLE_SELECTOR}
        visibleComponents = self.__savedVisibleComponents - hiddenComponents
        self.__savedVisibleComponents = set()
        self._setComponentsVisibility(visible=visibleComponents, hidden=hiddenComponents)
        self.as_setRespawnModeS(False)
        self.app.leaveGuiControlMode(FORT_RUSH_BATTLE_VIEW_ALIASES.FORT_RUSH_RESPAWN_VIEW)
        g_eventBus.handleEvent(RespawnCtrlEvent(RespawnCtrlEvent.HIDE_SPAWN_POINTS), scope=EVENT_BUS_SCOPE.GLOBAL)
        self.__toggleExternalComponentsVisibility(externalComponents=self._external, isVisible=True)
        if BigWorld.player().arena.period == ARENA_PERIOD.BATTLE:
            self.__setVisibilityInitBattlePeriod()

    def __toggleExternalComponentsVisibility(self, externalComponents, isVisible):
        for component in externalComponents:
            component.setVisible(isVisible)