from battle_royale.gui.game_control.battle_royale_controller import BattleRoyaleController as _BattleRoyale
from battle_royale.gui.game_control.battle_royale_tournament_controller import BattleRoyaleTournamentController as _BRTournament
import skeletons.gui.game_control as _interface
from gui.shared.system_factory import registerGameControllers

def registerBRGameControllers():
    registerGameControllers([
     (
      _interface.IBattleRoyaleController, _BattleRoyale, False),
     (
      _interface.IBattleRoyaleTournamentController, _BRTournament, False)])