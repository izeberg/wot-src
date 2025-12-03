from gui import GUI_SETTINGS
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

def getNewYearOldCollectionRewardUrl():
    return _getNyUrl('newYearOldCollectionRewardUrl')


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def _getNyUrl(urlName, lobbyContext=None):
    hostUrl = lobbyContext.getServerSettings().shop.hostUrl
    return hostUrl + GUI_SETTINGS.nyShop.get(urlName, '')