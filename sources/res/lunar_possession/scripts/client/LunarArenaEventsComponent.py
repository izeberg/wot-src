import typing
from script_component.DynamicScriptComponent import DynamicScriptComponent
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from lunar_possession.gui.shared.events import PointZoneAnimationEvents, MatchRoundsEvents, SpiritEvents
if typing.TYPE_CHECKING:
    from typing import Any

class LunarArenaEventsComponent(DynamicScriptComponent):

    def onSpiritDelivered(self, vehicleID):
        g_eventBus.handleEvent(PointZoneAnimationEvents(PointZoneAnimationEvents.VEHICLE_DELIVERED_SPIRIT, vehicleID=vehicleID, animationType='delivered'), scope=EVENT_BUS_SCOPE.BATTLE)

    def onSpiritCarrierDestroyed(self, targetID, attackerID):
        g_eventBus.handleEvent(PointZoneAnimationEvents(PointZoneAnimationEvents.VEHICLE_DESTROYED_WITH_SPIRIT, vehicleID=targetID, animationType='default'), scope=EVENT_BUS_SCOPE.BATTLE)

    def onRoundEnd(self, timeBeforeNextRound, roundEndReason):
        g_eventBus.handleEvent(MatchRoundsEvents(MatchRoundsEvents.ROUND_END, timer=timeBeforeNextRound, roundEndReason=roundEndReason), scope=EVENT_BUS_SCOPE.BATTLE)

    def onRoundStart(self, timeBeforeRoundStart):
        g_eventBus.handleEvent(MatchRoundsEvents(MatchRoundsEvents.ROUND_START, timer=timeBeforeRoundStart), scope=EVENT_BUS_SCOPE.BATTLE)

    def onSpiritSpawned(self, *args):
        g_eventBus.handleEvent(SpiritEvents(SpiritEvents.SPIRIT_SPAWNED), scope=EVENT_BUS_SCOPE.BATTLE)