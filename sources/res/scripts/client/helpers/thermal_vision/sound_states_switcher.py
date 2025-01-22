import SoundGroups

class SoundStatesSwitcher(object):

    def __init__(self, soundGroup, startState, stopState):
        super(SoundStatesSwitcher, self).__init__()
        self.soundGroup = soundGroup
        self.startState = startState
        self.stopState = stopState

    def enable(self):
        SoundGroups.g_instance.setState(self.soundGroup, self.startState)

    def disable(self):
        SoundGroups.g_instance.setState(self.soundGroup, self.stopState)