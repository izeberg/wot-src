import logging
from typing import Tuple, Optional, TYPE_CHECKING
import BigWorld, Math
from constants import EQUIPMENT_STAGES
from shared_utils import forEach
from AvatarInputHandler.AimingSystems import getShotTargetInfo
from grinch_common.grinch_constants import ARENA_BONUS_TYPE, GrinchAbilities
from gui.battle_control import avatar_getter
from gui.battle_control.controllers.consumables import equipment_ctrl
from gui.battle_control.controllers.consumables.equipment_ctrl import _VisualScriptItem, _ReplayItem, _ActivationError, EquipmentsReplayPlayer
from gui.shared.system_factory import registerEquipmentItem
if TYPE_CHECKING:
    from Avatar import Avatar
_logger = logging.getLogger(__name__)

class _GrinchVisualScriptItem(_VisualScriptItem):
    __slots__ = ('_tags', '_descriptor', '_quantity', '_stage', '_prevStage', '_timeRemaining',
                 '_prevQuantity', '_totalTime', '_isLocked', '_animationType', '_serverPrevStage',
                 '_index')

    def __init__(self, *args):
        super(_GrinchVisualScriptItem, self).__init__(*args)
        component = self._getComponent()
        self._isLocked = component.locked if component else False

    def canActivate(self, entityName=None, avatar=None):
        if self._isLocked:
            _logger.debug('Equipment is locked %r :\nEquipment id=%s', self, self._descriptor.userString)
            return (
             False, _ActivationError('equipmentIsLocked', {'name': self._descriptor.userString}))
        return super(_GrinchVisualScriptItem, self).canActivate(entityName, avatar)

    def getQuantity(self):
        if not self._isLocked:
            return self._quantity
        return 0

    def getTimeRemaining(self):
        if not self._isLocked:
            return self._timeRemaining
        return 0

    def getTotalTime(self):
        if not self._isLocked:
            return self._totalTime
        return 0

    def setLocked(self, isLocked):
        self._isLocked = isLocked

    def isLocked(self):
        return self._isLocked


class _GrinchAimingVisualScriptItem(_GrinchVisualScriptItem):

    def setLocked(self, isLocked):
        if isLocked:
            from AvatarInputHandler import MapCaseMode
            MapCaseMode.turnOffMapCase(self.getEquipmentID(), self._getAimingControlMode())
        super(_GrinchAimingVisualScriptItem, self).setLocked(isLocked)

    def _getAimingControlMode(self):
        from grinch.avatar_input_handler.grinch_map_case_mode import GrinchArcadeMapCaseControlMode
        return GrinchArcadeMapCaseControlMode


class _GrinchCameraDirectionAimingVisualScriptItem(_GrinchVisualScriptItem):

    def activate(self, entityName=None, avatar=None):
        cameraMatrix = Math.Matrix(BigWorld.camera().matrix)
        cameraMatrix.invert()
        BigWorld.player().setEquipmentApplicationPoint(self._descriptor.id[1], Math.Vector3(cameraMatrix.yaw, cameraMatrix.pitch, cameraMatrix.roll), Math.Vector2())
        super(_GrinchCameraDirectionAimingVisualScriptItem, self).activate(entityName, avatar)


class _GrinchReplayItem(_ReplayItem):
    pass


class GrinchEquipmentsController(equipment_ctrl.EquipmentsController):

    def _doChangeSetting(self, item, entityName=None, avatar=None):
        result, error = item.canActivate(entityName, avatar)
        if not result or not avatar_getter.isPlayerOnArena(avatar):
            return (result, error)
        else:
            if item.isInPreparing():
                item.deactivate()
                return (
                 result, error)
            avatar = BigWorld.player()
            curCtrl = avatar.inputHandler.ctrl
            if curCtrl is not None and curCtrl.isEnabled:
                desiredShotPoint = curCtrl.getDesiredShotPoint(ignoreAimingMode=True)
                vehicle = avatar.getVehicleAttached()
                gunRotator = avatar.gunRotator
                if gunRotator:
                    hitPoint, _ = getShotTargetInfo(vehicle, desiredShotPoint, gunRotator)
                    if vehicle and vehicle.position.distTo(hitPoint) < vehicle.position.distTo(desiredShotPoint):
                        desiredShotPoint = hitPoint
                self.__preferredPosition = desiredShotPoint
            if item.getDescriptor().name in (GrinchAbilities.GRINCH_REPAIR_KIT, GrinchAbilities.GRINCH_SONAR):
                forEach(lambda equipment: equipment.deactivate(), [ equipment for equipment in self._equipments.itervalues() if equipment.getStage() == EQUIPMENT_STAGES.PREPARING and equipment.getDescriptor().name != GrinchAbilities.GRINCH_MISSILES
                                                                  ])
            else:
                forEach(lambda equipment: equipment.deactivate(), [ equipment for equipment in self._equipments.itervalues() if equipment.getStage() == EQUIPMENT_STAGES.PREPARING
                                                                  ])
            item.activate(entityName, avatar)
            return (result, error)


class GrinchReplayEquipmentsController(EquipmentsReplayPlayer, GrinchEquipmentsController):
    pass


def registerEquipmentsItems():
    registerEquipmentItem('builtinGrinchRepairkit', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchTurret', _GrinchAimingVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchHeal', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchStealth', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchFlare', _GrinchAimingVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchBlizzard', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchRage', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchJump', _GrinchCameraDirectionAimingVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchMissiles', _GrinchAimingVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchDart', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchSonar', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('builtinGrinchRam', _GrinchVisualScriptItem, _GrinchReplayItem)
    registerEquipmentItem('presentDrop', _GrinchAimingVisualScriptItem, _GrinchReplayItem)


def registerController():
    from gui.battle_control.controllers.consumables import extendEquipmentController
    extendEquipmentController({ARENA_BONUS_TYPE.GRINCH: GrinchEquipmentsController}, {ARENA_BONUS_TYPE.GRINCH: GrinchReplayEquipmentsController})