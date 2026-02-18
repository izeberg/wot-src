import typing
from fun_random.gui.feature.sub_modes.base_sub_mode import FunBaseSubMode
from gui.impl.gen.view_models.views.lobby.battle_results.efficiency_param_constants import EfficiencyParamConstants
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME
EFFICIENCY_PARAMS = (
 EfficiencyParamConstants.KILLS, EfficiencyParamConstants.DAMAGE_DEALT,
 'spiritPoints')

class LunarPossessionSubMode(FunBaseSubMode):
    __slots__ = ()

    def getEfficiencyParameters(self):
        _PARAMETERS = {VEHICLE_CLASS_NAME.AT_SPG: EFFICIENCY_PARAMS, 
           VEHICLE_CLASS_NAME.HEAVY_TANK: EFFICIENCY_PARAMS, 
           VEHICLE_CLASS_NAME.MEDIUM_TANK: EFFICIENCY_PARAMS, 
           VEHICLE_CLASS_NAME.LIGHT_TANK: EFFICIENCY_PARAMS}
        return _PARAMETERS

    def getAssetsPointer(self):
        return 'undefined'

    def canEnqueueVehicle(self, callback=None):
        pass

    def isSquadAvailable(self):
        return False