from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from comp7_light.gui.Scaleform.daapi.view.battle.shared.ingame_menu import Comp7LightIngameMenu
    return (
     ViewSettings(VIEW_ALIAS.INGAME_MENU, Comp7LightIngameMenu, 'ingameMenu.swf', WindowLayer.TOP_WINDOW, None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canClose=False, canDrag=False),)


def getBusinessHandlers():
    return ()