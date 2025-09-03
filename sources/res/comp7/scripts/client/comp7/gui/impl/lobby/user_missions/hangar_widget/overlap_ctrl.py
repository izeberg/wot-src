from comp7.gui.impl.lobby.hangar.states import Comp7RootHangarState
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin

class Comp7OverlapCtrlMixin(OverlapCtrlMixin):

    def _onVisibleRouteChanged(self, routeInfo):
        self._isInHangar = routeInfo.state == self._lobbyStateMachine.getStateByCls(Comp7RootHangarState)
        self._updateViewModelIfNeeded()