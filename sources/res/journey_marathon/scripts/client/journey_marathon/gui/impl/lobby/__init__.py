from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.app_loader.settings import APP_NAME_SPACE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.shared import EVENT_BUS_SCOPE

def getStateMachineRegistrators():
    from journey_marathon.gui.impl.lobby.jm_lsm_states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    from journey_marathon.gui.impl.lobby.jm_map_view import JmMapWindow
    return (
     ViewSettings(VIEW_ALIAS.JM_MAP_VIEW, JmMapWindow, '', WindowLayer.SUB_VIEW, VIEW_ALIAS.JM_MAP_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE),)


def getContextMenuHandlers():
    return ()


class _JmBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        super(_JmBusinessHandler, self).__init__(listeners=(
         (
          VIEW_ALIAS.JM_MAP_VIEW, self.loadView),), appNS=APP_NAME_SPACE.SF_LOBBY, scope=EVENT_BUS_SCOPE.LOBBY)


def getBusinessHandlers():
    return (
     _JmBusinessHandler(),)