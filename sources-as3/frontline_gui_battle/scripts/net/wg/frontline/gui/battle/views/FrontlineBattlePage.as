package net.wg.frontline.gui.battle.views
{
   import fl.transitions.easing.Strong;
   import flash.events.Event;
   import flash.geom.Rectangle;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.data.constants.generated.DAMAGE_INFO_PANEL_CONSTS;
   import net.wg.frontline.data.constants.generated.FRONTLINE_BATTLE_VIEW_ALIASES;
   import net.wg.frontline.gui.battle.battleLoading.FrontlineBattleLoading;
   import net.wg.frontline.gui.battle.battleLoading.events.FrontlineBattleLoadingEvent;
   import net.wg.frontline.gui.battle.views.consumablesPanel.FrontlineBattleConsumablesPanel;
   import net.wg.frontline.gui.battle.views.frontlineDeploymentMap.FrontlineDeploymentMap;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.FrontlineInGameRankPanel;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.FrontlineMissionsPanel;
   import net.wg.frontline.gui.battle.views.frontlineOverviewMapScreen.FrontlineOverviewMapScreen;
   import net.wg.frontline.gui.battle.views.frontlinePlatoonPanel.FrontlinePlatoonPanel;
   import net.wg.frontline.gui.battle.views.frontlineReinforcementPanel.FrontlineReinforcementPanel;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.FrontlineRespawnView;
   import net.wg.frontline.gui.battle.views.frontlineRespawnView.events.FrontlineRespawnEvent;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.FrontlineScorePanel;
   import net.wg.frontline.gui.battle.views.frontlineScorePanel.events.FrontlineScorePanelEvent;
   import net.wg.frontline.gui.battle.views.minimap.FrontlineMinimap;
   import net.wg.frontline.gui.battle.views.modificationPanel.FrontlineModificationPanel;
   import net.wg.frontline.gui.battle.views.recoveryPanel.RecoveryPanel;
   import net.wg.frontline.gui.battle.views.stats.FrontlineFullStats;
   import net.wg.frontline.gui.battle.views.upgradePanel.FrontlineBattleUpgradePanel;
   import net.wg.frontline.infrastructure.base.meta.IFrontlineBattlePageMeta;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineBattlePageMeta;
   import net.wg.frontline.infrastructure.helpers.statisticsDataController.FrontlineBattleStatisticDataController;
   import net.wg.gui.battle.components.StatusNotificationsPanel;
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamBasesPanel;
   import net.wg.gui.battle.views.battleEndWarning.BattleEndWarningPanel;
   import net.wg.gui.battle.views.battleMessenger.BattleMessenger;
   import net.wg.gui.battle.views.consumablesPanel.events.ConsumablesPanelEvent;
   import net.wg.gui.battle.views.damageInfoPanel.DamageInfoPanel;
   import net.wg.gui.battle.views.debugPanel.DebugPanel;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.gui.battle.views.minimap.events.MinimapEvent;
   import net.wg.gui.battle.views.prebattleTimer.PrebattleTimerBg;
   import net.wg.gui.battle.views.prebattleTimer.PrebattleTimerEvent;
   import net.wg.gui.battle.views.radialMenu.RadialMenu;
   import net.wg.gui.battle.views.siegeModePanel.SiegeModePanel;
   import net.wg.gui.battle.views.sixthSense.SixthSense;
   import net.wg.gui.components.battleDamagePanel.BattleDamageLogPanel;
   import net.wg.gui.components.battleDamagePanel.constants.BattleDamageLogConstants;
   import net.wg.gui.components.hintPanel.HintPanel;
   import net.wg.infrastructure.events.FocusRequestEvent;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.events.ComponentEvent;
   import scaleform.clik.motion.Tween;
   
   public class FrontlineBattlePage extends FrontlineBattlePageMeta implements IFrontlineBattlePageMeta
   {
      
      private static const BATTLE_DAMAGE_LOG_X_POSITION:int = 229;
      
      private static const BATTLE_DAMAGE_LOG_Y_PADDING:int = 3;
      
      private static const MESSENGER_OFFSET_Y:int = 44;
      
      private static const MESSENGER_IN_RESPAWN_OFFSET_Y_SMALL:int = 287;
      
      private static const MESSENGER_IN_RESPAWN_OFFSET_Y_BIG:int = 205;
      
      private static const PREBATTLE_TIMER_Y_OFFSET:int = 82;
      
      private static const PREBATTLE_TIMER_FINAL_Y_OFFSET:int = 30;
      
      private static const MODIFICATION_PANEL_Y_OFFSET:int = 258;
      
      private static const MODIFICATION_PANEL_Y_SHIFT_SMALL:int = 80;
      
      private static const MODIFICATION_PANEL_Y_SHIFT_BIG:int = 130;
      
      private static const MODIFICATION_PANEL_Y_BREAKPOINT:int = 768;
      
      private static const TEAM_BASES_PANEL_OFFSETS:Vector.<int> = new <int>[62,102,102];
      
      private static const TEAM_BASES_PANEL_TOP_OFFSET:int = 12;
      
      private static const SCORE_PANEL_HIDDEN_OFFSET:int = -80;
      
      private static const MSG_PNL_OFFSET:int = 128;
      
      private static const MSG_PNL_Y_BREAKPOINT:int = 1024;
      
      private static const SCORE_PANEL_FADE_OUT_TWEEN_LENGTH:int = 400;
      
      private static const SCORE_PANEL_FADE_IN_TWEEN_LENGTH:int = 800;
      
      private static const CAPTURE_BAR_TWEEN_LENGTH:int = 600;
      
      private static const PREBATTLE_TIMER_TWEEN_LENGTH:int = 600;
      
      private static const PREBATTLE_TIMER_BACKGROUND_TWEEN_LENGTH:int = 700;
      
      private static const TOP_EPIC_BATTLE_EAR_ELEMENTS_OFFSET:int = 60;
      
      private static const SUPER_PLATOON_MAX_HEIGHT:int = 160;
      
      private static const HINT_PANEL_Y_SHIFT_MULTIPLIER:Number = 1.5;
      
      private static const HINT_PANEL_AMMUNITION_OFFSET_Y:int = -160;
      
      private static const AMMUNITION_PANEL_Y_SHIFT:int = 587;
      
      private static const MESSAGE_STAGE_HEIGHT_SMALL:int = 1000;
      
      private static const UPGRADE_PANEL_MESSAGE_OFFSET:int = 230;
       
      
      public var fullStats:FrontlineFullStats = null;
      
      public var debugPanel:DebugPanel = null;
      
      public var sixthSense:SixthSense = null;
      
      public var radialMenu:RadialMenu = null;
      
      public var teamBasesPanelUI:TeamBasesPanel = null;
      
      public var damageInfoPanel:DamageInfoPanel = null;
      
      public var battleMessenger:BattleMessenger = null;
      
      public var consumablesPanel:FrontlineBattleConsumablesPanel = null;
      
      public var battleDamageLogPanel:BattleDamageLogPanel = null;
      
      public var siegeModePanel:SiegeModePanel = null;
      
      public var epicMissionsPanel:FrontlineMissionsPanel = null;
      
      public var epicScorePanelUI:FrontlineScorePanel = null;
      
      public var epicRespawnView:FrontlineRespawnView = null;
      
      public var epicDeploymentMap:FrontlineDeploymentMap = null;
      
      public var epicOverviewMapScreen:FrontlineOverviewMapScreen = null;
      
      public var endWarningPanel:BattleEndWarningPanel = null;
      
      public var recoveryPanel:RecoveryPanel = null;
      
      public var epicReinforcementPanel:FrontlineReinforcementPanel = null;
      
      public var superPlatoonPanel:FrontlinePlatoonPanel = null;
      
      public var epicInGameRank:FrontlineInGameRankPanel = null;
      
      public var hintPanel:HintPanel = null;
      
      public var prebattleTimerBackground:PrebattleTimerBg = null;
      
      public var statusNotificationsPanel:StatusNotificationsPanel = null;
      
      public var upgradePanel:FrontlineBattleUpgradePanel = null;
      
      public var modificationPanel:FrontlineModificationPanel = null;
      
      private var _scorePanelState:int = 0;
      
      private var _messagePlaying:Boolean = false;
      
      private var _countDownComplete:Boolean = false;
      
      private var _selectReservesAvailable:Boolean = true;
      
      private var _isVehPostProgressionEnabled:Boolean;
      
      public function FrontlineBattlePage()
      {
         super();
         this.battleDamageLogPanel.init(ATLAS_CONSTANTS.BATTLE_ATLAS);
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         var _loc3_:Number = param1 >> 1;
         _originalWidth = param1;
         _originalHeight = param2;
         this.upgradePanel.x = _loc3_;
         if(this.prebattleTimerBackground)
         {
            this.prebattleTimerBackground.y = 0;
            this.prebattleTimerBackground.x = _loc3_;
            this.prebattleTimerBackground.updateSize(param1,param2);
         }
         gameMessagesPanel.x = param1 >> 1;
         gameMessagesPanel.y = MSG_PNL_OFFSET;
         if(param2 >= MSG_PNL_Y_BREAKPOINT)
         {
            gameMessagesPanel.y = param2 >> 3;
         }
         if(this._messagePlaying)
         {
            this.teamBasesPanelUI.y = TEAM_BASES_PANEL_TOP_OFFSET;
         }
         else
         {
            this.teamBasesPanelUI.y = TEAM_BASES_PANEL_OFFSETS[this._scorePanelState];
         }
         this.teamBasesPanelUI.x = _loc3_;
         this.sixthSense.x = _loc3_;
         this.sixthSense.y = param2 >> 2;
         this.damageInfoPanel.y = (param2 >> 1) / stage.scaleY + DAMAGE_INFO_PANEL_CONSTS.HEIGHT * stage.scaleY | 0;
         this.damageInfoPanel.x = param1 - DAMAGE_INFO_PANEL_CONSTS.WIDTH >> 1;
         this.battleMessenger.x = damagePanel.x;
         this.epicReinforcementPanel.x = damagePanel.x;
         this.epicReinforcementPanel.y = damagePanel.y;
         this.updateChatAndReinforcementPosition();
         this.battleMessenger.updateSwapAreaHeight(damagePanel.y - (this.superPlatoonPanel.y + SUPER_PLATOON_MAX_HEIGHT));
         this.epicRespawnView.x = _loc3_;
         this.epicRespawnView.y = 0;
         this.epicOverviewMapScreen.x = _loc3_;
         this.epicOverviewMapScreen.y = 0;
         this.fullStats.updateStageSize(param1,param2);
         this.consumablesPanel.updateStage(param1,param2);
         this.radialMenu.updateStage(param1,param2);
         this.battleDamageLogPanel.x = BATTLE_DAMAGE_LOG_X_POSITION;
         this.battleDamageLogPanel.y = damagePanel.y + BATTLE_DAMAGE_LOG_Y_PADDING;
         this.battleDamageLogPanel.updateSize(param1,param2);
         this.updateBattleDamageLogPanelPosition();
         if(this._messagePlaying)
         {
            this.epicScorePanelUI.x = param1 >> 1;
            this.epicScorePanelUI.y = SCORE_PANEL_HIDDEN_OFFSET;
         }
         else
         {
            this.epicScorePanelUI.updateStage(param1,param2);
         }
         this.epicRespawnView.updateStage(param1,param2);
         this.epicRespawnView.isVehPostProgressionEnabled = this._isVehPostProgressionEnabled;
         this.epicDeploymentMap.updateStagePosition(param1,param2);
         this.epicDeploymentMap.isVehPostProgressionEnabled = this._isVehPostProgressionEnabled;
         this.epicOverviewMapScreen.updateStage(param1,param2);
         this.endWarningPanel.x = _loc3_;
         this.epicMissionsPanel.x = param1;
         this.epicMissionsPanel.y = TOP_EPIC_BATTLE_EAR_ELEMENTS_OFFSET;
         this.epicInGameRank.x = 0;
         this.epicInGameRank.y = TOP_EPIC_BATTLE_EAR_ELEMENTS_OFFSET;
         this.recoveryPanel.updateStage(param1,param2);
         this.statusNotificationsPanel.updateStage(param1,param2);
         this.updateHintPanelPosition();
         this.updateModificationPanelPosition();
      }
      
      override protected function updatePrebattleTimerPosition(param1:int) : void
      {
         prebattleTimer.x = param1;
         prebattleTimer.y = !!this._countDownComplete ? Number(PREBATTLE_TIMER_FINAL_Y_OFFSET) : Number(PREBATTLE_TIMER_Y_OFFSET);
      }
      
      override protected function initializeStatisticsController(param1:BattleStatisticDataController) : void
      {
         var _loc2_:FrontlineBattleStatisticDataController = FrontlineBattleStatisticDataController(param1);
         _loc2_.setDisplayObjectContainer(this);
         _loc2_.registerComponentController(this.fullStats);
         _loc2_.registerComponentController(battleLoading);
         _loc2_.registerComponentController(this.superPlatoonPanel);
         _loc2_.registerEpicComponentController(this.fullStats);
         _loc2_.registerEpicComponentController(battleLoading as FrontlineBattleLoading);
         _loc2_.registerEpicComponentController(minimap as FrontlineMinimap);
         _loc2_.registerEpicComponentController(this.epicRespawnView);
         _loc2_.registerEpicComponentController(this.epicMissionsPanel);
         _loc2_.registerEpicComponentController(this.epicScorePanelUI);
         _loc2_.registerEpicComponentController(this.epicOverviewMapScreen);
         _loc2_.registerEpicComponentController(this.superPlatoonPanel);
         super.initializeStatisticsController(param1);
      }
      
      override protected function configUI() : void
      {
         this.battleMessenger.addEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onBattleMessengerRequestFocusHandler);
         this.battleMessenger.addEventListener(BattleMessenger.REMOVE_FOCUS,this.onBattleMessengerRemoveFocusHandler);
         this.consumablesPanel.addEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         super.configUI();
         prebattleTimer.hideBackground();
         prebattleTimer.addEventListener(PrebattleTimerEvent.START_HIDING,this.onPrebattleTimerStartHidingHandler);
         this.epicRespawnView.mouseEnabled = false;
         this.hintPanel.addEventListener(Event.RESIZE,this.onHintPanelResizeHandler);
         this.upgradePanel.addEventListener(ComponentEvent.STATE_CHANGE,this.onUpgradePanelStateChange);
         this.radialMenu.addEventListener(Event.DEACTIVATE,this.onRedialMenuDeactivateHandler);
      }
      
      override protected function onPopulate() : void
      {
         registerComponent(this.teamBasesPanelUI,BATTLE_VIEW_ALIASES.TEAM_BASES_PANEL);
         registerComponent(this.sixthSense,BATTLE_VIEW_ALIASES.SIXTH_SENSE);
         registerComponent(this.damageInfoPanel,BATTLE_VIEW_ALIASES.DAMAGE_INFO_PANEL);
         registerComponent(this.fullStats,BATTLE_VIEW_ALIASES.FULL_STATS);
         registerComponent(this.debugPanel,BATTLE_VIEW_ALIASES.DEBUG_PANEL);
         registerComponent(this.battleMessenger,BATTLE_VIEW_ALIASES.BATTLE_MESSENGER);
         registerComponent(this.consumablesPanel,BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL);
         registerComponent(this.radialMenu,BATTLE_VIEW_ALIASES.RADIAL_MENU);
         registerComponent(this.battleDamageLogPanel,BATTLE_VIEW_ALIASES.BATTLE_DAMAGE_LOG_PANEL);
         registerComponent(this.siegeModePanel,BATTLE_VIEW_ALIASES.SIEGE_MODE_INDICATOR);
         registerComponent(this.hintPanel,BATTLE_VIEW_ALIASES.HINT_PANEL);
         registerComponent(this.statusNotificationsPanel,BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL);
         registerComponent(this.epicReinforcementPanel,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_REINFORCEMENT_PANEL);
         registerComponent(this.epicScorePanelUI,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_SCORE_PANEL);
         registerComponent(this.epicMissionsPanel,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_MISSIONS_PANEL);
         registerComponent(this.epicRespawnView,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_RESPAWN_VIEW);
         registerComponent(this.epicDeploymentMap,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_DEPLOYMENT_MAP);
         registerComponent(this.epicOverviewMapScreen,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_OVERVIEW_MAP_SCREEN);
         registerComponent(this.recoveryPanel,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_RECOVERY_PANEL);
         registerComponent(this.superPlatoonPanel,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_PLATOON_PANEL);
         registerComponent(this.epicInGameRank,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_INGAME_RANK);
         registerComponent(this.upgradePanel,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_UPGRADE_PANEL);
         registerComponent(this.modificationPanel,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_MODIFICATION_PANEL);
         super.onPopulate();
         this.endWarningPanel.alpha = 0;
      }
      
      override protected function onPrebattleAmmunitionPanelShown() : void
      {
         super.onPrebattleAmmunitionPanelShown();
         this.updateConsumablePanel();
         this.updateHintPanelPosition();
         this.updateModificationPanelPosition();
      }
      
      override protected function onPrebattleAmmunitionPanelHidden(param1:Boolean) : void
      {
         this.updateConsumablePanel(param1);
      }
      
      override protected function onRegisterStatisticController() : void
      {
         registerFlashComponentS(battleStatisticDataController,BATTLE_VIEW_ALIASES.BATTLE_STATISTIC_DATA_CONTROLLER);
      }
      
      override protected function onBeforeDispose() : void
      {
         prebattleTimer.removeEventListener(PrebattleTimerEvent.START_HIDING,this.onPrebattleTimerStartHidingHandler);
         this.battleMessenger.removeEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onBattleMessengerRequestFocusHandler);
         this.battleMessenger.removeEventListener(BattleMessenger.REMOVE_FOCUS,this.onBattleMessengerRemoveFocusHandler);
         this.consumablesPanel.removeEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         this.epicRespawnView.removeEventListener(FrontlineRespawnEvent.VIEW_CHANGED,this.onRespawnViewChangedHandler);
         this.epicScorePanelUI.removeEventListener(FrontlineScorePanelEvent.STATE_CHANGED,this.onScorePanelStateChangedHandler);
         battleLoading.removeEventListener(FrontlineBattleLoadingEvent.VISIBILITY_CHANGED,this.onBattleLoadingVisibilityChangedHandler);
         this.hintPanel.removeEventListener(Event.RESIZE,this.onHintPanelResizeHandler);
         this.radialMenu.removeEventListener(Event.DEACTIVATE,this.onRedialMenuDeactivateHandler);
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.hintPanel = null;
         this.upgradePanel.removeEventListener(ComponentEvent.STATE_CHANGE,this.onUpgradePanelStateChange);
         this.upgradePanel = null;
         this.sixthSense = null;
         this.debugPanel = null;
         this.fullStats = null;
         this.radialMenu = null;
         this.battleMessenger = null;
         this.damageInfoPanel = null;
         this.teamBasesPanelUI = null;
         this.consumablesPanel = null;
         this.battleDamageLogPanel = null;
         this.epicRespawnView = null;
         this.epicScorePanelUI = null;
         this.epicDeploymentMap = null;
         this.epicOverviewMapScreen = null;
         this.modificationPanel = null;
         this.recoveryPanel = null;
         this.endWarningPanel = null;
         this.epicMissionsPanel = null;
         this.epicReinforcementPanel = null;
         this.superPlatoonPanel = null;
         this.epicInGameRank = null;
         this.siegeModePanel = null;
         this.prebattleTimerBackground.dispose();
         this.prebattleTimerBackground = null;
         this.statusNotificationsPanel = null;
         super.onDispose();
      }
      
      override protected function initializeMessageLists() : void
      {
         super.initializeMessageLists();
         addChild(this.upgradePanel);
         swapChildren(battleLoading,this.upgradePanel);
      }
      
      override protected function getAllowedMinimapSizeIndex(param1:Number) : Number
      {
         var _loc2_:Number = App.appWidth - this.consumablesPanel.panelWidth;
         var _loc3_:Rectangle = null;
         while(param1 > MinimapSizeConst.MIN_SIZE_INDEX)
         {
            _loc3_ = minimap.getMinimapRectBySizeIndex(param1);
            if(_loc2_ - _loc3_.width >= 0)
            {
               break;
            }
            param1--;
         }
         return param1;
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.epicRespawnView.addEventListener(FrontlineRespawnEvent.VIEW_CHANGED,this.onRespawnViewChangedHandler);
         this.epicScorePanelUI.addEventListener(FrontlineScorePanelEvent.STATE_CHANGED,this.onScorePanelStateChangedHandler);
         battleLoading.addEventListener(FrontlineBattleLoadingEvent.VISIBILITY_CHANGED,this.onBattleLoadingVisibilityChangedHandler);
      }
      
      override protected function createStatisticsController() : BattleStatisticDataController
      {
         return new FrontlineBattleStatisticDataController();
      }
      
      override protected function onAllMessagesEndedPlaying(param1:String) : void
      {
         var messageType:String = param1;
         super.onAllMessagesEndedPlaying(messageType);
         if(!this._messagePlaying)
         {
            return;
         }
         this._messagePlaying = false;
         this.epicScorePanelUI.checkState();
         var scoreTween:Tween = new Tween(SCORE_PANEL_FADE_IN_TWEEN_LENGTH,this.epicScorePanelUI,{
            "alpha":1,
            "y":0
         },{
            "ease":Strong.easeInOut,
            "onComplete":function(param1:Tween):void
            {
               param1.dispose();
               param1 = null;
            }
         });
         var capBarTween:Tween = new Tween(CAPTURE_BAR_TWEEN_LENGTH,this.teamBasesPanelUI,{"y":TEAM_BASES_PANEL_OFFSETS[this._scorePanelState]},{
            "ease":Strong.easeInOut,
            "onComplete":function(param1:Tween):void
            {
               param1.dispose();
               param1 = null;
            }
         });
      }
      
      override protected function onMessagesStartedPlaying(param1:String) : void
      {
         var messageType:String = param1;
         super.onMessagesStartedPlaying(messageType);
         this._messagePlaying = true;
         var scoreTween:Tween = new Tween(SCORE_PANEL_FADE_OUT_TWEEN_LENGTH,this.epicScorePanelUI,{
            "alpha":0,
            "y":SCORE_PANEL_HIDDEN_OFFSET
         },{
            "ease":Strong.easeInOut,
            "onComplete":function(param1:Tween):void
            {
               epicScorePanelUI.checkState();
               param1.dispose();
               param1 = null;
            }
         });
         var capBarTween:Tween = new Tween(CAPTURE_BAR_TWEEN_LENGTH,this.teamBasesPanelUI,{"y":TEAM_BASES_PANEL_TOP_OFFSET},{
            "ease":Strong.easeInOut,
            "onComplete":function(param1:Tween):void
            {
               param1.dispose();
               param1 = null;
            }
         });
      }
      
      override protected function getAmmunitionPanelYShift() : int
      {
         return AMMUNITION_PANEL_Y_SHIFT;
      }
      
      public function as_setSelectReservesAvailable(param1:Boolean) : void
      {
         this._selectReservesAvailable = param1;
      }
      
      public function as_setVehPostProgressionEnabled(param1:Boolean) : void
      {
         this._isVehPostProgressionEnabled = param1;
         this.updateStage(App.appWidth,App.appHeight);
      }
      
      private function updateConsumablePanel(param1:Boolean = false) : void
      {
         if(prebattleAmmunitionPanelShown)
         {
            this.consumablesPanel.hide(param1);
         }
         else
         {
            this.consumablesPanel.show(param1);
         }
      }
      
      private function updateChatAndReinforcementPosition() : void
      {
         this.battleMessenger.y = !!this.epicRespawnView.visible ? Number(_originalHeight - this.messangerInrespawnOffsetY) : Number(damagePanel.y - this.battleMessenger.height - MESSENGER_OFFSET_Y);
      }
      
      private function updateBattleDamageLogPanelPosition() : void
      {
         var _loc1_:int = BattleDamageLogConstants.MAX_VIEW_RENDER_COUNT;
         if(this.battleDamageLogPanel.x + BattleDamageLogConstants.MAX_DAMAGE_LOG_VIEW_WIDTH >= this.consumablesPanel.x)
         {
            _loc1_ = BattleDamageLogConstants.MIN_VIEW_RENDER_COUNT;
         }
         this.battleDamageLogPanel.setDetailActionCount(_loc1_);
      }
      
      private function updateHintPanelPosition() : void
      {
         this.hintPanel.x = _originalWidth - this.hintPanel.width >> 1;
         this.hintPanel.y = HINT_PANEL_Y_SHIFT_MULTIPLIER * (_originalHeight - this.hintPanel.height >> 1) | 0;
         if(prebattleAmmunitionPanelShown)
         {
            this.hintPanel.y += HINT_PANEL_AMMUNITION_OFFSET_Y;
         }
      }
      
      private function updateModificationPanelPosition() : void
      {
         var _loc1_:int = 0;
         this.modificationPanel.x = _originalWidth >> 1;
         this.modificationPanel.y = _originalHeight - MODIFICATION_PANEL_Y_OFFSET;
         if(prebattleAmmunitionPanelShown)
         {
            _loc1_ = _originalHeight <= MODIFICATION_PANEL_Y_BREAKPOINT ? int(MODIFICATION_PANEL_Y_SHIFT_SMALL) : int(MODIFICATION_PANEL_Y_SHIFT_BIG);
            this.modificationPanel.y -= _loc1_;
         }
      }
      
      override protected function get prebattleAmmunitionPanelAvailable() : Boolean
      {
         return true;
      }
      
      private function get messangerInrespawnOffsetY() : int
      {
         return _originalHeight < StageSizeBoundaries.HEIGHT_900 ? int(MESSENGER_IN_RESPAWN_OFFSET_Y_SMALL) : int(MESSENGER_IN_RESPAWN_OFFSET_Y_BIG);
      }
      
      override protected function onMinimapSizeChangedHandler(param1:MinimapEvent) : void
      {
         super.onMinimapSizeChangedHandler(param1);
         super.updateStage(App.appWidth,App.appHeight);
      }
      
      private function onHintPanelResizeHandler(param1:Event) : void
      {
         this.updateHintPanelPosition();
      }
      
      private function onRedialMenuDeactivateHandler(param1:Event) : void
      {
         onDeactivateRadialMenuS();
      }
      
      private function onBattleMessengerRequestFocusHandler(param1:FocusRequestEvent) : void
      {
         setFocus(param1.focusContainer.getComponentForFocus());
         if(getChildIndex(this.battleMessenger) < getChildIndex(this.epicRespawnView))
         {
            swapChildren(this.battleMessenger,this.epicRespawnView);
         }
      }
      
      private function onBattleMessengerRemoveFocusHandler(param1:Event) : void
      {
         setFocus(this);
         if(getChildIndex(this.battleMessenger) > getChildIndex(this.epicRespawnView))
         {
            swapChildren(this.battleMessenger,this.epicRespawnView);
         }
      }
      
      private function onConsumablesPanelUpdatePositionHandler(param1:ConsumablesPanelEvent) : void
      {
         if(isPostMortem)
         {
            this.consumablesPanel.removeEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         }
         this.updateBattleDamageLogPanelPosition();
         minimap.updateSizeIndex(false);
      }
      
      private function onRespawnViewChangedHandler(param1:FrontlineRespawnEvent) : void
      {
         this.epicDeploymentMap.activeInRespawn(this.epicRespawnView.visible,_originalWidth,_originalHeight);
         this.updateChatAndReinforcementPosition();
      }
      
      private function onBattleLoadingVisibilityChangedHandler(param1:FrontlineBattleLoadingEvent) : void
      {
         var _loc2_:FrontlineBattleStatisticDataController = null;
         var _loc3_:FrontlineBattleLoading = null;
         this.epicDeploymentMap.activeInLoadingScreen(battleLoading.visible,_originalWidth,_originalHeight);
         if(!battleLoading.visible)
         {
            battleStatisticDataController.unregisterComponentController(battleLoading);
            _loc2_ = battleStatisticDataController as FrontlineBattleStatisticDataController;
            if(_loc2_)
            {
               _loc3_ = battleLoading as FrontlineBattleLoading;
               if(_loc3_)
               {
                  _loc2_.unregisterEpicComponentController(_loc3_);
               }
            }
            this.epicInGameRank.isActive = true;
         }
      }
      
      private function onScorePanelStateChangedHandler(param1:FrontlineScorePanelEvent) : void
      {
         var CountDownEnd:Tween = null;
         var event:FrontlineScorePanelEvent = param1;
         var scorePanelState:String = event.state;
         if(scorePanelState == FrontlineScorePanelEvent.SINGLE_ROW_STATE)
         {
            this._scorePanelState = 0;
         }
         else if(scorePanelState == FrontlineScorePanelEvent.DOUBLE_ROW_STATE)
         {
            this._scorePanelState = 1;
         }
         else if(scorePanelState == FrontlineScorePanelEvent.PRE_BATTLE_TRANSITION_START)
         {
            this._countDownComplete = true;
            CountDownEnd = new Tween(PREBATTLE_TIMER_TWEEN_LENGTH,prebattleTimer,{"y":PREBATTLE_TIMER_FINAL_Y_OFFSET},{"onComplete":function(param1:Tween):void
            {
               param1.dispose();
               param1 = null;
            }});
         }
         if(!this._messagePlaying)
         {
            this.teamBasesPanelUI.y = TEAM_BASES_PANEL_OFFSETS[this._scorePanelState];
         }
      }
      
      private function onPrebattleTimerStartHidingHandler(param1:PrebattleTimerEvent) : void
      {
         var countDownEnding:Tween = null;
         var event:PrebattleTimerEvent = param1;
         if(this.prebattleTimerBackground)
         {
            if(event.useAnim && this.prebattleTimerBackground.visible)
            {
               countDownEnding = new Tween(PREBATTLE_TIMER_BACKGROUND_TWEEN_LENGTH,this.prebattleTimerBackground,{"alpha":0},{"onComplete":function(param1:Tween):void
               {
                  prebattleTimerBackground.visible = false;
                  param1.dispose();
                  param1 = null;
               }});
            }
            else
            {
               this.prebattleTimerBackground.visible = false;
            }
         }
      }
      
      private function onUpgradePanelStateChange(param1:ComponentEvent) : void
      {
         this.vehicleErrorMessageListPositionUpdate();
      }
      
      override protected function vehicleErrorMessageListPositionUpdate() : void
      {
         var _loc1_:Boolean = true;
         if(this.upgradePanel.isActive)
         {
            if(_originalHeight < MESSAGE_STAGE_HEIGHT_SMALL)
            {
               _loc1_ = false;
            }
            else
            {
               vehicleErrorMessageList.setLocation(_originalWidth - VEHICLE_ERRORS_LIST_OFFSET.x >> 1,this.upgradePanel.y + UPGRADE_PANEL_MESSAGE_OFFSET);
            }
         }
         else
         {
            super.vehicleErrorMessageListPositionUpdate();
         }
         this.updateVehicleErrorMessageListVisible(_loc1_);
      }
      
      private function updateVehicleErrorMessageListVisible(param1:Boolean) : void
      {
         if(vehicleErrorMessageList.visible != param1)
         {
            vehicleErrorMessageList.visible = param1;
         }
      }
   }
}
