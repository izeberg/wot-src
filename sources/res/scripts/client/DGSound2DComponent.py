import SoundGroups
from DGSoundAbstractComponent import DGSoundAbstractComponent

class DGSound2DComponent(DGSoundAbstractComponent):

    def _play(self, soundName):
        SoundGroups.g_instance.playSound2D(soundName)