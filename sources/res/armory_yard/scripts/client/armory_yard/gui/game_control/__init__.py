from armory_yard.gui.game_control.armory_yard_controller import ArmoryYardController
from armory_yard.gui.game_control.armory_yard_shop_controller import ArmoryYardShopController
from skeletons.gui.game_control import IArmoryYardController, IArmoryYardShopController
from gui.shared.system_factory import registerGameControllers

def registerAYGameControllers():
    registerGameControllers([
     (
      IArmoryYardController, ArmoryYardController, False)])


def registerAYShopControllers():
    registerGameControllers([
     (
      IArmoryYardShopController, ArmoryYardShopController, False)])