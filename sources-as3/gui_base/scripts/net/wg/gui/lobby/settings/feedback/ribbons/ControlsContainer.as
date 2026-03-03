package net.wg.gui.lobby.settings.feedback.ribbons
{
   import flash.text.TextField;
   import net.wg.gui.components.controls.CheckBox;
   import net.wg.gui.interfaces.IContentSize;
   import net.wg.gui.lobby.settings.events.SettingsGroupEvent;
   import net.wg.infrastructure.interfaces.IDisplayObject;
   
   public class ControlsContainer extends GroupContent implements IContentSize
   {
      
      private static const HEIGHT_OFFSET:int = 8;
       
      
      public var battleEventsLabel:TextField = null;
      
      public var battleEventsShowInBattleCheckbox:CheckBox = null;
      
      public var battleEventsEventNameCheckbox:CheckBox = null;
      
      public var battleEventsVehicleInfoCheckbox:CheckBox = null;
      
      public var damageControlsGroup:ControlsGroup;
      
      public var battleEfficiencyControlsGroup:ControlsGroup;
      
      public var crewPerksControlsGroup:ControlsGroup;
      
      public function ControlsContainer()
      {
         super();
      }
      
      public function getControlByName(param1:String) : IDisplayObject
      {
         return this[param1] || this.damageControlsGroup.getControlByName(param1) || this.battleEfficiencyControlsGroup.getControlByName(param1) || this.crewPerksControlsGroup.getControlByName(param1);
      }
      
      public function get contentWidth() : Number
      {
         return this.width;
      }
      
      public function get contentHeight() : Number
      {
         return this.height + HEIGHT_OFFSET;
      }
      
      override public function set isEnabled(param1:Boolean) : void
      {
         this.battleEventsEventNameCheckbox.enabled = param1;
         this.battleEventsVehicleInfoCheckbox.enabled = param1;
         this.damageControlsGroup.content.isEnabled = param1;
         this.battleEfficiencyControlsGroup.content.isEnabled = param1;
         this.crewPerksControlsGroup.content.isEnabled = param1;
      }
      
      override public function get isSelectedAnyCheckbox() : Boolean
      {
         return this.damageControlsGroup.content.isSelectedAnyCheckbox || this.battleEfficiencyControlsGroup.content.isSelectedAnyCheckbox || this.crewPerksControlsGroup.content.isSelectedAnyCheckbox;
      }
      
      override public function selectAllCheckBoxes() : void
      {
         this.damageControlsGroup.content.selectAllCheckBoxes();
         this.battleEfficiencyControlsGroup.content.selectAllCheckBoxes();
         this.crewPerksControlsGroup.content.selectAllCheckBoxes();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.battleEventsLabel.text = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_LABEL_BATTLEEVENTS;
         this.battleEventsShowInBattleCheckbox.label = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_CHECKBOX_SHOWINBATTLE;
         this.battleEventsEventNameCheckbox.label = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_CHECKBOX_EVENTNAME;
         this.battleEventsVehicleInfoCheckbox.label = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_CHECKBOX_VEHICLEINFO;
         this.damageControlsGroup.title = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_LABEL_NEGATIVE;
         this.battleEfficiencyControlsGroup.title = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_LABEL_POSITIVE;
         this.crewPerksControlsGroup.title = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_LABEL_CREWPERKS;
         this.addEventListener(SettingsGroupEvent.ON_GROUP_STATE_CHANGE,this.onGroupStateChangeHandler);
      }
      
      override protected function onDispose() : void
      {
         this.removeEventListener(SettingsGroupEvent.ON_GROUP_STATE_CHANGE,this.onGroupStateChangeHandler);
         this.battleEventsShowInBattleCheckbox.dispose();
         this.battleEventsShowInBattleCheckbox = null;
         this.battleEventsLabel = null;
         this.battleEventsEventNameCheckbox.dispose();
         this.battleEventsEventNameCheckbox = null;
         this.battleEventsVehicleInfoCheckbox.dispose();
         this.battleEventsVehicleInfoCheckbox = null;
         this.damageControlsGroup.dispose();
         this.damageControlsGroup = null;
         this.battleEfficiencyControlsGroup.dispose();
         this.battleEfficiencyControlsGroup = null;
         this.crewPerksControlsGroup.dispose();
         this.crewPerksControlsGroup = null;
         super.onDispose();
      }
      
      private function onGroupStateChangeHandler(param1:SettingsGroupEvent) : void
      {
         invalidateLayout();
      }
   }
}
