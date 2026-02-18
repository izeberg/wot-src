from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.classic.page import DynamicAliases, ClassicPage
from gui.Scaleform.daapi.view.battle.shared import drone_music_player
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.shared.indicators import createPredictionIndicator, createDamageIndicator
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from helpers import dependency
from lunar_possession.gui.Scaleform.daapi.view.battle.markers2d import LunarPossessionMarkersManager
from lunar_possession.gui.lunar_possession_gui_constants import BATTLE_CTRL_ID
from skeletons.gui.impl import IGuiLoader

class _ComponentsConfig(ComponentsConfig):

    def __init__(self):
        super(_ComponentsConfig, self).__init__((
         (
          BATTLE_CTRL_ID.ARENA_PERIOD,
          (
           BATTLE_VIEW_ALIASES.BATTLE_TIMER,
           BATTLE_VIEW_ALIASES.PREBATTLE_TIMER,
           DynamicAliases.PREBATTLE_TIMER_SOUND_PLAYER,
           BATTLE_VIEW_ALIASES.PLAYERS_PANEL,
           BATTLE_VIEW_ALIASES.HINT_PANEL,
           DynamicAliases.DRONE_MUSIC_PLAYER)),
         (
          BATTLE_CTRL_ID.PERKS, (BATTLE_VIEW_ALIASES.EVENT_BUFFS_PANEL,)),
         (
          BATTLE_CTRL_ID.TEAM_BASES,
          (
           BATTLE_VIEW_ALIASES.TEAM_BASES_PANEL,
           DynamicAliases.DRONE_MUSIC_PLAYER)),
         (
          BATTLE_CTRL_ID.CALLOUT, (BATTLE_VIEW_ALIASES.CALLOUT_PANEL,)),
         (
          BATTLE_CTRL_ID.MAPS, (BATTLE_VIEW_ALIASES.MINIMAP,)),
         (
          BATTLE_CTRL_ID.DEBUG, (BATTLE_VIEW_ALIASES.DEBUG_PANEL,)),
         (
          BATTLE_CTRL_ID.BATTLE_FIELD_CTRL,
          (
           DynamicAliases.DRONE_MUSIC_PLAYER,
           BATTLE_VIEW_ALIASES.PLAYERS_PANEL)),
         (
          BATTLE_CTRL_ID.ARENA_LOAD_PROGRESS, (DynamicAliases.DRONE_MUSIC_PLAYER,)),
         (
          BATTLE_CTRL_ID.GAME_MESSAGES_PANEL, (BATTLE_VIEW_ALIASES.GAME_MESSAGES_PANEL,)),
         (
          BATTLE_CTRL_ID.PREBATTLE_SETUPS_CTRL,
          (
           BATTLE_VIEW_ALIASES.PREBATTLE_AMMUNITION_PANEL, BATTLE_VIEW_ALIASES.DAMAGE_PANEL)),
         (
          BATTLE_CTRL_ID.AMMO,
          (
           BATTLE_VIEW_ALIASES.PREBATTLE_AMMUNITION_PANEL, BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL)),
         (
          BATTLE_CTRL_ID.HIT_DIRECTION,
          (
           BATTLE_VIEW_ALIASES.PREDICTION_INDICATOR, BATTLE_VIEW_ALIASES.HIT_DIRECTION)),
         (
          BATTLE_CTRL_ID.BATTLE_HINTS,
          (
           BATTLE_VIEW_ALIASES.BATTLE_HINT,
           BATTLE_VIEW_ALIASES.HINT_PANEL)),
         (
          BATTLE_CTRL_ID.LUNAR_POSSESSION_BATTLE_CTRL,
          (
           BATTLE_VIEW_ALIASES.PLAYERS_PANEL,))), viewsConfig=(
         (
          DynamicAliases.DRONE_MUSIC_PLAYER, drone_music_player.DroneMusicPlayer),
         (
          DynamicAliases.PREBATTLE_TIMER_SOUND_PLAYER, StartCountdownSoundPlayer),
         (
          BATTLE_VIEW_ALIASES.PREDICTION_INDICATOR, createPredictionIndicator),
         (
          BATTLE_VIEW_ALIASES.HIT_DIRECTION, createDamageIndicator)))


_EXTERNAL_COMPONENTS = (
 LunarPossessionMarkersManager,
 CrosshairPanelContainer)
_CONFIG = _ComponentsConfig()

class LunarPossessionBattlePageMeta(ClassicPage):
    pass


class LunarPossessionBattlePage(LunarPossessionBattlePageMeta):
    CONFIG = _CONFIG

    def __init__(self, components=None, external=_EXTERNAL_COMPONENTS, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS):
        if components is None:
            components = self.CONFIG
        self.__guiLoader = dependency.instance(IGuiLoader)
        self.__fullStatsIsShown = False
        super(LunarPossessionBattlePage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        return

    def _populate(self):
        super(LunarPossessionBattlePage, self)._populate()
        LOG_DEBUG('-=>> Lunar battle page is created.')

    def _dispose(self):
        super(LunarPossessionBattlePage, self)._dispose()
        LOG_DEBUG('-=>> Lunar battle page is destroyed.')