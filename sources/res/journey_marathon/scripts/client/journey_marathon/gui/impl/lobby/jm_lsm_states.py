from __future__ import absolute_import
import typing
from gui.impl.backport import text
from gui.impl.gen import R
from gui.lobby_state_machine.states import SubScopeSubLayerState, LobbyStateDescription, ViewLobbyState
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from journey_marathon.gui.shared.jm_event_dispatcher import showInfoPage
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine

def registerStates(machine):
    machine.addState(JmMapState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(JmMapState))


@SubScopeSubLayerState.parentOf
class JmMapState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.JM_MAP_VIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.JM_MAP_VIEW)

    def registerTransitions(self):
        from gui.impl.lobby.vehicle_hub import OverviewState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(OverviewState), record=True)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=text(R.strings.journey_marathon.lsm.mapView.title()), infos=(
         LobbyStateDescription.Info(type=LobbyStateDescription.Info.Type.INFO, onMoreInfoRequested=showInfoPage),))

    def getBackNavigationDescription(self, params):
        return text(R.strings.journey_marathon.lsm.mapView.backButton())