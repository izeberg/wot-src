from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent

class RespawnFrameworkEvent(SharedEvent):
    VEHICLES_LOADED = 'respawnFramework/respawnVehiclesLoaded'
    POSTMORTEM_ENTERED = 'respawnFramework/postmortemEntered'
    POSTMORTEM_LEFT = 'respawnFramework/postmortemLeft'