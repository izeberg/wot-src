from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper

class Comp7MissionsGuiHelper(DefaultMissionsGuiHelper):

    @classmethod
    def isDailyMissionsSupported(cls):
        return True

    @classmethod
    def isPM3MissionsSupported(cls):
        return False