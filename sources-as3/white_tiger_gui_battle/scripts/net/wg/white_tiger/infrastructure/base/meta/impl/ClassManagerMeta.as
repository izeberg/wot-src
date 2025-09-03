package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.white_tiger.data.constants.WhiteTigerSoundTypes;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_EFFICIENCY_TYPES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_VIEW_ALIASES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_CONSUMABLES_PANEL_TAGS;
   import net.wg.white_tiger.data.constants.generated.WT_BATTLE_NOTIFICATIONS_TIMER_LINKAGES;
   import net.wg.white_tiger.data.constants.generated.WT_BATTLE_NOTIFICATIONS_TIMER_TYPES;
   import net.wg.white_tiger.gui.battle.VO.DAAPIHunterVehicleInfoVO;
   import net.wg.white_tiger.gui.battle.VO.DAAPIHunterVehiclesDataVO;
   import net.wg.white_tiger.gui.battle.VO.DAAPIWhiteTigerBossBotInfoVO;
   import net.wg.white_tiger.gui.battle.VO.WhiteTigerBattleHintVO;
   import net.wg.white_tiger.gui.battle.WhiteTigerBattlePage;
   import net.wg.white_tiger.gui.battle.WhiteTigerBattleStatisticDataController;
   import net.wg.white_tiger.gui.battle.components.WhiteTigerBaseProgressCircle;
   import net.wg.white_tiger.gui.battle.components.WhiteTigerBattleUIComponent;
   import net.wg.white_tiger.gui.battle.components.WhiteTigerGeneratorHoverIndicator;
   import net.wg.white_tiger.gui.battle.components.WhiteTigerGeneratorProgressCircle;
   import net.wg.white_tiger.gui.battle.infrastructure.WhiteTigerBattleStatisticDataController;
   import net.wg.white_tiger.gui.battle.views.battleHints.WhiteTigerBattleHint;
   import net.wg.white_tiger.gui.battle.views.battleHints.WhiteTigerInfoContainer;
   import net.wg.white_tiger.gui.battle.views.battleHints.WhiteTigerObjectives;
   import net.wg.white_tiger.gui.battle.views.battleHints.WhiteTigerTextContainer;
   import net.wg.white_tiger.gui.battle.views.battleHints.WhiteTigerTimerContainer;
   import net.wg.white_tiger.gui.battle.views.battleTimer.AddTimeAnimation;
   import net.wg.white_tiger.gui.battle.views.battleTimer.BattleTimerEvent;
   import net.wg.white_tiger.gui.battle.views.battleTimer.WhiteTigerBattleTimer;
   import net.wg.white_tiger.gui.battle.views.battleTimer.WhiteTigerTextFieldContainer;
   import net.wg.white_tiger.gui.battle.views.bossTeleportation.WhiteTigerTeleportView;
   import net.wg.white_tiger.gui.battle.views.helpers.IAnimateAlpha;
   import net.wg.white_tiger.gui.battle.views.hunterRespawn.WhiteTigerHunterRespawnHint;
   import net.wg.white_tiger.gui.battle.views.hunterRespawn.WhiteTigerHunterRespawnView;
   import net.wg.white_tiger.gui.battle.views.minimap.WhiteTigerDeploymentMapEntriesContainer;
   import net.wg.white_tiger.gui.battle.views.minimap.WhiteTigerMinimap;
   import net.wg.white_tiger.gui.battle.views.minimap.WhiteTigerMinimapSizeConst;
   import net.wg.white_tiger.gui.battle.views.minimap.entries.CustomDeathZoneMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.minimap.entries.WhiteTigerDeathZoneMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.minimap.entries.WhiteTigerDeploymentPointMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.minimap.entries.WhiteTigerGeneratorMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.minimap.entries.WhiteTigerIndexedMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.ribbonsPanel.WhiteTigerRibbonSettings;
   import net.wg.white_tiger.gui.battle.views.ribbonsPanel.WhiteTigerRibbonsPanel;
   import net.wg.white_tiger.gui.battle.views.ribbonsPanel.WhiteTigerRibbonsPool;
   import net.wg.white_tiger.gui.battle.views.shared.WhiteTigerDeploymentMapView;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerGeneratorContent;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerIndexedActionMarker;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerIndexedContent;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerIndexedMarker;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerScaleAnimation;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerScaleContainer;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WhiteTigerDamageLabel;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WhiteTigerPlasmaDamageAnimatedLabel;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WhiteTigerVehicleMarker;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.IWhiteTigerBattleShellButton;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.IWhiteTigerConsumablesButton;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.VO.WhiteTigerConsumablesVO;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.WhiteTigerBattleEquipmentActiveGlow;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.WhiteTigerBattleEquipmentButton;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.WhiteTigerBattleEquipmentButtonGlow;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.WhiteTigerBattleShellButton;
   import net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel.WhiteTigerConsumablesPanel;
   import net.wg.white_tiger.gui.battle.views.whiteTigerHud.WhiteTigerHud;
   import net.wg.white_tiger.gui.battle.views.whiteTigerOvertime.WhiteTigerOvertime;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.IHuntersWhiteTigerPanelListItem;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.IWhiteTigerPlayersPanel;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerBossBotList;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerBossBotListItem;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerBossPanelList;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerHunterPanelList;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerHunterPanelListItem;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerHunterPanelListItemHolder;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerHunterPanelListLeft;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerHunterPanelListRight;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerPlayersInfo;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerPlayersPanel;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.IWhiteTigerTimerAnimation;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerBotHealthBar;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerBotHealthBarLeft;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerBotHealthBarRight;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerBotListInfo;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerBotListInfoIcon;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerHunterResurrectTimer;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps.WhiteTigerTimerAnimHelper;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStats.VO.WhiteTigerStatsPlayerVO;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStats.WhiteTigerFullStatsTable;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStats.WhiteTigerFullStatsTableCtrl;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStats.WhiteTigerStats;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStats.WhiteTigerStatsTableItem;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStats.WhiteTigerStatsTableItemHolder;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStatusNotificationPanel.WhiteTigerStatusNotificationsPanel;
   import net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel.WhiteTigerTeamBasesPanel;
   import net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel.WhiteTigerTeamCaptureBar;
   import net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel.WhiteTigerTeamCaptureProgress;
   import net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel.WhiteTigerTeamCaptureProgressReset;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerBattleHintMeta;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerBattleTimerMeta;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerBossTeleportViewMeta;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerHunterRespawnViewMeta;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerOvertimeMeta;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerPlayersPanelMeta;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerTeamBasesPanelMeta;
   
   public class ClassManagerMeta
   {
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_WHITETIGERSOUNDTYPES:Class = WhiteTigerSoundTypes;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_EFFICIENCY_TYPES:Class = WHITE_TIGER_BATTLE_EFFICIENCY_TYPES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_VIEW_ALIASES:Class = WHITE_TIGER_BATTLE_VIEW_ALIASES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_CONSUMABLES_PANEL_TAGS:Class = WHITE_TIGER_CONSUMABLES_PANEL_TAGS;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WT_BATTLE_NOTIFICATIONS_TIMER_LINKAGES:Class = WT_BATTLE_NOTIFICATIONS_TIMER_LINKAGES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WT_BATTLE_NOTIFICATIONS_TIMER_TYPES:Class = WT_BATTLE_NOTIFICATIONS_TIMER_TYPES;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_WHITETIGERBATTLEPAGE:Class = WhiteTigerBattlePage;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_WHITETIGERBATTLESTATISTICDATACONTROLLER:Class = WhiteTigerBattleStatisticDataController;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_COMPONENTS_WHITETIGERBASEPROGRESSCIRCLE:Class = WhiteTigerBaseProgressCircle;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_COMPONENTS_WHITETIGERBATTLEUICOMPONENT:Class = WhiteTigerBattleUIComponent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_COMPONENTS_WHITETIGERGENERATORHOVERINDICATOR:Class = WhiteTigerGeneratorHoverIndicator;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_COMPONENTS_WHITETIGERGENERATORPROGRESSCIRCLE:Class = WhiteTigerGeneratorProgressCircle;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_INFRASTRUCTURE_WHITETIGERBATTLESTATISTICDATACONTROLLER:Class = WhiteTigerBattleStatisticDataController;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLEHINTS_WHITETIGERBATTLEHINT:Class = WhiteTigerBattleHint;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLEHINTS_WHITETIGERINFOCONTAINER:Class = WhiteTigerInfoContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLEHINTS_WHITETIGEROBJECTIVES:Class = WhiteTigerObjectives;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLEHINTS_WHITETIGERTEXTCONTAINER:Class = WhiteTigerTextContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLEHINTS_WHITETIGERTIMERCONTAINER:Class = WhiteTigerTimerContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLETIMER_ADDTIMEANIMATION:Class = AddTimeAnimation;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLETIMER_BATTLETIMEREVENT:Class = BattleTimerEvent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLETIMER_WHITETIGERBATTLETIMER:Class = WhiteTigerBattleTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BATTLETIMER_WHITETIGERTEXTFIELDCONTAINER:Class = WhiteTigerTextFieldContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_BOSSTELEPORTATION_WHITETIGERTELEPORTVIEW:Class = WhiteTigerTeleportView;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_HELPERS_IANIMATEALPHA:Class = IAnimateAlpha;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_HUNTERRESPAWN_WHITETIGERHUNTERRESPAWNHINT:Class = WhiteTigerHunterRespawnHint;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_HUNTERRESPAWN_WHITETIGERHUNTERRESPAWNVIEW:Class = WhiteTigerHunterRespawnView;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_WHITETIGERDEPLOYMENTMAPENTRIESCONTAINER:Class = WhiteTigerDeploymentMapEntriesContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_WHITETIGERMINIMAP:Class = WhiteTigerMinimap;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_WHITETIGERMINIMAPSIZECONST:Class = WhiteTigerMinimapSizeConst;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_CUSTOMDEATHZONEMINIMAPENTRY:Class = CustomDeathZoneMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_WHITETIGERDEATHZONEMINIMAPENTRY:Class = WhiteTigerDeathZoneMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_WHITETIGERDEPLOYMENTPOINTMINIMAPENTRY:Class = WhiteTigerDeploymentPointMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_WHITETIGERGENERATORMINIMAPENTRY:Class = WhiteTigerGeneratorMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_WHITETIGERINDEXEDMINIMAPENTRY:Class = WhiteTigerIndexedMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_RIBBONSPANEL_WHITETIGERRIBBONSETTINGS:Class = WhiteTigerRibbonSettings;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_RIBBONSPANEL_WHITETIGERRIBBONSPANEL:Class = WhiteTigerRibbonsPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_RIBBONSPANEL_WHITETIGERRIBBONSPOOL:Class = WhiteTigerRibbonsPool;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_SHARED_WHITETIGERDEPLOYMENTMAPVIEW:Class = WhiteTigerDeploymentMapView;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_WHITETIGERGENERATORCONTENT:Class = WhiteTigerGeneratorContent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_WHITETIGERINDEXEDACTIONMARKER:Class = WhiteTigerIndexedActionMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_WHITETIGERINDEXEDCONTENT:Class = WhiteTigerIndexedContent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_WHITETIGERINDEXEDMARKER:Class = WhiteTigerIndexedMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_WHITETIGERSCALEANIMATION:Class = WhiteTigerScaleAnimation;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_WHITETIGERSCALECONTAINER:Class = WhiteTigerScaleContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_WHITETIGERDAMAGELABEL:Class = WhiteTigerDamageLabel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_WHITETIGERPLASMADAMAGEANIMATEDLABEL:Class = WhiteTigerPlasmaDamageAnimatedLabel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_WHITETIGERVEHICLEMARKER:Class = WhiteTigerVehicleMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_IWHITETIGERBATTLESHELLBUTTON:Class = IWhiteTigerBattleShellButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_IWHITETIGERCONSUMABLESBUTTON:Class = IWhiteTigerConsumablesButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_WHITETIGERBATTLEEQUIPMENTACTIVEGLOW:Class = WhiteTigerBattleEquipmentActiveGlow;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_WHITETIGERBATTLEEQUIPMENTBUTTON:Class = WhiteTigerBattleEquipmentButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_WHITETIGERBATTLEEQUIPMENTBUTTONGLOW:Class = WhiteTigerBattleEquipmentButtonGlow;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_WHITETIGERBATTLESHELLBUTTON:Class = WhiteTigerBattleShellButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_WHITETIGERCONSUMABLESPANEL:Class = WhiteTigerConsumablesPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERCONSUMABLESPANEL_VO_WHITETIGERCONSUMABLESVO:Class = WhiteTigerConsumablesVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERHUD_WHITETIGERHUD:Class = WhiteTigerHud;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGEROVERTIME_WHITETIGEROVERTIME:Class = WhiteTigerOvertime;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_IHUNTERSWHITETIGERPANELLISTITEM:Class = IHuntersWhiteTigerPanelListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_IWHITETIGERPLAYERSPANEL:Class = IWhiteTigerPlayersPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERBOSSBOTLIST:Class = WhiteTigerBossBotList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERBOSSBOTLISTITEM:Class = WhiteTigerBossBotListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERBOSSPANELLIST:Class = WhiteTigerBossPanelList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERHUNTERPANELLIST:Class = WhiteTigerHunterPanelList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERHUNTERPANELLISTITEM:Class = WhiteTigerHunterPanelListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERHUNTERPANELLISTITEMHOLDER:Class = WhiteTigerHunterPanelListItemHolder;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERHUNTERPANELLISTLEFT:Class = WhiteTigerHunterPanelListLeft;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERHUNTERPANELLISTRIGHT:Class = WhiteTigerHunterPanelListRight;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERPLAYERSINFO:Class = WhiteTigerPlayersInfo;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_WHITETIGERPLAYERSPANEL:Class = WhiteTigerPlayersPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_IWHITETIGERTIMERANIMATION:Class = IWhiteTigerTimerAnimation;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERBOTHEALTHBAR:Class = WhiteTigerBotHealthBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERBOTHEALTHBARLEFT:Class = WhiteTigerBotHealthBarLeft;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERBOTHEALTHBARRIGHT:Class = WhiteTigerBotHealthBarRight;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERBOTLISTINFO:Class = WhiteTigerBotListInfo;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERBOTLISTINFOICON:Class = WhiteTigerBotListInfoIcon;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERHUNTERRESURRECTTIMER:Class = WhiteTigerHunterResurrectTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERPLAYERSPANEL_COMPS_WHITETIGERTIMERANIMHELPER:Class = WhiteTigerTimerAnimHelper;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATS_WHITETIGERFULLSTATSTABLE:Class = WhiteTigerFullStatsTable;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATS_WHITETIGERFULLSTATSTABLECTRL:Class = WhiteTigerFullStatsTableCtrl;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATS_WHITETIGERSTATS:Class = WhiteTigerStats;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATS_WHITETIGERSTATSTABLEITEM:Class = WhiteTigerStatsTableItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATS_WHITETIGERSTATSTABLEITEMHOLDER:Class = WhiteTigerStatsTableItemHolder;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATS_VO_WHITETIGERSTATSPLAYERVO:Class = WhiteTigerStatsPlayerVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERSTATUSNOTIFICATIONPANEL_WHITETIGERSTATUSNOTIFICATIONSPANEL:Class = WhiteTigerStatusNotificationsPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERTEAMBASEPANEL_WHITETIGERTEAMBASESPANEL:Class = WhiteTigerTeamBasesPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERTEAMBASEPANEL_WHITETIGERTEAMCAPTUREBAR:Class = WhiteTigerTeamCaptureBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERTEAMBASEPANEL_WHITETIGERTEAMCAPTUREPROGRESS:Class = WhiteTigerTeamCaptureProgress;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WHITETIGERTEAMBASEPANEL_WHITETIGERTEAMCAPTUREPROGRESSRESET:Class = WhiteTigerTeamCaptureProgressReset;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VO_DAAPIHUNTERVEHICLEINFOVO:Class = DAAPIHunterVehicleInfoVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VO_DAAPIHUNTERVEHICLESDATAVO:Class = DAAPIHunterVehiclesDataVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VO_DAAPIWHITETIGERBOSSBOTINFOVO:Class = DAAPIWhiteTigerBossBotInfoVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VO_WHITETIGERBATTLEHINTVO:Class = WhiteTigerBattleHintVO;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGERBATTLEHINTMETA:Class = IWhiteTigerBattleHintMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGERBATTLETIMERMETA:Class = IWhiteTigerBattleTimerMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGERBOSSTELEPORTVIEWMETA:Class = IWhiteTigerBossTeleportViewMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGERHUNTERRESPAWNVIEWMETA:Class = IWhiteTigerHunterRespawnViewMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGEROVERTIMEMETA:Class = IWhiteTigerOvertimeMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGERPLAYERSPANELMETA:Class = IWhiteTigerPlayersPanelMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IWHITETIGERTEAMBASESPANELMETA:Class = IWhiteTigerTeamBasesPanelMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGERBATTLEHINTMETA:Class = WhiteTigerBattleHintMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGERBATTLETIMERMETA:Class = WhiteTigerBattleTimerMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGERBOSSTELEPORTVIEWMETA:Class = WhiteTigerBossTeleportViewMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGERHUNTERRESPAWNVIEWMETA:Class = WhiteTigerHunterRespawnViewMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGEROVERTIMEMETA:Class = WhiteTigerOvertimeMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGERPLAYERSPANELMETA:Class = WhiteTigerPlayersPanelMeta;
      
      public static const NET_WG_WHITE_TIGER_INFRASTRUCTURE_BASE_META_IMPL_WHITETIGERTEAMBASESPANELMETA:Class = WhiteTigerTeamBasesPanelMeta;
       
      
      public function ClassManagerMeta()
      {
         super();
      }
   }
}
