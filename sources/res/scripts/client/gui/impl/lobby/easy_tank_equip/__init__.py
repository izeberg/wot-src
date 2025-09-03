

def getStateMachineRegistrators():
    from gui.impl.lobby.easy_tank_equip.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()