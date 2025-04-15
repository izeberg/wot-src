from gui.shared.system_factory import registerGameControllers
from resource_well.gui.game_control.resource_well_controller import ResourceWellController
from skeletons.gui.resource_well import IResourceWellController

def registerResourceWellController():
    registerGameControllers([
     (
      IResourceWellController, ResourceWellController, True)])