from comp7_core.gui.impl.lobby.hangar.presenters.comp7_core_vehicles_info_presenter import Comp7CoreVehiclesInfoPresenter
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightVehiclesInfoPresenter(Comp7CoreVehiclesInfoPresenter):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController