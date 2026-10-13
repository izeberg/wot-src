from __future__ import absolute_import

def getStateMachineRegistrators():
    from comp7.gui.impl.lobby.hangar.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()