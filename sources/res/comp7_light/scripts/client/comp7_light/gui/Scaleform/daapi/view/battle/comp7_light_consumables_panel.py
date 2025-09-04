from comp7_core.gui.Scaleform.daapi.view.battle.consumables_panel import Comp7CoreConsumablesPanel
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightConsumablesPanel(Comp7CoreConsumablesPanel):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController