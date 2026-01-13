package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.frontline.data.constants.FrontlineLinkages;
   import net.wg.frontline.data.constants.generated.FRONTLINE_BATTLE_VIEW_ALIASES;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlinePlayerStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehicleStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehiclesStatsVO;
   import net.wg.frontline.gui.battle.battleLoading.FrontlineBattleLoading;
   import net.wg.frontline.gui.battle.battleLoading.FrontlineBattleLoadingForm;
   import net.wg.frontline.gui.battle.battleLoading.components.FrontlineBattleLoadingTankBalance;
   import net.wg.frontline.gui.battle.battleLoading.components.FrontlineBattleLoadingTankTypeComponent;
   import net.wg.frontline.gui.battle.battleLoading.components.FrontlineBattleScrollingList;
   import net.wg.frontline.gui.battle.battleLoading.components.FrontlineBattleStatsTable;
   import net.wg.frontline.gui.battle.battleLoading.components.FrontlineBattleStatsTableCtrl;
   import net.wg.frontline.gui.battle.battleLoading.events.FrontlineBattleLoadingEvent;
   import net.wg.frontline.gui.battle.battleLoading.renderers.FrontlineBattleLoadingPlayerItemRenderer;
   import net.wg.frontline.gui.battle.components.FrontlineFilterDropDown;
   import net.wg.frontline.gui.battle.components.FrontlineListItemRenderer;
   import net.wg.frontline.gui.battle.components.FrontlineProgressCircle;
   import net.wg.frontline.gui.battle.views.FrontlineBattlePage;
   import net.wg.frontline.gui.battle.views.FrontlineBattleTimer;
   import net.wg.frontline.gui.battle.views.FrontlineCarouselFilterPopoverView;
   import net.wg.frontline.gui.battle.views.ammunitionPanel.FrontlineRespawnAmmunitionPanelView;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.BattleCarouselEnvironment;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.BattleTankCarouselFilters;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.FrontlineBattleTankCarousel;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.data.BattleVehicleCarouselVO;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.renderers.BaseBattleTankIcon;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.renderers.BattleTankCarouselItemRenderer;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.renderers.ResetFilters;
   import net.wg.frontline.gui.battle.views.consumablesPanel.FrontlineBattleConsumableButton;
   import net.wg.frontline.gui.battle.views.consumablesPanel.FrontlineBattleConsumablesPanel;
   import net.wg.frontline.gui.battle.views.consumablesPanel.components.FrontlineBattleEquipmentButtonGlow;
   import net.wg.frontline.gui.battle.views.consumablesPanel.interfaces.IFrontlineBattleConsumableButton;
   import net.wg.frontline.gui.battle.views.data.FrontlineStatsDataProviderBaseCtrl;
   import net.wg.frontline.gui.battle.views.data.FrontlineVehicleDataProvider;
   import net.wg.frontline.gui.battle.views.data.PlayListsVO;
   import net.wg.frontline.gui.battle.views.frontlineDamagePanel.FrontlineDamagePanel;
   import net.wg.frontline.gui.battle.views.frontlineDamagePanel.components.GeneralBonus;
   import net.wg.frontline.gui.battle.views.frontlineDeploymentMap.FrontlineDeploymentMap;
   import net.wg.frontline.gui.battle.views.frontlineDeploymentMap.components.FrontlineDeploymentMapEntriesContainer;
   import net.wg.frontline.gui.battle.views.frontlineDeploymentMap.components.FrontlineMapContainer;
   import net.wg.frontline.gui.battle.views.frontlineDeploymentMap.constants.DeploymentMapConstants;
   import net.wg.frontline.gui.battle.views.frontlineDeploymentMap.events.FrontlineDeploymentMapEvent;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.FrontlineInGameRankAnimatedProgress;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.FrontlineInGameRankIcon;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.FrontlineInGameRankPanel;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.data.FrontlineInGameRankVO;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.events.FrontlineInGameRankEvent;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.FrontlineMessagesPanel;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.BaseCaptureMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.BaseContestedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.FirstGeneralRankReachedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.HeadquarterAttackedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.HeadquarterDestroyedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.MessageBaseMarker;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.MessageHQMarker;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.OverTimeMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.RankUpMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.RankUpSubElement;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.RetreatMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.TimeRemainingMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.UnlockTankLevelMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.FirstGeneralRankReachedMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.FrontlineGameMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.HeadquarterAttackedMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.HeadquarterDestroyedMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.MissionChangeMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.OverTimeMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.RankUpMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.SectorBaseContestedMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.SectorBaseMessageVO;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.FrontlineMissionsPanel;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.components.FrontlineMissionsAnimatedMarker;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.data.FrontlineMissionVO;
   import net.wg.frontline.gui.battle.views.frontlineOverviewMapScreen.FrontlineOverviewMapScreen;
   import net.wg.frontline.gui.battle.views.frontlineOverviewMapScreen.data.FrontlineOverviewMapScreenVO;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.FrontlinePlatoonPanel;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.components.PlatoonInvitePanel;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.components.PlatoonMembersPanel;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.list.PlatoonMemberListItemHolder;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.list.PlatoonPanelList;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.renderers.PlatoonInviteRenderer;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.renderers.PlatoonMemberListItemRenderer;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.renderers.PlayerInfoContainer;
   import net.wg.frontline.gui.battle.views.frontlineReinforcementPanel.FrontlineReinforcementPanel;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.FrontlineRespawnView;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.components.FrontlineRespawnDeployButtonGroup;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.components.FrontlineRespawnMapEntriesContainer;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.components.FrontlineRespawnPoint;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.data.RespawnPointVO;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.events.FrontlineRespawnEvent;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.FrontlineScorePanel;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.components.HeadquarterEntryAnimated;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.components.HeadquarterScoreEntry;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.components.SectorBaseEntryAnimated;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.components.SectorBaseScoreEntry;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.events.FrontlineScorePanelEvent;
   import net.wg.frontline.gui.battle.views.minimap.FrontlineMinimap;
   import net.wg.frontline.gui.battle.views.minimap.containers.FrontlineMinimapEntriesContainer;
   import net.wg.frontline.gui.battle.views.minimap.entries.MapShortcutLabel;
   import net.wg.frontline.gui.battle.views.minimap.entries.ShortcutLabel;
   import net.wg.frontline.gui.battle.views.modificationPanel.FrontlineModificationPanel;
   import net.wg.frontline.gui.battle.views.modificationPanel.components.FrontlineModificationIcon;
   import net.wg.frontline.gui.battle.views.modificationPanel.components.FrontlineModificationInfo;
   import net.wg.frontline.gui.battle.views.modificationPanel.data.FrontlineModificationPanelVO;
   import net.wg.frontline.gui.battle.views.recoveryPanel.RecoveryHint;
   import net.wg.frontline.gui.battle.views.recoveryPanel.RecoveryPanel;
   import net.wg.frontline.gui.battle.views.staticMarkers.ObjectiveIdReplyState;
   import net.wg.frontline.gui.battle.views.staticMarkers.headquarter.HeadquarterAnimation;
   import net.wg.frontline.gui.battle.views.staticMarkers.headquarter.HeadquarterIcon;
   import net.wg.frontline.gui.battle.views.staticMarkers.sectorWaypoint.SectorWaypointIcon;
   import net.wg.frontline.gui.battle.views.staticMarkers.sectorbase.SectorBaseIcon;
   import net.wg.frontline.gui.battle.views.stats.FrontlineFullStats;
   import net.wg.frontline.gui.battle.views.stats.components.FrontlineFullStatsTable;
   import net.wg.frontline.gui.battle.views.stats.components.FrontlineFullStatsTableCtrl;
   import net.wg.frontline.gui.battle.views.stats.components.FrontlineStatsGeneralBonus;
   import net.wg.frontline.gui.battle.views.stats.components.FrontlineStatsHeader;
   import net.wg.frontline.gui.battle.views.stats.components.FrontlineStatsTableFilterGroup;
   import net.wg.frontline.gui.battle.views.stats.components.FrontlineStatsTableTabButton;
   import net.wg.frontline.gui.battle.views.stats.components.PlayerScrollingList;
   import net.wg.frontline.gui.battle.views.stats.events.FrontlineFullStatsEvent;
   import net.wg.frontline.gui.battle.views.stats.events.FrontlineFullStatsRendererEvent;
   import net.wg.frontline.gui.battle.views.stats.renderers.FrontlineStatsPlayerRenderer;
   import net.wg.frontline.gui.battle.views.upgradePanel.FrontlineBattleUpgradePanel;
   import net.wg.frontline.gui.battle.views.upgradePanel.FrontlineChoiceInfoPanel;
   import net.wg.frontline.gui.battle.views.upgradePanel.FrontlineConfiguratorRenderer;
   import net.wg.frontline.gui.battle.views.upgradePanel.FrontlineModuleInfo;
   import net.wg.frontline.gui.battle.views.upgradePanel.IFrontlineConfiguratorRenderer;
   import net.wg.frontline.gui.battle.views.upgradePanel.data.FrontlineChoiceInfoPanelVO;
   import net.wg.frontline.gui.battle.views.upgradePanel.data.FrontlineConfiguratorModuleVO;
   import net.wg.frontline.gui.battle.views.upgradePanel.data.FrontlineModuleInfoVO;
   import net.wg.frontline.gui.battle.views.upgradePanel.data.FrontlineUpgradePanelVO;
   import net.wg.frontline.infrastructure.helpers.statisticsDataController.FrontlineBattleStatisticDataController;
   import net.wg.frontline.infrastructure.helpers.statisticsDataController.interfaces.IFrontlineBattleStatisticDataController;
   
   public class ClassManagerMeta
   {
      
      public static const NET_WG_FRONTLINE_DATA_CONSTANTS_FRONTLINELINKAGES:Class = FrontlineLinkages;
      
      public static const NET_WG_FRONTLINE_DATA_CONSTANTS_GENERATED_FRONTLINE_BATTLE_VIEW_ALIASES:Class = FRONTLINE_BATTLE_VIEW_ALIASES;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_FRONTLINEBATTLELOADING:Class = FrontlineBattleLoading;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_FRONTLINEBATTLELOADINGFORM:Class = FrontlineBattleLoadingForm;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_COMPONENTS_FRONTLINEBATTLELOADINGTANKBALANCE:Class = FrontlineBattleLoadingTankBalance;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_COMPONENTS_FRONTLINEBATTLELOADINGTANKTYPECOMPONENT:Class = FrontlineBattleLoadingTankTypeComponent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_COMPONENTS_FRONTLINEBATTLESCROLLINGLIST:Class = FrontlineBattleScrollingList;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_COMPONENTS_FRONTLINEBATTLESTATSTABLE:Class = FrontlineBattleStatsTable;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_COMPONENTS_FRONTLINEBATTLESTATSTABLECTRL:Class = FrontlineBattleStatsTableCtrl;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_EVENTS_FRONTLINEBATTLELOADINGEVENT:Class = FrontlineBattleLoadingEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_BATTLELOADING_RENDERERS_FRONTLINEBATTLELOADINGPLAYERITEMRENDERER:Class = FrontlineBattleLoadingPlayerItemRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_COMPONENTS_FRONTLINEFILTERDROPDOWN:Class = FrontlineFilterDropDown;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_COMPONENTS_FRONTLINELISTITEMRENDERER:Class = FrontlineListItemRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_COMPONENTS_FRONTLINEPROGRESSCIRCLE:Class = FrontlineProgressCircle;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEBATTLEPAGE:Class = FrontlineBattlePage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEBATTLETIMER:Class = FrontlineBattleTimer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINECAROUSELFILTERPOPOVERVIEW:Class = FrontlineCarouselFilterPopoverView;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_AMMUNITIONPANEL_FRONTLINERESPAWNAMMUNITIONPANELVIEW:Class = FrontlineRespawnAmmunitionPanelView;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_BATTLECAROUSELENVIRONMENT:Class = BattleCarouselEnvironment;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_BATTLETANKCAROUSELFILTERS:Class = BattleTankCarouselFilters;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_FRONTLINEBATTLETANKCAROUSEL:Class = FrontlineBattleTankCarousel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_DATA_BATTLEVEHICLECAROUSELVO:Class = BattleVehicleCarouselVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_RENDERERS_BASEBATTLETANKICON:Class = BaseBattleTankIcon;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_RENDERERS_BATTLETANKCAROUSELITEMRENDERER:Class = BattleTankCarouselItemRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_BATTLETANKCAROUSEL_RENDERERS_RESETFILTERS:Class = ResetFilters;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_FRONTLINEBATTLECONSUMABLEBUTTON:Class = FrontlineBattleConsumableButton;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_FRONTLINEBATTLECONSUMABLESPANEL:Class = FrontlineBattleConsumablesPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_COMPONENTS_FRONTLINEBATTLEEQUIPMENTBUTTONGLOW:Class = FrontlineBattleEquipmentButtonGlow;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_CONSUMABLESPANEL_INTERFACES_IFRONTLINEBATTLECONSUMABLEBUTTON:Class = IFrontlineBattleConsumableButton;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_DATA_FRONTLINESTATSDATAPROVIDERBASECTRL:Class = FrontlineStatsDataProviderBaseCtrl;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_DATA_FRONTLINEVEHICLEDATAPROVIDER:Class = FrontlineVehicleDataProvider;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_DATA_PLAYLISTSVO:Class = PlayListsVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDAMAGEPANEL_FRONTLINEDAMAGEPANEL:Class = FrontlineDamagePanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDAMAGEPANEL_COMPONENTS_GENERALBONUS:Class = GeneralBonus;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDEPLOYMENTMAP_FRONTLINEDEPLOYMENTMAP:Class = FrontlineDeploymentMap;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDEPLOYMENTMAP_COMPONENTS_FRONTLINEDEPLOYMENTMAPENTRIESCONTAINER:Class = FrontlineDeploymentMapEntriesContainer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDEPLOYMENTMAP_COMPONENTS_FRONTLINEMAPCONTAINER:Class = FrontlineMapContainer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDEPLOYMENTMAP_CONSTANTS_DEPLOYMENTMAPCONSTANTS:Class = DeploymentMapConstants;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEDEPLOYMENTMAP_EVENTS_FRONTLINEDEPLOYMENTMAPEVENT:Class = FrontlineDeploymentMapEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEINGAMERANK_FRONTLINEINGAMERANKANIMATEDPROGRESS:Class = FrontlineInGameRankAnimatedProgress;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEINGAMERANK_FRONTLINEINGAMERANKICON:Class = FrontlineInGameRankIcon;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEINGAMERANK_FRONTLINEINGAMERANKPANEL:Class = FrontlineInGameRankPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEINGAMERANK_DATA_FRONTLINEINGAMERANKVO:Class = FrontlineInGameRankVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEINGAMERANK_EVENTS_FRONTLINEINGAMERANKEVENT:Class = FrontlineInGameRankEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_FRONTLINEMESSAGESPANEL:Class = FrontlineMessagesPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_BASECAPTUREMESSAGE:Class = BaseCaptureMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_BASECONTESTEDMESSAGE:Class = BaseContestedMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_FIRSTGENERALRANKREACHEDMESSAGE:Class = FirstGeneralRankReachedMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_HEADQUARTERATTACKEDMESSAGE:Class = HeadquarterAttackedMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_HEADQUARTERDESTROYEDMESSAGE:Class = HeadquarterDestroyedMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_MESSAGEBASEMARKER:Class = MessageBaseMarker;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_MESSAGEHQMARKER:Class = MessageHQMarker;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_OVERTIMEMESSAGE:Class = OverTimeMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_RANKUPMESSAGE:Class = RankUpMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_RANKUPSUBELEMENT:Class = RankUpSubElement;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_RETREATMESSAGE:Class = RetreatMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_TIMEREMAININGMESSAGE:Class = TimeRemainingMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_COMPONENTS_UNLOCKTANKLEVELMESSAGE:Class = UnlockTankLevelMessage;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_FIRSTGENERALRANKREACHEDMESSAGEVO:Class = FirstGeneralRankReachedMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_FRONTLINEGAMEMESSAGEVO:Class = FrontlineGameMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_HEADQUARTERATTACKEDMESSAGEVO:Class = HeadquarterAttackedMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_HEADQUARTERDESTROYEDMESSAGEVO:Class = HeadquarterDestroyedMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_MISSIONCHANGEMESSAGEVO:Class = MissionChangeMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_OVERTIMEMESSAGEVO:Class = OverTimeMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_RANKUPMESSAGEVO:Class = RankUpMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_SECTORBASECONTESTEDMESSAGEVO:Class = SectorBaseContestedMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMESSAGESPANEL_DATA_SECTORBASEMESSAGEVO:Class = SectorBaseMessageVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMISSIONSPANEL_FRONTLINEMISSIONSPANEL:Class = FrontlineMissionsPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMISSIONSPANEL_COMPONENTS_FRONTLINEMISSIONSANIMATEDMARKER:Class = FrontlineMissionsAnimatedMarker;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEMISSIONSPANEL_DATA_FRONTLINEMISSIONVO:Class = FrontlineMissionVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEOVERVIEWMAPSCREEN_FRONTLINEOVERVIEWMAPSCREEN:Class = FrontlineOverviewMapScreen;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEOVERVIEWMAPSCREEN_DATA_FRONTLINEOVERVIEWMAPSCREENVO:Class = FrontlineOverviewMapScreenVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_FRONTLINEPLATOONPANEL:Class = FrontlinePlatoonPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_COMPONENTS_PLATOONINVITEPANEL:Class = PlatoonInvitePanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_COMPONENTS_PLATOONMEMBERSPANEL:Class = PlatoonMembersPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_LIST_PLATOONMEMBERLISTITEMHOLDER:Class = PlatoonMemberListItemHolder;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_LIST_PLATOONPANELLIST:Class = PlatoonPanelList;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_RENDERERS_PLATOONINVITERENDERER:Class = PlatoonInviteRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_RENDERERS_PLATOONMEMBERLISTITEMRENDERER:Class = PlatoonMemberListItemRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEPLATOONPANEL_RENDERERS_PLAYERINFOCONTAINER:Class = PlayerInfoContainer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINEREINFORCEMENTPANEL_FRONTLINEREINFORCEMENTPANEL:Class = FrontlineReinforcementPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINERESPAWNVIEW_FRONTLINERESPAWNVIEW:Class = FrontlineRespawnView;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINERESPAWNVIEW_COMPONENTS_FRONTLINERESPAWNDEPLOYBUTTONGROUP:Class = FrontlineRespawnDeployButtonGroup;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINERESPAWNVIEW_COMPONENTS_FRONTLINERESPAWNMAPENTRIESCONTAINER:Class = FrontlineRespawnMapEntriesContainer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINERESPAWNVIEW_COMPONENTS_FRONTLINERESPAWNPOINT:Class = FrontlineRespawnPoint;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINERESPAWNVIEW_DATA_RESPAWNPOINTVO:Class = RespawnPointVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINERESPAWNVIEW_EVENTS_FRONTLINERESPAWNEVENT:Class = FrontlineRespawnEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINESCOREPANEL_FRONTLINESCOREPANEL:Class = FrontlineScorePanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINESCOREPANEL_COMPONENTS_HEADQUARTERENTRYANIMATED:Class = HeadquarterEntryAnimated;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINESCOREPANEL_COMPONENTS_HEADQUARTERSCOREENTRY:Class = HeadquarterScoreEntry;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINESCOREPANEL_COMPONENTS_SECTORBASEENTRYANIMATED:Class = SectorBaseEntryAnimated;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINESCOREPANEL_COMPONENTS_SECTORBASESCOREENTRY:Class = SectorBaseScoreEntry;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_FRONTLINESCOREPANEL_EVENTS_FRONTLINESCOREPANELEVENT:Class = FrontlineScorePanelEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MINIMAP_FRONTLINEMINIMAP:Class = FrontlineMinimap;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MINIMAP_CONTAINERS_FRONTLINEMINIMAPENTRIESCONTAINER:Class = FrontlineMinimapEntriesContainer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_MAPSHORTCUTLABEL:Class = MapShortcutLabel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MINIMAP_ENTRIES_SHORTCUTLABEL:Class = ShortcutLabel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MODIFICATIONPANEL_FRONTLINEMODIFICATIONPANEL:Class = FrontlineModificationPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MODIFICATIONPANEL_COMPONENTS_FRONTLINEMODIFICATIONICON:Class = FrontlineModificationIcon;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MODIFICATIONPANEL_COMPONENTS_FRONTLINEMODIFICATIONINFO:Class = FrontlineModificationInfo;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_MODIFICATIONPANEL_DATA_FRONTLINEMODIFICATIONPANELVO:Class = FrontlineModificationPanelVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_RECOVERYPANEL_RECOVERYHINT:Class = RecoveryHint;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_RECOVERYPANEL_RECOVERYPANEL:Class = RecoveryPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATICMARKERS_OBJECTIVEIDREPLYSTATE:Class = ObjectiveIdReplyState;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATICMARKERS_HEADQUARTER_HEADQUARTERANIMATION:Class = HeadquarterAnimation;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATICMARKERS_HEADQUARTER_HEADQUARTERICON:Class = HeadquarterIcon;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATICMARKERS_SECTORBASE_SECTORBASEICON:Class = SectorBaseIcon;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATICMARKERS_SECTORWAYPOINT_SECTORWAYPOINTICON:Class = SectorWaypointIcon;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_FRONTLINEFULLSTATS:Class = FrontlineFullStats;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_FRONTLINEFULLSTATSTABLE:Class = FrontlineFullStatsTable;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_FRONTLINEFULLSTATSTABLECTRL:Class = FrontlineFullStatsTableCtrl;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_FRONTLINESTATSGENERALBONUS:Class = FrontlineStatsGeneralBonus;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_FRONTLINESTATSHEADER:Class = FrontlineStatsHeader;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_FRONTLINESTATSTABLEFILTERGROUP:Class = FrontlineStatsTableFilterGroup;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_FRONTLINESTATSTABLETABBUTTON:Class = FrontlineStatsTableTabButton;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_COMPONENTS_PLAYERSCROLLINGLIST:Class = PlayerScrollingList;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_EVENTS_FRONTLINEFULLSTATSEVENT:Class = FrontlineFullStatsEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_EVENTS_FRONTLINEFULLSTATSRENDEREREVENT:Class = FrontlineFullStatsRendererEvent;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_STATS_RENDERERS_FRONTLINESTATSPLAYERRENDERER:Class = FrontlineStatsPlayerRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_FRONTLINEBATTLEUPGRADEPANEL:Class = FrontlineBattleUpgradePanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_FRONTLINECHOICEINFOPANEL:Class = FrontlineChoiceInfoPanel;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_FRONTLINECONFIGURATORRENDERER:Class = FrontlineConfiguratorRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_FRONTLINEMODULEINFO:Class = FrontlineModuleInfo;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_IFRONTLINECONFIGURATORRENDERER:Class = IFrontlineConfiguratorRenderer;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_DATA_FRONTLINECHOICEINFOPANELVO:Class = FrontlineChoiceInfoPanelVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_DATA_FRONTLINECONFIGURATORMODULEVO:Class = FrontlineConfiguratorModuleVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_DATA_FRONTLINEMODULEINFOVO:Class = FrontlineModuleInfoVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VIEWS_UPGRADEPANEL_DATA_FRONTLINEUPGRADEPANELVO:Class = FrontlineUpgradePanelVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VO_DAAPI_FRONTLINEPLAYERSTATSVO:Class = FrontlinePlayerStatsVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VO_DAAPI_FRONTLINEVEHICLESSTATSVO:Class = FrontlineVehiclesStatsVO;
      
      public static const NET_WG_FRONTLINE_GUI_BATTLE_VO_DAAPI_FRONTLINEVEHICLESTATSVO:Class = FrontlineVehicleStatsVO;
      
      public static const NET_WG_FRONTLINE_INFRASTRUCTURE_HELPERS_STATISTICSDATACONTROLLER_FRONTLINEBATTLESTATISTICDATACONTROLLER:Class = FrontlineBattleStatisticDataController;
      
      public static const NET_WG_FRONTLINE_INFRASTRUCTURE_HELPERS_STATISTICSDATACONTROLLER_INTERFACES_IFRONTLINEBATTLESTATISTICDATACONTROLLER:Class = IFrontlineBattleStatisticDataController;
       
      
      public function ClassManagerMeta()
      {
         super();
      }
   }
}
