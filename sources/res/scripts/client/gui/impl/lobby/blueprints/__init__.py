from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips

def getStateMachineRegistrators():
    from gui.impl.lobby.blueprints.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()


def getBlueprintTooltipData(ttId, itemCD):
    if ttId == BlueprintScreenTooltips.TOOLTIP_BLUEPRINT and itemCD is not None:
        return createTooltipData(isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_INFO, specialArgs=[
         int(itemCD)])
    else:
        return