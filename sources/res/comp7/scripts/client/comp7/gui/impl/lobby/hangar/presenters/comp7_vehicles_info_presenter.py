from comp7_core.gui.impl.lobby.hangar.presenters.comp7_core_vehicles_info_presenter import Comp7CoreVehiclesInfoPresenter
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7VehiclesInfoPresenter(Comp7CoreVehiclesInfoPresenter):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @property
    def _modeController(self):
        return self.__comp7Controller