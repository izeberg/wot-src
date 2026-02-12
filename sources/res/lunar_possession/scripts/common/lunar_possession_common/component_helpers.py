import typing, BigWorld
from ArenaInfo import ArenaInfo
from Vehicle import Vehicle
from constants import IS_CLIENT, IS_CELLAPP
from debug_utils import LOG_WARNING, LOG_DEBUG_DEV
from lunar_constants import LUNAR_ARENA_EVENT_COMPONENT, LUNAR_SCORE_COMPONENT, LUNAR_SPIRIT_BUFF, SPIRIT_BUFF_COMPONENT_COLLECTION
if typing.TYPE_CHECKING:
    if IS_CLIENT:
        from ClientArena import ClientArena as Arena
    elif IS_CELLAPP:
        from Arena import Arena
        from LunarArenaEventsComponent import LunarArenaEvents
        from LunarScoreComponent import LunarScoreEvents

def _getArenaInfo(arena):
    if not arena:
        return None
    else:
        if not isinstance(arena, ArenaInfo):
            if not hasattr(arena, 'arenaInfo'):
                return None
            arena = arena.arenaInfo
        return arena


def _getArenaInfoComponentEvent(arena, componentName):
    arenaInfo = _getArenaInfo(arena)
    if arenaInfo is None:
        return
    else:
        eventsComponent = arenaInfo.dynamicComponents.get(componentName)
        if eventsComponent is None:
            LOG_WARNING('[Lunar][ArenaInfo][Events] cant fetch events, dynamic component is None %s', componentName)
            return
        if getattr(eventsComponent, 'events', None) is None:
            LOG_DEBUG_DEV('[Lunar][ArenaInfo][Events] %s has no events attribute', componentName)
            return
        return eventsComponent.events


def getLunarArenaEvents(arena):
    return _getArenaInfoComponentEvent(arena, LUNAR_ARENA_EVENT_COMPONENT)


def getLunarScoreComponentEvents(arena):
    return _getArenaInfoComponentEvent(arena, LUNAR_SCORE_COMPONENT)


def removeSpiritBuffFromVehicle(vehicle):
    if vehicle is None:
        return
    else:
        for componentName in SPIRIT_BUFF_COMPONENT_COLLECTION:
            if componentName in vehicle.dynamicComponents:
                component = vehicle.dynamicComponents.get(componentName)
                if component is not None:
                    component.destroy()

        return


def isSpiritCarrier(vehicle):
    if isinstance(vehicle, int):
        vehicle = BigWorld.entities.get(vehicle)
    if vehicle is None:
        return False
    else:
        if IS_CLIENT:
            from LunarSpiritBuffComponent import LunarSpiritBuffComponent
            return vehicle.entityGameObject.hasComponent(LunarSpiritBuffComponent)
        if IS_CELLAPP:
            return LUNAR_SPIRIT_BUFF in vehicle.dynamicComponents
        return False