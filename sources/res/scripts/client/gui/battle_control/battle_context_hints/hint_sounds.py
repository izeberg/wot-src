from typing import Callable, Optional, NamedTuple
from gui.battle_control.avatar_getter import isVehicleAlive
HintSoundEvent = NamedTuple('HintSoundEvent', [
 (
  'eventName', str),
 (
  'checkFn', Optional[Callable[([], bool)]])])

def createCommonSound(eventName):
    return HintSoundEvent(eventName, None)


def createVehicleAliveSound(eventName):
    return HintSoundEvent(eventName, isVehicleAlive)


PLAYER_VEHICLE_OBSERVED = createCommonSound('vo_contextHints_04_00')
KILLED_WHILE_OBSERVED = createCommonSound('vo_contextHints_04_01')
IN_SAFETY_WHILE_NOT_OBSERVED = createCommonSound('vo_contextHints_InSafetyWhileNotObserved')
MODULE_REPAIR_KIT = createVehicleAliveSound('vo_contextHints_04_03')
AMMUNITION_CRIT = createCommonSound('vo_contextHints_04_08')
FUELTANK_CRIT = createCommonSound('vo_contextHints_04_09')
MODULE_DAMAGE = createCommonSound('vo_contextHints_04_14')
TANKMAN_DAMAGE = createVehicleAliveSound('vo_contextHints_04_15')
AMMO_TYPE_AVAILABLE = createCommonSound('vo_contextHints_AmmoTypeAvailable')
AMMO_TYPE_SWITCH = createVehicleAliveSound('vo_contextHints_AmmoTypeSwitch_01')
AMMO_TYPE_SWITCH_APPLIED = createVehicleAliveSound('vo_contextHints_AmmoTypeSwitch_02')