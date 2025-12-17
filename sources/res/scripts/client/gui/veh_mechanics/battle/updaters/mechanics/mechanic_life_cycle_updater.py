from __future__ import absolute_import
import typing
from events_handler import eventHandler
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater

class VehicleMechanicLifeCycleUpdater(VehicleMechanicUpdater):

    @eventHandler
    def onMechanicComponentCatching(self, component):
        component.lifeCycleEvents.lateSubscribe(self.view)

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        self.view.unsubscribeFrom(component.lifeCycleEvents)