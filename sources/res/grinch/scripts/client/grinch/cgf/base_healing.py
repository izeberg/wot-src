import logging, weakref, typing, BigWorld, CGF, GenericComponents
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from grinch.cgf import getVehicleFromGO
from grinch_common.grinch_constants import ARENA_BONUS_TYPE_CAPS
if typing.TYPE_CHECKING:
    from typing import Optional, Dict
    from Vehicle import Vehicle
_logger = logging.getLogger(__name__)

@registerComponent
class GrinchBaseHealingComponent(object):
    category = 'Grinch'
    editorTitle = 'Grinch Base Healing Component'
    animator = ComponentProperty(type=CGFMetaTypes.LINK, editorName='animator', value=GenericComponents.AnimatorComponent)
    domain = CGF.DomainOption.DomainClient

    def __init__(self):
        self.enabled = False
        self.vehicleID = None
        return

    @property
    def currentAnimator(self):
        return self.animator()

    def enable(self):
        self.enabled = True
        self.updateVisual()

    def disable(self):
        self.enabled = False
        self.updateVisual()

    def updateVisual(self):
        if not self.currentAnimator:
            return
        if self.enabled:
            self.currentAnimator.start()
        else:
            self.currentAnimator.stop()


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchBaseHealingManager(CGF.ComponentManager):

    def __init__(self):
        super(GrinchBaseHealingManager, self).__init__()
        self._componentsMap = {}

    def activate(self):
        if hasattr(BigWorld.player(), 'arena'):
            BigWorld.player().arena.onVehicleHealthChanged += self._onHealthChanged

    def deactivate(self):
        if hasattr(BigWorld.player(), 'arena'):
            BigWorld.player().arena.onVehicleHealthChanged -= self._onHealthChanged

    @onAddedQuery(CGF.GameObject, GrinchBaseHealingComponent, tickGroup='postTickUpdate')
    def onAdded(self, go, baseHealingComponent):
        vehicle = getVehicleFromGO(self.spaceID, go)
        baseHealingComponent.vehicleID = vehicle.id
        self._componentsMap[vehicle.id] = weakref.ref(baseHealingComponent)

    @onRemovedQuery(CGF.GameObject, GrinchBaseHealingComponent, tickGroup='postTickUpdate')
    def onRemoved(self, go, baseHealingComponent):
        self._componentsMap.pop(baseHealingComponent.vehicleID, None)
        return

    def _onHealthChanged(self, vehicleID, attackerID, deltaHealth):
        healComponent = self._getCachedHealingComponent(vehicleID)
        if healComponent and deltaHealth < 0:
            healComponent.enable()

    def _getCachedHealingComponent(self, vehicleID):
        healComponentRef = self._componentsMap.get(vehicleID)
        if healComponentRef:
            return healComponentRef()
        else:
            return