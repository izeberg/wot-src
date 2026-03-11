import BigWorld, AccountCommands

class NewbieStartPageComponent(BigWorld.StaticScriptComponent):

    def setInitialPlayerExperienceLevel(self, expLevel, callback=None):
        self.entity._doCmdInt(AccountCommands.CMD_SET_INITIAL_PLAYER_EXPERIENCE_LEVEL, expLevel, callback)