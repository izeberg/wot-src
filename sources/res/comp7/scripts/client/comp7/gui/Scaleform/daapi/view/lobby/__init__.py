from gui.Scaleform.framework import ComponentSettings, ScopeTemplates
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.impl.gen import R
from gui.shared.system_factory import registerBattleModifiersPanel

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from comp7.gui.Scaleform.daapi.view.lobby.hangar.comp7_modifiers_panel import Comp7ModifiersPanel
    registerBattleModifiersPanel(R.views.lobby.comp7.SeasonModifier(), Comp7ModifiersPanel)
    return ()


def getBusinessHandlers():
    return ()