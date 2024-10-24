package net.wg.gui.battle.random.views
{
   import fl.motion.easing.Linear;
   import flash.display.DisplayObject;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.data.constants.generated.DAMAGE_INFO_PANEL_CONSTS;
   import net.wg.data.constants.generated.PLAYERS_PANEL_STATE;
   import net.wg.gui.battle.components.TimersPanel;
   import net.wg.gui.battle.interfaces.IFullStats;
   import net.wg.gui.battle.interfaces.IReservesStats;
   import net.wg.gui.battle.random.views.fragCorrelationBar.FragCorrelationBar;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.PlayersPanel;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.events.PlayersPanelEvent;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.events.PlayersPanelSwitchEvent;
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamBasesPanel;
   import net.wg.gui.battle.views.BattlePageQuestsProgress;
   import net.wg.gui.battle.views.battleEndWarning.BattleEndWarningPanel;
   import net.wg.gui.battle.views.battleEndWarning.EndWarningPanelEvent;
   import net.wg.gui.battle.views.battleHint.BattleHint;
   import net.wg.gui.battle.views.battleMessenger.BattleMessenger;
   import net.wg.gui.battle.views.battleNotifier.BattleNotifier;
   import net.wg.gui.battle.views.consumablesPanel.ConsumablesPanel;
   import net.wg.gui.battle.views.consumablesPanel.events.ConsumablesPanelEvent;
   import net.wg.gui.battle.views.damageInfoPanel.DamageInfoPanel;
   import net.wg.gui.battle.views.debugPanel.DebugPanel;
   import net.wg.gui.battle.views.mapInfoTip.MapInfoTip;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.gui.battle.views.newbieHint.NewbieHint;
   import net.wg.gui.battle.views.questProgress.interfaces.IQuestProgressView;
   import net.wg.gui.battle.views.radialMenu.RadialMenu;
   import net.wg.gui.battle.views.siegeModePanel.SiegeModePanel;
   import net.wg.gui.battle.views.sixthSense.SixthSense;
   import net.wg.gui.components.battleDamagePanel.BattleDamageLogPanel;
   import net.wg.gui.components.battleDamagePanel.constants.BattleDamageLogConstants;
   import net.wg.gui.components.hintPanel.HintPanel;
   import net.wg.infrastructure.events.FocusRequestEvent;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import scaleform.clik.motion.Tween;
   
   public class BattlePage extends BattlePageQuestsProgress
   {
      
      private static const OFFSET_MAP_INFO_X:uint = 70;
      
      private static const BATTLE_DAMAGE_LOG_X_POSITION:int = 229;
      
      private static const BATTLE_DAMAGE_LOG_Y_PADDING:int = 3;
      
      private static const MINIMAP_MARGIN_HEIGHT:int = 6;
      
      private static const MINIMAP_MARGIN_WIDTH:int = 0;
      
      private static const TWEEN_DURATION:uint = 300;
      
      private static const TEAM_BASES_PANEL_OFFSET:uint = 10;
      
      private static const MESSANGER_SWAP_AREA_TOP_OFFSET:Number = -27;
      
      private static const QUEST_PROGRESS_TOP_SHIFT:int = 45;
      
      private static const INVALID_PLAYERS_PANEL_STATE:String = "invalidPlayersPanelState";
      
      private static const HINT_PANEL_Y_SHIFT_MULTIPLIER:Number = 1.5;
      
      protected static const HINT_PANEL_AMMUNITION_OFFSET_Y:int = -160;
       
      
      public var debugPanel:DebugPanel = null;
      
      public var battleDamageLogPanel:BattleDamageLogPanel = null;
      
      public var teamBasesPanelUI:TeamBasesPanel = null;
      
      public var sixthSense:SixthSense = null;
      
      public var battleNotifier:BattleNotifier = null;
      
      public var consumablesPanel:ConsumablesPanel = null;
      
      public var destroyTimersPanel:TimersPanel = null;
      
      public var hintPanel:HintPanel = null;
      
      public var damageInfoPanel:DamageInfoPanel = null;
      
      public var battleMessenger:BattleMessenger = null;
      
      public var fragCorrelationBar:FragCorrelationBar = null;
      
      public var fullStats:IFullStats = null;
      
      public var playersPanel:PlayersPanel = null;
      
      public var radialMenu:RadialMenu = null;
      
      public var endWarningPanel:BattleEndWarningPanel = null;
      
      public var siegeModePanel:SiegeModePanel = null;
      
      public var mapInfoTip:MapInfoTip = null;
      
      public var battleHint:BattleHint = null;
      
      public var newbieHint:NewbieHint = null;
      
      private var _playersPanelState:int = -1;
      
      private var _playersPanelHasInvite:Boolean = false;
      
      private var _isPlayersPanelIsEmpty:Boolean = true;
      
      private var _teamBasesPanelY:int = 0;
      
      private var _teamBasesPanelDefaultY:int = 0;
      
      private var _tweens:Vector.<Tween>;
      
      public function BattlePage()
      {
         this._tweens = new Vector.<Tween>();
         super();
      }
      
      protected function getDamagePanelSpacing() : int
      {
         return Values.ZERO;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         var _loc3_:Number = param1 >> 1;
         this.teamBasesPanelUI.x = _loc3_;
         this.sixthSense.x = _loc3_;
         this.sixthSense.y = param2 >> 2;
         var _loc4_:Number = stage.scaleY;
         this.damageInfoPanel.y = (param2 >> 1) / _loc4_ + DAMAGE_INFO_PANEL_CONSTS.HEIGHT * _loc4_ | 0;
         this.damageInfoPanel.x = param1 - DAMAGE_INFO_PANEL_CONSTS.WIDTH >> 1;
         if(this.fragCorrelationBar)
         {
            this.fragCorrelationBar.x = _loc3_;
            this.fragCorrelationBar.updateStage(param1,param2);
         }
         if(this.destroyTimersPanel)
         {
            this.destroyTimersPanel.updateStage(param1,param2);
         }
         if(this.fullStats)
         {
            this.fullStats.updateStageSize(param1,param2);
         }
         if(this.playersPanel)
         {
            this.playersPanel.updateStageSize(param1,param2);
         }
         this.consumablesPanel.updateStage(param1,param2);
         if(this.battleHint)
         {
            this.battleHint.updateStage(param1,param2);
         }
         if(this.newbieHint)
         {
            this.newbieHint.updateStage(param1,param2);
         }
         this.battleDamageLogPanel.x = BATTLE_DAMAGE_LOG_X_POSITION;
         this.battleDamageLogPanel.y = damagePanel.y + BATTLE_DAMAGE_LOG_Y_PADDING;
         this.battleDamageLogPanel.updateSize(param1,param2);
         if(this.radialMenu)
         {
            this.radialMenu.updateStage(param1,param2);
         }
         if(this.endWarningPanel)
         {
            this.endWarningPanel.x = _loc3_;
         }
         if(this.battleNotifier)
         {
            this.battleNotifier.updateStage(param1,param2);
            if(this.radialMenu)
            {
               this.setChildIndex(this.battleNotifier,this.getChildIndex(this.radialMenu) - 1);
            }
         }
         this.updateBattleMessengerPosition();
         this.updateBattleMessengerSwapArea();
         this.updateHintPanelPosition();
         this.updateMapInfoHintLayout();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.battleDamageLogPanel.init(ATLAS_CONSTANTS.BATTLE_ATLAS);
         if(this.playersPanel)
         {
            this.playersPanel.addEventListener(Event.CHANGE,this.onPlayersPanelChangeHandler);
         }
         this.teamBasesPanelUI.addEventListener(Event.CHANGE,this.onTeamBasesPanelUIChangeHandler);
         this._teamBasesPanelY = this._teamBasesPanelDefaultY = this.teamBasesPanelUI.y;
         if(this.endWarningPanel)
         {
            this.endWarningPanel.addEventListener(EndWarningPanelEvent.VISIBILITY_CHANGED,this.onEndWarningPanelVisibilityChangedHandler);
         }
      }
      
      override protected function createStatisticsController() : BattleStatisticDataController
      {
         return new BattleStatisticDataController(this);
      }
      
      override protected function initializeStatisticsController(param1:BattleStatisticDataController) : void
      {
         if(battleLoading)
         {
            param1.registerComponentController(battleLoading);
         }
         if(this.fragCorrelationBar)
         {
            param1.registerComponentController(this.fragCorrelationBar);
         }
         if(this.fullStats)
         {
            param1.registerComponentController(this.fullStats);
         }
         if(this.playersPanel)
         {
            param1.registerComponentController(this.playersPanel);
         }
         super.initializeStatisticsController(param1);
      }
      
      override protected function configUI() : void
      {
         this.battleMessenger.addEventListener(MouseEvent.ROLL_OVER,this.onBattleMessengerRollOverHandler);
         this.battleMessenger.addEventListener(MouseEvent.ROLL_OUT,this.onBattleMessengerRollOutHandler);
         this.consumablesPanel.addEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         this.battleMessenger.addEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onBattleMessengerRequestFocusHandler);
         this.battleMessenger.addEventListener(BattleMessenger.REMOVE_FOCUS,this.onBattleMessengerRemoveFocusHandler);
         if(this.playersPanel)
         {
            this.playersPanel.addEventListener(PlayersPanelEvent.ON_ITEMS_COUNT_CHANGE,this.onPlayersPanelOnItemsCountChangeHandler);
            this.playersPanel.addEventListener(PlayersPanelSwitchEvent.STATE_REQUESTED,this.onPlayersPanelStateRequestedHandler);
         }
         this.hintPanel.addEventListener(Event.RESIZE,this.onHintPanelResizeHandler);
         super.configUI();
      }
      
      override protected function onPopulate() : void
      {
         var _loc2_:IDAAPIModule = null;
         registerComponent(this.teamBasesPanelUI,BATTLE_VIEW_ALIASES.TEAM_BASES_PANEL);
         registerComponent(this.sixthSense,BATTLE_VIEW_ALIASES.SIXTH_SENSE);
         registerComponent(this.damageInfoPanel,BATTLE_VIEW_ALIASES.DAMAGE_INFO_PANEL);
         registerComponent(this.battleDamageLogPanel,BATTLE_VIEW_ALIASES.BATTLE_DAMAGE_LOG_PANEL);
         if(this.fullStats)
         {
            registerComponent(this.fullStats,BATTLE_VIEW_ALIASES.FULL_STATS);
         }
         registerComponent(this.debugPanel,BATTLE_VIEW_ALIASES.DEBUG_PANEL);
         if(this.playersPanel)
         {
            registerComponent(this.playersPanel,BATTLE_VIEW_ALIASES.PLAYERS_PANEL);
         }
         registerComponent(this.battleMessenger,BATTLE_VIEW_ALIASES.BATTLE_MESSENGER);
         if(this.fragCorrelationBar)
         {
            registerComponent(this.fragCorrelationBar,BATTLE_VIEW_ALIASES.FRAG_CORRELATION_BAR);
         }
         registerComponent(this.consumablesPanel,BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL);
         if(this.radialMenu)
         {
            registerComponent(this.radialMenu,BATTLE_VIEW_ALIASES.RADIAL_MENU);
         }
         if(this.endWarningPanel)
         {
            registerComponent(this.endWarningPanel,BATTLE_VIEW_ALIASES.BATTLE_END_WARNING_PANEL);
         }
         registerComponent(this.siegeModePanel,BATTLE_VIEW_ALIASES.SIEGE_MODE_INDICATOR);
         registerComponent(this.hintPanel,BATTLE_VIEW_ALIASES.HINT_PANEL);
         if(this.battleHint)
         {
            registerComponent(this.battleHint,BATTLE_VIEW_ALIASES.BATTLE_HINT);
         }
         if(this.newbieHint)
         {
            registerComponent(this.newbieHint,BATTLE_VIEW_ALIASES.NEWBIE_HINT);
         }
         if(this.mapInfoTip)
         {
            registerComponent(this.mapInfoTip,BATTLE_VIEW_ALIASES.MAP_INFO_TIP);
         }
         if(this.destroyTimersPanel)
         {
            registerComponent(this.destroyTimersPanel,BATTLE_VIEW_ALIASES.TIMERS_PANEL);
         }
         if(this.battleNotifier)
         {
            registerComponent(this.battleNotifier,BATTLE_VIEW_ALIASES.BATTLE_NOTIFIER);
         }
         var _loc1_:IReservesStats = this.fullStats as IReservesStats;
         if(_loc1_)
         {
            _loc2_ = _loc1_.getReservesView();
            if(_loc2_)
            {
               registerComponent(_loc2_,BATTLE_VIEW_ALIASES.PERSONAL_RESERVES_TAB);
            }
         }
         super.onPopulate();
      }
      
      override protected function onRegisterStatisticController() : void
      {
         registerFlashComponentS(battleStatisticDataController,BATTLE_VIEW_ALIASES.BATTLE_STATISTIC_DATA_CONTROLLER);
      }
      
      override protected function onBeforeDispose() : void
      {
         this.battleMessenger.removeEventListener(MouseEvent.ROLL_OVER,this.onBattleMessengerRollOverHandler);
         this.battleMessenger.removeEventListener(MouseEvent.ROLL_OUT,this.onBattleMessengerRollOutHandler);
         if(this.playersPanel)
         {
            this.playersPanel.removeEventListener(Event.CHANGE,this.onPlayersPanelChangeHandler);
            this.playersPanel.removeEventListener(PlayersPanelSwitchEvent.STATE_REQUESTED,this.onPlayersPanelStateRequestedHandler);
            this.playersPanel.removeEventListener(PlayersPanelEvent.ON_ITEMS_COUNT_CHANGE,this.onPlayersPanelOnItemsCountChangeHandler);
         }
         this.teamBasesPanelUI.removeEventListener(Event.CHANGE,this.onTeamBasesPanelUIChangeHandler);
         this.consumablesPanel.removeEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         this.battleMessenger.removeEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onBattleMessengerRequestFocusHandler);
         this.battleMessenger.removeEventListener(BattleMessenger.REMOVE_FOCUS,this.onBattleMessengerRemoveFocusHandler);
         this.battleMessenger = null;
         if(this.endWarningPanel)
         {
            this.endWarningPanel.removeEventListener(EndWarningPanelEvent.VISIBILITY_CHANGED,this.onEndWarningPanelVisibilityChangedHandler);
         }
         this.hintPanel.removeEventListener(Event.RESIZE,this.onHintPanelResizeHandler);
         this.clearTweens();
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.hintPanel = null;
         this.debugPanel = null;
         this.teamBasesPanelUI = null;
         this.sixthSense = null;
         this.damageInfoPanel = null;
         this.fragCorrelationBar = null;
         this.fullStats = null;
         this.playersPanel = null;
         this.consumablesPanel = null;
         this.destroyTimersPanel = null;
         this.radialMenu = null;
         this.endWarningPanel = null;
         this.battleDamageLogPanel = null;
         this.siegeModePanel = null;
         this.battleNotifier = null;
         this.mapInfoTip = null;
         this.battleHint = null;
         this.newbieHint = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INVALID_PLAYERS_PANEL_STATE))
         {
            this.updateDamageLogPosition();
         }
      }
      
      override protected function getAllowedMinimapSizeIndex(param1:Number) : Number
      {
         var _loc2_:Number = this.getAvailableMinimapHeight() - MINIMAP_MARGIN_HEIGHT;
         var _loc3_:Number = this.getAvailableMinimapWidth() - MINIMAP_MARGIN_WIDTH;
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
      
      protected function getAvailableMinimapHeight() : Number
      {
         var _loc1_:Number = Values.ZERO;
         if(this.playersPanel)
         {
            _loc1_ = this.playersPanel.panelHeight;
         }
         return App.appHeight - _loc1_;
      }
      
      protected function getAvailableMinimapWidth() : Number
      {
         return App.appWidth - this.consumablesPanel.panelWidth;
      }
      
      override protected function playerMessageListPositionUpdate() : void
      {
         if(minimap.visible)
         {
            playerMessageList.setLocation(_originalWidth - PLAYER_MESSAGES_LIST_OFFSET.x | 0,_originalHeight - minimap.getMessageCoordinate() + PLAYER_MESSAGES_LIST_OFFSET.y);
         }
         else
         {
            playerMessageList.setLocation(_originalWidth - PLAYER_MESSAGES_LIST_OFFSET.x | 0,this.battleMessenger.y);
         }
      }
      
      override protected function updateBattleDamageLogPosInPostmortem() : void
      {
         var _loc1_:int = BattleDamageLogConstants.MAX_VIEW_RENDER_COUNT;
         var _loc2_:int = postmortemPanelUI.x - (postmortemPanelUI.width >> 1);
         if(this.battleDamageLogPanel.x + BattleDamageLogConstants.MAX_DAMAGE_LOG_VIEW_WIDTH >= _loc2_)
         {
            _loc1_ = BattleDamageLogConstants.MIN_VIEW_RENDERER_COUNT_IN_POSTMORTEM;
         }
         this.battleDamageLogPanel.setDetailActionCount(_loc1_);
      }
      
      override protected function onComponentVisibilityChanged(param1:String, param2:Boolean) : void
      {
         super.onComponentVisibilityChanged(param1,param2);
         if(param1 == BATTLE_VIEW_ALIASES.MINIMAP)
         {
            this.playerMessageListPositionUpdate();
         }
         if(param1 == BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL && param2 && prebattleAmmunitionPanelShown)
         {
            this.updateConsumablePanel(false);
         }
         if(param1 == BATTLE_VIEW_ALIASES.FRAG_CORRELATION_BAR)
         {
            this.updateTeamBasesPanelPosition(true);
         }
      }
      
      override protected function getFullStatsTabQuestProgress() : IQuestProgressView
      {
         if(this.fullStats)
         {
            return this.fullStats.getStatsProgressView();
         }
         return null;
      }
      
      override protected function onPrebattleAmmunitionPanelShown() : void
      {
         super.onPrebattleAmmunitionPanelShown();
         this.updateConsumablePanel();
         this.updateHintPanelPosition();
      }
      
      override protected function onPrebattleAmmunitionPanelHidden(param1:Boolean) : void
      {
         super.onPrebattleAmmunitionPanelHidden(false);
         this.updateConsumablePanel(param1);
      }
      
      protected function updateMapInfoHintLayout() : void
      {
         if(this.mapInfoTip)
         {
            this.mapInfoTip.x = _originalWidth - OFFSET_MAP_INFO_X - this.mapInfoTip.width | 0;
            this.mapInfoTip.updateLayout(_originalWidth);
         }
      }
      
      protected function updateBattleMessengerSwapArea() : void
      {
         var _loc1_:Number = Values.ZERO;
         if(this.playersPanel)
         {
            _loc1_ = this.playersPanel.y + this.playersPanel.height;
         }
         this.battleMessenger.updateSwapAreaHeight(damagePanel.y - _loc1_ + MESSANGER_SWAP_AREA_TOP_OFFSET);
      }
      
      protected function updateHintPanelPosition() : void
      {
         this.hintPanel.x = _originalWidth - this.hintPanel.width >> 1;
         this.hintPanel.y = HINT_PANEL_Y_SHIFT_MULTIPLIER * (_originalHeight - this.hintPanel.height >> 1) ^ 0;
         if(prebattleAmmunitionPanelShown)
         {
            this.hintPanel.y += HINT_PANEL_AMMUNITION_OFFSET_Y;
         }
      }
      
      protected function updateBattleMessengerPosition() : void
      {
         this.battleMessenger.x = damagePanel.x;
         this.battleMessenger.y = damagePanel.y - this.battleMessenger.height + MESSENGER_Y_OFFSET - this.getDamagePanelSpacing();
      }
      
      override protected function setComponentsVisibility(param1:Vector.<String>, param2:Vector.<String>) : void
      {
         var _loc3_:Boolean = this.teamBasesPanelUI.isCompVisible();
         super.setComponentsVisibility(param1,param2);
         if(this.teamBasesPanelUI.isCompVisible() != _loc3_)
         {
            this.updateTeamBasesPanelPosition();
         }
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
      
      private function updatePositionForQuestProgress() : void
      {
         var _loc1_:int = 0;
         if(this.endWarningPanel)
         {
            this.endWarningPanel.y = this._teamBasesPanelY + this.teamBasesPanelUI.panelHeight;
         }
         if(isQuestProgress)
         {
            _loc1_ = this._teamBasesPanelY + QUEST_PROGRESS_TOP_SHIFT;
            if(this.endWarningPanel)
            {
               _loc1_ += this.endWarningPanel.panelHeight;
            }
            _loc1_ += this.teamBasesPanelUI.panelHeight;
            updatePositionQuestProgressTop(_loc1_);
         }
      }
      
      private function checkZIndexes(param1:DisplayObject, param2:DisplayObject) : Boolean
      {
         return this.getChildIndex(param1) > this.getChildIndex(param2);
      }
      
      protected function updateBattleDamageLogPanelPosition() : void
      {
         var _loc1_:int = BattleDamageLogConstants.MAX_VIEW_RENDER_COUNT;
         if(this.battleDamageLogPanel.x + BattleDamageLogConstants.MAX_DAMAGE_LOG_VIEW_WIDTH >= this.consumablesPanel.x)
         {
            _loc1_ = BattleDamageLogConstants.MIN_VIEW_RENDER_COUNT;
         }
         this.battleDamageLogPanel.setDetailActionCount(_loc1_);
      }
      
      private function swapElementsByMouseInteraction(param1:DisplayObject, param2:DisplayObject) : void
      {
         if(!App.contextMenuMgr.isShown() && this.checkZIndexes(param1,param2))
         {
            this.swapChildren(param1,param2);
         }
      }
      
      protected function updateDamageLogPosition() : void
      {
         if(this.playersPanel && (this._playersPanelHasInvite || this._playersPanelState > PLAYERS_PANEL_STATE.HIDDEN))
         {
            this.battleDamageLogPanel.updateTopContainerPosition(this.playersPanel.listLeft.getRenderersVisibleWidth() + BattleDamageLogPanel.PLAYERS_PANEL_OFFSET);
         }
         else
         {
            this.battleDamageLogPanel.updateTopContainerPosition(BattleDamageLogPanel.SCREEN_BORDER_X_POS);
         }
      }
      
      override protected function get prebattleAmmunitionPanelAvailable() : Boolean
      {
         return true;
      }
      
      private function onHintPanelResizeHandler(param1:Event) : void
      {
         this.updateHintPanelPosition();
      }
      
      private function onEndWarningPanelVisibilityChangedHandler(param1:EndWarningPanelEvent) : void
      {
         this.updatePositionForQuestProgress();
      }
      
      private function onTeamBasesPanelUIChangeHandler(param1:Event) : void
      {
         this.updateTeamBasesPanelPosition(true);
      }
      
      private function onPlayersPanelStateRequestedHandler(param1:PlayersPanelSwitchEvent) : void
      {
         this._playersPanelState = param1.state;
         this._playersPanelHasInvite = this.playersPanel.isInviteReceived;
         invalidate(INVALID_PLAYERS_PANEL_STATE);
      }
      
      private function onPlayersPanelChangeHandler(param1:Event) : void
      {
         this.updateBattleMessengerSwapArea();
         if(this._isPlayersPanelIsEmpty || this._playersPanelHasInvite != this.playersPanel.isInviteReceived)
         {
            this._isPlayersPanelIsEmpty = false;
            this._playersPanelState = this.playersPanel.state;
            this._playersPanelHasInvite = this.playersPanel.isInviteReceived;
            invalidate(INVALID_PLAYERS_PANEL_STATE);
         }
      }
      
      private function onBattleMessengerRollOutHandler(param1:MouseEvent) : void
      {
         if(!this.battleMessenger.isEnterButtonPressed && this.playersPanel)
         {
            this.swapElementsByMouseInteraction(this.battleMessenger,this.playersPanel);
         }
      }
      
      private function onBattleMessengerRollOverHandler(param1:MouseEvent) : void
      {
         if(this.playersPanel != null)
         {
            this.swapElementsByMouseInteraction(this.playersPanel,this.battleMessenger);
         }
      }
      
      private function onBattleMessengerRequestFocusHandler(param1:FocusRequestEvent) : void
      {
         setFocus(param1.focusContainer.getComponentForFocus());
         if(this.playersPanel != null)
         {
            if(this.battleMessenger.isEnterButtonPressed)
            {
               this.swapElementsByMouseInteraction(this.playersPanel,this.battleMessenger);
            }
            else
            {
               this.swapElementsByMouseInteraction(this.battleMessenger,this.playersPanel);
            }
         }
      }
      
      private function onBattleMessengerRemoveFocusHandler(param1:Event) : void
      {
         setFocus(this);
         if(this.playersPanel != null)
         {
            this.swapElementsByMouseInteraction(this.playersPanel,this.battleMessenger);
         }
      }
      
      private function onPlayersPanelOnItemsCountChangeHandler(param1:PlayersPanelEvent) : void
      {
         minimap.updateSizeIndex(false);
         invalidate(INVALID_PLAYERS_PANEL_STATE);
      }
      
      private function onConsumablesPanelUpdatePositionHandler(param1:ConsumablesPanelEvent) : void
      {
         minimap.updateSizeIndex(false);
         this.consumablesPanelUpdatePosition();
      }
      
      protected function consumablesPanelUpdatePosition() : void
      {
         if(isPostMortem)
         {
            this.consumablesPanel.removeEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
            this.updateBattleDamageLogPosInPostmortem();
         }
         else
         {
            this.updateBattleDamageLogPanelPosition();
         }
      }
      
      private function updateTeamBasesPanelPosition(param1:Boolean = false) : void
      {
         var _loc2_:int = 0;
         this._teamBasesPanelY = this.fragCorrelationBar != null && this.fragCorrelationBar.isCompVisible() ? int(this._teamBasesPanelDefaultY) : int(TEAM_BASES_PANEL_OFFSET);
         this.clearTweens();
         if(this.teamBasesPanelUI.y != this._teamBasesPanelY)
         {
            if(param1)
            {
               this._tweens.push(new Tween(TWEEN_DURATION,this.teamBasesPanelUI,{"y":this._teamBasesPanelY},{"ease":Linear.easeIn}));
            }
            else
            {
               this.teamBasesPanelUI.y = this._teamBasesPanelY;
            }
         }
         this.updatePositionForQuestProgress();
         if(this.newbieHint)
         {
            _loc2_ = Boolean(this.teamBasesPanelUI.panelHeight) ? int(this._teamBasesPanelY + this.teamBasesPanelUI.panelHeight | 0) : int(0);
            if(this.newbieHint.y != _loc2_)
            {
               if(param1)
               {
                  this._tweens.push(new Tween(TWEEN_DURATION,this.newbieHint,{"y":_loc2_},{"ease":Linear.easeIn}));
               }
               else
               {
                  this.newbieHint.y = _loc2_;
               }
            }
         }
      }
      
      private function clearTweens() : void
      {
         var _loc1_:Tween = null;
         if(this._tweens.length > 0)
         {
            for each(_loc1_ in this._tweens)
            {
               _loc1_.dispose();
               _loc1_ = null;
            }
            this._tweens.length = 0;
         }
      }
   }
}
