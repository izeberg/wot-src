from __future__ import absolute_import
import SoundGroups

def play2DSound(eventName):
    SoundGroups.g_instance.playSafeSound2D(eventName)


def get2DSound(eventName):
    return SoundGroups.g_instance.getSound2D(eventName)