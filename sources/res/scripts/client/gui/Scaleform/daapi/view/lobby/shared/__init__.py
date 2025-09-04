

def getStateMachineRegistrators():
    from gui.Scaleform.daapi.view.lobby.shared.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()