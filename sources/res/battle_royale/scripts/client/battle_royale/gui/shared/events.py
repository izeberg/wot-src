from gui.shared.events import HasCtxEvent

class DeathZoneEvent(HasCtxEvent):
    UPDATE_DEATH_ZONE = 'deathZone/update'


class AirDropEvent(HasCtxEvent):
    AIR_DROP_SPAWNED = 'onAirDropSpawned'
    AIR_DROP_LANDED = 'onAirDropLanded'
    AIR_DROP_ENTERED = 'onAirDropEntered'
    AIR_DROP_LEFT = 'onAirDropLeft'
    AIR_DROP_NXT_SPAWNED = 'onAirDropNxtSpawned'


class LootEvent(HasCtxEvent):
    LOOT_PICKED_UP = 'onLootPickedUp'