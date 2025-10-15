package net.wg.portal.infrastructure.base.meta.impl
{
   import net.wg.portal.data.VO.fullStats.DescriptionBlockWithIconVO;
   import net.wg.portal.data.VO.fullStats.PortalEventHeaderVO;
   import net.wg.portal.data.VO.fullStats.PortalFullStatsVO;
   import net.wg.portal.data.VO.fullStats.RespawnMessageVO;
   import net.wg.portal.data.constants.PortalLinkages;
   import net.wg.portal.data.constants.generated.PORTAL_BATTLE_NOTIFICATIONS_TIMER_TYPES;
   import net.wg.portal.data.constants.generated.PORTAL_BATTLE_VIEW_ALIASES;
   import net.wg.portal.data.constants.generated.PORTAL_PLAYERS_PANEL_ITEM_STATE;
   import net.wg.portal.gui.battle.PortalBattlePage;
   import net.wg.portal.gui.battle.battleloading.PortalBattleLoading;
   import net.wg.portal.gui.battle.components.AbilityDurationWidget;
   import net.wg.portal.gui.battle.components.AbilityProgressFill;
   import net.wg.portal.gui.battle.components.PortalShortcutBtn;
   import net.wg.portal.gui.battle.components.VehicleType;
   import net.wg.portal.gui.battle.fullStats.PortalFullStats;
   import net.wg.portal.gui.battle.fullStats.components.DescriptionWithIconRenderer;
   import net.wg.portal.gui.battle.fullStats.components.DescriptionWithIconRendererSmall;
   import net.wg.portal.gui.battle.fullStats.components.Header;
   import net.wg.portal.gui.battle.fullStats.components.MinimapItemsInfo;
   import net.wg.portal.gui.battle.fullStats.components.ScoreBlock;
   import net.wg.portal.gui.battle.minimap.PortalMinimap;
   import net.wg.portal.gui.battle.portalHudWidgetView.PortalHudWidgetView;
   import net.wg.portal.gui.battle.portalPostmortemPanel.PortalPostmortemPanel;
   import net.wg.portal.gui.battle.portalPostmortemPanel.PostmortemTimer;
   import net.wg.portal.gui.battle.portalPostmortemPanel.PostmortemTimerContainer;
   import net.wg.portal.gui.battle.ribbonsPanel.RibbonCtrl;
   import net.wg.portal.gui.battle.ribbonsPanel.RibbonIcons;
   import net.wg.portal.gui.battle.ribbonsPanel.RibbonTexts;
   import net.wg.portal.gui.battle.ribbonsPanel.RibbonsPanel;
   import net.wg.portal.gui.battle.ribbonsPanel.RibbonsPool;
   import net.wg.portal.gui.battle.views.battleHints.InfoContainer;
   import net.wg.portal.gui.battle.views.battleHints.PortalBattleHint;
   import net.wg.portal.gui.battle.views.battleHints.TextContainer;
   import net.wg.portal.gui.battle.views.campCapturePanel.CampCaptureBar;
   import net.wg.portal.gui.battle.views.campCapturePanel.CampCapturePanel;
   import net.wg.portal.gui.battle.views.campCapturePanel.CampCaptureProgress;
   import net.wg.portal.gui.battle.views.campCapturePanel.CampCaptureProgressReset;
   import net.wg.portal.gui.battle.views.campCapturePanel.CaptureBar;
   import net.wg.portal.gui.battle.views.campCapturePanel.CaptureBarsPanel;
   import net.wg.portal.gui.battle.views.consumablesPanel.BattleEquipmentButton;
   import net.wg.portal.gui.battle.views.consumablesPanel.BattleEquipmentButtonGlow;
   import net.wg.portal.gui.battle.views.consumablesPanel.BattleEquipmentCooldown;
   import net.wg.portal.gui.battle.views.consumablesPanel.BattleShellButton;
   import net.wg.portal.gui.battle.views.consumablesPanel.ConsumablesPanel;
   import net.wg.portal.gui.battle.views.enemiesPanel.EnemiesPanel;
   import net.wg.portal.gui.battle.views.enemiesPanel.LaneVehiclesRenderer;
   import net.wg.portal.gui.battle.views.enemiesPanel.VehicleTypesAmount;
   import net.wg.portal.gui.battle.views.guidedMissileWidget.GuidedMissileWidget;
   import net.wg.portal.gui.battle.views.interceptionWidget.InterceptionWidget;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.PlayersBaseMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.PortalMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.RatteMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.abilities.MinefieldMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.abilities.TrapMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.camps.HookCampMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.camps.HorseCampMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.camps.PerspectiveCampMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.camps.SateliteCampMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.MinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapProgressCircle;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.SimpleMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.HookTpCooldownMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.HookTpMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.HorseTpCooldownMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.HorseTpMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.PerspectiveTpCooldownMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.PerspectiveTpMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.SateliteTpCooldownMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports.SateliteTpMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.vehicle.MarkerTopAnimation;
   import net.wg.portal.gui.battle.views.minimap.components.entries.vehicle.MinimapEntryLabelHelper;
   import net.wg.portal.gui.battle.views.minimap.components.entries.vehicle.VehicleAnimationMinimapEntry;
   import net.wg.portal.gui.battle.views.minimap.components.entries.vehicle.VehicleMinimapEntry;
   import net.wg.portal.gui.battle.views.playersPanel.PlayerRenderer;
   import net.wg.portal.gui.battle.views.playersPanel.PlayersList;
   import net.wg.portal.gui.battle.views.playersPanel.PlayersPanel;
   import net.wg.portal.gui.battle.views.playersPanel.VO.PlayerInfoVO;
   import net.wg.portal.gui.battle.views.playersPanel.components.DynamicSquad;
   import net.wg.portal.gui.battle.views.playersPanel.components.PlayerName;
   import net.wg.portal.gui.battle.views.playersPanel.components.RespawnTimer;
   import net.wg.portal.gui.battle.views.playersPanel.components.healthBar.HealthBar;
   import net.wg.portal.gui.battle.views.playersPanel.components.healthBar.HealthBarFx;
   import net.wg.portal.gui.battle.views.playersPanel.events.PlayerListEvent;
   import net.wg.portal.gui.battle.views.playersPanel.events.PlayerRendererEvent;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.PlayersBaseMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.PortalMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.abilities.TrapMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.camps.HookCampMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.camps.HorseCampMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.camps.PerspectiveCampMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.camps.SateliteCampMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.CooldownTimeMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.MarkerCircle;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarkerProgressCircle;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.SimpleMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.HookTpCooldownMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.HookTpMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.HookTpReadyMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.HorseTpCooldownMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.HorseTpMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.HorseTpReadyMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.PerspectiveTpCooldownMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.PerspectiveTpMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.PerspectiveTpReadyMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.SateliteTpCooldownMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.SateliteTpMarker;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports.SateliteTpReadyMarker;
   import net.wg.portal.gui.battle.views.vehicleMarkers.VehicleMarker;
   
   public class ClassManagerMeta
   {
      
      public static const NET_WG_PORTAL_DATA_CONSTANTS_PORTALLINKAGES:Class = PortalLinkages;
      
      public static const NET_WG_PORTAL_DATA_CONSTANTS_GENERATED_PORTAL_BATTLE_NOTIFICATIONS_TIMER_TYPES:Class = PORTAL_BATTLE_NOTIFICATIONS_TIMER_TYPES;
      
      public static const NET_WG_PORTAL_DATA_CONSTANTS_GENERATED_PORTAL_BATTLE_VIEW_ALIASES:Class = PORTAL_BATTLE_VIEW_ALIASES;
      
      public static const NET_WG_PORTAL_DATA_CONSTANTS_GENERATED_PORTAL_PLAYERS_PANEL_ITEM_STATE:Class = PORTAL_PLAYERS_PANEL_ITEM_STATE;
      
      public static const NET_WG_PORTAL_DATA_VO_FULLSTATS_DESCRIPTIONBLOCKWITHICONVO:Class = DescriptionBlockWithIconVO;
      
      public static const NET_WG_PORTAL_DATA_VO_FULLSTATS_PORTALEVENTHEADERVO:Class = PortalEventHeaderVO;
      
      public static const NET_WG_PORTAL_DATA_VO_FULLSTATS_PORTALFULLSTATSVO:Class = PortalFullStatsVO;
      
      public static const NET_WG_PORTAL_DATA_VO_FULLSTATS_RESPAWNMESSAGEVO:Class = RespawnMessageVO;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_PORTALBATTLEPAGE:Class = PortalBattlePage;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_BATTLELOADING_PORTALBATTLELOADING:Class = PortalBattleLoading;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_COMPONENTS_ABILITYDURATIONWIDGET:Class = AbilityDurationWidget;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_COMPONENTS_ABILITYPROGRESSFILL:Class = AbilityProgressFill;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_COMPONENTS_PORTALSHORTCUTBTN:Class = PortalShortcutBtn;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_COMPONENTS_VEHICLETYPE:Class = VehicleType;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_FULLSTATS_PORTALFULLSTATS:Class = PortalFullStats;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_FULLSTATS_COMPONENTS_DESCRIPTIONWITHICONRENDERER:Class = DescriptionWithIconRenderer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_FULLSTATS_COMPONENTS_DESCRIPTIONWITHICONRENDERERSMALL:Class = DescriptionWithIconRendererSmall;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_FULLSTATS_COMPONENTS_HEADER:Class = Header;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_FULLSTATS_COMPONENTS_MINIMAPITEMSINFO:Class = MinimapItemsInfo;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_FULLSTATS_COMPONENTS_SCOREBLOCK:Class = ScoreBlock;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_MINIMAP_PORTALMINIMAP:Class = PortalMinimap;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_PORTALHUDWIDGETVIEW_PORTALHUDWIDGETVIEW:Class = PortalHudWidgetView;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_PORTALPOSTMORTEMPANEL_PORTALPOSTMORTEMPANEL:Class = PortalPostmortemPanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_PORTALPOSTMORTEMPANEL_POSTMORTEMTIMER:Class = PostmortemTimer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_PORTALPOSTMORTEMPANEL_POSTMORTEMTIMERCONTAINER:Class = PostmortemTimerContainer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_RIBBONSPANEL_RIBBONCTRL:Class = RibbonCtrl;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_RIBBONSPANEL_RIBBONICONS:Class = RibbonIcons;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_RIBBONSPANEL_RIBBONSPANEL:Class = RibbonsPanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_RIBBONSPANEL_RIBBONSPOOL:Class = RibbonsPool;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_RIBBONSPANEL_RIBBONTEXTS:Class = RibbonTexts;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_BATTLEHINTS_INFOCONTAINER:Class = InfoContainer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_BATTLEHINTS_PORTALBATTLEHINT:Class = PortalBattleHint;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_BATTLEHINTS_TEXTCONTAINER:Class = TextContainer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CAMPCAPTUREPANEL_CAMPCAPTUREBAR:Class = CampCaptureBar;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CAMPCAPTUREPANEL_CAMPCAPTUREPANEL:Class = CampCapturePanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CAMPCAPTUREPANEL_CAMPCAPTUREPROGRESS:Class = CampCaptureProgress;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CAMPCAPTUREPANEL_CAMPCAPTUREPROGRESSRESET:Class = CampCaptureProgressReset;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CAMPCAPTUREPANEL_CAPTUREBAR:Class = CaptureBar;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CAMPCAPTUREPANEL_CAPTUREBARSPANEL:Class = CaptureBarsPanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_BATTLEEQUIPMENTBUTTON:Class = BattleEquipmentButton;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_BATTLEEQUIPMENTBUTTONGLOW:Class = BattleEquipmentButtonGlow;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_BATTLEEQUIPMENTCOOLDOWN:Class = BattleEquipmentCooldown;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_BATTLESHELLBUTTON:Class = BattleShellButton;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_CONSUMABLESPANEL:Class = ConsumablesPanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_ENEMIESPANEL_ENEMIESPANEL:Class = EnemiesPanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_ENEMIESPANEL_LANEVEHICLESRENDERER:Class = LaneVehiclesRenderer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_ENEMIESPANEL_VEHICLETYPESAMOUNT:Class = VehicleTypesAmount;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_GUIDEDMISSILEWIDGET_GUIDEDMISSILEWIDGET:Class = GuidedMissileWidget;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_INTERCEPTIONWIDGET_INTERCEPTIONWIDGET:Class = InterceptionWidget;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_PLAYERSBASEMINIMAPENTRY:Class = PlayersBaseMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_PORTALMINIMAPENTRY:Class = PortalMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_RATTEMINIMAPENTRY:Class = RatteMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_ABILITIES_MINEFIELDMINIMAPENTRY:Class = MinefieldMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_ABILITIES_TRAPMINIMAPENTRY:Class = TrapMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CAMPS_HOOKCAMPMINIMAPENTRY:Class = HookCampMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CAMPS_HORSECAMPMINIMAPENTRY:Class = HorseCampMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CAMPS_PERSPECTIVECAMPMINIMAPENTRY:Class = PerspectiveCampMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CAMPS_SATELITECAMPMINIMAPENTRY:Class = SateliteCampMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CORE_MINIMAPENTRY:Class = MinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CORE_SCENARIOMINIMAPENTRY:Class = ScenarioMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CORE_SCENARIOMINIMAPPROGRESSCIRCLE:Class = ScenarioMinimapProgressCircle;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_CORE_SIMPLEMINIMAPENTRY:Class = SimpleMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_HOOKTPCOOLDOWNMINIMAPENTRY:Class = HookTpCooldownMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_HOOKTPMINIMAPENTRY:Class = HookTpMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_HORSETPCOOLDOWNMINIMAPENTRY:Class = HorseTpCooldownMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_HORSETPMINIMAPENTRY:Class = HorseTpMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_PERSPECTIVETPCOOLDOWNMINIMAPENTRY:Class = PerspectiveTpCooldownMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_PERSPECTIVETPMINIMAPENTRY:Class = PerspectiveTpMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_SATELITETPCOOLDOWNMINIMAPENTRY:Class = SateliteTpCooldownMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_SCENARIO_TELEPORTS_SATELITETPMINIMAPENTRY:Class = SateliteTpMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_VEHICLE_MARKERTOPANIMATION:Class = MarkerTopAnimation;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_VEHICLE_MINIMAPENTRYLABELHELPER:Class = MinimapEntryLabelHelper;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_VEHICLE_VEHICLEANIMATIONMINIMAPENTRY:Class = VehicleAnimationMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_MINIMAP_COMPONENTS_ENTRIES_VEHICLE_VEHICLEMINIMAPENTRY:Class = VehicleMinimapEntry;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_PLAYERRENDERER:Class = PlayerRenderer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_PLAYERSLIST:Class = PlayersList;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_PLAYERSPANEL:Class = PlayersPanel;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_DYNAMICSQUAD:Class = DynamicSquad;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_PLAYERNAME:Class = PlayerName;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_RESPAWNTIMER:Class = RespawnTimer;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HEALTHBAR_HEALTHBAR:Class = HealthBar;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_COMPONENTS_HEALTHBAR_HEALTHBARFX:Class = HealthBarFx;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_EVENTS_PLAYERLISTEVENT:Class = PlayerListEvent;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_EVENTS_PLAYERRENDEREREVENT:Class = PlayerRendererEvent;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_PLAYERSPANEL_VO_PLAYERINFOVO:Class = PlayerInfoVO;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_PLAYERSBASEMARKER:Class = PlayersBaseMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_PORTALMARKER:Class = PortalMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_ABILITIES_TRAPMARKER:Class = TrapMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CAMPS_HOOKCAMPMARKER:Class = HookCampMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CAMPS_HORSECAMPMARKER:Class = HorseCampMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CAMPS_PERSPECTIVECAMPMARKER:Class = PerspectiveCampMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CAMPS_SATELITECAMPMARKER:Class = SateliteCampMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CORE_COOLDOWNTIMEMARKER:Class = CooldownTimeMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CORE_MARKERCIRCLE:Class = MarkerCircle;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CORE_SCENARIOMARKER:Class = ScenarioMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CORE_SCENARIOMARKERPROGRESSCIRCLE:Class = ScenarioMarkerProgressCircle;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_CORE_SIMPLEMARKER:Class = SimpleMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_HOOKTPCOOLDOWNMARKER:Class = HookTpCooldownMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_HOOKTPMARKER:Class = HookTpMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_HOOKTPREADYMARKER:Class = HookTpReadyMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_HORSETPCOOLDOWNMARKER:Class = HorseTpCooldownMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_HORSETPMARKER:Class = HorseTpMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_HORSETPREADYMARKER:Class = HorseTpReadyMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_PERSPECTIVETPCOOLDOWNMARKER:Class = PerspectiveTpCooldownMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_PERSPECTIVETPMARKER:Class = PerspectiveTpMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_PERSPECTIVETPREADYMARKER:Class = PerspectiveTpReadyMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_SATELITETPCOOLDOWNMARKER:Class = SateliteTpCooldownMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_SATELITETPMARKER:Class = SateliteTpMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_STATICMARKERS_SCENARIO_TELEPORTS_SATELITETPREADYMARKER:Class = SateliteTpReadyMarker;
      
      public static const NET_WG_PORTAL_GUI_BATTLE_VIEWS_VEHICLEMARKERS_VEHICLEMARKER:Class = VehicleMarker;
       
      
      public function ClassManagerMeta()
      {
         super();
      }
   }
}
