from collections import defaultdict
from gui import TANKMEN_ROLES_ORDER_DICT
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import VEHICLE_DEVICES, VEHICLE_INDICATOR_TYPE, AUTO_ROTATION_FLAG, WHEELED_VEHICLE_DEVICES, TRACK_WITHIN_TRACK_DEVICES
_COATED_OPTICS_TAG = 'coatedOptics'

def hasTurretRotator(vDesc):
    if vDesc is None:
        return False
    else:
        result = True
        tags = vDesc.type.tags
        if tags & {'SPG', 'AT-SPG'}:
            if vDesc.gun.turretYawLimits is not None and vDesc.hull.fakeTurrets.get('battle', ()):
                result = False
        return result


def isWheeledTech(vDesc):
    if vDesc is None:
        return False
    else:
        return 'wheeledVehicle' in vDesc.type.tags


def isTrackWithinTrackTech(vDesc):
    if vDesc is None:
        return False
    else:
        return vDesc.isTrackWithinTrack


def getYawLimits(vDesc):
    if vDesc is None:
        return
    else:
        return vDesc.gun.turretYawLimits


def hasYawLimits(vDesc):
    return getYawLimits(vDesc) is not None


def getVehicleIndicatorType(vDesc):
    if vDesc is None:
        return VEHICLE_INDICATOR_TYPE.DEFAULT
    else:
        iType = VEHICLE_INDICATOR_TYPE.DEFAULT
        if not hasTurretRotator(vDesc):
            tags = vDesc.type.tags
            if 'SPG' in tags:
                iType = VEHICLE_INDICATOR_TYPE.SPG
            elif 'AT-SPG' in tags:
                iType = VEHICLE_INDICATOR_TYPE.AT_SPG
        return iType


def getAutoRotationFlag(vDesc):
    flag = AUTO_ROTATION_FLAG.IGNORE_IN_UI
    if hasYawLimits(vDesc):
        aih = avatar_getter.getInputHandler()
        if aih is None or aih.getAutorotation():
            flag = AUTO_ROTATION_FLAG.TURN_ON
        else:
            flag = AUTO_ROTATION_FLAG.TURN_OFF
    return flag


def getOptionalDevicesByVehID(vehicleID, avatar=None):
    arena = avatar_getter.getArena(avatar=avatar)
    if arena is None:
        return []
    else:
        if vehicleID not in arena.vehicles:
            return []
        vehicleType = arena.vehicles[vehicleID].get('vehicleType')
        if vehicleType is None:
            return []
        return vehicleType.optionalDevices


def getOptionalDevices(avatar=None):
    vehicleID = avatar_getter.getPlayerVehicleID(avatar=avatar)
    if not vehicleID:
        return []
    return getOptionalDevicesByVehID(vehicleID, avatar=avatar)


def isCoatedOpticsInstalled(avatar=None):
    for device in getOptionalDevices(avatar=avatar):
        if device is None:
            continue
        if _COATED_OPTICS_TAG in device.tags:
            return True

    return False


def getCrewMainRolesWoIndexes(crewRoles):
    order = TANKMEN_ROLES_ORDER_DICT['plain']
    default = len(order)
    return sorted([ roles[0] for roles in crewRoles ], key=lambda item: order.index(item) if item in order else default)


def getCrewMainRolesWithIndexes(crewRoles):
    indexes = defaultdict(lambda : 1)

    def _mapping(item):
        role = item[0]
        if role not in ('commander', 'driver'):
            ind = indexes[role]
            indexes[role] += 1
            role += str(ind)
        return role

    return map(_mapping, crewRoles)


class TankmenStatesIterator(object):

    def __init__(self, states=None, vDesc=None):
        super(TankmenStatesIterator, self).__init__()
        if vDesc is None:
            crewRoles = []
        else:
            crewRoles = vDesc.type.crewRoles
        self._rolesEnum = list(TANKMEN_ROLES_ORDER_DICT['enum'])
        self._mainRoles = getCrewMainRolesWithIndexes(crewRoles)
        self._states = defaultdict(lambda : 'normal', states or {})
        return

    def __iter__(self):
        return self

    def next(self):
        if self._rolesEnum:
            role = self._rolesEnum.pop(0)
            if role in self._mainRoles:
                state = self._states[role]
            else:
                state = None
            return (
             role, state)
        else:
            self._states.clear()
            raise StopIteration()
            return


class VehicleDeviceStatesIterator(object):

    def __init__(self, states=None, vDesc=None, devices=None):
        super(VehicleDeviceStatesIterator, self).__init__()
        self._states = defaultdict(lambda : 'normal', states or {})
        self._hasTurret = hasTurretRotator(vDesc)
        if isWheeledTech(vDesc):
            self._devices = list(devices or WHEELED_VEHICLE_DEVICES)
        elif isTrackWithinTrackTech(vDesc):
            self._devices = list(devices or TRACK_WITHIN_TRACK_DEVICES)
        else:
            self._devices = list(devices or VEHICLE_DEVICES)

    def __iter__(self):
        return self

    def next(self):
        if self._devices:
            name = self._devices.pop(0)
            if name == 'turretRotator' and not self._hasTurret:
                return (name, None)
            return (name, self._states[name])
        else:
            self._states.clear()
            raise StopIteration()
            return

    def clear(self):
        self._states.clear()