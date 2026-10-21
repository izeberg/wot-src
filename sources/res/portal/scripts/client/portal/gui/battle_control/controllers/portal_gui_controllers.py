from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

@dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
def getPortalBattleMarkersController(portalCtrlID, sessionProvider=None):
    if sessionProvider is not None:
        repository = sessionProvider.dynamic._repository
        if hasattr(repository, '_ctrls'):
            return repository._ctrls.get(portalCtrlID)
        return
    return