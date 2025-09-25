from battle_royale.gui.impl.lobby.views.states import BattleRoyaleHangarState
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin

class BattleRoyaleOverlapCtrlMixin(OverlapCtrlMixin):

    def _onVisibleRouteChanged(self, routeInfo):
        self._isInHangar = routeInfo.state == self._lobbyStateMachine.getStateByCls(BattleRoyaleHangarState)
        self._updateViewModelIfNeeded()