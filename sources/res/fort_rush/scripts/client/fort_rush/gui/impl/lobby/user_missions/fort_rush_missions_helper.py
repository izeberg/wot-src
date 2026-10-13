from __future__ import absolute_import
from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper

class FortRushMissionsGuiHelper(DefaultMissionsGuiHelper):

    @classmethod
    def isDailyMissionsSupported(cls):
        return True

    @classmethod
    def isPM3MissionsSupported(cls):
        return False