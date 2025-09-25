from comp7_light.gui.impl.lobby.hangar.states import Comp7LightRootHangarState
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin

class Comp7LightOverlapCtrlMixin(OverlapCtrlMixin):

    def _onVisibleRouteChanged(self, routeInfo):
        self._isInHangar = routeInfo.state == self._lobbyStateMachine.getStateByCls(Comp7LightRootHangarState)
        self._updateViewModelIfNeeded()