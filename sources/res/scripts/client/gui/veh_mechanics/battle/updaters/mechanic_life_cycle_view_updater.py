from gui.veh_mechanics.battle.updaters.updaters_common import VehicleMechanicUpdater

class VehicleMechanicLifeCycleUpdater(VehicleMechanicUpdater):

    def _subscribeToMechanicComponent(self, mechanicComponent):
        super(VehicleMechanicLifeCycleUpdater, self)._subscribeToMechanicComponent(mechanicComponent)
        mechanicComponent.lifeCycleEvents.lateSubscribe(self.view)

    def _unsubscribeFromMechanicComponent(self, mechanicComponent):
        self.view.unsubscribeFrom(mechanicComponent.lifeCycleEvents)
        super(VehicleMechanicLifeCycleUpdater, self)._unsubscribeFromMechanicComponent(mechanicComponent)