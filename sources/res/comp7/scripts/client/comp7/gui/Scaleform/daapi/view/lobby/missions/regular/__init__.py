from gui.Scaleform.framework import ComponentSettings, ScopeTemplates
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from comp7.gui.Scaleform.daapi.view.lobby.missions.regular.daily_quests_injector_view import Comp7DailyQuestsInjectorView
    return (
     ComponentSettings(QUESTS_ALIASES.MISSIONS_PREMIUM_VIEW_PY_ALIAS, Comp7DailyQuestsInjectorView, ScopeTemplates.VIEW_SCOPE),)


def getBusinessHandlers():
    return ()