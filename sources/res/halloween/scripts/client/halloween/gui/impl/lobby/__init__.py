

def getStateMachineRegistrators():
    from halloween.gui.impl.lobby.states import registerStates
    from halloween.gui.impl.lobby.states import registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()