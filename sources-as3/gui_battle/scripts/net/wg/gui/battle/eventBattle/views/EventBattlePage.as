package net.wg.gui.battle.eventBattle.views
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.data.constants.generated.DAMAGE_INFO_PANEL_CONSTS;
   import net.wg.gui.battle.components.StatusNotificationsPanel;
   import net.wg.gui.battle.eventBattle.views.battleHints.EventBattleHint;
   import net.wg.gui.battle.eventBattle.views.battleHints.EventObjectives;
   import net.wg.gui.battle.eventBattle.views.buffsPanel.BuffsPanel;
   import net.wg.gui.battle.eventBattle.views.eventPlayersPanel.EventPlayersPanel;
   import net.wg.gui.battle.eventBattle.views.eventPointCounter.EventPointCounter;
   import net.wg.gui.battle.eventBattle.views.eventStats.EventStats;
   import net.wg.gui.battle.eventBattle.views.eventTimer.EventTimer;
   import net.wg.gui.battle.views.BaseBattlePage;
   import net.wg.gui.battle.views.battleMessenger.BattleMessenger;
   import net.wg.gui.battle.views.consumablesPanel.ConsumablesPanel;
   import net.wg.gui.battle.views.consumablesPanel.events.ConsumablesPanelEvent;
   import net.wg.gui.battle.views.damageInfoPanel.DamageInfoPanel;
   import net.wg.gui.battle.views.debugPanel.DebugPanel;
   import net.wg.gui.battle.views.radialMenu.RadialMenu;
   import net.wg.gui.battle.views.sixthSense.SixthSense;
   import net.wg.gui.components.battleDamagePanel.BattleDamageLogPanel;
   import net.wg.gui.components.battleDamagePanel.constants.BattleDamageLogConstants;
   import net.wg.gui.components.hintPanel.HintPanel;
   import net.wg.infrastructure.events.FocusRequestEvent;
   
   public class EventBattlePage extends BaseBattlePage
   {
      
      private static const BATTLE_DAMAGE_LOG_X_POSITION:int = 229;
      
      private static const BATTLE_DAMAGE_LOG_Y_PADDING:int = 3;
      
      private static const HINT_PANEL_Y_SHIFT_MULTIPLIER:Number = 1.5;
      
      private static const POINT_COUNTER_HEIGHT:int = 160;
      
      private static const VEHICLE_MESSAGES_LIST_OFFSET_Y:int = 106;
      
      private static const BUFF_PANEL_OFFSET_Y:int = 135;
      
      private static const PANEL_VEHICLES_OFFSET:int = 61;
       
      
      public var debugPanel:DebugPanel = null;
      
      public var battleDamageLogPanel:BattleDamageLogPanel = null;
      
      public var sixthSense:SixthSense = null;
      
      public var consumablesPanel:ConsumablesPanel = null;
      
      public var statusNotificationsPanel:StatusNotificationsPanel = null;
      
      public var hintPanel:HintPanel = null;
      
      public var damageInfoPanel:DamageInfoPanel = null;
      
      public var battleMessenger:BattleMessenger = null;
      
      public var fullStats:EventStats = null;
      
      public var radialMenu:RadialMenu = null;
      
      public var playersPanelEvent:EventPlayersPanel = null;
      
      public var eventMessage:EventBattleHint = null;
      
      public var eventPointCounter:EventPointCounter = null;
      
      public var eventTimer:EventTimer = null;
      
      public var buffsPanel:BuffsPanel = null;
      
      public var eventObjectives:EventObjectives = null;
      
      public function EventBattlePage()
      {
         super();
         this.battleDamageLogPanel.init(ATLAS_CONSTANTS.BATTLE_ATLAS);
         battleTimer.visible = false;
      }
      
      override public function as_onPostmortemActive(param1:Boolean) : void
      {
         super.as_onPostmortemActive(param1);
         if(!param1 && !this.consumablesPanel.hasEventListener(ConsumablesPanelEvent.UPDATE_POSITION))
         {
            this.consumablesPanel.addEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         }
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         this.battleDamageLogPanel.x = BATTLE_DAMAGE_LOG_X_POSITION;
         this.battleDamageLogPanel.y = damagePanel.y + BATTLE_DAMAGE_LOG_Y_PADDING >> 0;
         this.battleDamageLogPanel.updateSize(param1,param2);
         var _loc3_:uint = param1 >> 1;
         var _loc4_:uint = param2 >> 1;
         this.sixthSense.x = _loc3_;
         this.sixthSense.y = param2 >> 2;
         this.consumablesPanel.updateStage(param1,param2);
         this.statusNotificationsPanel.updateStage(param1,param2);
         this.damageInfoPanel.y = (param2 >> 1) / scaleY + DAMAGE_INFO_PANEL_CONSTS.HEIGHT * scaleY | 0;
         this.damageInfoPanel.x = param1 - DAMAGE_INFO_PANEL_CONSTS.WIDTH >> 1;
         this.radialMenu.updateStage(param1,param2);
         this.eventMessage.updateStage(param1,param2);
         this.fullStats.updateStageSize(param1,param2);
         this.fullStats.x = _loc3_;
         this.fullStats.y = _loc4_;
         this.eventTimer.x = _loc3_;
         this.eventObjectives.x = param1 - this.eventObjectives.width >> 0;
         this.buffsPanel.x = _loc3_;
         this.buffsPanel.y = App.appHeight - BUFF_PANEL_OFFSET_Y;
         this.battleMessenger.x = damagePanel.x;
         this.battleMessenger.y = damagePanel.y - this.battleMessenger.height + MESSENGER_Y_OFFSET - PANEL_VEHICLES_OFFSET >> 0;
         this.updateHintPanelPosition();
         this.updateConsumablesPanelPosition();
      }
      
      override protected function configUI() : void
      {
         this.battleMessenger.addEventListener(MouseEvent.ROLL_OVER,this.onBattleMessengerRollOverHandler);
         this.battleMessenger.addEventListener(MouseEvent.ROLL_OUT,this.onBattleMessengerRollOutHandler);
         this.consumablesPanel.addEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         this.battleMessenger.addEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onBattleMessengerRequestFocusHandler);
         this.battleMessenger.addEventListener(BattleMessenger.REMOVE_FOCUS,this.onBattleMessengerRemoveFocusHandler);
         this.hintPanel.addEventListener(Event.RESIZE,this.onHintPanelResizeHandler);
         super.configUI();
      }
      
      override protected function onPopulate() : void
      {
         registerComponent(this.debugPanel,BATTLE_VIEW_ALIASES.DEBUG_PANEL);
         registerComponent(this.battleDamageLogPanel,BATTLE_VIEW_ALIASES.BATTLE_DAMAGE_LOG_PANEL);
         registerComponent(this.sixthSense,BATTLE_VIEW_ALIASES.SIXTH_SENSE);
         registerComponent(this.battleMessenger,BATTLE_VIEW_ALIASES.BATTLE_MESSENGER);
         registerComponent(this.consumablesPanel,BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL);
         registerComponent(this.statusNotificationsPanel,BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL);
         registerComponent(this.hintPanel,BATTLE_VIEW_ALIASES.HINT_PANEL);
         registerComponent(this.damageInfoPanel,BATTLE_VIEW_ALIASES.DAMAGE_INFO_PANEL);
         registerComponent(this.fullStats,BATTLE_VIEW_ALIASES.EVENT_STATS);
         registerComponent(this.playersPanelEvent,BATTLE_VIEW_ALIASES.PLAYERS_PANEL_EVENT);
         registerComponent(this.eventMessage,BATTLE_VIEW_ALIASES.BATTLE_HINT);
         registerComponent(this.eventTimer,BATTLE_VIEW_ALIASES.EVENT_TIMER);
         registerComponent(this.buffsPanel,BATTLE_VIEW_ALIASES.EVENT_BUFFS_PANEL);
         registerComponent(this.eventPointCounter,BATTLE_VIEW_ALIASES.EVENT_POINT_COUNTER);
         registerComponent(this.radialMenu,BATTLE_VIEW_ALIASES.RADIAL_MENU);
         registerComponent(this.eventObjectives,BATTLE_VIEW_ALIASES.EVENT_OBJECTIVES);
         super.onPopulate();
      }
      
      override protected function onDispose() : void
      {
         this.consumablesPanel.removeEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
         this.consumablesPanel = null;
         this.battleMessenger.removeEventListener(MouseEvent.ROLL_OVER,this.onBattleMessengerRollOverHandler);
         this.battleMessenger.removeEventListener(MouseEvent.ROLL_OUT,this.onBattleMessengerRollOutHandler);
         this.battleMessenger.removeEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onBattleMessengerRequestFocusHandler);
         this.battleMessenger.removeEventListener(BattleMessenger.REMOVE_FOCUS,this.onBattleMessengerRemoveFocusHandler);
         this.battleMessenger = null;
         this.hintPanel.removeEventListener(Event.RESIZE,this.onHintPanelResizeHandler);
         this.hintPanel = null;
         this.debugPanel = null;
         this.battleDamageLogPanel = null;
         this.sixthSense = null;
         this.statusNotificationsPanel = null;
         this.damageInfoPanel = null;
         this.fullStats = null;
         this.radialMenu = null;
         this.playersPanelEvent = null;
         this.eventMessage = null;
         this.eventObjectives = null;
         this.eventPointCounter = null;
         this.buffsPanel = null;
         this.eventTimer = null;
         super.onDispose();
      }
      
      override protected function vehicleMessageListPositionUpdate() : void
      {
         if(postmortemPanelUI && postmortemPanelUI.visible)
         {
            super.vehicleMessageListPositionUpdate();
         }
         else
         {
            vehicleMessageList.setLocation(_originalWidth - VEHICLE_MESSAGES_LIST_OFFSET.x >> 1,_originalHeight - VEHICLE_MESSAGES_LIST_OFFSET_Y | 0);
         }
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
         this.hintPanel.y = HINT_PANEL_Y_SHIFT_MULTIPLIER * (_originalHeight - this.hintPanel.height >> 1) ^ 0;
      }
      
      private function updateConsumablesPanelPosition() : void
      {
         this.eventPointCounter.x = App.appWidth >> 1;
         this.eventPointCounter.y = App.appHeight - POINT_COUNTER_HEIGHT;
      }
      
      private function swapElementsByMouseInteraction(param1:DisplayObject, param2:DisplayObject) : void
      {
         if(!App.contextMenuMgr.isShown() && this.checkZIndexes(param1,param2))
         {
            this.swapChildren(param1,param2);
         }
      }
      
      private function checkZIndexes(param1:DisplayObject, param2:DisplayObject) : Boolean
      {
         return this.getChildIndex(param1) > this.getChildIndex(param2);
      }
      
      private function onBattleMessengerRollOutHandler(param1:MouseEvent) : void
      {
         if(!this.battleMessenger.isEnterButtonPressed)
         {
            this.swapElementsByMouseInteraction(this.battleMessenger,this.playersPanelEvent);
         }
      }
      
      private function onBattleMessengerRollOverHandler(param1:MouseEvent) : void
      {
         this.swapElementsByMouseInteraction(this.playersPanelEvent,this.battleMessenger);
      }
      
      private function onBattleMessengerRequestFocusHandler(param1:FocusRequestEvent) : void
      {
         setFocus(param1.focusContainer.getComponentForFocus());
         if(this.battleMessenger.isEnterButtonPressed)
         {
            this.swapElementsByMouseInteraction(this.playersPanelEvent,this.battleMessenger);
         }
         else
         {
            this.swapElementsByMouseInteraction(this.battleMessenger,this.playersPanelEvent);
         }
      }
      
      private function onBattleMessengerRemoveFocusHandler(param1:Event) : void
      {
         setFocus(this);
         this.swapElementsByMouseInteraction(this.playersPanelEvent,this.battleMessenger);
      }
      
      private function onConsumablesPanelUpdatePositionHandler(param1:ConsumablesPanelEvent) : void
      {
         if(isPostMortem)
         {
            this.consumablesPanel.removeEventListener(ConsumablesPanelEvent.UPDATE_POSITION,this.onConsumablesPanelUpdatePositionHandler);
            updateBattleDamageLogPosInPostmortem();
         }
         else
         {
            this.updateBattleDamageLogPanelPosition();
         }
         minimap.updateSizeIndex(false);
      }
      
      private function onHintPanelResizeHandler(param1:Event) : void
      {
         this.updateHintPanelPosition();
      }
   }
}
