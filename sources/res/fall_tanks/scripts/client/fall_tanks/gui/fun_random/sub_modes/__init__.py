from __future__ import absolute_import
from fun_random.gui.shared.fun_system_factory import registerFunRandomSubMode
from fall_tanks_constants import FunSubModeImpl
from fall_tanks.gui.fun_random.sub_modes.fall_tanks_sub_mode import FallTanksSubMode

def registerFallTanksSubModes():
    registerFunRandomSubMode(FunSubModeImpl.FALL_TANKS, FallTanksSubMode)