from typing import Union
import BigWorld
from Event import Event
from aih_constants import CTRL_MODE_NAME
from constants import NULL_ENTITY_ID
from grinch_common.grinch_constants import VEHICLE_MARKER_UPDATE_TIME
from script_component.DynamicScriptComponent import DynamicScriptComponent

class GrinchTargetLockingComponent(DynamicScriptComponent):
    _CHECK_STATUS_TICK = 0.1

    def __init__(self):
        super(GrinchTargetLockingComponent, self).__init__()
        self.__initDelayer()
        self.delayed = False
        self._previousVehicleID = NULL_ENTITY_ID
        self._canShoot = False
        self._passedTime = 0
        self.onTargetAcquiring = Event()
        self.onTargetAcquired = Event()
        self.onTargetLost = Event()

    def _onAvatarReady(self):
        arcadeControlMode = BigWorld.player().inputHandler.ctrls.get(CTRL_MODE_NAME.MAP_CASE_ARCADE)
        self._camera = arcadeControlMode.camera

    def onDestroy(self):
        super(GrinchTargetLockingComponent, self).onDestroy()
        self.delayer.clearCallbacks()
        self.onTargetAcquiring.clear()
        self.onTargetAcquired.clear()
        self.onTargetLost.clear()

    def setTargetVehicleID(self, targetVehicleID, forceUpdate=False, skipUpdate=False):
        if (targetVehicleID == self.targetVehicleID or targetVehicleID == self._previousVehicleID) and not forceUpdate:
            return
        self.delayer.stopCallback(self._updateHUDInfo)
        self._canShoot = False
        self._passedTime = 0
        if not skipUpdate:
            self._updateHUDInfo(currentVehicleID=targetVehicleID, previousVehicleID=self._previousVehicleID)
        if self.delayed:
            self.delayed = False
            self.delayer.stopCallback(self.updateDelayStatus)
            self.delayer.stopCallback(self._checkDelayStatus)
        if targetVehicleID:
            self.delayer.delayCallback(VEHICLE_MARKER_UPDATE_TIME, self._updateHUDInfo, VEHICLE_MARKER_UPDATE_TIME, targetVehicleID)
        self._previousVehicleID = targetVehicleID
        self.cell.updateTargetVehicleID(targetVehicleID)

    def canShoot(self):
        return self._canShoot

    def _enableCanShoot(self, vehicleIDToLock):
        if self.delayed:
            self.setTargetVehicleID(NULL_ENTITY_ID)
            return
        self._canShoot = True
        self.onTargetAcquired(vehicleIDToLock)

    def _updateHUDInfo(self, time=0.0, currentVehicleID=0, previousVehicleID=0):
        self._passedTime += time
        timeRemaining = self.timeToLock - self._passedTime
        if previousVehicleID:
            self.onTargetLost(previousVehicleID)
        self.onTargetAcquiring(currentVehicleID, timeRemaining)
        if timeRemaining >= VEHICLE_MARKER_UPDATE_TIME:
            return VEHICLE_MARKER_UPDATE_TIME
        self._enableCanShoot(currentVehicleID)
        return -1

    def updateDelayStatus(self):
        if self._canShoot:
            self.setTargetVehicleID(NULL_ENTITY_ID)
            return
        if not self.delayed:
            self.delayed = True
            self.delayer.delayCallback(self.lockOnDelay, self.updateDelayStatus)
            self.delayer.delayCallback(self._CHECK_STATUS_TICK, self._checkDelayStatus)
        else:
            isTargetVisible = self.__isVehicleVisible()
            if not isTargetVisible:
                self.setTargetVehicleID(NULL_ENTITY_ID)
            else:
                self.delayed = False
                self.delayer.stopCallback(self._checkDelayStatus)

    def _checkDelayStatus(self):
        if not self.targetVehicleID:
            return
        isTargetVisible = self.__isVehicleVisible()
        if isTargetVisible:
            self.delayed = False
            self.delayer.stopCallback(self.updateDelayStatus)
            return
        return self._CHECK_STATUS_TICK

    def __initDelayer(self):
        from helpers.CallbackDelayer import CallbackDelayer
        self.delayer = CallbackDelayer()

    def __isVehicleVisible(self):
        from grinch.avatar_input_handler.grinch_map_case_mode import isVehicleVisibleFromPlayersTurret
        if not self.targetVehicleID:
            return False
        targetVehicle = BigWorld.entities.get(self.targetVehicleID)
        if targetVehicle:
            return isVehicleVisibleFromPlayersTurret(targetVehicle)
        return False