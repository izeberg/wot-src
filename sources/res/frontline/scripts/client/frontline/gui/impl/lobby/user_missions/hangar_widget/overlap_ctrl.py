from frontline.gui.impl.lobby.states import FrontlineRootHangarState
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin

class FLOverlapCtrlMixin(OverlapCtrlMixin):

    def _onVisibleRouteChanged(self, routeInfo):
        self._isInHangar = routeInfo.state == self._lobbyStateMachine.getStateByCls(FrontlineRootHangarState)
        self._updateViewModelIfNeeded()