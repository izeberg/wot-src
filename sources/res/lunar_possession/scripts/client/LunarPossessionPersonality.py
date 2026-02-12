import lunar_constants
from AvatarInputHandler import OVERWRITE_CTRLS_DESC_MAP, _CTRL_MODE, _CTRL_TYPE
from constants import ARENA_BONUS_TYPE
from debug_utils import LOG_DEBUG
from gui.battle_results.reusable import ReusableInfoFactory
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig
from gui.prb_control.prb_utils import initScaleformGuiTypes, initBattleCtrlIDs
from lunar_possession.AvatarInpitHandler.control_modes import LunarPossessionPostMortemCtrlMode
from lunar_possession.gui import lunar_possession_gui_constants
from lunar_possession.gui.battle_control import registerLunarPossessionBattle
from lunar_possession.gui.battle_results import registerLunarPossessionBattleResults
from lunar_possession.gui.fun_random.sub_modes import registerLunarPossessionSubModes
from lunar_possession.gui.hangar_presets import registerHangarPresetConfig
from lunar_possession.gui.impl.lobby import registerFunRandomHangarComponentsConfig
from lunar_possession.messenger.formatters import registerLunarPossessionFormatters
from lunar_possession_common.lunar_possession_battle_mode import LunarPossessionBattleMode

class ClientLunarPossessionBattleMode(LunarPossessionBattleMode):
    _CLIENT_BATTLE_PAGE = lunar_possession_gui_constants.VIEW_ALIAS.LUNAR_POSSESSION_BATTLE_PAGE

    @property
    def _client_arenaDescrClass(self):
        from lunar_possession.gui.battle_control.arena_info.arena_descrs import LunarPossessionArenaDescription
        return LunarPossessionArenaDescription

    @property
    def _client_canSelectPrbEntity(self):
        return True

    @property
    def _client_battleControllersRepository(self):
        from lunar_possession.gui.battle_control.repository import LunarPossessionControllersRepository
        return LunarPossessionControllersRepository

    @property
    def _client_battleRequiredLibraries(self):
        return ['lunar_possession|lunar_possession_battle.swf']

    @property
    def _client_battleResultsReusables(self):
        from lunar_possession.gui.battle_results.reusable.lunar_possession_shared import LunarPossessionVehicleDetailedInfo, LunarPossessionVehicleSummarizeInfo
        return {ReusableInfoFactory.Keys.VEHICLE_DETAILED: LunarPossessionVehicleDetailedInfo, 
           ReusableInfoFactory.Keys.VEHICLE_SUMMARIZED: LunarPossessionVehicleSummarizeInfo}

    @property
    def _client_controlModes(self):
        from lunar_possession.AvatarInpitHandler import LUNAR_POSSESSION_CTRLS_DESC_MAP
        return LUNAR_POSSESSION_CTRLS_DESC_MAP

    @property
    def _client_sharedControllersRepository(self):
        from lunar_possession.gui.battle_control.repository import LunarPossessionSharedControllersRepository
        return LunarPossessionSharedControllersRepository


def preInit():
    LOG_DEBUG('preInit personality:', __name__)
    lunar_constants.injectConsts(__name__)
    initBattleCtrlIDs(lunar_possession_gui_constants, __name__)
    initScaleformGuiTypes(lunar_possession_gui_constants, __name__)
    battleMode = ClientLunarPossessionBattleMode(__name__)
    battleMode.registerGuiType()
    battleMode.registerControlModes()
    battleMode.registerBattleResultsConfig()
    battleMode.registerClientArenaInfoKeys()
    battleMode.registerSharedControllersRepository()
    battleMode.registerBattleControllersRepository()
    battleMode.registerScaleformRequiredLibraries()
    battleMode.registerClientBattleResultReusabled()
    battleMode.registerMessengerServerFormatters()
    battleMode.registerClientEquipmentItems()
    battleMode.registerMessengerClientFormatters(lunar_possession_gui_constants)
    battleMode.registerNonReplayMode()
    registerHangarPresetConfig()
    registerLunarPossessionFormatters()
    registerLunarPossessionSubModes()
    registerLunarPossessionBattle(__name__)
    registerLunarPossessionBattleResults()
    registerFunRandomHangarComponentsConfig()


def init():
    g_overrideScaleFormViewsConfig.initExtensionBattlePackages(__name__, [
     'lunar_possession.gui.Scaleform.daapi.view.battle'], lunar_constants.ARENA_GUI_TYPE.LUNAR_POSSESSION)
    OVERWRITE_CTRLS_DESC_MAP[ARENA_BONUS_TYPE.FUN_RANDOM] = {_CTRL_MODE.POSTMORTEM: (
                             LunarPossessionPostMortemCtrlMode, 'postMortemMode', _CTRL_TYPE.USUAL)}


def start():
    pass


def fini():
    pass