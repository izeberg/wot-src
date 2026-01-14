import typing
from SMSoundAbstractComponent import SMSoundAbstractComponent
from SMSound3DObjectComponent import SMSound3DObjectComponent

class SMSound3DComponent(SMSoundAbstractComponent):

    @property
    def soundObject(self):
        if self.entity is None or self.entity.isDestroyed:
            return
        component = self.entity.dynamicComponents.get(SMSound3DObjectComponent.__name__)
        if component:
            return component.soundObject
        else:
            return

    def _play(self, soundName):
        if self.soundObject is not None:
            self.soundObject.play(soundName)
        return