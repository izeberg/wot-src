from gui.Scaleform.framework import ComponentSettings, ScopeTemplates
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from tank_academy.gui.impl.lobby.tank_academy.tank_academy_entry_point_view import TankAcademyEntryPointWidget
    return (
     ComponentSettings(HANGAR_ALIASES.TANK_ACADEMY_ENTRY_POINT, TankAcademyEntryPointWidget, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()