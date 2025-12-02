from gui.shared.system_factory import registerGameControllers
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
from one_time_gift.gui.game_control.one_time_gift_controller import OneTimeGiftController

def registerOneTimeGiftController():
    registerGameControllers([
     (
      IOneTimeGiftController, OneTimeGiftController, False)])