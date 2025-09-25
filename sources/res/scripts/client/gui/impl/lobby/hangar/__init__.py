from __future__ import absolute_import

def getStateMachineRegistrators():
    from gui.impl.lobby.hangar.states_registration import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()