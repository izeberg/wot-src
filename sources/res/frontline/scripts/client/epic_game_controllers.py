from frontline.battle_controller import EpicBattleController
from gui.shared.system_factory import registerGameControllers
from skeletons.gui.game_control import IEpicBattleController

def register():
    registerGameControllers([
     (
      IEpicBattleController, EpicBattleController, False)])