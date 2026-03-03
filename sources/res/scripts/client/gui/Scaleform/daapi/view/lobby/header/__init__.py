from __future__ import absolute_import
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.LobbyView import LobbyHeaderInject
    from gui.Scaleform.daapi.view.lobby.LobbyView import LobbyFooterInject
    return (
     ComponentSettings(VIEW_ALIAS.LOBBY_HEADER_OVERLAPPING, LobbyHeaderInject, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.LOBBY_FOOTER_OVERLAPPING, LobbyFooterInject, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return ()