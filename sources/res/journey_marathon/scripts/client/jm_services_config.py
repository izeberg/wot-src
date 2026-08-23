from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.game_control.state_tracker import GameStateTracker
    from helpers.dependency import DependencyManager

def updateServicesConfig(manager):
    from journey_marathon.gui.game_control.jm_controller import JourneyMarathonController
    from journey_marathon.skeletons.game_control import IJourneyMarathonController
    from skeletons.gui.game_control import IGameStateTracker
    controller = JourneyMarathonController()
    tracker = manager.getService(IGameStateTracker)
    tracker.addController(controller)
    manager.addInstance(IJourneyMarathonController, controller)
    controller.init()