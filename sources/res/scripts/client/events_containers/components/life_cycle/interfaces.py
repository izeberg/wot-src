from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener

class ILifeCycleComponent(object):

    @property
    def lifeCycleEvents(self):
        raise NotImplementedError

    def getComponentParams(self):
        return


class IComponentLifeCycleEventsLogic(object):
    onComponentParamsCollected = None
    onComponentAppearanceReady = None
    onComponentAppearanceReset = None
    onComponentDestroyed = None

    def processAppearanceReady(self):
        raise NotImplementedError

    def processAppearanceReset(self):
        raise NotImplementedError

    def processParamsCollected(self):
        raise NotImplementedError


class IComponentLifeCycleEvents(IClientEventsContainer, IComponentLifeCycleEventsLogic):
    pass


class IComponentLifeCycleListenerLogic(object):

    def onComponentParamsCollected(self, params):
        pass

    def onComponentAppearanceReady(self, component):
        pass

    def onComponentAppearanceReset(self, component):
        pass

    def onComponentDestroyed(self, component):
        pass


class IComponentLifeCycleListener(IClientEventsContainerListener, IComponentLifeCycleListenerLogic):
    pass