

def getStateMachineRegistrators():
    from gui.impl.lobby.account_dashboard.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()