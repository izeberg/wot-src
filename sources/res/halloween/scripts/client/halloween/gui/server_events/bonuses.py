from gui.server_events.bonuses import TokensBonus
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController
from helpers import dependency

@dependency.replace_none_kwargs(ctrl=IHalloweenTwitchConController)
def cerfTokenChecker(tokenID, ctrl=None):
    return tokenID == str(ctrl.getCertificateTokenName())


class CerfTokenBonus(TokensBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__('cerfToken', value, isCompensation, ctx)

    def isShowInGUI(self):
        return True