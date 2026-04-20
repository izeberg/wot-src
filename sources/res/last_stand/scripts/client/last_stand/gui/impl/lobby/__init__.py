from __future__ import absolute_import

def getStateMachineRegistrators():
    from last_stand.gui.impl.lobby.states import registerStates
    from last_stand.gui.impl.lobby.states import registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()