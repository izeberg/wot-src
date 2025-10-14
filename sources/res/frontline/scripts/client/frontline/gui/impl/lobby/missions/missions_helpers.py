from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper

class FrontlineMissionsGuiHelper(DefaultMissionsGuiHelper):

    @classmethod
    def isDailyMissionsSupported(cls):
        return False

    @classmethod
    def isPM3MissionsSupported(cls):
        return True