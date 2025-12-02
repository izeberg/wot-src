import typing
from Event import Event
from frameworks.state_machine import BaseStateObserver, visitor
from gui.impl.lobby.new_year.states import HolidayOpsState, getMainMenuName
if typing.TYPE_CHECKING:
    from typing import Union
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
    from frameworks.state_machine import StateEvent
    from gui.impl.lobby.new_year.states import BaseState

class HolidayOpsObjectStateObserver(BaseStateObserver):

    def __init__(self):
        super(HolidayOpsObjectStateObserver, self).__init__()
        self.onObjectStateChanged = Event()

    def clear(self):
        super(HolidayOpsObjectStateObserver, self).clear()
        self.onObjectStateChanged.clear()

    def isObservingState(self, state):
        lsm = state.getMachine()
        return visitor.isDescendantOf(state, lsm.getStateByCls(HolidayOpsState)) or state.getStateID() == HolidayOpsState.STATE_ID

    def onEnterState(self, state, event=None):
        if state.getStateID() == HolidayOpsState.STATE_ID:
            return
        self.onObjectStateChanged(state.getObject())

    def onExitState(self, state, event=None):
        if state.getStateID() == HolidayOpsState.STATE_ID:
            self.onObjectStateChanged(None)
        return


class HolidayOpsObserver(BaseStateObserver):

    def __init__(self):
        super(HolidayOpsObserver, self).__init__()
        self.onNavigationChanged = Event()
        self.onExitView = Event()

    def clear(self):
        super(HolidayOpsObserver, self).clear()
        self.onNavigationChanged.clear()
        self.onExitView.clear()

    def isObservingState(self, state):
        lsm = state.getMachine()
        return state.getParent() == lsm.getStateByCls(HolidayOpsState)

    def onEnterState(self, state, event):
        menuName = getMainMenuName(state.getStateID())
        self.onNavigationChanged(menuName)

    def onExitState(self, state, event):
        exitMenuName = getMainMenuName(state.getStateID())
        self.onExitView(exitMenuName)