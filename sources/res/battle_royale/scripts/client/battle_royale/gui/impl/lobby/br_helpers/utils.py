from gui.Scaleform.lobby_entry import getLobbyStateMachine
from battle_royale.gui.impl.lobby.views.states import BattleRoyaleBattleResultsState

def isBattleResultsStateEntered():
    state = getLobbyStateMachine().getStateByCls(BattleRoyaleBattleResultsState)
    return state and state.isEntered()