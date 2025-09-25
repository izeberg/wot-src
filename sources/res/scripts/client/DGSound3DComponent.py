import typing
from DGSoundAbstractComponent import DGSoundAbstractComponent
from DGSound3DObjectComponent import DGSound3DObjectComponent

class DGSound3DComponent(DGSoundAbstractComponent):

    @property
    def soundObject(self):
        if self.entity is None or self.entity.isDestroyed:
            return
        component = self.entity.dynamicComponents.get(DGSound3DObjectComponent.__name__)
        if component:
            return component.soundObject
        else:
            return

    def _play(self, soundName):
        if self.soundObject is not None:
            self.soundObject.play(soundName)
        return