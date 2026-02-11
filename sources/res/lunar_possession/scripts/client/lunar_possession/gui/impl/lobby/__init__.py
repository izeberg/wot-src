from fun_random.gui.shared.fun_system_factory import registerFunHangarComponent
from gui.impl.gen import R
from lunar_constants import FunSubModeImpl
from lunar_possession.gui.impl.lobby.lunar_possession_crew_presenter import LunarPossessionCrewPresenter
from lunar_possession.gui.impl.lobby.lunar_possession_loadout_presenter import LunarPossessionLoadoutPresenter

def registerFunRandomHangarComponentsConfig():
    hangar = R.aliases.hangar.shared
    registerFunHangarComponent(FunSubModeImpl.LUNAR_POSSESSION, hangar.Loadout(), LunarPossessionLoadoutPresenter)
    registerFunHangarComponent(FunSubModeImpl.LUNAR_POSSESSION, hangar.Crew(), LunarPossessionCrewPresenter)