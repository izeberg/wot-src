from gui.impl.gen import R
from gui.impl.lobby.page.lobby_header import LobbyHeader

class GrinchLobbyHeader(LobbyHeader):

    def _getChildComponents(self):
        header = R.aliases.lobby_header.default
        childComponents = super(GrinchLobbyHeader, self)._getChildComponents()
        childComponents.pop(header.ReservesEntryPoint())
        return childComponents