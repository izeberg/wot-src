from frameworks.wulf import WindowLayer
from grinch_progression.gui.impl.lobby.views.game_board import GameBoardWindow
from grinch_progression.gui.impl.lobby.views.info_view import GameBoardInfoWindow
from gui.app_loader import settings as app_settings
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework import ViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.shared import EVENT_BUS_SCOPE

def getStateMachineRegistrators():
    from grinch_progression.gui.impl.lobby.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return (
     ViewSettings(VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD, GameBoardWindow, '', WindowLayer.SUB_VIEW, VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD_INFO, GameBoardInfoWindow, '', WindowLayer.SUB_VIEW, VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD_INFO, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     GrinchProgressionLobbyBusinessHandler(),)


class GrinchProgressionLobbyBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD_INFO, self.loadViewByCtxEvent))
        super(GrinchProgressionLobbyBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)


def getContextMenuHandlers():
    return ()