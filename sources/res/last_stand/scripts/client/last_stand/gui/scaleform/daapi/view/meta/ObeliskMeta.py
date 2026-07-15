from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ObeliskMeta(BaseDAAPIComponent):

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)

    def as_setNameS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_setName(name)