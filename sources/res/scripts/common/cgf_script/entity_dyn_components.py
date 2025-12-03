from cgf_network import processCreateDynamicComponent, processDestroyDynamicComponent

class BWEntityComponentTracker(object):

    def onDynamicComponentCreated(self, component):
        networkID = getattr(component, 'game_object_network_id', None)
        supMethod = getattr(super(BWEntityComponentTracker, self), 'onDynamicComponentCreated', None)
        if networkID is not None:
            processCreateDynamicComponent(networkID, self.spaceID, component)
        else:
            existing = self.entityGameObject.findComponentByType(type(component))
            if existing is None:
                self.entityGameObject.addComponent(component)
        supMethod = getattr(super(BWEntityComponentTracker, self), 'onDynamicComponentCreated', None)
        if supMethod is not None:
            supMethod(self, component)
        return

    def onDynamicComponentDestroyed(self, component):
        networkID = getattr(component, 'game_object_network_id', None)
        if networkID is not None:
            processDestroyDynamicComponent(networkID, self.spaceID, component)
        else:
            existing = self.entityGameObject.findComponentByType(type(component))
            if existing is component:
                self.entityGameObject.removeComponent(component)
        supMethod = getattr(super(BWEntityComponentTracker, self), 'onDynamicComponentDestroyed', None)
        if supMethod is not None:
            supMethod(self, component)
        return