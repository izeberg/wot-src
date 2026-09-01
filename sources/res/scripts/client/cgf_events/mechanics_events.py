from __future__ import absolute_import
import CGF, Vehicular

def postSightPointerSectorEvent(spaceID, entityID, slotName, targetWidth, targetDistance, targetOpacity, duration):
    CGF.postEvent(spaceID, Vehicular.VariablesChangedEvent(entityID=entityID, slotName=slotName, varValueMap={'sectorVision/length': targetDistance, 
       'sectorVision/width': targetWidth, 
       'sectorVision/opacity': targetOpacity, 
       'sectorVision/duration': duration}))