from vehicles.components.component_events import IComponentEvents, IComponentListener

class ILifeCycleComponent(object):

    @property
    def lifeCycleEvents(self):
        raise NotImplementedError


class IComponentLifeCycleEventsLogic(object):
    onComponentParamsCollected = None
    onComponentDestroyed = None

    def lateSubscribe(self, listener):
        raise NotImplementedError

    def processParamsCollected(self):
        raise NotImplementedError


class IComponentLifeCycleEvents(IComponentEvents, IComponentLifeCycleEventsLogic):
    pass


class IComponentLifeCycleListenerLogic(object):

    def onComponentParamsCollected(self, component):
        pass

    def onComponentDestroyed(self):
        pass


class IComponentLifeCycleListener(IComponentListener, IComponentLifeCycleListenerLogic):
    pass