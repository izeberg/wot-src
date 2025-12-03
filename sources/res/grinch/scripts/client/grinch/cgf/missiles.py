import CGF, weakref
from typing import Dict, Optional
from debug_utils import LOG_DEBUG
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from grinch.cgf import getVehicleFromGO
from grinch_common.grinch_constants import ARENA_BONUS_TYPE_CAPS, MissileLauncherStatuses
from grinch_common.cgf.missiles import LAUNCHER_CONTROLLER_COMPONENT_NAME, GrinchMissileLauncherComponent
from helpers.CallbackDelayer import CallbackDelayer

@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class MissileLauncherManager(CGF.ComponentManager):
    _UPDATE_PERIOD = 0.1

    def __init__(self):
        super(MissileLauncherManager, self).__init__()
        self._launchersMap = {}
        self._vehGOsToProcess = set()
        self._delayer = CallbackDelayer()

    @onAddedQuery(CGF.GameObject, GrinchMissileLauncherComponent, tickGroup='postTickUpdate')
    def onAdded(self, go, _):
        self._vehGOsToProcess.add(go)
        self._delayer.delayCallback(self._UPDATE_PERIOD, self._processVehicleGOs)

    @onRemovedQuery(CGF.GameObject, GrinchMissileLauncherComponent, tickGroup='postTickUpdate')
    def onRemoved(self, go, missileComponent):
        if go not in self._vehGOsToProcess:
            missileComponent.setState(go, MissileLauncherStatuses.IDLE)
            self._launchersMap.pop(missileComponent.vehicleID, None)
        else:
            self._vehGOsToProcess.discard(go)
        return

    def _onStateChanged(self, vehicleID, newState):
        missileLauncherInfo = self._getMissileLauncherCache(vehicleID)
        if not missileLauncherInfo:
            return
        missileComponent = missileLauncherInfo['componentRef']()
        missileComponent.setState(missileLauncherInfo['gameObject'], newState)

    def _getMissileLauncherCache(self, vehicleID):
        missileLauncherInfo = self._launchersMap.get(vehicleID)
        return missileLauncherInfo

    def _processVehicleGOs(self):
        processedVehGOs = set()
        for vehicleGO in self._vehGOsToProcess:
            vehicle = getVehicleFromGO(self.spaceID, vehicleGO)
            if not vehicle:
                LOG_DEBUG("Couldn't find vehicle")
                continue
            missileComponent = vehicleGO.findComponentByType(GrinchMissileLauncherComponent)
            if not missileComponent:
                LOG_DEBUG("Couldn't find missile launcher component for vehicle ID = ", vehicle.id)
                continue
            missileComponent.vehicleID = vehicle.id
            component = vehicle.dynamicComponents.get(LAUNCHER_CONTROLLER_COMPONENT_NAME, None)
            if not component:
                LOG_DEBUG("Couldn't find tracker component for vehicle ID = ", vehicle.id)
                continue
            else:
                component.onLauncherStateChanged += self._onStateChanged
                missileComponent.updateVisual(vehicleGO, component)
            self._launchersMap[vehicle.id] = {'gameObject': vehicleGO, 'componentRef': weakref.ref(missileComponent)}
            processedVehGOs.add(vehicleGO)

        self._vehGOsToProcess.difference_update(processedVehGOs)
        if self._vehGOsToProcess:
            return self._UPDATE_PERIOD
        else:
            return