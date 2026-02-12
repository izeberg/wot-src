import CGF, SoundGroups
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from lunar_constants import ARENA_BONUS_TYPE_CAPS
from lunar_possession.gui.shared.events import PointZoneAnimationEvents
from cgf_script.bonus_caps_rules import bonusCapsManager

@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.LUNAR_POSSESSION, CGF.DomainOption.DomainClient)
class LunarSoundManager(CGF.ComponentManager):
    _LUNAR_DELIVERY_SOUND = 'ev_lunar_pos_coin_deliver'

    def activate(self):
        g_eventBus.addListener(PointZoneAnimationEvents.VEHICLE_DELIVERED_SPIRIT, self.__playDeliverySound, EVENT_BUS_SCOPE.BATTLE)

    def deactivate(self):
        g_eventBus.removeListener(PointZoneAnimationEvents.VEHICLE_DELIVERED_SPIRIT, self.__playDeliverySound, EVENT_BUS_SCOPE.BATTLE)

    def __playDeliverySound(self, _):
        SoundGroups.g_instance.playSound2D(self._LUNAR_DELIVERY_SOUND)