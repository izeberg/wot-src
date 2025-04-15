from fun_random.gui.feature.sub_modes.base_sub_mode import FunBaseSubMode
from fall_tanks.gui.impl.lobby.fall_tanks_ammunition_setup import FallTanksAmmunitionSetupView

class FallTanksSubMode(FunBaseSubMode):
    __slots__ = ()

    def getAmmoSetupViewAlias(self):
        return FallTanksAmmunitionSetupView.__name__