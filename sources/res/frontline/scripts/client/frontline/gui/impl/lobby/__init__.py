from __future__ import absolute_import

def getStateMachineRegistrators():
    from frontline.gui.impl.lobby.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()