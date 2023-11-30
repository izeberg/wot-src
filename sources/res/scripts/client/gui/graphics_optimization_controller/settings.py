from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.Scaleform.genConsts.GRAPHICS_OPTIMIZATION_ALIASES import GRAPHICS_OPTIMIZATION_ALIASES
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.graphics_optimization_controller.utils import OptimizationSetting
from gui.impl.gen import R
OPTIMIZED_VIEWS_SETTINGS = {VIEW_ALIAS.LOBBY_HEADER: OptimizationSetting(), 
   VIEW_ALIAS.LOBBY_TECHTREE: OptimizationSetting(), 
   VIEW_ALIAS.LOBBY_RESEARCH: OptimizationSetting(), 
   HANGAR_ALIASES.TANK_CAROUSEL: OptimizationSetting(), 
   HANGAR_ALIASES.RANKED_TANK_CAROUSEL: OptimizationSetting(), 
   HANGAR_ALIASES.BATTLEPASS_TANK_CAROUSEL: OptimizationSetting(), 
   HANGAR_ALIASES.ROYALE_TANK_CAROUSEL: OptimizationSetting(), 
   HANGAR_ALIASES.MAPBOX_TANK_CAROUSEL: OptimizationSetting(), 
   HANGAR_ALIASES.FUN_RANDOM_TANK_CAROUSEL: OptimizationSetting(), 
   HANGAR_ALIASES.COMP7_TANK_CAROUSEL: OptimizationSetting(), 
   GRAPHICS_OPTIMIZATION_ALIASES.CUSTOMISATION_BOTTOM_PANEL: OptimizationSetting(), 
   BATTLE_VIEW_ALIASES.MINIMAP: OptimizationSetting('minimapAlphaEnabled', True), 
   BATTLE_VIEW_ALIASES.DAMAGE_PANEL: OptimizationSetting(), 
   R.views.lobby.advent_calendar.MainView(): OptimizationSetting()}