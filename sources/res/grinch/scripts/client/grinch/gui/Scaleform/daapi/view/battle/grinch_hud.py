import logging, BigWorld
from constants import ARENA_PERIOD, LocalizableBotName, BotNamingType
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from grinch.gui.impl.battle.grinch_hud_view import GrinchHudView
from gui.battle_control.controllers.arena_load_ctrl import IArenaLoadCtrlListener
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.impl import IGuiLoader
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
def isMastersSlave(vInfo, sessionProvider=None):
    if not vInfo.player.isBot:
        return False
    namingType, args = LocalizableBotName.parse(vInfo.player.fakeName)
    if namingType != BotNamingType.MASTER:
        return False
    arenaDP = sessionProvider.getArenaDP()
    curPlayerVehID = arenaDP.getPlayerVehicleID()
    _, _, _, masterVehID = args
    if curPlayerVehID == masterVehID:
        return True
    masterVInfo = arenaDP.getVehicleInfo(masterVehID)
    if masterVInfo.isEnemy() or masterVInfo.squadIndex == 0:
        return False
    playerVInfo = arenaDP.getVehicleInfo(curPlayerVehID)
    if masterVInfo.squadIndex == playerVInfo.squadIndex:
        return True
    return False


class GrinchHud(InjectComponentAdaptor, IAbstractPeriodView, IArenaLoadCtrlListener):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def setPeriod(self, period):
        if period == ARENA_PERIOD.WAITING:
            self._sessionProvider.dynamic.battleHints.showHint('grinch.await_for_players', {})
        if period == ARENA_PERIOD.PREBATTLE:
            self._sessionProvider.dynamic.battleHints.hideHint('grinch.await_for_players')
            periodCtrl = self._sessionProvider.shared.arenaPeriod
            remainingTime = periodCtrl.getEndTime() - BigWorld.serverTime()
            self._sessionProvider.dynamic.battleHints.showHint('grinch.prebattle', {'overrideShowTime': remainingTime})
        if period == ARENA_PERIOD.BATTLE:
            self._sessionProvider.dynamic.battleHints.hideHint('grinch.prebattle')
            self._sessionProvider.dynamic.battleHints.showHint('grinch.start_battle', {})

    def arenaLoadCompleted(self):
        if self._injectView is not None:
            self._injectView.arenaLoadCompleted()
        return

    def _makeInjectView(self):
        return GrinchHudView()


class GrinchHudComponent(object):
    GRINCH_HUD_R = R.views.grinch.battle.GrinchHudView()
    gui = dependency.descriptor(IGuiLoader)

    @property
    def hud(self):
        return self.gui.windowsManager.getViewByLayoutID(self.GRINCH_HUD_R)