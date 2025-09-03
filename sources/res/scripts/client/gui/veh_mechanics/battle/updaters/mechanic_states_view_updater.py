from gui.veh_mechanics.battle.updaters.updaters_common import VehicleMechanicUpdater

class VehicleMechanicStatesUpdater(VehicleMechanicUpdater):

    def _subscribeToMechanicComponent(self, mechanicComponent):
        super(VehicleMechanicStatesUpdater, self)._subscribeToMechanicComponent(mechanicComponent)
        mechanicComponent.statesEvents.lateSubscribe(self.view)

    def _unsubscribeFromMechanicComponent(self, mechanicComponent):
        self.view.unsubscribeFrom(mechanicComponent.statesEvents)
        super(VehicleMechanicStatesUpdater, self)._unsubscribeFromMechanicComponent(mechanicComponent)