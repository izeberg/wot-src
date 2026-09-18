from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent
from gui.shared.events import HasCtxEvent

class HWHangarEvent(SharedEvent):
    REFRESH = 'hwHangarEvent/refresh'


class HWBattleLootEvent(HasCtxEvent):
    VEH_CAPTURING_START = 'HWBattleLootEvent/VEH_CAPTURING_START'
    VEH_CAPTURING_CANCEL = 'HWBattleLootEvent/VEH_CAPTURING_CANCEL'
    APPEAR = 'HWBattleLootEvent/APPEAR'
    CAPTURED = 'HWBattleLootEvent/CAPTURED'