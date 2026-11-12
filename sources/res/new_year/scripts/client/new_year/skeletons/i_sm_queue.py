

class IStateMachineQueue(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def lock(self):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError

    def bind(self, personaType, animatorComponent):
        raise NotImplementedError

    def unbind(self, personaType):
        raise NotImplementedError

    def handleCloseUp(self, personaType, state):
        raise NotImplementedError

    def handleRewards(self, personaType, rewards):
        raise NotImplementedError

    def handleLoaded(self):
        raise NotImplementedError