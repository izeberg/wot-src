package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.white_tiger.data.VO.daapi.DAAPIHunterVehiclesDataVO;
   import net.wg.white_tiger.data.constants.WT_LINKAGES;
   import net.wg.white_tiger.data.constants.WT_SOUND_TYPE;
   import net.wg.white_tiger.data.constants.WT_VEHICLE_TYPE;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_CONSUMABLES_PANEL_TAGS;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_MARKER_STATES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_NOTIFICATIONS_TIMER_LINKAGES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_NOTIFICATIONS_TIMER_TYPES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_VIEW_ALIASES;
   import net.wg.white_tiger.gui.battle.WTBattlePage;
   import net.wg.white_tiger.gui.battle.infrastructure.WTBattleStatisticDataController;
   import net.wg.white_tiger.gui.battle.views.shared.GeneratorProgressCircle;
   import net.wg.white_tiger.gui.battle.views.shared.HunterResurrectTimer;
   import net.wg.white_tiger.gui.battle.views.shared.TimerAnimHelper;
   import net.wg.white_tiger.gui.battle.views.shared.WTDeploymentMapView;
   import net.wg.white_tiger.gui.battle.views.shared.interfaces.ITimerAnimation;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.DistanceMarker;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.GeneratorContent;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.IndexedActionMarker;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.IndexedContent;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.IndexedMarker;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.ScaleAnimation;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.ScaleContainer;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.DamageLabel;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.PlasmaDamageAnimatedLabel;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WTVehicleMarker;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WTVehicleMarkersConstants;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WTVehicleStatusContainerMarker;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers.WTUnionStrengthCounter;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers.WTUnionStrengthMarker;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers.WTVehicleStatusMarker;
   import net.wg.white_tiger.gui.battle.views.wtAbilityWidget.WTAbilityWidget;
   import net.wg.white_tiger.gui.battle.views.wtBattleHints.BattleHint;
   import net.wg.white_tiger.gui.battle.views.wtBattleHints.InfoContainer;
   import net.wg.white_tiger.gui.battle.views.wtBattleHints.TextContainer;
   import net.wg.white_tiger.gui.battle.views.wtBattleHints.TimerContainer;
   import net.wg.white_tiger.gui.battle.views.wtBattleHints.data.HintInfoVO;
   import net.wg.white_tiger.gui.battle.views.wtBattleLoading.WTBattleLoading;
   import net.wg.white_tiger.gui.battle.views.wtBattleTimer.AddTimeAnimation;
   import net.wg.white_tiger.gui.battle.views.wtBattleTimer.BattleTimerEvent;
   import net.wg.white_tiger.gui.battle.views.wtBattleTimer.WTBattleTimer;
   import net.wg.white_tiger.gui.battle.views.wtBattleTimer.WTTextFieldContainer;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.BossWidget;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.BossBackground;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.BossHyperion;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.BossShield;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.BossTankIcon;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.BossWidgetMainProgressBar;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.CaptureTimer;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.Generator;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.GeneratorBar;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.components.ProgressBar;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.data.BossWidgetVO;
   import net.wg.white_tiger.gui.battle.views.wtBossWidget.events.BossWidgetEvent;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.BaseConsumablesButton;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.BattleEquipmentButton;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.BattleEquipmentButtonGlow;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.BattleShellButton;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.ConsumablesPanel;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.PassiveAbilityButton;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.components.EquipmentButtonBackground;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.components.PassiveAbilityActive;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.constants.WT_ABILITY_STATES;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces.IWTBaseConsumablesButton;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces.IWTConsumablesButton;
   import net.wg.white_tiger.gui.battle.views.wtFullStats.FullStats;
   import net.wg.white_tiger.gui.battle.views.wtFullStats.FullStatsTable;
   import net.wg.white_tiger.gui.battle.views.wtFullStats.FullStatsTableCtrl;
   import net.wg.white_tiger.gui.battle.views.wtFullStats.FullStatsTableItem;
   import net.wg.white_tiger.gui.battle.views.wtFullStats.FullStatsTableItemHolder;
   import net.wg.white_tiger.gui.battle.views.wtHunterRespawn.WTHunterRespawnHint;
   import net.wg.white_tiger.gui.battle.views.wtHunterRespawn.WTHunterRespawnView;
   import net.wg.white_tiger.gui.battle.views.wtMinimap.WTDeploymentMapEntriesContainer;
   import net.wg.white_tiger.gui.battle.views.wtMinimap.WTMinimap;
   import net.wg.white_tiger.gui.battle.views.wtMinimap.WTMinimapSizeConst;
   import net.wg.white_tiger.gui.battle.views.wtMinimap.entries.WTDeploymentPointMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.wtMinimap.entries.WTGeneratorMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.wtMinimap.entries.WTIndexedMinimapEntry;
   import net.wg.white_tiger.gui.battle.views.wtMissileWidget.AltitudeIndicator;
   import net.wg.white_tiger.gui.battle.views.wtMissileWidget.WTMissileWidget;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.BossBombList;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.BossBombListItem;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.BossBotList;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.BossBotListItem;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.BossPanelList;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.HunterPanelList;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.HunterPanelListItem;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.HunterPanelListItemHolder;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.HunterPanelListLeft;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.HunterPanelListRight;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.IHunterPanelListItem;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.PlayersPanel;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.VO.BossBotInfoVO;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.comps.BotHealthBar;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.comps.BotHealthBarLeft;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.comps.BotHealthBarRight;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.comps.BotListInfo;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.comps.BotListInfoIcon;
   import net.wg.white_tiger.gui.battle.views.wtPlayersPanel.comps.HunterBombTimer;
   import net.wg.white_tiger.gui.battle.views.wtPrebattleTimer.PrebattleTimerBg;
   import net.wg.white_tiger.gui.battle.views.wtStatusNotificationsPanel.WTCounterTimer;
   import net.wg.white_tiger.gui.battle.views.wtTeamBasePanel.TeamBasesPanel;
   import net.wg.white_tiger.gui.battle.views.wtTeamBasePanel.TeamCaptureBar;
   import net.wg.white_tiger.gui.battle.views.wtTeamBasePanel.TeamCaptureProgress;
   import net.wg.white_tiger.gui.battle.views.wtTeamBasePanel.TeamCaptureProgressReset;
   import net.wg.white_tiger.gui.battle.views.wtTeleportView.WTBossTeleportView;
   
   public class ClassManagerMeta
   {
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_WT_LINKAGES:Class = WT_LINKAGES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_WT_SOUND_TYPE:Class = WT_SOUND_TYPE;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_WT_VEHICLE_TYPE:Class = WT_VEHICLE_TYPE;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_CONSUMABLES_PANEL_TAGS:Class = WHITE_TIGER_BATTLE_CONSUMABLES_PANEL_TAGS;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_MARKER_STATES:Class = WHITE_TIGER_BATTLE_MARKER_STATES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_NOTIFICATIONS_TIMER_LINKAGES:Class = WHITE_TIGER_BATTLE_NOTIFICATIONS_TIMER_LINKAGES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_NOTIFICATIONS_TIMER_TYPES:Class = WHITE_TIGER_BATTLE_NOTIFICATIONS_TIMER_TYPES;
      
      public static const NET_WG_WHITE_TIGER_DATA_CONSTANTS_GENERATED_WHITE_TIGER_BATTLE_VIEW_ALIASES:Class = WHITE_TIGER_BATTLE_VIEW_ALIASES;
      
      public static const NET_WG_WHITE_TIGER_DATA_VO_DAAPI_DAAPIHUNTERVEHICLESDATAVO:Class = DAAPIHunterVehiclesDataVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_WTBATTLEPAGE:Class = WTBattlePage;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_INFRASTRUCTURE_WTBATTLESTATISTICDATACONTROLLER:Class = WTBattleStatisticDataController;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_SHARED_GENERATORPROGRESSCIRCLE:Class = GeneratorProgressCircle;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_SHARED_HUNTERRESURRECTTIMER:Class = HunterResurrectTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_SHARED_TIMERANIMHELPER:Class = TimerAnimHelper;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_SHARED_WTDEPLOYMENTMAPVIEW:Class = WTDeploymentMapView;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_SHARED_INTERFACES_ITIMERANIMATION:Class = ITimerAnimation;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_DISTANCEMARKER:Class = DistanceMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_GENERATORCONTENT:Class = GeneratorContent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_INDEXEDACTIONMARKER:Class = IndexedActionMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_INDEXEDCONTENT:Class = IndexedContent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_INDEXEDMARKER:Class = IndexedMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_SCALEANIMATION:Class = ScaleAnimation;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_STATICMARKERS_SCALECONTAINER:Class = ScaleContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_DAMAGELABEL:Class = DamageLabel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_PLASMADAMAGEANIMATEDLABEL:Class = PlasmaDamageAnimatedLabel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_WTVEHICLEMARKER:Class = WTVehicleMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_WTVEHICLEMARKERSCONSTANTS:Class = WTVehicleMarkersConstants;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_WTVEHICLESTATUSCONTAINERMARKER:Class = WTVehicleStatusContainerMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_STATUSMARKERS_WTUNIONSTRENGTHCOUNTER:Class = WTUnionStrengthCounter;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_STATUSMARKERS_WTUNIONSTRENGTHMARKER:Class = WTUnionStrengthMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_VEHICLEMARKERS_STATUSMARKERS_WTVEHICLESTATUSMARKER:Class = WTVehicleStatusMarker;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTABILITYWIDGET_WTABILITYWIDGET:Class = WTAbilityWidget;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLEHINTS_BATTLEHINT:Class = BattleHint;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLEHINTS_INFOCONTAINER:Class = InfoContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLEHINTS_TEXTCONTAINER:Class = TextContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLEHINTS_TIMERCONTAINER:Class = TimerContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLEHINTS_DATA_HINTINFOVO:Class = HintInfoVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLELOADING_WTBATTLELOADING:Class = WTBattleLoading;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLETIMER_ADDTIMEANIMATION:Class = AddTimeAnimation;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLETIMER_BATTLETIMEREVENT:Class = BattleTimerEvent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLETIMER_WTBATTLETIMER:Class = WTBattleTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBATTLETIMER_WTTEXTFIELDCONTAINER:Class = WTTextFieldContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_BOSSWIDGET:Class = BossWidget;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_BOSSBACKGROUND:Class = BossBackground;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_BOSSHYPERION:Class = BossHyperion;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_BOSSSHIELD:Class = BossShield;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_BOSSTANKICON:Class = BossTankIcon;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_BOSSWIDGETMAINPROGRESSBAR:Class = BossWidgetMainProgressBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_CAPTURETIMER:Class = CaptureTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_GENERATOR:Class = Generator;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_GENERATORBAR:Class = GeneratorBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_COMPONENTS_PROGRESSBAR:Class = ProgressBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_DATA_BOSSWIDGETVO:Class = BossWidgetVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTBOSSWIDGET_EVENTS_BOSSWIDGETEVENT:Class = BossWidgetEvent;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_BASECONSUMABLESBUTTON:Class = BaseConsumablesButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_BATTLEEQUIPMENTBUTTON:Class = BattleEquipmentButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_BATTLEEQUIPMENTBUTTONGLOW:Class = BattleEquipmentButtonGlow;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_BATTLESHELLBUTTON:Class = BattleShellButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_CONSUMABLESPANEL:Class = ConsumablesPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_PASSIVEABILITYBUTTON:Class = PassiveAbilityButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_COMPONENTS_EQUIPMENTBUTTONBACKGROUND:Class = EquipmentButtonBackground;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_COMPONENTS_PASSIVEABILITYACTIVE:Class = PassiveAbilityActive;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_CONSTANTS_WT_ABILITY_STATES:Class = WT_ABILITY_STATES;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_INTERFACES_IWTBASECONSUMABLESBUTTON:Class = IWTBaseConsumablesButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTCONSUMABLESPANEL_INTERFACES_IWTCONSUMABLESBUTTON:Class = IWTConsumablesButton;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTFULLSTATS_FULLSTATS:Class = FullStats;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTFULLSTATS_FULLSTATSTABLE:Class = FullStatsTable;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTFULLSTATS_FULLSTATSTABLECTRL:Class = FullStatsTableCtrl;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTFULLSTATS_FULLSTATSTABLEITEM:Class = FullStatsTableItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTFULLSTATS_FULLSTATSTABLEITEMHOLDER:Class = FullStatsTableItemHolder;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTHUNTERRESPAWN_WTHUNTERRESPAWNHINT:Class = WTHunterRespawnHint;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTHUNTERRESPAWN_WTHUNTERRESPAWNVIEW:Class = WTHunterRespawnView;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMINIMAP_WTDEPLOYMENTMAPENTRIESCONTAINER:Class = WTDeploymentMapEntriesContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMINIMAP_WTMINIMAP:Class = WTMinimap;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMINIMAP_WTMINIMAPSIZECONST:Class = WTMinimapSizeConst;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMINIMAP_ENTRIES_WTDEPLOYMENTPOINTMINIMAPENTRY:Class = WTDeploymentPointMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMINIMAP_ENTRIES_WTGENERATORMINIMAPENTRY:Class = WTGeneratorMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMINIMAP_ENTRIES_WTINDEXEDMINIMAPENTRY:Class = WTIndexedMinimapEntry;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMISSILEWIDGET_ALTITUDEINDICATOR:Class = AltitudeIndicator;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTMISSILEWIDGET_WTMISSILEWIDGET:Class = WTMissileWidget;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_BOSSBOMBLIST:Class = BossBombList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_BOSSBOMBLISTITEM:Class = BossBombListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_BOSSBOTLIST:Class = BossBotList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_BOSSBOTLISTITEM:Class = BossBotListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_BOSSPANELLIST:Class = BossPanelList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_HUNTERPANELLIST:Class = HunterPanelList;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_HUNTERPANELLISTITEM:Class = HunterPanelListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_HUNTERPANELLISTITEMHOLDER:Class = HunterPanelListItemHolder;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_HUNTERPANELLISTLEFT:Class = HunterPanelListLeft;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_HUNTERPANELLISTRIGHT:Class = HunterPanelListRight;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_IHUNTERPANELLISTITEM:Class = IHunterPanelListItem;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_PLAYERSPANEL:Class = PlayersPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_COMPS_BOTHEALTHBAR:Class = BotHealthBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_COMPS_BOTHEALTHBARLEFT:Class = BotHealthBarLeft;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_COMPS_BOTHEALTHBARRIGHT:Class = BotHealthBarRight;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_COMPS_BOTLISTINFO:Class = BotListInfo;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_COMPS_BOTLISTINFOICON:Class = BotListInfoIcon;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_COMPS_HUNTERBOMBTIMER:Class = HunterBombTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPLAYERSPANEL_VO_BOSSBOTINFOVO:Class = BossBotInfoVO;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTPREBATTLETIMER_PREBATTLETIMERBG:Class = PrebattleTimerBg;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTSTATUSNOTIFICATIONSPANEL_WTCOUNTERTIMER:Class = WTCounterTimer;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTTEAMBASEPANEL_TEAMBASESPANEL:Class = TeamBasesPanel;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTTEAMBASEPANEL_TEAMCAPTUREBAR:Class = TeamCaptureBar;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTTEAMBASEPANEL_TEAMCAPTUREPROGRESS:Class = TeamCaptureProgress;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTTEAMBASEPANEL_TEAMCAPTUREPROGRESSRESET:Class = TeamCaptureProgressReset;
      
      public static const NET_WG_WHITE_TIGER_GUI_BATTLE_VIEWS_WTTELEPORTVIEW_WTBOSSTELEPORTVIEW:Class = WTBossTeleportView;
       
      
      public function ClassManagerMeta()
      {
         super();
      }
   }
}
