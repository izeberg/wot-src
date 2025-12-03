import math
from typing import TYPE_CHECKING, List
import BigWorld, CommandMapping
from Math import Vector2, Vector3, Vector4
from AvatarInputHandler import MapCaseMode, cameras, AimingSystems
from AvatarInputHandler.AimingSystems.magnetic_aim import getVisibilityCheckPointsGen
from AvatarInputHandler.DynamicCameras import ArcadeCamera
from aih_constants import CTRL_MODE_NAME
from constants import CollisionFlags, NULL_ENTITY_ID
from grinch_common.cgf.missiles import TRACKING_COMPONENT_NAME
from grinch_common.grinch_constants import TURRET_SPHERE_COLLIDER_RADIUS, TURRET_MINIMUM_ROTATION, SWITCHING_AREA_PERCENTAGE, Y_CENTER_OFFSET_PERCENTAGE, MISSILE_ABILITY_EQUIPMENT_ID
if TYPE_CHECKING:
    from Vehicle import Vehicle
    from GrinchTargetLockingComponent import GrinchTargetLockingComponent
_SQRT_2 = math.sqrt(2)
_DIR_UP = Vector3(0.0, 1.0, 0.0)

def getPointOnScreen(point):
    posInClip = Vector4(point.x, point.y, point.z, 1)
    return cameras.getViewProjectionMatrix().applyV4Point(posInClip)


def isPointOnScreen(point, screenFactorX=1.0, screenFactorY=1.0, yOffset=0.0):
    if point.lengthSquared == 0.0:
        return False
    posInClip = getPointOnScreen(point)
    return posInClip.w != 0 and -screenFactorX <= posInClip.x / posInClip.w <= screenFactorX and -screenFactorY + yOffset <= posInClip.y / posInClip.w <= screenFactorY + yOffset


def isVehicleVisibleFromPlayersTurret(vehicle):
    spaceID = vehicle.spaceID
    player = BigWorld.player()
    gunRotator = player.gunRotator
    gunMatrix = AimingSystems.getPlayerGunMat(gunRotator.turretYaw, gunRotator.gunPitch)
    for endPosition in getVisibilityCheckPointsGen(vehicle):
        staticCollision = BigWorld.wg_collideSegment(spaceID, gunMatrix.translation, endPosition, CollisionFlags.TRIANGLE_PROJECTILENOCOLLIDE)
        if staticCollision is None:
            return True

    return False


def isVehicleVisible(vehicle, component):
    if component.targetVehicleID == vehicle.id:
        if component.delayed:
            return True
        isTargetVisible = isVehicleVisibleFromPlayersTurret(vehicle)
        if isTargetVisible:
            return True
        component.updateDelayStatus()
        return True
    return isVehicleVisibleFromPlayersTurret(vehicle)


class _MissilesStrikeSelector(MapCaseMode._DefaultStrikeSelector, MapCaseMode._VehiclesSelector):

    def __init__(self, position, equipment):
        MapCaseMode._DefaultStrikeSelector.__init__(self, position, equipment)
        MapCaseMode._VehiclesSelector.__init__(self, self._intersected)

    def destroy(self):
        MapCaseMode._DefaultStrikeSelector.destroy(self)
        MapCaseMode._VehiclesSelector.destroy(self)

    def processSelection(self, position, reset=False):
        if reset:
            return True
        BigWorld.player().setEquipmentApplicationPoint(self.equipment.id[1], position, Vector2(0, 1))
        return True

    def tick(self):
        self.highlightVehicles()

    def _intersected(self, vehicles):
        pass


class GrinchStrikeSelector(MapCaseMode._ArcadeBomberStrikeSelector):

    def __init__(self, position, equipment):
        super(GrinchStrikeSelector, self).__init__(position, equipment)
        self.area.enableAccurateCollision(False)
        self.outFromBoundsAimArea.enableAccurateCollision(False)


class GrinchTurretStrikeSelector(MapCaseMode._ArenaBoundsAreaStrikeSelector):

    def __init__(self, position, equipment):
        self.ctrlMode = BigWorld.player().inputHandler.ctrls.get(CTRL_MODE_NAME.MAP_CASE_ARCADE, None)
        super(GrinchTurretStrikeSelector, self).__init__(position, equipment, terrainOnly=True)
        self.area.enableAccurateCollision(False)
        self.outFromBoundsAimArea.enableAccurateCollision(False)
        return

    def _isTerrain(self, position):
        spaceID = BigWorld.player().spaceID
        vehicle = BigWorld.player().vehicle
        if not vehicle:
            return False
        if position.distTo(vehicle.position) > self.equipment.maxApplyRadius * _SQRT_2:
            return False
        if self.ctrlMode.lastCollide and self.ctrlMode.lastCollide.normal.dot(_DIR_UP) < 0.9:
            return False
        anythingCollide = BigWorld.wg_collideCustomSphereDynamicStatic(spaceID, position + Vector3(0, TURRET_SPHERE_COLLIDER_RADIUS * 2, 0), position + Vector3(0, TURRET_SPHERE_COLLIDER_RADIUS, 0), self.ctrlMode.turretSphereCollider, CollisionFlags.TRIANGLE_TERRAIN)
        return not anythingCollide


class GrinchMissileReticle(_MissilesStrikeSelector):

    def __init__(self, position, equipment):
        player = BigWorld.player()
        self.ctrlMode = player.inputHandler.ctrls.get(CTRL_MODE_NAME.MAP_CASE_ARCADE, None)
        super(GrinchMissileReticle, self).__init__(position, equipment)
        self.component = player.vehicle.dynamicComponents.get(TRACKING_COMPONENT_NAME)
        self.screenFactorX = self.component.screenFactorX
        self.screenFactorY = self.component.screenFactorY
        return

    def _intersected(self, vehicles):
        isTurretInCorrectRotation = self._isTurretInCorrectRotation()
        if not isTurretInCorrectRotation:
            self.component.setTargetVehicleID(NULL_ENTITY_ID)
            return
        availableToShootVehicles = [ vehicle for vehicle in vehicles if isPointOnScreen(vehicle.position, self.screenFactorX, self.screenFactorY) and isVehicleVisible(vehicle, self.component) and self._isTargetInFrontOfTurret(vehicle.position, self.component.turretVisionCone) and not any(blocker in vehicle.dynamicComponents for blocker in self.component.blockers)
                                   ]
        if not availableToShootVehicles:
            self.component.setTargetVehicleID(NULL_ENTITY_ID)
            return
        if self.component.targetVehicleID not in [ veh.id for veh in availableToShootVehicles ]:
            self.component.setTargetVehicleID(NULL_ENTITY_ID)
        self._pickTarget(availableToShootVehicles)

    def processSelection(self, position, reset=False):
        if self.component.canShoot():
            super(GrinchMissileReticle, self).processSelection(position, reset)
        return reset

    def _validateVehicle(self, vehicle):
        isValid = super(GrinchMissileReticle, self)._validateVehicle(vehicle)
        return isValid and not vehicle.isPlayerTeam and vehicle.isAlive()

    def _pickTarget(self, vehicleList):
        shortestDistance = 0
        refVehicleID = NULL_ENTITY_ID
        for vehicle in vehicleList:
            distance = self._getPointDistanceFromOffsetCenter(vehicle.position)
            if not shortestDistance or distance < shortestDistance:
                shortestDistance = distance
                refVehicleID = vehicle.id

        previousVehicle = BigWorld.entities.get(self.component.targetVehicleID)
        if not self.component.targetVehicleID or not refVehicleID or not previousVehicle:
            self.component.setTargetVehicleID(refVehicleID)
            return
        if refVehicleID == self.component.targetVehicleID:
            return
        refVehicle = BigWorld.entities.get(refVehicleID)
        if not isPointOnScreen(refVehicle.position, SWITCHING_AREA_PERCENTAGE, SWITCHING_AREA_PERCENTAGE, Y_CENTER_OFFSET_PERCENTAGE):
            if not isPointOnScreen(previousVehicle.position, self.component.screenFactorX, self.component.screenFactorY):
                self.component.setTargetVehicleID(refVehicleID)
            return
        if isPointOnScreen(previousVehicle.position, SWITCHING_AREA_PERCENTAGE, SWITCHING_AREA_PERCENTAGE, Y_CENTER_OFFSET_PERCENTAGE):
            return
        self.component.setTargetVehicleID(refVehicleID)

    def _isTurretInCorrectRotation(self):
        player = BigWorld.player()
        aimCameraDirection = self.ctrlMode.camera.aimingSystem.matrixProvider.applyToAxis(2)
        turretYaw = player.vehicle.yaw + player.vehicle.getServerGunAngles()[0]
        turretDir = Vector3(math.sin(turretYaw), 0, math.cos(turretYaw))
        turretDir.normalise()
        dotResult = turretDir.dot(aimCameraDirection)
        return dotResult >= TURRET_MINIMUM_ROTATION

    def _isTargetInFrontOfTurret(self, position, turretVisionAngle):
        player = BigWorld.player()
        gunRotator = player.gunRotator
        gunMatrix = AimingSystems.getPlayerGunMat(gunRotator.turretYaw, gunRotator.gunPitch)
        turretForward = gunMatrix.applyToAxis(2)
        directionToTarget = position - player.vehicle.position
        projection = turretForward.dot(directionToTarget)
        if projection < 0:
            return False
        projectionPoint = projection * turretForward
        targetPoint = projectionPoint - directionToTarget
        radius = math.tan(turretVisionAngle) * projection
        return targetPoint.length < radius

    def _getPointDistanceFromOffsetCenter(self, position):
        posOnScreen = getPointOnScreen(position)
        normalizedX = posOnScreen.x / posOnScreen.w
        normalizedY = posOnScreen.y / posOnScreen.w
        return normalizedX ** 2 + (normalizedY - Y_CENTER_OFFSET_PERCENTAGE) ** 2


class GrinchArcadeMapCaseControlMode(MapCaseMode.MapCaseControlModeBase):
    MODE_NAME = CTRL_MODE_NAME.MAP_CASE_ARCADE
    SNIPER_MODE = CTRL_MODE_NAME.SNIPER

    def __init__(self, dataSection, avatarInputHandler):
        self.turretSphereCollider = None
        self.lastCollide = None
        super(GrinchArcadeMapCaseControlMode, self).__init__(dataSection, avatarInputHandler)
        return

    def enable(self, **args):
        super(GrinchArcadeMapCaseControlMode, self).enable(**args)
        BigWorld.player().autoAim(None)
        return

    def disable(self):
        super(GrinchArcadeMapCaseControlMode, self).disable()
        player = BigWorld.player()
        playerVehicle = player.vehicle
        if not playerVehicle:
            return
        else:
            component = player.vehicle.dynamicComponents.get(TRACKING_COMPONENT_NAME, None)
            if not component:
                return
            component.setTargetVehicleID(NULL_ENTITY_ID, skipUpdate=True)
            return

    def destroy(self):
        spaceID = BigWorld.player().spaceID
        self.lastCollide = None
        if self.turretSphereCollider is not None:
            BigWorld.wg_destroyCollideShape(spaceID, self.turretSphereCollider)
        super(GrinchArcadeMapCaseControlMode, self).destroy()
        return

    def _createCamera(self, config, offset=Vector2(0, 0)):
        return ArcadeCamera.ArcadeCamera(config, offset)

    def _initCamera(self):
        self.camera.create()
        self.turretSphereCollider = BigWorld.wg_createCollideSphere(BigWorld.player().spaceID, TURRET_SPHERE_COLLIDER_RADIUS)

    def _getCameraDesiredShotPoint(self):
        position = self.camera.aimingSystem.getDesiredShotPoint()
        terrainCollide = BigWorld.wg_collideSegment(BigWorld.player().spaceID, position + Vector3(0, 1000, 0), position + Vector3(0, -1000, 0), CollisionFlags.TRIANGLE_PROJECTILENOCOLLIDE, CollisionFlags.TRIANGLE_TERRAIN)
        self.lastCollide = terrainCollide
        if terrainCollide:
            return terrainCollide.closestPoint
        return position

    def _getPreferedPositionOnQuit(self):
        return self.camera.aimingSystem.getThirdPersonShotPoint()

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if self.equipmentID != MISSILE_ABILITY_EQUIPMENT_ID:
            return super(GrinchArcadeMapCaseControlMode, self).handleKeyEvent(isDown, key, mods, event)
        cmdMap = CommandMapping.g_instance
        if cmdMap.isFired(CommandMapping.CMD_CM_ALTERNATE_MODE, key) and isDown:
            return True
        return super(GrinchArcadeMapCaseControlMode, self).handleKeyEvent(isDown, key, mods, event)