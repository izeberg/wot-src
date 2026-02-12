from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.view.battle.shared import hint_panel
from gui.Scaleform.daapi.view.battle.shared.page import BattlePageBusinessHandler
from gui.Scaleform.framework import ViewSettings, ScopeTemplates, ComponentSettings, getSwfExtensionUrl
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from lunar_possession.gui.Scaleform.genConsts.LUNAR_POSSESSION_BATTLE_VIEW_ALIASES import LUNAR_POSSESSION_BATTLE_VIEW_ALIASES
from lunar_possession.gui.lunar_possession_gui_constants import VIEW_ALIAS

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.component import FunRandomBattleHintPanel
    from gui.Scaleform.daapi.view.battle.shared import consumables_panel
    from gui.Scaleform.daapi.view.battle.shared import situation_indicators
    from gui.Scaleform.daapi.view.battle.shared import messages
    from gui.Scaleform.daapi.view.battle.shared import postmortem_panel
    from gui.Scaleform.daapi.view.battle.classic import battle_end_warning_panel
    from gui.Scaleform.daapi.view.battle.classic import team_bases_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle.page import LunarPossessionBattlePage
    from lunar_possession.gui.Scaleform.daapi.view.battle import minimap
    from lunar_possession.gui.Scaleform.daapi.view.battle import battle_loading
    from lunar_possession.gui.Scaleform.daapi.view.battle import battle_timers
    from lunar_possession.gui.Scaleform.daapi.view.battle import ribbons_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle import timers_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle import damage_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle import damage_log_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle import top_score_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle import players_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle.game_messages_panel import LunarPossessionGameMessagesPanel
    from lunar_possession.gui.Scaleform.daapi.view.battle.status_notifications import panel as sn_panel
    from lunar_possession.gui.Scaleform.daapi.view.battle.ingame_menu import LunarPossessionIngameMenu
    from lunar_possession.gui.impl.battle.battle_page.ammunition_panel import prebattle_ammunition_panel_inject
    return (
     ViewSettings(VIEW_ALIAS.LUNAR_POSSESSION_BATTLE_PAGE, LunarPossessionBattlePage, getSwfExtensionUrl('lunar_possession', 'lunarPossessionBattlePage.swf'), WindowLayer.VIEW, None, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.TEAM_BASES_PANEL, team_bases_panel.TeamBasesPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.MINIMAP, minimap.LunarMinimapComponent, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.BATTLE_LOADING, battle_loading.LunarPossessionBattleLoading, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.DAMAGE_PANEL, damage_panel.LunarPossessionDamagePanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.TIMERS_PANEL, timers_panel.LunarPossessionTimersPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.BATTLE_TIMER, battle_timers.LunarPossessionBattleTimer, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.BATTLE_END_WARNING_PANEL, battle_end_warning_panel.BattleEndWarningPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL, consumables_panel.ConsumablesPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.SITUATION_INDICATORS, situation_indicators.SituationIndicators, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.RIBBONS_PANEL, ribbons_panel.LunarPossessionBattleRibbonsPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.HINT_PANEL, FunRandomBattleHintPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.GAME_MESSAGES_PANEL, LunarPossessionGameMessagesPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.PLAYER_MESSAGES, messages.PlayerMessages, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.POSTMORTEM_PANEL, postmortem_panel.PostmortemPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.PLAYERS_PANEL, players_panel.LunarPlayersPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.PREBATTLE_TIMER, battle_timers.LunarPossessionPreBattleTimer, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL, sn_panel.LunarStatusNotificationTimerPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(LUNAR_POSSESSION_BATTLE_VIEW_ALIASES.LUNAR_POSSESSION_TOP_SCORE_PANEL, top_score_panel.LunarPossessionTopScorePanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.BATTLE_DAMAGE_LOG_PANEL, damage_log_panel.LunarDamageLogPanel, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(BATTLE_VIEW_ALIASES.PREBATTLE_AMMUNITION_PANEL, prebattle_ammunition_panel_inject.LunarPrebattleAmmunitionPanelInject, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.INGAME_MENU, LunarPossessionIngameMenu, 'ingameMenu.swf', WindowLayer.TOP_WINDOW, None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canClose=False, canDrag=False))


def getBusinessHandlers():
    return (
     BattlePageBusinessHandler(VIEW_ALIAS.LUNAR_POSSESSION_BATTLE_PAGE),)