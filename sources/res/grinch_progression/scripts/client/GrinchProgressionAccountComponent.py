from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from grinch_progression_common.grinch_progression_account_commands import CMD_GP_OPEN_STEP

class GrinchProgressionAccountComponent(BaseAccountExtensionComponent):

    def openStep(self, chapterID, stepID, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext: callback(resultID, errorStr, ext)
        else:
            proxy = None
        self.account._doCmdInt2(CMD_GP_OPEN_STEP, chapterID, stepID, proxy)
        return