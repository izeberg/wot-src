from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

@dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
def getPortalBattleMarkersController(portalCtrlID, sessionProvider=None):
    if sessionProvider is not None:
        portalGuiBattleControllers = sessionProvider.dynamic._repository._ctrls
        return portalGuiBattleControllers.get(portalCtrlID)
    else:
        return