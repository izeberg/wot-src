import typing
from WeakMethod import WeakMethodProxy
from frameworks.state_machine import StateFlags
from frameworks.state_machine.transitions import TransitionType
from grinch.gui.impl.lobby.post_battle.post_battle_view import PostBattleView
from gui.Scaleform.framework import ScopeTemplates
from gui.lobby_state_machine.states import LobbyStateDescription, GuiImplViewLobbyState, SubScopeTopLayerState
from grinch.skeletons.battle_controller import IGrinchController
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.hangar.states import HangarState
from gui.lobby_state_machine.states import SubScopeSubLayerState, LobbyState, LobbyStateFlags, SFViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition
from helpers import dependency
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
    from gui.shared.events import NavigationEvent

def registerStates(machine):
    machine.addState(GrinchModeState())
    machine.addState(GrinchBattleResultsState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(GrinchModeState))
    machine.addNavigationTransitionFromParent(machine.getStateByCls(GrinchBattleResultsState))


@SubScopeSubLayerState.parentOf
class GrinchModeState(LobbyState):
    STATE_ID = 'grinchMode'
    __grinchCtrl = dependency.descriptor(IGrinchController)

    def registerStates(self):
        self.addChildState(GrinchHangarState(StateFlags.INITIAL))
        self.addChildState(GrinchInfoState())

    def registerTransitions(self):
        machine = self.getMachine()
        parent = self.getParent()
        hangar = machine.getStateByCls(GrinchHangarState)
        parent.addTransition(HijackTransition(HangarState, WeakMethodProxy(self._isEventPrb)), hangar)
        parent.addNavigationTransition(hangar)
        info = machine.getStateByCls(GrinchInfoState)
        hangar.addNavigationTransition(info, record=True)
        parent.addNavigationTransition(info)

    @classmethod
    def _isEventPrb(cls, _):
        return cls.__grinchCtrl.isEventPrbActive()


@GrinchModeState.parentOf
class GrinchHangarState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD
    VIEW_KEY = ViewKey(VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(GrinchHangarState, self).__init__(flags=flags | LobbyStateFlags.HANGAR)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.grinch_progression.gameBoardView.header.title()))


@GrinchModeState.parentOf
class GrinchInfoState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD_INFO
    VIEW_KEY = ViewKey(VIEW_ALIAS.HOLIDAY_OPS_GAMEBOARD_INFO)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.grinch_progression.infoView.title()))


@SubScopeTopLayerState.parentOf
class GrinchBattleResultsState(GuiImplViewLobbyState):
    STATE_ID = 'grinchBattleResults'
    VIEW_KEY = ViewKey(R.views.grinch.lobby.post_battle.PostBattleView())

    def __init__(self):
        super(GrinchBattleResultsState, self).__init__(PostBattleView, ScopeTemplates.LOBBY_TOP_SUB_SCOPE)

    def registerTransitions(self):
        super(GrinchBattleResultsState, self).registerTransitions()
        self.addNavigationTransition(self, transitionType=TransitionType.EXTERNAL)

    @classmethod
    def goTo(cls, arenaUniqueID=None):
        super(GrinchBattleResultsState, cls).goTo(arenaUniqueID=arenaUniqueID)

    def _getViewLoadCtx(self, event):
        return {'arenaUniqueID': event.params.get('arenaUniqueID')}

    def _focusView(self, view, event):
        super(GrinchBattleResultsState, self)._focusView(view, event)
        arenaUniqueId = event.params.get('arenaUniqueID')
        view.refreshView(arenaUniqueId)