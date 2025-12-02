from __future__ import absolute_import
from fun_random.gui.battle_control.controllers.sound_ctrls.fun_random_battle_sounds import createFunRandomBattleSoundsController
from gui.battle_control.controllers.repositories import ClassicControllersRepository

class FunRandomControllerRepository(ClassicControllersRepository):
    __slots__ = ()

    @staticmethod
    def _getSoundController(setup):
        return createFunRandomBattleSoundsController(setup)