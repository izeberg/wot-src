from __future__ import absolute_import

def getStateMachineRegistrators():
    from battle_royale.gui.impl.lobby.views.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()