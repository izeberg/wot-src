import logging, WWISE, BigWorld
from constants import ARENA_PERIOD
from PlayerEvents import g_playerEvents
from script_component.DynamicScriptComponent import DynamicScriptComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent
from halloween_common.halloween_constants import INVALID_PHASE
from halloween.gui.sounds.sound_constants import BATTLE_START, ACTIVE_PHASE_RTPC, BATTLE_FINISH, PHASE_CHANGED, ARENA_PHASE_END_WARNING_EVENT_PREFIX, ActivePhaseState, DifficultyState, PhaseStartedVoiceover
from halloween.gui.sounds.arena_components import HWStaticDeathZoneSounds, HWPostMortemSounds, HWBossBattleMusic, HWEquipmentPanelSounds, HWBuffsPanelSounds, HWPersonalDeathZoneSounds, HWVoiceovers, HWTeamFightVoiceovers, HWPhaseStateUpdateSounds, HWVehicleDetectorSounds, HWBotSpawnSounds
from halloween.gui.sounds import playSound, ComponentsHolder
_logger = logging.getLogger(__name__)
_ARENA_SOUND_COMPONENTS = [
 HWStaticDeathZoneSounds,
 HWPostMortemSounds,
 HWBossBattleMusic,
 HWEquipmentPanelSounds,
 HWBuffsPanelSounds,
 HWPersonalDeathZoneSounds,
 HWVoiceovers,
 HWTeamFightVoiceovers,
 HWPhaseStateUpdateSounds,
 HWVehicleDetectorSounds,
 HWBotSpawnSounds]
_SUPPORTED_END_WARNING_PHASE_IDS = (1, 2, 3)
_PHASE_END_WARNING_TIME_OFFSET = 62

class HWArenaSoundComponent(DynamicScriptComponent):

    def __init__(self):
        super(HWArenaSoundComponent, self).__init__()
        self._components = ComponentsHolder(_ARENA_SOUND_COMPONENTS, self)
        self._shouldTriggerPhaseEndWarningEvent = False
        self._bossAuraIntersectionsCounter = 0

    def onDestroy(self):
        HWArenaPhasesComponent.onPhaseChanged -= self._onPhaseChanged
        HWArenaPhasesComponent.onPhaseTimeChanged -= self._onPhaseTimeChanged
        g_playerEvents.onArenaPeriodChange -= self._onArenaPeriodChaned
        if BigWorld.player().arena.period == ARENA_PERIOD.BATTLE:
            playSound(BATTLE_FINISH)
        self._components.onDestroy()
        super(HWArenaSoundComponent, self).onDestroy()

    def _onAvatarReady(self):
        HWArenaPhasesComponent.onPhaseChanged += self._onPhaseChanged
        HWArenaPhasesComponent.onPhaseTimeChanged += self._onPhaseTimeChanged
        g_playerEvents.onArenaPeriodChange += self._onArenaPeriodChaned
        arena = BigWorld.player().arena
        if arena.period == ARENA_PERIOD.BATTLE:
            playSound(BATTLE_START)
        self._setPhaseStates(HWArenaPhasesComponent.getInstance().activePhase)
        self._components.onAvatarReady()
        WWISE.WW_setState(DifficultyState.GROUP, DifficultyState.VALUE(arena.bonusType))

    def onBotCreated(self, vehicleType, position):
        self._components.call('onBotCreated', vehicleType, position)

    def onShotAtBoss(self, attackerID, attackReason, damage):
        self._components.call('onShotAtBoss', attackerID, attackReason, damage)

    def onBossEnterWorld(self, bossEntity):
        self._components.call('onBossEnterWorld', bossEntity)

    def _onPhaseChanged(self, arenaPhases):
        activePhase = arenaPhases.activePhase
        self._setPhaseStates(activePhase)
        PhaseStartedVoiceover.get(activePhase).play()
        if activePhase > 1:
            playSound(PHASE_CHANGED)

    def _setPhaseStates(self, activePhase):
        if activePhase == INVALID_PHASE:
            return
        self._shouldTriggerPhaseEndWarningEvent = activePhase in _SUPPORTED_END_WARNING_PHASE_IDS
        WWISE.WW_setRTCPGlobal(ACTIVE_PHASE_RTPC, activePhase)
        WWISE.WW_setState(ActivePhaseState.GROUP, ActivePhaseState.getStateByPhase(activePhase))

    def _onPhaseTimeChanged(self, timeLeft, _, lastPhase):
        if not lastPhase and self._shouldTriggerPhaseEndWarningEvent and 0 < timeLeft <= _PHASE_END_WARNING_TIME_OFFSET:
            self._shouldTriggerPhaseEndWarningEvent = False
            playSound(ARENA_PHASE_END_WARNING_EVENT_PREFIX.format(phase=HWArenaPhasesComponent.getInstance().activePhase))

    def _onArenaPeriodChaned(self, period, *_):
        if period == ARENA_PERIOD.BATTLE:
            playSound(BATTLE_START)
        elif period == ARENA_PERIOD.AFTERBATTLE:
            playSound(BATTLE_FINISH)

    def onBossAuraIntersect(self, vehicleId, entered):
        player = BigWorld.player()
        if not player or player.playerVehicleID != vehicleId:
            return
        if entered:
            if self._bossAuraIntersectionsCounter == 0:
                self._components.call('onBossAuraIntersectEvent', vehicleId, True)
            self._bossAuraIntersectionsCounter += 1
        else:
            self._bossAuraIntersectionsCounter -= 1
            if self._bossAuraIntersectionsCounter == 0:
                self._components.call('onBossAuraIntersectEvent', vehicleId, False)