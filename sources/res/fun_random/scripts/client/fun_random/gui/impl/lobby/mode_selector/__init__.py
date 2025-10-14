from __future__ import absolute_import

def getStateMachineRegistrators():
    from fun_random.gui.impl.lobby.mode_selector.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()