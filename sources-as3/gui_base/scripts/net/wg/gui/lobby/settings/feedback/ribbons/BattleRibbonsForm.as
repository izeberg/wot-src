package net.wg.gui.lobby.settings.feedback.ribbons
{
   import flash.display.DisplayObject;
   import flash.text.TextFormatAlign;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.BATTLE_EFFICIENCY_TYPES;
   import net.wg.gui.components.controls.CheckBox;
   import net.wg.gui.components.controls.ResizableScrollPane;
   import net.wg.gui.components.controls.ScrollBar;
   import net.wg.gui.lobby.settings.config.SettingsConfigHelper;
   import net.wg.gui.lobby.settings.events.SettingsGroupEvent;
   import net.wg.gui.lobby.settings.feedback.FeedbackBaseForm;
   import net.wg.infrastructure.interfaces.IDisplayObject;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterProps;
   
   public class BattleRibbonsForm extends FeedbackBaseForm
   {
      
      private static const RIBBONS_COUNTER_CONTAINER_ID:String = "RIBBONS_COUNTER_CONTAINER_ID ";
      
      private static const COUNTER_CHECKBOX_OFFSET_X:Number = -27;
      
      private static const COUNTER_CONTROLS_GROUP_OFFSET_X:Number = -11;
      
      private static const COUNTER_CONTROLS_GROUP_OFFSET_Y:Number = 3;
      
      private static const SCROLL_STEP_FACTOR:int = 30;
      
      private static const CONTROLS_SCROLL_PANE_WIDTH:uint = 200;
      
      private static const CONTROLS_SCROLL_PANE_HEIGHT:uint = 494;
      
      private static const RIBBONS_SCROLL_PANE_WIDTH:uint = 550;
      
      private static const RIBBONS_SCROLL_PANE_HEIGHT:uint = 460;
       
      
      public var controlsContainer:ControlsContainer = null;
      
      public var controlsScrollBar:ScrollBar = null;
      
      public var controlsScrollPane:ResizableScrollPane = null;
      
      public var ribbonsContainer:SettingsRibbonContainer = null;
      
      public var infoView:InfoView = null;
      
      public var ribbonsScrollBar:ScrollBar = null;
      
      public var ribbonsScrollPane:ResizableScrollPane = null;
      
      private var _itemsMap:Dictionary = null;
      
      public function BattleRibbonsForm()
      {
         super();
         this._itemsMap = new Dictionary();
         this._itemsMap["battleEventsReceivedDamageCheckbox"] = BATTLE_EFFICIENCY_TYPES.RECEIVED_DAMAGE;
         this._itemsMap["battleEventsReceivedCritsCheckbox"] = BATTLE_EFFICIENCY_TYPES.RECEIVED_CRITS;
         this._itemsMap["battleEventsBlockedDamageCheckbox"] = BATTLE_EFFICIENCY_TYPES.ARMOR;
         this._itemsMap["battleEventsBaseCaptureDropCheckbox"] = BATTLE_EFFICIENCY_TYPES.DEFENCE;
         this._itemsMap["battleEventsBaseCaptureCheckbox"] = BATTLE_EFFICIENCY_TYPES.CAPTURE;
         this._itemsMap["battleEventsEnemyDetectionCheckbox"] = BATTLE_EFFICIENCY_TYPES.DETECTION;
         this._itemsMap["battleEventsEnemyRamAttackCheckbox"] = BATTLE_EFFICIENCY_TYPES.RAM;
         this._itemsMap["battleEventsEnemyKillCheckbox"] = BATTLE_EFFICIENCY_TYPES.DESTRUCTION;
         this._itemsMap["battleEventsEnemyTrackDamageCheckbox"] = BATTLE_EFFICIENCY_TYPES.ASSIST_TRACK;
         this._itemsMap["battleEventsEnemyCriticalHitCheckbox"] = BATTLE_EFFICIENCY_TYPES.CRITS;
         this._itemsMap["battleEventsEnemyHpDamageCheckbox"] = BATTLE_EFFICIENCY_TYPES.DAMAGE;
         this._itemsMap["battleEventsEnemyWorldCollisionCheckbox"] = BATTLE_EFFICIENCY_TYPES.WORLD_COLLISION;
         this._itemsMap["battleEventsEnemyDetectionDamageCheckbox"] = BATTLE_EFFICIENCY_TYPES.ASSIST_SPOT;
         this._itemsMap["battleEventsEnemyAssistStunCheckbox"] = BATTLE_EFFICIENCY_TYPES.ASSIST_STUN;
         this._itemsMap["battleEventsEnemyBurningCheckbox"] = BATTLE_EFFICIENCY_TYPES.BURN;
         this._itemsMap["commander_eagleEyeCheckbox"] = BATTLE_EFFICIENCY_TYPES.COMMANDER_EAGLE_EYE;
         this._itemsMap["commander_emergencyCheckbox"] = BATTLE_EFFICIENCY_TYPES.COMMANDER_EMERGENCY;
         this._itemsMap["commander_tutorCheckbox"] = BATTLE_EFFICIENCY_TYPES.COMMANDER_TUTOR;
         this._itemsMap["commander_coordinationCheckbox"] = BATTLE_EFFICIENCY_TYPES.COMMANDER_COORDINATION;
         this._itemsMap["commander_holdLineCheckbox"] = BATTLE_EFFICIENCY_TYPES.COMMANDER_HOLD_LINE;
         this._itemsMap["commander_staySharpCheckbox"] = BATTLE_EFFICIENCY_TYPES.COMMANDER_STAY_SHARP;
         this._itemsMap["gunner_focusCheckbox"] = BATTLE_EFFICIENCY_TYPES.GUNNER_FOCUS;
         this._itemsMap["gunner_loneWolfCheckbox"] = BATTLE_EFFICIENCY_TYPES.GUNNER_LONE_WOLF;
         this._itemsMap["driver_motorExpertCheckbox"] = BATTLE_EFFICIENCY_TYPES.DRIVER_MOTOR_EXPERT;
         this._itemsMap["driver_suspensionRepairCheckbox"] = BATTLE_EFFICIENCY_TYPES.DRIVER_SUSPENSION_REPAIR;
         this._itemsMap["driver_bulletproofCheckbox"] = BATTLE_EFFICIENCY_TYPES.DRIVER_BULLETPROOF;
         this._itemsMap["loader_desperadoCheckbox"] = BATTLE_EFFICIENCY_TYPES.LOADER_DESPERADO;
         this._itemsMap["loader_intuitionCheckbox"] = BATTLE_EFFICIENCY_TYPES.LOADER_INTUITION;
         this._itemsMap["loader_meleeCheckbox"] = BATTLE_EFFICIENCY_TYPES.LOADER_MELEE;
         this._itemsMap["loader_secondChanceCheckbox"] = BATTLE_EFFICIENCY_TYPES.LOADER_SECOND_CHANCE;
         this._itemsMap["radioman_sideBySideCheckbox"] = BATTLE_EFFICIENCY_TYPES.RADIOMAN_SIDE_BY_SIDE;
         this._itemsMap["radioman_expertCheckbox"] = BATTLE_EFFICIENCY_TYPES.RADIOMAN_EXPERT;
         this._itemsMap["radioman_threatSearchCheckbox"] = BATTLE_EFFICIENCY_TYPES.RADIOMAN_THREAT_SEARCH;
      }
      
      override public function updateContent(param1:Object) : void
      {
         var _loc2_:CheckBox = null;
         var _loc3_:* = null;
         super.updateContent(param1);
         this.controlsContainer.isEnabled = this.controlsContainer.battleEventsShowInBattleCheckbox.selected;
         for(_loc3_ in this._itemsMap)
         {
            _loc2_ = CheckBox(this.getControlByName(_loc3_));
            this.ribbonsContainer.updateItemVisible(this._itemsMap[_loc3_],_loc2_.selected && _loc2_.enabled);
         }
         this.infoView.visible = this.ribbonsContainer.numChildren > 0;
         this.ribbonsContainer.redraw();
         this.ribbonsContainer.updateSettings(this.controlsContainer.battleEventsEventNameCheckbox.selected,this.controlsContainer.battleEventsVehicleInfoCheckbox.selected);
      }
      
      override public function get formId() : String
      {
         return Linkages.FEEDBACK_BATTLE_EVENTS;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.controlsScrollPane.scrollBar = this.controlsScrollBar;
         this.controlsScrollPane.scrollStepFactor = SCROLL_STEP_FACTOR;
         this.controlsScrollPane.target = this.controlsContainer;
         this.controlsScrollPane.scrollPosition = 0;
         this.controlsScrollPane.setSize(CONTROLS_SCROLL_PANE_WIDTH,CONTROLS_SCROLL_PANE_HEIGHT);
         this.ribbonsScrollBar.trackScrollPageSize = SCROLL_STEP_FACTOR;
         this.ribbonsScrollPane.scrollBar = this.ribbonsScrollBar;
         this.ribbonsScrollPane.scrollStepFactor = SCROLL_STEP_FACTOR;
         this.ribbonsContainer.x -= this.ribbonsScrollPane.x;
         this.ribbonsContainer.y -= this.ribbonsScrollPane.y;
         this.ribbonsScrollPane.target = this.ribbonsContainer;
         this.ribbonsScrollPane.setSize(RIBBONS_SCROLL_PANE_WIDTH,RIBBONS_SCROLL_PANE_HEIGHT);
         this.addEventListener(SettingsGroupEvent.ON_GROUP_STATE_CHANGE,this.onGroupStateChangeHandler);
      }
      
      override protected function onDispose() : void
      {
         App.utils.data.cleanupDynamicObject(this._itemsMap);
         this._itemsMap = null;
         this.ribbonsScrollPane.target = null;
         this.ribbonsScrollPane.dispose();
         this.ribbonsScrollPane = null;
         this.ribbonsScrollBar.dispose();
         this.ribbonsScrollBar = null;
         this.ribbonsContainer.dispose();
         this.ribbonsContainer = null;
         this.controlsScrollPane.target = null;
         this.controlsScrollPane.dispose();
         this.controlsScrollPane = null;
         this.controlsScrollBar.dispose();
         this.controlsScrollBar = null;
         this.controlsContainer.dispose();
         this.controlsContainer = null;
         this.infoView.dispose();
         this.infoView = null;
         this.removeEventListener(SettingsGroupEvent.ON_GROUP_STATE_CHANGE,this.onGroupStateChangeHandler);
         super.onDispose();
      }
      
      override protected function getControlByName(param1:String) : IDisplayObject
      {
         return this.controlsContainer.getControlByName(param1) || super.getControlByName(param1);
      }
      
      override protected function getControl(param1:String, param2:String) : DisplayObject
      {
         return this.getControlByName(param1 + param2) as DisplayObject;
      }
      
      override protected function getCounterProps(param1:String) : ICounterProps
      {
         if(param1 == SettingsConfigHelper.TYPE_CHECKBOX)
         {
            return new CounterProps(COUNTER_CHECKBOX_OFFSET_X,CounterProps.DEFAULT_OFFSET_Y,TextFormatAlign.LEFT,false,Linkages.COUNTER_LINE_UI);
         }
         if(param1 == SettingsConfigHelper.TYPE_CONTROLS_GROUP)
         {
            return new CounterProps(COUNTER_CONTROLS_GROUP_OFFSET_X,COUNTER_CONTROLS_GROUP_OFFSET_Y,TextFormatAlign.LEFT,false,Linkages.COUNTER_LINE_UI);
         }
         return super.getCounterProps(param1);
      }
      
      override protected function getContainerId() : String
      {
         return RIBBONS_COUNTER_CONTAINER_ID;
      }
      
      override protected function onCheckBoxSelected(param1:CheckBox) : void
      {
         var _loc2_:ControlsGroup = null;
         super.onCheckBoxSelected(param1);
         if(param1.selected)
         {
            if(param1 == this.controlsContainer.battleEventsShowInBattleCheckbox && !this.controlsContainer.isSelectedAnyCheckbox)
            {
               this.controlsContainer.selectAllCheckBoxes();
            }
            else if(param1 == CrewPerksGroupContent(this.controlsContainer.crewPerksControlsGroup.content).battleEventsCrewPerksCheckbox)
            {
               this.controlsContainer.crewPerksControlsGroup.content.selectAllCheckBoxes();
            }
         }
         else if(this._itemsMap.hasOwnProperty(param1.name))
         {
            _loc2_ = this.controlsContainer.crewPerksControlsGroup;
            if(_loc2_.getControlByName(param1.name) && !_loc2_.content.isSelectedAnyCheckbox)
            {
               CrewPerksGroupContent(_loc2_.content).battleEventsCrewPerksCheckbox.selected = false;
            }
            if(!this.controlsContainer.isSelectedAnyCheckbox)
            {
               this.controlsContainer.battleEventsShowInBattleCheckbox.selected = false;
            }
         }
      }
      
      private function onGroupStateChangeHandler(param1:SettingsGroupEvent) : void
      {
         var _loc2_:ControlsGroup = param1.target as ControlsGroup;
         if(_loc2_ && _loc2_.isOpen)
         {
            if(_loc2_ == this.controlsContainer.damageControlsGroup)
            {
               this.ribbonsScrollPane.scrollPosition = 0;
            }
            else if(_loc2_ == this.controlsContainer.battleEfficiencyControlsGroup)
            {
               this.ribbonsScrollPane.scrollPosition = this.controlsContainer.damageControlsGroup.content.selectedItemsAmount;
            }
            else if(_loc2_ == this.controlsContainer.crewPerksControlsGroup)
            {
               this.ribbonsScrollPane.scrollPosition = this.controlsContainer.damageControlsGroup.content.selectedItemsAmount + this.controlsContainer.battleEfficiencyControlsGroup.content.selectedItemsAmount;
            }
         }
      }
   }
}
