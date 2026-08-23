import typing
if typing.TYPE_CHECKING:
    from dependency_injection_container import DependencyManager

def registerSkeletons(manager):
    from skeletons.gui.game_control import IMuseumOfGloryController
    from museum_of_glory.gui.game_control.museum_of_glory_controller import MuseumOfGloryController
    manager.addInstance(IMuseumOfGloryController, MuseumOfGloryController())


def registerMuseumOfGloryPersonality():
    from gui.shared.system_factory import registerGameControllers
    from skeletons.gui.game_control import IMuseumOfGloryController
    from museum_of_glory.gui.game_control.museum_of_glory_controller import MuseumOfGloryController
    registerGameControllers([
     (
      IMuseumOfGloryController, MuseumOfGloryController, True)])