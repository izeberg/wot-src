from gui.shared.system_factory import registerGameControllers
from open_bundle.gui.game_control.open_bundle_controller import OpenBundleController
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController

def registerOpenBundleController():
    registerGameControllers([
     (
      IOpenBundleController, OpenBundleController, False)])