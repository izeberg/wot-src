from fun_random_common.fun_constants import ARENA_GUI_TYPE

def addArenaGuiTypesFromExtensionToFunRange(extArenaGuiType):
    extraAttrs = extArenaGuiType.getExtraAttrs()
    extraValues = tuple(extraAttrs.itervalues())
    ARENA_GUI_TYPE.FUN_RANDOM_RANGE += extraValues