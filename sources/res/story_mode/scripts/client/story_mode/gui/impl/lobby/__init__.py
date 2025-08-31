

def getStateMachineRegistrators():
    from story_mode.gui.impl.lobby.states import registerStates
    from story_mode.gui.impl.lobby.states import registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()