package net.wg.portal.gui.battle
{
   import flash.events.Event;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.StatusNotificationsPanel;
   import net.wg.gui.battle.interfaces.IReservesStats;
   import net.wg.gui.battle.random.views.BattlePage;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.gui.battle.views.minimap.events.MinimapEvent;
   import net.wg.infrastructure.events.LifeCycleEvent;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import net.wg.portal.data.constants.PortalLinkages;
   import net.wg.portal.data.constants.generated.PORTAL_BATTLE_VIEW_ALIASES;
   import net.wg.portal.gui.battle.fullStats.PortalFullStats;
   import net.wg.portal.gui.battle.minimap.PortalMinimap;
   import net.wg.portal.gui.battle.portalHudWidgetView.PortalHudWidgetView;
   import net.wg.portal.gui.battle.portalPostmortemPanel.PortalPostmortemPanel;
   import net.wg.portal.gui.battle.views.battleHints.PortalBattleHint;
   import net.wg.portal.gui.battle.views.campCapturePanel.CampCapturePanel;
   import net.wg.portal.gui.battle.views.enemiesPanel.EnemiesPanel;
   import net.wg.portal.gui.battle.views.guidedMissileWidget.GuidedMissileWidget;
   import net.wg.portal.gui.battle.views.interceptionWidget.InterceptionWidget;
   import net.wg.portal.gui.battle.views.playersPanel.PlayersPanel;
   import net.wg.utils.StageBreakPoint;
   import net.wg.utils.StageBreakPointList;
   import scaleform.clik.motion.Tween;
   
   public class PortalBattlePage extends BattlePage
   {
      
      private static const MINIMAP_SMALL_SCREEN_OFFSET_X:uint = 20;
      
      private static const GRID_BIG_OFFSET:Point = new Point(-24,-25);
      
      private static const GRID_SMALL_OFFSET:Point = new Point(-18,-15);
      
      private static const TIMERS_PANEL_Y_OFFSET:Vector.<int> = new <int>[50,50,51,51,52,52,52];
      
      private static const HUD_WIDGET_WIDTH:uint = 714;
      
      private static const HUD_WIDGET_HEIGHT:uint = 180;
      
      private static const ENEMIES_DATA_PANEL_OFFSET_X:uint = 39;
      
      private static const ENEMIES_DATA_PANEL_Y:uint = 100;
      
      private static const PLAYERS_DATA_PANEL_Y:uint = 139;
      
      private static const ENEMIES_DATA_PANEL_Y_SMALL:uint = 70;
      
      private static const PLAYERS_DATA_PANEL_Y_SMALL:uint = 109;
      
      private static const BATTLE_DAMAGE_LOG_PANEL_ICONS_MODIFICATOR:String = "Portal";
      
      private static const CAMP_CAPTURE_PANEL_OFFSET_Y:int = 10;
      
      private static const TEAM_BASE_PANEL_OFFSET_Y:int = -30;
      
      private static const EVENT_MESSAGE_TWEEN:uint = 300;
      
      private static const EVENT_MESSAGE_Y:int = 130;
      
      private static const PORTAL_EVENT_COLOR:Number = 5944516;
       
      
      public var interceptionWidget:InterceptionWidget = null;
      
      public var guidedMissileWidget:GuidedMissileWidget = null;
      
      public var statusNotificationsPanel:StatusNotificationsPanel = null;
      
      public var eventMessage:PortalBattleHint = null;
      
      public var playersDataPanel:PlayersPanel = null;
      
      public var enemiesDataPanel:EnemiesPanel = null;
      
      public var grid:BattleAtlasSprite = null;
      
      public var campCapturePanel:CampCapturePanel = null;
      
      private var _hudWidgetInject:PortalHudWidgetView = null;
      
      private var _fullStats:PortalFullStats = null;
      
      private var _minimap:PortalMinimap = null;
      
      private var _fullStatsVisible:Boolean = false;
      
      private var _portalPostmortemTips:PortalPostmortemPanel = null;
      
      private var _eventMessageTween:Tween = null;
      
      public function PortalBattlePage()
      {
         super();
      }
      
      override public function as_setPostmortemTipsVisible(param1:Boolean) : void
      {
         if(this._portalPostmortemTips)
         {
            this._portalPostmortemTips.setCompVisible(param1);
         }
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         var _loc3_:StageBreakPoint = App.stageSizeMgr.currentBreakPoint;
         var _loc4_:Number = param1 >> 1;
         var _loc5_:Number = param2 >> 1;
         this.campCapturePanel.x = _loc4_ | 0;
         this._fullStats.x = _loc4_;
         this._hudWidgetInject.x = _loc4_ - (HUD_WIDGET_WIDTH >> 1);
         this.enemiesDataPanel.x = param1 - this.enemiesDataPanel.width + ENEMIES_DATA_PANEL_OFFSET_X | 0;
         if(_loc3_ == StageBreakPointList.EXTRA_SMALL || _loc3_ == StageBreakPointList.SMALL)
         {
            this.enemiesDataPanel.y = ENEMIES_DATA_PANEL_Y_SMALL;
            this.playersDataPanel.y = PLAYERS_DATA_PANEL_Y_SMALL;
         }
         else
         {
            this.enemiesDataPanel.y = ENEMIES_DATA_PANEL_Y;
            this.playersDataPanel.y = PLAYERS_DATA_PANEL_Y;
         }
         this.eventMessage.updateStage(param1,param2);
         this.statusNotificationsPanel.updateStage(param1,param2);
         this.guidedMissileWidget.x = _loc4_;
         this.guidedMissileWidget.y = _loc5_;
         this.interceptionWidget.x = _loc4_;
         this.interceptionWidget.y = _loc5_;
         this.guidedMissileWidget.updateStage(param1,param2);
         this.interceptionWidget.updateStage(param1,param2);
         if(this._portalPostmortemTips)
         {
            this._portalPostmortemTips.updateStage(param1,param2);
         }
         this.updateMinimapPosition();
         this.updateCapturePanelsPosition();
      }
      
      override protected function initializeStatisticsController(param1:BattleStatisticDataController) : void
      {
         param1.registerComponentController(fullStats);
      }
      
      override protected function updatePositionForQuestProgress() : void
      {
         this.updateCapturePanelsPosition();
         super.updatePositionForQuestProgress();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._minimap.isTabModeCustomAlpha = true;
         this._minimap.tabModeCustomAlpha = Values.DEFAULT_ALPHA;
         battleMessenger.greenMessageColorOverride = PORTAL_EVENT_COLOR;
         vehicleErrorMessageList.greenMessageColorOverride = PORTAL_EVENT_COLOR;
         vehicleMessageList.greenMessageColorOverride = PORTAL_EVENT_COLOR;
         playerMessageList.greenMessageColorOverride = PORTAL_EVENT_COLOR;
         damagePanel.setHealthBarProgressImageName(BATTLEATLAS.PORTAL_PROGRESS_BG);
      }
      
      override protected function initialize() : void
      {
         battleDamageLogPanel.init(ATLAS_CONSTANTS.BATTLE_ATLAS,BATTLE_DAMAGE_LOG_PANEL_ICONS_MODIFICATOR);
         super.initialize();
         this.grid.visible = false;
         this._minimap = PortalMinimap(minimap);
         this._minimap.addEventListener(Event.RESIZE,this.onMinimapResizeHandler);
         this._fullStats = PortalFullStats(fullStats);
         this._fullStats.setAnchorDO(this.grid);
         this._fullStats.addEventListener(Event.OPEN,this.onFullStatsOpenHandler);
         this._fullStats.addEventListener(Event.CLOSE,this.onFullStatsCloseHandler);
         this._hudWidgetInject = new PortalHudWidgetView();
         this._hudWidgetInject.name = PORTAL_BATTLE_VIEW_ALIASES.PORTAL_HUD_WIDGET_VIEW;
         this._hudWidgetInject.width = HUD_WIDGET_WIDTH;
         this._hudWidgetInject.height = HUD_WIDGET_HEIGHT;
         playersPanel.visible = false;
         this.enemiesDataPanel.visible = false;
         fragCorrelationBar.visible = false;
         this.guidedMissileWidget.visible = false;
         this.interceptionWidget.visible = false;
         this.campCapturePanel.addEventListener(Event.CHANGE,this.onCampPanelUIChangeHandler);
         addChild(this._hudWidgetInject);
      }
      
      override protected function onPopulate() : void
      {
         var _loc2_:IDAAPIModule = null;
         registerComponent(this.interceptionWidget,PORTAL_BATTLE_VIEW_ALIASES.INTERCEPTION_WIDGET);
         registerComponent(teamBasesPanelUI,BATTLE_VIEW_ALIASES.TEAM_BASES_PANEL);
         registerComponent(this.campCapturePanel,PORTAL_BATTLE_VIEW_ALIASES.PORTAL_CAMP_CAPTURABLE_PROGRESS_BAR);
         registerComponent(this.guidedMissileWidget,PORTAL_BATTLE_VIEW_ALIASES.GUIDED_MISSILE_WIDGET);
         registerComponent(this.playersDataPanel,PORTAL_BATTLE_VIEW_ALIASES.PLAYERS_DATA_PANEL);
         registerComponent(this.enemiesDataPanel,PORTAL_BATTLE_VIEW_ALIASES.ENEMIES_DATA_PANEL);
         registerComponent(this._hudWidgetInject,PORTAL_BATTLE_VIEW_ALIASES.PORTAL_HUD_WIDGET_VIEW);
         registerComponent(sixthSense,BATTLE_VIEW_ALIASES.SIXTH_SENSE);
         registerComponent(damageInfoPanel,BATTLE_VIEW_ALIASES.DAMAGE_INFO_PANEL);
         registerComponent(battleDamageLogPanel,BATTLE_VIEW_ALIASES.BATTLE_DAMAGE_LOG_PANEL);
         registerComponent(fullStats,BATTLE_VIEW_ALIASES.FULL_STATS);
         registerComponent(debugPanel,BATTLE_VIEW_ALIASES.DEBUG_PANEL);
         registerComponent(battleMessenger,BATTLE_VIEW_ALIASES.BATTLE_MESSENGER);
         registerComponent(consumablesPanel,BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL);
         registerComponent(radialMenu,BATTLE_VIEW_ALIASES.RADIAL_MENU);
         registerComponent(endWarningPanel,BATTLE_VIEW_ALIASES.BATTLE_END_WARNING_PANEL);
         registerComponent(siegeModePanel,BATTLE_VIEW_ALIASES.SIEGE_MODE_INDICATOR);
         registerComponent(hintPanel,BATTLE_VIEW_ALIASES.HINT_PANEL);
         if(mapInfoTip)
         {
            registerComponent(mapInfoTip,BATTLE_VIEW_ALIASES.MAP_INFO_TIP);
         }
         if(battleNotifier)
         {
            registerComponent(battleNotifier,BATTLE_VIEW_ALIASES.BATTLE_NOTIFIER);
         }
         var _loc1_:IReservesStats = fullStats as IReservesStats;
         if(_loc1_)
         {
            _loc2_ = _loc1_.getReservesView();
            if(_loc2_)
            {
               registerComponent(_loc2_,BATTLE_VIEW_ALIASES.PERSONAL_RESERVES_TAB);
            }
         }
         if(battleLoading)
         {
            registerComponent(battleLoading,BATTLE_VIEW_ALIASES.BATTLE_LOADING);
         }
         registerComponent(minimap,BATTLE_VIEW_ALIASES.MINIMAP);
         registerComponent(prebattleTimer,BATTLE_VIEW_ALIASES.PREBATTLE_TIMER);
         registerComponent(damagePanel,BATTLE_VIEW_ALIASES.DAMAGE_PANEL);
         if(battleTimer)
         {
            registerComponent(battleTimer,BATTLE_VIEW_ALIASES.BATTLE_TIMER);
         }
         if(ribbonsPanel)
         {
            registerComponent(ribbonsPanel,BATTLE_VIEW_ALIASES.RIBBONS_PANEL);
         }
         if(perksPanel)
         {
            registerComponent(perksPanel,BATTLE_VIEW_ALIASES.PERKS_PANEL);
         }
         registerComponent(vehicleMessageList,BATTLE_VIEW_ALIASES.VEHICLE_MESSAGES);
         registerComponent(vehicleErrorMessageList,BATTLE_VIEW_ALIASES.VEHICLE_ERROR_MESSAGES);
         registerComponent(playerMessageList,BATTLE_VIEW_ALIASES.PLAYER_MESSAGES);
         registerComponent(gameMessagesPanel,BATTLE_VIEW_ALIASES.GAME_MESSAGES_PANEL);
         if(calloutPanel)
         {
            registerComponent(calloutPanel,BATTLE_VIEW_ALIASES.CALLOUT_PANEL);
         }
         if(prebattleAmmunitionPanelAvailable && prebattleAmmunitionPanel)
         {
            registerComponent(prebattleAmmunitionPanel,BATTLE_VIEW_ALIASES.PREBATTLE_AMMUNITION_PANEL);
         }
         if(dualGunPanel)
         {
            registerComponent(dualGunPanel,BATTLE_VIEW_ALIASES.DUAL_GUN_PANEL);
         }
         if(rocketAcceleratorPanel)
         {
            registerComponent(rocketAcceleratorPanel,BATTLE_VIEW_ALIASES.ROCKET_ACCELERATOR_INDICATOR);
         }
         if(thermalVisionPanel)
         {
            registerComponent(thermalVisionPanel,BATTLE_VIEW_ALIASES.THERMAL_VISION_INDICATOR);
         }
         this.createPostmortemTipsComponent();
         this._portalPostmortemTips.setCompVisible(false);
         addChild(this._portalPostmortemTips);
         registerComponent(this._portalPostmortemTips,BATTLE_VIEW_ALIASES.POSTMORTEM_PANEL);
         registerComponent(this.eventMessage,BATTLE_VIEW_ALIASES.BATTLE_HINT);
         registerComponent(this.statusNotificationsPanel,BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL);
         onRegisterStatisticController();
      }
      
      override protected function onBeforeDispose() : void
      {
         if(!_baseDisposed)
         {
            if(isFlashComponentRegistered(PORTAL_BATTLE_VIEW_ALIASES.PLAYERS_DATA_PANEL))
            {
               unregisterComponent(PORTAL_BATTLE_VIEW_ALIASES.PLAYERS_DATA_PANEL);
            }
            if(isFlashComponentRegistered(PORTAL_BATTLE_VIEW_ALIASES.PORTAL_HUD_WIDGET_VIEW))
            {
               unregisterComponent(PORTAL_BATTLE_VIEW_ALIASES.PORTAL_HUD_WIDGET_VIEW);
            }
         }
         this.campCapturePanel.removeEventListener(Event.CHANGE,this.onCampPanelUIChangeHandler);
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.interceptionWidget = null;
         this.guidedMissileWidget = null;
         this.playersDataPanel = null;
         this.enemiesDataPanel = null;
         this.grid = null;
         this.eventMessage = null;
         this.statusNotificationsPanel = null;
         this._portalPostmortemTips = null;
         this.campCapturePanel = null;
         this._hudWidgetInject = null;
         this._fullStats.removeEventListener(Event.OPEN,this.onFullStatsOpenHandler);
         this._fullStats.removeEventListener(Event.CLOSE,this.onFullStatsCloseHandler);
         this._fullStats = null;
         this._minimap = null;
         this.clearEventMessageTween();
         super.onDispose();
      }
      
      override protected function getAllowedMinimapSizeIndex(param1:Number) : Number
      {
         var _loc5_:StageBreakPoint = null;
         if(this._minimap.isTabMode)
         {
            _loc5_ = App.stageSizeMgr.currentBreakPoint;
            if(_loc5_ == StageBreakPointList.EXTRA_SMALL || _loc5_ == StageBreakPointList.SMALL || _loc5_ == StageBreakPointList.MEDIUM)
            {
               return PortalMinimap.TAB_MODE_502_IDX;
            }
            return PortalMinimap.TAB_MODE_700_IDX;
         }
         var _loc2_:Number = App.appHeight >> 1;
         var _loc3_:Number = App.appWidth - consumablesPanel.panelWidth | 0;
         var _loc4_:Rectangle = null;
         while(param1 > MinimapSizeConst.MIN_SIZE_INDEX)
         {
            _loc4_ = minimap.getMinimapRectBySizeIndex(param1);
            if(_loc2_ - _loc4_.height >= 0 && _loc3_ - _loc4_.width >= 0)
            {
               break;
            }
            param1--;
         }
         return param1;
      }
      
      override protected function updateMinimapPosition() : void
      {
         var _loc1_:StageBreakPoint = null;
         var _loc2_:Point = null;
         if(this._minimap.isTabMode)
         {
            this._minimap.x = (_width >> 1) - this._minimap.mapHit.width | 0;
            this._minimap.y = _height + this._fullStats.headerHeight - this._minimap.mapHit.height >> 1;
            this._minimap.dispatchEvent(new LifeCycleEvent(LifeCycleEvent.ON_GRAPHICS_RECTANGLES_UPDATE));
            _loc1_ = App.stageSizeMgr.currentBreakPoint;
            if(_loc1_ == StageBreakPointList.EXTRA_SMALL || _loc1_ == StageBreakPointList.SMALL || _loc1_ == StageBreakPointList.MEDIUM)
            {
               this._minimap.x += MINIMAP_SMALL_SCREEN_OFFSET_X;
               this.grid.imageName = BATTLEATLAS.MINIMAP_GRID_MINI;
               _loc2_ = GRID_SMALL_OFFSET;
            }
            else
            {
               this.grid.imageName = BATTLEATLAS.MINIMAP_GRID;
               _loc2_ = GRID_BIG_OFFSET;
            }
            this.grid.x = minimap.x + _loc2_.x;
            this.grid.y = minimap.y + _loc2_.y;
         }
         else
         {
            super.updateMinimapPosition();
            this.statusNotificationsPanel.y = minimap.y - TIMERS_PANEL_Y_OFFSET[minimap.currentSizeIndex];
         }
      }
      
      override protected function onComponentVisibilityChanged(param1:String, param2:Boolean) : void
      {
         super.onComponentVisibilityChanged(param1,param2);
         if(param1 == BATTLE_VIEW_ALIASES.FULL_STATS)
         {
            this._fullStatsVisible = param2;
         }
         if(param1 == BATTLE_VIEW_ALIASES.MINIMAP)
         {
            if(this._fullStatsVisible)
            {
               this._minimap.visible = true;
            }
         }
      }
      
      override protected function createPostmortemTipsComponent() : void
      {
         if(this._portalPostmortemTips == null)
         {
            this._portalPostmortemTips = App.utils.classFactory.getComponent(PortalLinkages.PORTAL_POSTMORTEM_PANEL,PortalPostmortemPanel);
         }
      }
      
      private function updateCapturePanelsPosition() : void
      {
         this.campCapturePanel.y = this._hudWidgetInject.y + this._hudWidgetInject.height + CAMP_CAPTURE_PANEL_OFFSET_Y | 0;
         teamBasesPanelUI.y = this.campCapturePanel.y + this.campCapturePanel.panelHeight + TEAM_BASE_PANEL_OFFSET_Y | 0;
         var _loc1_:int = teamBasesPanelUI.panelHeight == 0 ? int(this.campCapturePanel.height) : int(teamBasesPanelUI.panelHeight + this.campCapturePanel.panelHeight);
         this.clearEventMessageTween();
         this._eventMessageTween = new Tween(EVENT_MESSAGE_TWEEN,this.eventMessage,{"y":EVENT_MESSAGE_Y + _loc1_});
      }
      
      private function clearEventMessageTween() : void
      {
         if(this._eventMessageTween)
         {
            this._eventMessageTween.dispose();
            this._eventMessageTween = null;
         }
      }
      
      override protected function get isQuestProgress() : Boolean
      {
         return false;
      }
      
      override protected function onMinimapSizeChangedHandler(param1:MinimapEvent) : void
      {
      }
      
      private function onMinimapResizeHandler(param1:Event) : void
      {
         this.updateMinimapPosition();
         if(!this._minimap.isTabMode)
         {
            playerMessageListPositionUpdate();
         }
         this._fullStats.updateLayout();
      }
      
      private function onFullStatsCloseHandler(param1:Event) : void
      {
         if(this._fullStatsVisible)
         {
            this._minimap.restoreZoomMode();
            this._minimap.toggleTabMode(false);
            this.grid.visible = false;
         }
      }
      
      private function onFullStatsOpenHandler(param1:Event) : void
      {
         if(!this._fullStatsVisible)
         {
            this._minimap.toggleTabMode(true);
            this._minimap.setTabZoomMode();
            this._minimap.visible = true;
            this.grid.visible = true;
         }
      }
      
      private function onCampPanelUIChangeHandler(param1:Event) : void
      {
         this.updateCapturePanelsPosition();
      }
   }
}
