import BigWorld, logging
from Event import EventManager, Event
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID, FEEDBACK_EVENT_ID
from halloween.gui.scaleform.daapi.view.battle.buffs_notification_panel import BuffsNotificationSystem
from halloween.gui.scaleform.daapi.view.battle.buffs_panel import findBuffsPanelComponents
from helpers import dependency, isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider
from HWArenaInfoBossHealthBarComponent import getArenaInfoBossHealthBarComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from halloween.gui.battle_control.halloween_battle_constants import VEHICLE_VIEW_STATE
from helpers.CallbackDelayer import CallbackDelayer
_logger = logging.getLogger(__name__)

class EventBattleGoal(object):
    UNKNOWN = None
    COLLECT_SOULS = 'halloween.collectSouls'
    GET_TO_COLLECTOR = 'halloween.getToCollector'


class HWBattleGUIController(IArenaVehiclesController):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    _TIME_TO_END_NOTIFY = 10
    _UPDATE_PERIOD = 0.5

    def __init__(self):
        super(HWBattleGUIController, self).__init__()
        self.__eManager = EventManager()
        self.onApplyBuff = Event(self.__eManager)
        self.onUnapplyBuff = Event(self.__eManager)
        self.onBuffStateChanged = Event(self.__eManager)
        self.onVehicleDetectorChangeDistance = Event(self.__eManager)
        self.onBattleGoalChanged = Event(self.__eManager)
        self.onBossAuraVictimMarkerIcon = Event(self.__eManager)
        self.onVehicleBuffIconAdded = Event(self.__eManager)
        self.onVehicleBuffIconRemoved = Event(self.__eManager)
        self.onPhaseChanged = Event(self.__eManager)
        self.onSoulCollectorProgress = Event(self.__eManager)
        self.onHandleEquipmentPressed = Event(self.__eManager)
        self.onShowPanelBuffNotification = Event(self.__eManager)
        self.onBossHealthActivated = Event(self.__eManager)
        self.onBossHealthChanged = Event(self.__eManager)
        self.onBossLivesChanged = Event(self.__eManager)
        self.onBossMinionsCountChanged = Event(self.__eManager)
        self.onBossHPBarVisibilityChanged = Event(self.__eManager)
        self.onBossVulnerableChanged = Event(self.__eManager)
        self.onSoulsContainerReady = Event(self.__eManager)
        self.onVehicleMaxHealthChanged = Event(self.__eManager)
        self._callbackDelayer = CallbackDelayer()
        self._currentGoal = EventBattleGoal.UNKNOWN
        self._currentCollector = None
        self._vehiclesInRadius = set()
        self._isCollectorFull = False
        self._vehicleMarkerIcons = {}
        self._hiddenVehicleIDs = set()
        self._ignoreBuffNotification = set()
        return

    @property
    def currentGoal(self):
        return self._currentGoal

    @property
    def vehicleMarkerIcons(self):
        return self._vehicleMarkerIcons

    @property
    def battleHintsCtrl(self):
        return self.guiSessionProvider.dynamic.battleHints

    def getControllerID(self):
        return BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL

    def startControl(self, battleCtx, arenaVisitor):
        super(HWBattleGUIController, self).startControl(battleCtx, arenaVisitor)
        self._callbackDelayer.delayCallback(self._UPDATE_PERIOD, self._update)
        HWArenaPhasesComponent.onPhaseChanged += self._onPhaseChanged
        HWArenaPhasesComponent.onPhaseTimeChanged += self._onPhaseTimeChanged
        HWArenaPhasesComponent.onBossVulnerableChanged += self._onBossVulnerableChanged

    def stopControl(self):
        HWArenaPhasesComponent.onPhaseChanged -= self._onPhaseChanged
        HWArenaPhasesComponent.onPhaseTimeChanged -= self._onPhaseTimeChanged
        HWArenaPhasesComponent.onBossVulnerableChanged -= self._onBossVulnerableChanged
        self._callbackDelayer.clearCallbacks()
        self.__eManager.clear()
        self._vehicleMarkerIcons.clear()
        self._hiddenVehicleIDs.clear()
        self._currentCollector = None
        super(HWBattleGUIController, self).stopControl()
        return

    def onSoulsCollectorSpawned(self, collector):
        self._currentCollector = collector

    def onSoulsCollectorDestroyed(self, collector):
        if self._currentCollector == collector:
            self._currentCollector = None
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.COLLECTOR_FULL, False)
        self._isCollectorFull = False
        self._vehiclesInRadius = set()
        return

    def setVehicleHidden(self, vehicleID, isHidden):
        if isHidden:
            self.guiSessionProvider.shared.feedback.onVehicleMarkerRemoved(vehicleID)
            self._hiddenVehicleIDs.add(vehicleID)
        else:
            self._hiddenVehicleIDs.discard(vehicleID)

    def isVehicleHidden(self, vehicleID):
        return vehicleID in self._hiddenVehicleIDs

    def applyBuff(self, ctx):
        if not self._isPlayerVehicle(ctx.get('vehicleID')):
            return
        buffKey = ctx.get('buffKey')
        if not buffKey:
            return
        self.onApplyBuff(ctx)
        if self.battleHintsCtrl and buffKey not in self._ignoreBuffNotification:
            self.battleHintsCtrl.showHint(BuffsNotificationSystem.BATTLE_HINT_TEMPLATE, ctx)
            self._ignoreBuffNotification.add(buffKey)

    def unapplyBuff(self, ctx):
        if not self._isPlayerVehicle(ctx.get('vehicleID')):
            return
        buffKey = ctx.get('buffKey')
        if not buffKey:
            return
        self.onUnapplyBuff(ctx)
        if self.battleHintsCtrl:
            self.battleHintsCtrl.hideHint(BuffsNotificationSystem.BATTLE_HINT_TEMPLATE)
            self._ignoreBuffNotification.discard(buffKey)

    def buffStateChanged(self, ctx):
        if self._isPlayerVehicle(ctx.get('vehicleID')):
            self.onBuffStateChanged(ctx)

    def addVehicleMarkerIcon(self, vehicleID, iconName, iconPriority):
        self._vehicleMarkerIcons.setdefault(vehicleID, set()).add((iconName, iconPriority))
        self.onVehicleBuffIconAdded(vehicleID, iconName, iconPriority)

    def removeVehicleMarkerIcon(self, vehicleID, iconName, iconPriority):
        self._vehicleMarkerIcons.get(vehicleID, set()).discard((iconName, iconPriority))
        self.onVehicleBuffIconRemoved(vehicleID, iconName, iconPriority)

    def vehicleDetectorChangeDistance(self, ctx):
        self.onVehicleDetectorChangeDistance(ctx)

    def getCurrentCollectorSoulsInfo(self):
        if self._currentCollector:
            return (self._currentCollector.collected, self._currentCollector.capacity)
        else:
            return (None, None)

    def updateCollector(self, collector):
        guiSessionProvider = self.guiSessionProvider
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is None:
            return
        else:
            vehicleID = vehicle.id
            if vehicleID in collector.vehiclesInRadius:
                if collector.isFull and vehicle.isAlive():
                    arenaDP = guiSessionProvider.getArenaDP()
                    alivePlayerNotInRadius = any(vInfo for vInfo in arenaDP.getVehiclesInfoIterator() if vInfo.player.accountDBID > 0 and vInfo.team == arenaDP.getAllyTeams()[0] and vInfo.isAlive() and vInfo.vehicleID not in collector.vehiclesInRadius)
                    if alivePlayerNotInRadius:
                        self._callbackDelayer.delayCallback(self._UPDATE_PERIOD, lambda : guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.COLLECTOR_FULL, True))
                    if not self._isCollectorFull:
                        self._callbackDelayer.delayCallback(self._UPDATE_PERIOD, self._onCollectorFull)
            removed = set(self._vehiclesInRadius) - set(collector.vehiclesInRadius)
            if vehicleID in removed:
                guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.COLLECTOR_FULL, False)
            self._vehiclesInRadius = set(collector.vehiclesInRadius)
            self.onSoulCollectorProgress(collector.collected, collector.capacity, collector.isFull, collector.isCampActivated)
            return

    def initIgnoreBuffNotification(self):
        self._ignoreBuffNotification = set(c.buffKey for c in findBuffsPanelComponents())

    def clearIgnoreBuffNotification(self):
        self._ignoreBuffNotification.clear()

    def _onCollectorFull(self):
        self._isCollectorFull = True

    def setVehicleMaxHealth(self, vehicleID, maxHealth):
        ctrl = self.guiSessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onVehicleFeedbackReceived(FEEDBACK_EVENT_ID.HW_VEHICLE_MARKER_HEALTH, vehicleID, maxHealth)
        return

    def _onPhaseChanged(self, arenaPhases):
        self._callbackDelayer.delayCallback(self._UPDATE_PERIOD, lambda : self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.COLLECTOR_FULL, False))
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.PHASE_END, (None, False))
        self.__removeAllBCMarkers(arenaPhases)
        self.onPhaseChanged()
        return

    def _onPhaseTimeChanged(self, timeLeft, prev, lastPhase):
        if lastPhase:
            return
        else:
            vehicle = BigWorld.player().vehicle
            if vehicle is None or not vehicle.isAlive() or timeLeft <= 0:
                self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.PHASE_END, (None, False))
            elif timeLeft < self._TIME_TO_END_NOTIFY and (self._TIME_TO_END_NOTIFY <= prev or timeLeft == prev):
                collector = self._currentCollector
                isFull = collector and collector.isFull
                self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.PHASE_END, (timeLeft, isFull))
            return

    def _onBossVulnerableChanged(self, isBossVulnerable):
        self.onBossVulnerableChanged(isBossVulnerable)

    def _update(self):
        if not isPlayerAvatar():
            return self._UPDATE_PERIOD
        relevantGoal = self._getRelevantGoal()
        if relevantGoal != self._currentGoal:
            self.onBattleGoalChanged(relevantGoal)
            self._showRelevantBattleHint(self._currentGoal, relevantGoal)
            self._currentGoal = relevantGoal
        return self._UPDATE_PERIOD

    def _getRelevantGoal(self):
        healthBarComponent = getArenaInfoBossHealthBarComponent()
        if healthBarComponent and healthBarComponent.isActive:
            return healthBarComponent.bossFightGoal or EventBattleGoal.UNKNOWN
        else:
            collector = self._currentCollector
            if collector is None or collector.capacity <= 0:
                return EventBattleGoal.UNKNOWN
            if collector.isFull:
                return EventBattleGoal.GET_TO_COLLECTOR
            if not self._getAliveAllyVehicles():
                return EventBattleGoal.UNKNOWN
            return EventBattleGoal.COLLECT_SOULS

    def _getAliveAllyVehicles(self):
        arenaDP = self.guiSessionProvider.getArenaDP()
        return [ vInfo.vehicleID for vInfo in arenaDP.getVehiclesInfoIterator() if arenaDP.isAllyTeam(vInfo.team) and vInfo.isAlive()
               ]

    def _showRelevantBattleHint(self, prevGoal, newGoal):
        if self.battleHintsCtrl is None:
            return
        else:
            if prevGoal is not None:
                self.battleHintsCtrl.removeHint(prevGoal, hide=True)
            if newGoal is None:
                return
            self.battleHintsCtrl.showHint(newGoal)
            return

    def _isPlayerVehicle(self, vehicleID):
        player = BigWorld.player()
        if not player:
            return False
        return vehicleID == player.playerVehicleID

    def __removeAllBCMarkers(self, arenaPhases):
        if arenaPhases.activePhase > 1:
            advChatCmp = getattr(self.guiSessionProvider.arenaVisitor.getComponentSystem(), 'advancedChatComponent', None)
            if advChatCmp:
                advChatCmp.cleanupBCMarkers()
        return