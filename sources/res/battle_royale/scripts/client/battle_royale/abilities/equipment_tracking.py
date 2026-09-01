from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class EquipmentAnimatorTrigger(object):
    domain = CGF.Domain.ClientEditor
    activeTrigger = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='active trigger name')
    inactiveTrigger = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='inactive trigger name')


class EquipmentStateComponent(object):
    state = property(lambda self: self.__state)

    def __init__(self, state):
        self.__state = state


class EquipmentTrackerComponent(object):

    def __init__(self):
        self.__equipmentGameObjects = {}
        self.__reservedIDs = set()

    def reserveID(self, equipmentID):
        self.__reservedIDs.add(equipmentID)

    def isReserved(self, equipmentID):
        return equipmentID in self.__reservedIDs

    def startTrack(self, equipmentID, gameObject):
        self.__equipmentGameObjects[equipmentID] = gameObject

    def getEquipmentGameObject(self, equipmentID):
        return self.__equipmentGameObjects.get(equipmentID, None)