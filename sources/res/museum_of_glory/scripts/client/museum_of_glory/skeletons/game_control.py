import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from museum_of_glory.gui.game_control.museum_of_glory_controller import VehicleDto

class IMuseumOfGloryController(IGameController):
    onConfigUpdate = None

    @property
    def isEnabled(self):
        raise NotImplementedError

    def getEpochMusics(self, year):
        raise NotImplementedError

    def getVehiclesDto(self):
        raise NotImplementedError

    def getBackgroundImage(self, year):
        raise NotImplementedError

    def getMinYear(self):
        raise NotImplementedError