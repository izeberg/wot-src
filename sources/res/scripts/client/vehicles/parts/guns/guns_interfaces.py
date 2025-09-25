import typing, CGF
from vehicles.components.component_events import IComponentEvents, IComponentListener

class IGunComponent(object):

    def getGunInstallationIndex(self):
        raise NotImplementedError

    def getGunRootGameObject(self):
        raise NotImplementedError


class IGunShootingEventsLogic(object):
    onAppearanceReady = None
    onDiscreteShot = None
    onMultiShot = None

    def processAppearanceReady(self):
        raise NotImplementedError

    def processDiscreteShot(self, gunIndex):
        raise NotImplementedError

    def processMultiShot(self, gunIndexes):
        raise NotImplementedError


class IGunShootingEvents(IComponentEvents, IGunShootingEventsLogic):
    pass


class IGunShootingListenerLogic(object):

    def onAppearanceReady(self):
        pass

    def onDiscreteShot(self, gunIndex):
        pass

    def onMultiShot(self, gunIndexes):
        pass


class IGunShootingListener(IComponentListener, IGunShootingListenerLogic):
    pass