from comp7_core.gui.Scaleform.daapi.view.battle.consumables_panel import Comp7CoreConsumablesPanel
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7ConsumablesPanel(Comp7CoreConsumablesPanel):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @property
    def _modeController(self):
        return self.__comp7Controller