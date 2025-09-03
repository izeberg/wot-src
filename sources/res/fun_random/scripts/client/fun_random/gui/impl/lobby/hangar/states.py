

def registerStates(machine):
    from gui.impl.lobby.hangar.states import LegacyHangarState
    from fun_random.gui.fun_gui_constants import FUNCTIONAL_FLAG
    LegacyHangarState.addLegacyHangarFunctionalFlag(FUNCTIONAL_FLAG.FUN_RANDOM)


def registerTransitions(machine):
    pass