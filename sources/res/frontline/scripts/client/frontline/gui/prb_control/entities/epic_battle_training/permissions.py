from constants import PREBATTLE_ROLE
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions, ILegacyPermissions

class EpicBattleTrainingPermissions(LegacyPermissions):

    def canChangeVehicle(self):
        return True

    def canCreateSquad(self):
        return False

    @classmethod
    def isCreator(cls, roles):
        return roles == PREBATTLE_ROLE.TRAINING_CREATOR

    def canChangeSetting(self):
        return self.canChangeComment() or self.canChangeArena() or self.canMakeOpenedClosed()

    def canStartBattle(self):
        return self.canSetTeamState(1) and self.canSetTeamState(2)


class EpicBattleTrainingIntroPermissions(ILegacyPermissions):

    def canCreateSquad(self):
        return False