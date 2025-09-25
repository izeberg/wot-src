

def getStateMachineRegistrators():
    from gui.impl.lobby.clan_supply.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()