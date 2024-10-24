from helpers import dependency
from entry_point_view import EpicBattlesEntryPointView
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.EpicBattlesEntryPointMeta import EpicBattlesEntryPointMeta
from gui.periodic_battles.models import PrimeTimeStatus
from skeletons.gui.game_control import IEpicBattleMetaGameController

@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)
def isEpicBattlesEntryPointAvailable(epicController=None):
    from frontline.gui.frontline_helpers import geFrontlineState
    from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState
    state, _, _ = geFrontlineState()
    primeTimeStatus, _, _ = epicController.getPrimeTimeStatus()
    hasUnclaimedRewards = epicController.getNotChosenRewardCount()
    if not epicController.isEnabled() or not epicController.getCurrentSeasonID() or primeTimeStatus in [PrimeTimeStatus.NOT_SET, PrimeTimeStatus.FROZEN] or state == FrontlineState.FINISHED and not hasUnclaimedRewards:
        return False
    return True


class EpicBattlesEntryPoint(EpicBattlesEntryPointMeta):

    def _makeInjectView(self):
        self.__view = EpicBattlesEntryPointView(flags=ViewFlags.VIEW)
        return self.__view