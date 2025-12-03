import weakref
from typing import TYPE_CHECKING
import CGF, Math, math_utils
from GenericComponents import TransformComponent, EntityGOSync
from Vehicle import Vehicle
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onProcessQuery
from grinch.cgf import registerComponentOnParams
from constants import IS_CLIENT
from helpers import isPlayerAvatar
from grinch_common.grinch_constants import ARENA_BONUS_TYPE_CAPS
if IS_CLIENT:
    from grinch.gui.game_control.performance_analyzer import PerformanceGroup
else:

    class PerformanceGroup(object):
        MEDIUM_RISK = 1
        HIGH_RISK = 2


if TYPE_CHECKING:
    from GrinchScoreComponent import GrinchScoreComponent
    from typing import Optional
presentAngleVector = Math.Vector3()

def getScoreComponent():
    import BigWorld
    player = BigWorld.player()
    if not (player and isPlayerAvatar() and player.arena and player.arena.arenaInfo):
        return
    else:
        return player.arena.arenaInfo.dynamicComponents.get('GrinchScoreComponent')


@registerComponent
class PresentComponent(object):
    category = 'Grinch'
    top = ComponentProperty(type=CGFMetaTypes.LINK, editorName='topSlot', value=CGF.GameObject)
    rotationTarget = ComponentProperty(type=CGFMetaTypes.LINK, editorName='rotationTarget', value=CGF.GameObject)
    present = ComponentProperty(type=CGFMetaTypes.LINK, editorName='present', value=CGF.GameObject)
    bigPresent = ComponentProperty(type=CGFMetaTypes.LINK, editorName='bigPresent', value=CGF.GameObject)
    topY = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='topY', value=1)
    topYBig = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='topYBig', value=1)

    def __init__(self):
        self.vehicle = None
        return

    def setVehicle(self, vehicle):
        self.vehicle = weakref.ref(vehicle) if vehicle else None
        return

    def getVehicle(self):
        if self.vehicle:
            return self.vehicle()
        else:
            return

    def setPresentType(self, isBig):
        if isBig:
            self.bigPresent.activate()
            self.present.deactivate()
        else:
            self.present.activate()
            self.bigPresent.deactivate()
        transformComponent = self.top.findComponentByType(TransformComponent)
        oldPosition = transformComponent.position
        val = Math.Vector3(oldPosition.x, self.topYBig if isBig else self.topY, oldPosition.z)
        newTransform = Math.Matrix()
        newTransform.setTranslate(val)
        transformComponent.transform = newTransform


@registerComponent
class PresentStackComponent(object):
    category = 'Grinch'
    appearance = ComponentProperty(type=CGFMetaTypes.LINK, editorName='appearanceLink', value=CGF.GameObject)

    def setCounter(self, go, presents):
        totalValue = len(presents)
        hierarchy = CGF.HierarchyManager(self.spaceID)
        for presentGO, presentComp in hierarchy.findComponentsInHierarchy(go, PresentComponent):
            index = int(presentGO.name.split('_')[(-1)])
            if index <= totalValue:
                presentGO.activate()
                presentComp.setPresentType(presents[(index - 1)])
            else:
                presentGO.deactivate()


@registerComponentOnParams(bonusCap=ARENA_BONUS_TYPE_CAPS.GRINCH, disabledPerformanceGroup=(
 PerformanceGroup.MEDIUM_RISK, PerformanceGroup.HIGH_RISK), domain=CGF.DomainOption.DomainClient)
class PresentCarryManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, PresentStackComponent)
    def onAdded(self, go, presentStack):
        vehicle = self.__getVehicle(go)
        if not vehicle:
            return
        scoreComponent = getScoreComponent()
        if not scoreComponent:
            return
        presents = scoreComponent.getVehiclePresents(vehicle.id)
        presentStack.setCounter(go, presents)

    @onAddedQuery(CGF.GameObject, PresentComponent)
    def onPresentAdded(self, go, present):
        present.setVehicle(self.__getVehicle(go))

    @onProcessQuery(CGF.GameObject, PresentComponent, tickGroup='Simulation')
    def onProcess(self, _, present):
        targetTransform = present.rotationTarget.findComponentByType(TransformComponent)
        speed = 0.0
        vehicle = present.getVehicle()
        if vehicle is not None and vehicle.appearance.filter is not None:
            speed = vehicle.appearance.filter.averageSpeed
        val = math_utils.clamp(-1.0, 1.0, speed / 45.0) * -0.5
        presentAngleVector.y = val
        if presentAngleVector.distTo(targetTransform.rotationPYR) < 0.01:
            return
        else:
            targetTransform.transform = Math.createRTMatrix(presentAngleVector, targetTransform.transform.translation)
            return

    def __getVehicle(self, gameObject):
        hierarchy = CGF.HierarchyManager(self.spaceID)
        rootGameObject = hierarchy.getTopMostParent(gameObject)
        goSyncComponent = rootGameObject.findComponentByType(EntityGOSync)
        if goSyncComponent is None:
            return
        else:
            return goSyncComponent.entity