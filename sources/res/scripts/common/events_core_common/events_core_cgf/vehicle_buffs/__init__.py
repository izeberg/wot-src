import typing
from debug_utils import LOG_WARNING
from .components import vehicleBuffsComponents, factorComponentClasses
if typing.TYPE_CHECKING:
    from typing import Dict, Any
    from CGF import GameObject

def getVehicleBuffComponentType(buffKey):
    className = vehicleBuffsComponents.get(buffKey)
    if className is None:
        return
    else:
        return factorComponentClasses.get(className)


def applyVehicleBuffsSettings(go, settings):
    for buffKey, properties in settings.iteritems():
        componentType = getVehicleBuffComponentType(buffKey)
        if componentType is None:
            LOG_WARNING(('[VehicleBuffs] Unknown vehicle buff key: {}').format(buffKey))
            continue
        component = go.findComponentByType(componentType)
        if component is None:
            component = go.createComponent(componentType)
        for propertyName, propertyValue in properties.iteritems():
            if hasattr(component, propertyName):
                setattr(component, propertyName, propertyValue)
            else:
                LOG_WARNING(('[VehicleBuffs] {} has no attribute {}').format(componentType.__name__, propertyName))

    return