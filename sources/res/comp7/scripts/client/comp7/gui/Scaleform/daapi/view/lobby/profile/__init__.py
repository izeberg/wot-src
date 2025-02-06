from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_statistics import Comp7ProfileStatistics
    from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_technique_page import Comp7ProfileTechniquePage
    from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_technique_window import Comp7ProfileTechniqueWindow
    return (
     ComponentSettings(VIEW_ALIAS.PROFILE_STATISTICS, Comp7ProfileStatistics, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE, Comp7ProfileTechniquePage, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_WINDOW, Comp7ProfileTechniqueWindow, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return ()