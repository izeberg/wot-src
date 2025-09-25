from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import ScopeTemplates, ViewSettings
from halloween.gui.impl.lobby.hangar_view import HangarWindow
from halloween.gui.impl.lobby.reward_path_view import RewardPathWindow
from halloween.gui.scaleform.daapi.view.lobby.hangar.halloween_browser import HalloweenBrowser
from gui.Scaleform.framework import GroupedViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from halloween.gui.scaleform.genConsts.HALLOWEEN_CM_HANDLER_TYPE import HALLOWEEN_CM_HANDLER_TYPE
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    from gui.Scaleform.daapi.view.lobby import user_cm_handlers
    return (
     (
      HALLOWEEN_CM_HANDLER_TYPE.HALLOWEEN_BATTLE_RESULTS, user_cm_handlers.AppealCMHandler),)


def getViewSettings():
    from halloween.gui.scaleform.daapi.view.lobby.hangar.halloween_module_info import HalloweenModuleInfoWindow
    from halloween.gui.scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import HWVehiclePreview
    return (
     GroupedViewSettings(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_MODULE_INFO, HalloweenModuleInfoWindow, 'moduleInfo.swf', WindowLayer.WINDOW, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_MODULE_INFO, None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_BROWSER, HalloweenBrowser, 'browserScreen.swf', WindowLayer.FULLSCREEN_WINDOW, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_BROWSER, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_VEHICLE_PREVIEW, HWVehiclePreview, 'vehiclePreview.swf', WindowLayer.SUB_VIEW, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_VEHICLE_PREVIEW, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HERO_PREVIEW, HWVehiclePreview, 'vehiclePreview.swf', WindowLayer.SUB_VIEW, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HERO_PREVIEW, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HANGAR, HangarWindow, '', WindowLayer.SUB_VIEW, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HANGAR, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_REWARD_PATH, RewardPathWindow, '', WindowLayer.SUB_VIEW, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_REWARD_PATH, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     LobbyPackageBusinessHandler(),)


class LobbyPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_MODULE_INFO, self.__moduleWindowHandler),
         (
          HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_BROWSER, self.loadViewByCtxEvent),
         (
          HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_VEHICLE_PREVIEW, self.loadViewByCtxEvent),
         (
          HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HERO_PREVIEW, self.loadViewByCtxEvent),
         (
          HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HANGAR, self.loadViewByCtxEvent),
         (
          HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_REWARD_PATH, self.loadViewByCtxEvent))
        super(LobbyPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)

    def __moduleWindowHandler(self, event):
        name = event.loadParams.viewKey.name
        window = self.findViewByName(WindowLayer.WINDOW, name)
        if window is not None:
            self.bringViewToFront(name)
        else:
            self.loadViewByCtxEvent(event)
        return