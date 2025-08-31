from comp7_core.arena_components.comp7_core_equipment_component import Comp7CoreEquipmentComponent, _AoeHealEffect
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class _Comp7LightAoeHealEffect(_AoeHealEffect):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController


class Comp7LightEquipmentComponent(Comp7CoreEquipmentComponent):
    _AOE_HEAL_EFFECT = _Comp7LightAoeHealEffect