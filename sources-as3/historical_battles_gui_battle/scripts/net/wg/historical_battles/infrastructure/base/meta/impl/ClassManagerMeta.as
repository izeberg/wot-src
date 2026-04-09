package net.wg.historical_battles.infrastructure.base.meta.impl
{
   import net.wg.historical_battles.data.constants.generated.HB_FRONT_NAME;
   import net.wg.historical_battles.data.constants.generated.HB_PHASE_INDICATOR_STATE;
   import net.wg.historical_battles.data.constants.generated.HB_PLAYERS_PANEL_ITEM_STATE;
   import net.wg.historical_battles.data.constants.generated.HB_VEHICLE_CARD_STATE;
   import net.wg.historical_battles.gui.battle.components.HBIconContainer;
   import net.wg.historical_battles.gui.battle.components.HBPlayerRole;
   import net.wg.historical_battles.gui.battle.components.HBVehicleType;
   import net.wg.historical_battles.gui.battle.components.LoadingProgress;
   import net.wg.historical_battles.gui.battle.constants.HB_ENEMY_TYPE;
   import net.wg.historical_battles.gui.battle.constants.HB_EQUIPMENT_STAGES;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.data.BattleLoadingHintVO;
   import net.wg.historical_battles.gui.battle.data.HBAbilitySlotVO;
   import net.wg.historical_battles.gui.battle.views.HBLoading;
   import net.wg.historical_battles.gui.battle.views.battleDamagePanel.HBDamageLogRenderer;
   import net.wg.historical_battles.gui.battle.views.battleHints.HBBattleHint;
   import net.wg.historical_battles.gui.battle.views.battleHints.InfoContainer;
   import net.wg.historical_battles.gui.battle.views.battleHints.TextContainer;
   import net.wg.historical_battles.gui.battle.views.battleHints.data.HintInfoVO;
   import net.wg.historical_battles.gui.battle.views.battlePage.HBBaseBattlePage;
   import net.wg.historical_battles.gui.battle.views.battlePage.HBDefenceBattlePage;
   import net.wg.historical_battles.gui.battle.views.battlePage.HBOffenceBattlePage;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBAbilityButton;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBAbilityButtonGlow;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBConsumablesPanel;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBEquipmentButton;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBEquipmentButtonBase;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBEquipmentButtonGlow;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBGlowBase;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBKeyIndicator;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBPassiveAbility;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBProgressBar;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBRoleAbilityButton;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.HBShellButton;
   import net.wg.historical_battles.gui.battle.views.consumablesPanel.events.HBProgressBarEvent;
   import net.wg.historical_battles.gui.battle.views.destroyTimers.HBDestroySecTimer;
   import net.wg.historical_battles.gui.battle.views.destroyTimers.HBDestroyTimer;
   import net.wg.historical_battles.gui.battle.views.destroyTimers.HBStatusNotificationPanel;
   import net.wg.historical_battles.gui.battle.views.destroyTimers.components.HBTextFieldContainer;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.HBEnemiesCounter;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.HBEnemiesList;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.HBEnemiesPanel;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.HBEnemyAnimHelper;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.HBEnemyGlow;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.HBEnemyRenderer;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.VO.HBEnemyInfoVO;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.HBGameMessagesPanel;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.HBEndGameMessage;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.HBEndGameMessageTextfields;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.HBEndGameMessageVictory;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.HBVictoryFlare;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.ObjectiveGameMessage;
   import net.wg.historical_battles.gui.battle.views.messenger.HBBattleMessenger;
   import net.wg.historical_battles.gui.battle.views.minimap.HBMinimap;
   import net.wg.historical_battles.gui.battle.views.minimap.components.MapSectors;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.ArtilleryAOEMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.ArtilleryMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.ArtilleryOnYourselfMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.AttackPlaneMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.BomberMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.HBAirstrikeMarkerMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.HBArrowContainer;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.HBArrowMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.HBCustomMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.HBKeyTargetMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.HbMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.MineMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.ReconMinimapEntry;
   import net.wg.historical_battles.gui.battle.views.phaseIndicator.HBPhaseIndicator;
   import net.wg.historical_battles.gui.battle.views.phaseIndicator.data.HBPhaseIndicatorVO;
   import net.wg.historical_battles.gui.battle.views.playersPanel.HBPlayerRenderer;
   import net.wg.historical_battles.gui.battle.views.playersPanel.HBPlayersList;
   import net.wg.historical_battles.gui.battle.views.playersPanel.HBPlayersPanel;
   import net.wg.historical_battles.gui.battle.views.playersPanel.VO.HBPlayerInfoVO;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.HBChatCommandItemComponent;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.HBDynamicSquad;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.HBLiveCounter;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.HBPlayerName;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.HBRespawnTimer;
   import net.wg.historical_battles.gui.battle.views.playersPanel.events.HBPlayerListEvent;
   import net.wg.historical_battles.gui.battle.views.playersPanel.events.HBPlayerRendererEvent;
   import net.wg.historical_battles.gui.battle.views.postmortemPanel.HBPostmortemPanel;
   import net.wg.historical_battles.gui.battle.views.postmortemPanel.HBPostmortemTimer;
   import net.wg.historical_battles.gui.battle.views.postmortemPanel.HBPostmortemTimerContainer;
   import net.wg.historical_battles.gui.battle.views.postmortemPanel.HBPostmortemVehiclePanel;
   import net.wg.historical_battles.gui.battle.views.radialMenu.components.HBIcons;
   import net.wg.historical_battles.gui.battle.views.respawn.HBRespawn;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBDivision;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBLine;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBTextBase;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBTimerResp;
   import net.wg.historical_battles.gui.battle.views.respawn.components.card.HBVehicleCard;
   import net.wg.historical_battles.gui.battle.views.respawn.components.card.HBVehicleContainer;
   import net.wg.historical_battles.gui.battle.views.respawn.components.card.HBVehicleImage;
   import net.wg.historical_battles.gui.battle.views.respawn.components.card.HBVehicleName;
   import net.wg.historical_battles.gui.battle.views.respawn.components.card.HBVehicleState;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_DIVISION_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_RESPAWN_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_TIMER_RESP_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_VEHICLE_CARD_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBDivisionVO;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBRespawnVO;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBTimerRespVO;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBVehicleCardVO;
   import net.wg.historical_battles.gui.battle.views.respawn.events.HBRespawnEvent;
   import net.wg.historical_battles.gui.battle.views.respawn.events.HBVehicleCardEvent;
   import net.wg.historical_battles.gui.battle.views.ribbonsPanel.HBRibbonSettings;
   import net.wg.historical_battles.gui.battle.views.ribbonsPanel.HBRibbonsPanel;
   import net.wg.historical_battles.gui.battle.views.ribbonsPanel.HBRibbonsPool;
   import net.wg.historical_battles.gui.battle.views.spgPanel.HBSPGPanel;
   import net.wg.historical_battles.gui.battle.views.spgPanel.HBSPGRenderer;
   import net.wg.historical_battles.gui.battle.views.spgPanel.VO.HBSPGInfoVO;
   import net.wg.historical_battles.gui.battle.views.spgPanel.events.HBSPGPanelEvent;
   import net.wg.historical_battles.gui.battle.views.staticMarkers.controlPoint.HBLocationActionMarker;
   import net.wg.historical_battles.gui.battle.views.stats.HBStatsWidget;
   import net.wg.historical_battles.gui.battle.views.timer.HBTimer;
   import net.wg.historical_battles.gui.battle.views.timer.controls.TimerGoalText;
   import net.wg.historical_battles.gui.battle.views.timer.controls.TimerMessage;
   import net.wg.historical_battles.gui.battle.views.timer.controls.TimerMovie;
   import net.wg.historical_battles.gui.battle.views.timer.controls.TimerTask;
   import net.wg.historical_battles.gui.battle.views.timer.controls.TimerTaskBar;
   import net.wg.historical_battles.gui.battle.views.timer.controls.TimerText;
   import net.wg.historical_battles.gui.battle.views.vehicleMarkers.HBVehicleActionMarker;
   import net.wg.historical_battles.gui.battle.views.vehicleMarkers.HBVehicleMarker;
   import net.wg.historical_battles.gui.battle.views.vehicleMarkers.HBVehicleMarkerBase;
   
   public class ClassManagerMeta
   {
      
      public static const NET_WG_HISTORICAL_BATTLES_DATA_CONSTANTS_GENERATED_HB_FRONT_NAME:Class = HB_FRONT_NAME;
      
      public static const NET_WG_HISTORICAL_BATTLES_DATA_CONSTANTS_GENERATED_HB_PHASE_INDICATOR_STATE:Class = HB_PHASE_INDICATOR_STATE;
      
      public static const NET_WG_HISTORICAL_BATTLES_DATA_CONSTANTS_GENERATED_HB_PLAYERS_PANEL_ITEM_STATE:Class = HB_PLAYERS_PANEL_ITEM_STATE;
      
      public static const NET_WG_HISTORICAL_BATTLES_DATA_CONSTANTS_GENERATED_HB_VEHICLE_CARD_STATE:Class = HB_VEHICLE_CARD_STATE;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_COMPONENTS_HBICONCONTAINER:Class = HBIconContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_COMPONENTS_HBPLAYERROLE:Class = HBPlayerRole;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_COMPONENTS_HBVEHICLETYPE:Class = HBVehicleType;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_COMPONENTS_LOADINGPROGRESS:Class = LoadingProgress;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_CONSTANTS_HB_ENEMY_TYPE:Class = HB_ENEMY_TYPE;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_CONSTANTS_HB_EQUIPMENT_STAGES:Class = HB_EQUIPMENT_STAGES;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_CONSTANTS_HB_STAGE_SIZE:Class = HB_STAGE_SIZE;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_DATA_BATTLELOADINGHINTVO:Class = BattleLoadingHintVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_DATA_HBABILITYSLOTVO:Class = HBAbilitySlotVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_HBLOADING:Class = HBLoading;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEDAMAGEPANEL_HBDAMAGELOGRENDERER:Class = HBDamageLogRenderer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEHINTS_HBBATTLEHINT:Class = HBBattleHint;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEHINTS_INFOCONTAINER:Class = InfoContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEHINTS_TEXTCONTAINER:Class = TextContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEHINTS_DATA_HINTINFOVO:Class = HintInfoVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEPAGE_HBBASEBATTLEPAGE:Class = HBBaseBattlePage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEPAGE_HBDEFENCEBATTLEPAGE:Class = HBDefenceBattlePage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_BATTLEPAGE_HBOFFENCEBATTLEPAGE:Class = HBOffenceBattlePage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBABILITYBUTTON:Class = HBAbilityButton;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBABILITYBUTTONGLOW:Class = HBAbilityButtonGlow;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBCONSUMABLESPANEL:Class = HBConsumablesPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBEQUIPMENTBUTTON:Class = HBEquipmentButton;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBEQUIPMENTBUTTONBASE:Class = HBEquipmentButtonBase;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBEQUIPMENTBUTTONGLOW:Class = HBEquipmentButtonGlow;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBGLOWBASE:Class = HBGlowBase;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBKEYINDICATOR:Class = HBKeyIndicator;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBPASSIVEABILITY:Class = HBPassiveAbility;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBPROGRESSBAR:Class = HBProgressBar;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBROLEABILITYBUTTON:Class = HBRoleAbilityButton;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_HBSHELLBUTTON:Class = HBShellButton;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_EVENTS_HBPROGRESSBAREVENT:Class = HBProgressBarEvent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_DESTROYTIMERS_HBDESTROYSECTIMER:Class = HBDestroySecTimer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_DESTROYTIMERS_HBDESTROYTIMER:Class = HBDestroyTimer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_DESTROYTIMERS_HBSTATUSNOTIFICATIONPANEL:Class = HBStatusNotificationPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_DESTROYTIMERS_COMPONENTS_HBTEXTFIELDCONTAINER:Class = HBTextFieldContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_HBENEMIESCOUNTER:Class = HBEnemiesCounter;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_HBENEMIESLIST:Class = HBEnemiesList;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_HBENEMIESPANEL:Class = HBEnemiesPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_HBENEMYANIMHELPER:Class = HBEnemyAnimHelper;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_HBENEMYGLOW:Class = HBEnemyGlow;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_HBENEMYRENDERER:Class = HBEnemyRenderer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_ENEMIESPANEL_VO_HBENEMYINFOVO:Class = HBEnemyInfoVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_GAMEMESSAGESPANEL_HBGAMEMESSAGESPANEL:Class = HBGameMessagesPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_GAMEMESSAGESPANEL_COMPONENTS_HBENDGAMEMESSAGE:Class = HBEndGameMessage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_GAMEMESSAGESPANEL_COMPONENTS_HBENDGAMEMESSAGETEXTFIELDS:Class = HBEndGameMessageTextfields;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_GAMEMESSAGESPANEL_COMPONENTS_HBENDGAMEMESSAGEVICTORY:Class = HBEndGameMessageVictory;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_GAMEMESSAGESPANEL_COMPONENTS_HBVICTORYFLARE:Class = HBVictoryFlare;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_GAMEMESSAGESPANEL_COMPONENTS_OBJECTIVEGAMEMESSAGE:Class = ObjectiveGameMessage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MESSENGER_HBBATTLEMESSENGER:Class = HBBattleMessenger;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_HBMINIMAP:Class = HBMinimap;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_MAPSECTORS:Class = MapSectors;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_ARTILLERYAOEMINIMAPENTRY:Class = ArtilleryAOEMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_ARTILLERYMINIMAPENTRY:Class = ArtilleryMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_ARTILLERYONYOURSELFMINIMAPENTRY:Class = ArtilleryOnYourselfMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_ATTACKPLANEMINIMAPENTRY:Class = AttackPlaneMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_BOMBERMINIMAPENTRY:Class = BomberMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_HBAIRSTRIKEMARKERMINIMAPENTRY:Class = HBAirstrikeMarkerMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_HBARROWCONTAINER:Class = HBArrowContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_HBARROWMINIMAPENTRY:Class = HBArrowMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_HBCUSTOMMINIMAPENTRY:Class = HBCustomMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_HBKEYTARGETMINIMAPENTRY:Class = HBKeyTargetMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_HBMINIMAPENTRY:Class = HbMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_MINEMINIMAPENTRY:Class = MineMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_RECONMINIMAPENTRY:Class = ReconMinimapEntry;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PHASEINDICATOR_HBPHASEINDICATOR:Class = HBPhaseIndicator;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PHASEINDICATOR_DATA_HBPHASEINDICATORVO:Class = HBPhaseIndicatorVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_HBPLAYERRENDERER:Class = HBPlayerRenderer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_HBPLAYERSLIST:Class = HBPlayersList;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_HBPLAYERSPANEL:Class = HBPlayersPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HBCHATCOMMANDITEMCOMPONENT:Class = HBChatCommandItemComponent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HBDYNAMICSQUAD:Class = HBDynamicSquad;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HBLIVECOUNTER:Class = HBLiveCounter;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HBPLAYERNAME:Class = HBPlayerName;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HBRESPAWNTIMER:Class = HBRespawnTimer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_EVENTS_HBPLAYERLISTEVENT:Class = HBPlayerListEvent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_EVENTS_HBPLAYERRENDEREREVENT:Class = HBPlayerRendererEvent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_PLAYERSPANEL_VO_HBPLAYERINFOVO:Class = HBPlayerInfoVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_POSTMORTEMPANEL_HBPOSTMORTEMPANEL:Class = HBPostmortemPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_POSTMORTEMPANEL_HBPOSTMORTEMTIMER:Class = HBPostmortemTimer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_POSTMORTEMPANEL_HBPOSTMORTEMTIMERCONTAINER:Class = HBPostmortemTimerContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_POSTMORTEMPANEL_HBPOSTMORTEMVEHICLEPANEL:Class = HBPostmortemVehiclePanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RADIALMENU_COMPONENTS_HBICONS:Class = HBIcons;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_HBRESPAWN:Class = HBRespawn;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_HBDIVISION:Class = HBDivision;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_HBLINE:Class = HBLine;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_HBTEXTBASE:Class = HBTextBase;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_HBTIMERRESP:Class = HBTimerResp;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_CARD_HBVEHICLECARD:Class = HBVehicleCard;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_CARD_HBVEHICLECONTAINER:Class = HBVehicleContainer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_CARD_HBVEHICLEIMAGE:Class = HBVehicleImage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_CARD_HBVEHICLENAME:Class = HBVehicleName;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_COMPONENTS_CARD_HBVEHICLESTATE:Class = HBVehicleState;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_CONSTANTS_HB_DIVISION_PROPS:Class = HB_DIVISION_PROPS;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_CONSTANTS_HB_RESPAWN_PROPS:Class = HB_RESPAWN_PROPS;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_CONSTANTS_HB_TIMER_RESP_PROPS:Class = HB_TIMER_RESP_PROPS;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_CONSTANTS_HB_VEHICLE_CARD_PROPS:Class = HB_VEHICLE_CARD_PROPS;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_DATA_HBDIVISIONVO:Class = HBDivisionVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_DATA_HBRESPAWNVO:Class = HBRespawnVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_DATA_HBTIMERRESPVO:Class = HBTimerRespVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_DATA_HBVEHICLECARDVO:Class = HBVehicleCardVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_EVENTS_HBRESPAWNEVENT:Class = HBRespawnEvent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RESPAWN_EVENTS_HBVEHICLECARDEVENT:Class = HBVehicleCardEvent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RIBBONSPANEL_HBRIBBONSETTINGS:Class = HBRibbonSettings;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RIBBONSPANEL_HBRIBBONSPANEL:Class = HBRibbonsPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_RIBBONSPANEL_HBRIBBONSPOOL:Class = HBRibbonsPool;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_SPGPANEL_HBSPGPANEL:Class = HBSPGPanel;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_SPGPANEL_HBSPGRENDERER:Class = HBSPGRenderer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_SPGPANEL_EVENTS_HBSPGPANELEVENT:Class = HBSPGPanelEvent;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_SPGPANEL_VO_HBSPGINFOVO:Class = HBSPGInfoVO;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_STATICMARKERS_CONTROLPOINT_HBLOCATIONACTIONMARKER:Class = HBLocationActionMarker;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_STATS_HBSTATSWIDGET:Class = HBStatsWidget;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_HBTIMER:Class = HBTimer;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_CONTROLS_TIMERGOALTEXT:Class = TimerGoalText;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_CONTROLS_TIMERMESSAGE:Class = TimerMessage;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_CONTROLS_TIMERMOVIE:Class = TimerMovie;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_CONTROLS_TIMERTASK:Class = TimerTask;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_CONTROLS_TIMERTASKBAR:Class = TimerTaskBar;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_TIMER_CONTROLS_TIMERTEXT:Class = TimerText;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_VEHICLEMARKERS_HBVEHICLEACTIONMARKER:Class = HBVehicleActionMarker;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_VEHICLEMARKERS_HBVEHICLEMARKER:Class = HBVehicleMarker;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_VEHICLEMARKERS_HBVEHICLEMARKERBASE:Class = HBVehicleMarkerBase;
       
      
      public function ClassManagerMeta()
      {
         super();
      }
   }
}
