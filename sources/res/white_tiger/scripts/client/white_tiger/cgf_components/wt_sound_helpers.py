from __future__ import absolute_import
import logging, BigWorld, WWISE, CGF
from shared_utils import findFirst
from constants import IS_CLIENT, CURRENT_REALM, IS_CHINA
import SoundGroups
from Math import Matrix
if IS_CLIENT:
    from Vehicle import Vehicle
_logger = logging.getLogger(__name__)
SWITCH_LANG_NAME = 'SWITCH_ext_WT_vo_language'
_RU_REALMS = ('QA', 'RU')
_SWITCH_LANG_VALUE_RU = 'SWITCH_ext_WT_vo_language_RU'
_SWITCH_LANG_VALUE_NON_RU = 'SWITCH_ext_WT_vo_language_nonRU'
_SWITCH_LANG_VALUE_CN = 'SWITCH_ext_WT_vo_language_CN'

def getVehicle(go, spaceID):
    hierarchy = CGF.findHierarchySingleton(spaceID)
    parent = hierarchy.getTopMostParent(go)
    if parent:
        return parent.findWrite(Vehicle)
    else:
        return


def play2d(soundName):
    SoundGroups.g_instance.playSound2D(soundName)


def play3d(soundName, go, spaceID):
    hierarchy = CGF.findHierarchySingleton(spaceID)
    parent = hierarchy.getTopMostParent(go)
    transform = parent.findRead(CGF.TransformComponent)
    if transform is not None:
        SoundGroups.g_instance.playSoundPos(soundName, transform.worldPosition)
    return


def getPlayerVehicleDistToGO(spaceID, goPosition=None, go=None):
    if goPosition is None and go is None:
        return
    else:
        if goPosition is None and go:
            hierarchy = CGF.findHierarchySingleton(spaceID)
            parent = hierarchy.getTopMostParent(go)
            transform = parent.findRead(CGF.TransformComponent)
            goPosition = transform.worldPosition
        avatar = BigWorld.player()
        vehicle = avatar.getVehicleAttached()
        if vehicle:
            vehiclePos = vehicle.position
            return vehiclePos.distTo(goPosition)
        return


def createSoundObject(soundObjectName, position):
    mProv = Matrix()
    mProv.translation = position
    soundObject = SoundGroups.g_instance.WWgetSoundObject(soundObjectName, mProv)
    return soundObject


def get3DSound(soundObjectName, soundEventName, pos):
    sound = SoundGroups.g_instance.WWgetSoundPos(soundEventName, soundObjectName, pos)
    return sound


def getSoundObject(sound):
    if sound:
        return sound.getSoundObject()
    else:
        return


def playVehiclePart(soundName, vehicle, partIndex):
    if vehicle.appearance is not None:
        if vehicle.appearance.engineAudition:
            soundObject = vehicle.appearance.engineAudition.getSoundObject(partIndex)
            soundObject.play(soundName)
        else:
            _logger.warning("Couldn't play sound. engineAudition is None. Part index: %s", str(partIndex))
    else:
        _logger.warning("Couldn't play sound. Appearance is None. Part index: %s", str(partIndex))
    return


def playNotification(notificationName):
    soundNotifications = getattr(BigWorld.player(), 'soundNotifications', None)
    if soundNotifications is not None:
        soundNotifications.play(notificationName)
    return


def _getSoundComponent(vehicle):
    from white_tiger.cgf_components.sound_components import WTVehicleSoundComponent
    if vehicle is not None and vehicle.appearance is not None and vehicle.isAlive():
        vehicleSoundComponent = vehicle.appearance.gameObject.findWrite(WTVehicleSoundComponent)
        if not vehicleSoundComponent:
            vehicle.appearance.addTempGameObject(WTVehicleSoundComponent(vehicle), 'sound_object')
            vehicleSoundComponent = vehicle.appearance.gameObject.findWrite(WTVehicleSoundComponent)
        return vehicleSoundComponent
    return


def playVehicleSound(event, vehicle):
    soundComponent = _getSoundComponent(vehicle)
    if soundComponent is not None:
        soundComponent.play(event)
    return


def hasVehicleSound(event, vehicle):
    soundComponent = _getSoundComponent(vehicle)
    if soundComponent is not None:
        return bool(findFirst(lambda soundObj: soundObj.name == event, soundComponent.soundObjects))
    else:
        return


def setState(name, value):
    WWISE.WW_setState(name, value)


def setRTCP(name, value):
    WWISE.WW_setRTCPGlobal(name, value)


def getEventInfo(eventName, param):
    soundNotifications = getattr(BigWorld.player(), 'soundNotifications', None)
    if soundNotifications is not None:
        return soundNotifications.getEventInfo(eventName, param)
    else:
        return


def getLanguageValue():
    if IS_CHINA:
        return _SWITCH_LANG_VALUE_CN
    if CURRENT_REALM in _RU_REALMS:
        return _SWITCH_LANG_VALUE_RU
    return _SWITCH_LANG_VALUE_NON_RU


def setLanguageSwitch():
    WWISE.WW_setSwitch(SWITCH_LANG_NAME, getLanguageValue())