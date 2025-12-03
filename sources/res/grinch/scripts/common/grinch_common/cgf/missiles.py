import CGF, Triggers
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from grinch_common.cgf.common_components import OnLinkedDisappearPrefabSpawner
from grinch_common.grinch_constants import MissileLauncherStatuses
from GenericComponents import HomingMovementComponent
TRACKING_COMPONENT_NAME = 'target_locking_ability'
LAUNCHER_CONTROLLER_COMPONENT_NAME = 'launcher_controller'
CHASED_BY_MISSILE_COMPONENT_NAME = 'chased_by_missile'

@registerComponent
class GrinchTrackerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchMissileCollisionComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll

    def __init__(self):
        self.vehicle = None
        self.attackerInfo = None
        return


@registerComponent
class ExplosionAreaTriggerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)
    maxDamage = ComponentProperty(type=CGFMetaTypes.INT, editorName='Max Damage', value=0)
    minDamage = ComponentProperty(type=CGFMetaTypes.INT, editorName='Min Damage', value=0)
    maxDamageRange = ComponentProperty(type=CGFMetaTypes.INT, editorName='Max Damage Range', value=0)
    ownerID = ComponentProperty(type=CGFMetaTypes.INT, editorName='Owner ID', value=0)

    def __init__(self):
        self.reactionID = None
        return


@registerComponent
class OnMissileDisappearComponent(OnLinkedDisappearPrefabSpawner):
    linkedComponent = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Missile component link', value=HomingMovementComponent)


@registerComponent
class GrinchMissileLauncherStateComponent(object):
    category = 'Grinch'
    state = ComponentProperty(type=CGFMetaTypes.INT, editorName='state', value=0)
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchMissileLauncherComponent(object):
    category = 'Grinch'
    currentState = ComponentProperty(type=CGFMetaTypes.INT, editorName='currentState', value=MissileLauncherStatuses.IDLE)
    domain = CGF.DomainOption.DomainAll

    def setState(self, go, state):
        if state == self.currentState:
            return
        hierarchy = CGF.HierarchyManager(self.spaceID)
        activationIsAllowed = go.isActive()
        for gameObject, stateComponent in hierarchy.findComponentsInHierarchy(go, GrinchMissileLauncherStateComponent):
            if stateComponent.state == self.currentState:
                gameObject.deactivate()
            elif stateComponent.state == state and activationIsAllowed:
                gameObject.activate()

        self.currentState = state

    def updateVisual(self, go, targetingComponent):
        self.setState(go, targetingComponent.launcherState)


@registerComponent
class MissilePivotPoint(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll