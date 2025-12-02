from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from grinch_progression_common.grinch_progression_account_commands import CMD_GP_OPEN_STEP, CMD_GP_RESET_REWARDS

class GrinchProgressionAccountComponent(BaseAccountExtensionComponent):

    def openStep(self, chapterID, stepID, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext: callback(resultID, errorStr, ext)
        else:
            proxy = None
        self.account._doCmdInt2(CMD_GP_OPEN_STEP, chapterID, stepID, proxy)
        return

    def resetProgression(self, callback=None):
        self.account._doCmdNoArgs(CMD_GP_RESET_REWARDS, None)
        return