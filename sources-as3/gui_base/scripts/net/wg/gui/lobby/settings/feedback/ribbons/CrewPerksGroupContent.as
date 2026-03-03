package net.wg.gui.lobby.settings.feedback.ribbons
{
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   import net.wg.data.constants.generated.COMMONBATTLELOBBY;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.controls.CheckBox;
   import net.wg.infrastructure.managers.ITooltipMgr;
   
   public class CrewPerksGroupContent extends GroupContent
   {
       
      
      public var battleEventsCrewPerksCheckbox:CheckBox = null;
      
      public var commander_eagleEyeCheckbox:CheckBox = null;
      
      public var commander_emergencyCheckbox:CheckBox = null;
      
      public var commander_tutorCheckbox:CheckBox = null;
      
      public var commander_coordinationCheckbox:CheckBox = null;
      
      public var commander_holdLineCheckbox:CheckBox = null;
      
      public var commander_staySharpCheckbox:CheckBox = null;
      
      public var gunner_focusCheckbox:CheckBox = null;
      
      public var gunner_loneWolfCheckbox:CheckBox = null;
      
      public var driver_motorExpertCheckbox:CheckBox = null;
      
      public var driver_suspensionRepairCheckbox:CheckBox = null;
      
      public var driver_bulletproofCheckbox:CheckBox = null;
      
      public var loader_desperadoCheckbox:CheckBox = null;
      
      public var loader_intuitionCheckbox:CheckBox = null;
      
      public var loader_meleeCheckbox:CheckBox = null;
      
      public var loader_secondChanceCheckbox:CheckBox = null;
      
      public var radioman_sideBySideCheckbox:CheckBox = null;
      
      public var radioman_expertCheckbox:CheckBox = null;
      
      public var radioman_threatSearchCheckbox:CheckBox = null;
      
      private var _tooltipDataDict:Dictionary;
      
      private var _toolTipMgr:ITooltipMgr;
      
      public function CrewPerksGroupContent()
      {
         this._tooltipDataDict = new Dictionary();
         this._toolTipMgr = App.toolTipMgr;
         super();
      }
      
      override public function set isEnabled(param1:Boolean) : void
      {
         var _loc2_:CheckBox = null;
         this.battleEventsCrewPerksCheckbox.enabled = param1;
         var _loc3_:int = 0;
         while(_loc3_ < this.numChildren)
         {
            _loc2_ = this.getChildAt(_loc3_) as CheckBox;
            if(_loc2_ && _loc2_ != this.battleEventsCrewPerksCheckbox)
            {
               _loc2_.enabled = param1 && this.battleEventsCrewPerksCheckbox.selected;
            }
            _loc3_++;
         }
      }
      
      override public function get isSelectedAnyCheckbox() : Boolean
      {
         var _loc1_:CheckBox = null;
         var _loc2_:int = 0;
         while(_loc2_ < this.numChildren)
         {
            _loc1_ = this.getChildAt(_loc2_) as CheckBox;
            if(_loc1_ != this.battleEventsCrewPerksCheckbox)
            {
               if(_loc1_.selected && _loc1_.enabled)
               {
                  return true;
               }
            }
            _loc2_++;
         }
         return false;
      }
      
      override public function selectAllCheckBoxes() : void
      {
         if(!this.isSelectedAnyCheckbox)
         {
            super.selectAllCheckBoxes();
         }
         else
         {
            this.battleEventsCrewPerksCheckbox.selected = true;
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.battleEventsCrewPerksCheckbox.label = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_CHECKBOX_ALLSITUATIONALPERKS;
         this.initCheckBox(this.commander_eagleEyeCheckbox,CREW_PERKS.COMMANDER_EAGLEEYE_NAME,COMMONBATTLELOBBY.COMMANDER_EAGLE_EYE);
         this.initCheckBox(this.commander_emergencyCheckbox,CREW_PERKS.COMMANDER_EMERGENCY_NAME,COMMONBATTLELOBBY.COMMANDER_EMERGENCY);
         this.initCheckBox(this.commander_tutorCheckbox,CREW_PERKS.COMMANDER_TUTOR_NAME,COMMONBATTLELOBBY.COMMANDER_TUTOR);
         this.initCheckBox(this.commander_coordinationCheckbox,CREW_PERKS.COMMANDER_COORDINATION_NAME,COMMONBATTLELOBBY.COMMANDER_COORDINATION);
         this.initCheckBox(this.commander_holdLineCheckbox,CREW_PERKS.COMMANDER_HOLDLINE_NAME,COMMONBATTLELOBBY.COMMANDER_HOLD_LINE);
         this.initCheckBox(this.commander_staySharpCheckbox,CREW_PERKS.COMMANDER_STAYSHARP_NAME,COMMONBATTLELOBBY.COMMANDER_STAY_SHARP);
         this.initCheckBox(this.gunner_focusCheckbox,CREW_PERKS.GUNNER_FOCUS_NAME,COMMONBATTLELOBBY.GUNNER_FOCUS);
         this.initCheckBox(this.gunner_loneWolfCheckbox,CREW_PERKS.GUNNER_LONEWOLF_NAME,COMMONBATTLELOBBY.GUNNER_LONE_WOLF);
         this.initCheckBox(this.driver_motorExpertCheckbox,CREW_PERKS.DRIVER_MOTOREXPERT_NAME,COMMONBATTLELOBBY.DRIVER_MOTOR_EXPERT);
         this.initCheckBox(this.driver_suspensionRepairCheckbox,CREW_PERKS.DRIVER_SUSPENSIONREPAIR_NAME,COMMONBATTLELOBBY.DRIVER_SUSPENSION_REPAIR);
         this.initCheckBox(this.driver_bulletproofCheckbox,CREW_PERKS.DRIVER_BULLETPROOF_NAME,COMMONBATTLELOBBY.DRIVER_BULLETPROOF);
         this.initCheckBox(this.loader_desperadoCheckbox,CREW_PERKS.LOADER_DESPERADO_NAME,COMMONBATTLELOBBY.LOADER_DESPERADO);
         this.initCheckBox(this.loader_intuitionCheckbox,CREW_PERKS.LOADER_INTUITION_NAME,COMMONBATTLELOBBY.LOADER_INTUITION);
         this.initCheckBox(this.loader_meleeCheckbox,CREW_PERKS.LOADER_MELEE_NAME,COMMONBATTLELOBBY.LOADER_MELEE);
         this.initCheckBox(this.loader_secondChanceCheckbox,CREW_PERKS.LOADER_SECONDCHANCE_NAME,COMMONBATTLELOBBY.LOADER_SECOND_CHANCE);
         this.initCheckBox(this.radioman_sideBySideCheckbox,CREW_PERKS.RADIOMAN_SIDEBYSIDE_NAME,COMMONBATTLELOBBY.RADIOMAN_SIDE_BY_SIDE);
         this.initCheckBox(this.radioman_expertCheckbox,CREW_PERKS.RADIOMAN_EXPERT_NAME,COMMONBATTLELOBBY.RADIOMAN_EXPERT);
         this.initCheckBox(this.radioman_threatSearchCheckbox,CREW_PERKS.RADIOMAN_THREATSEARCH_NAME,COMMONBATTLELOBBY.RADIOMAN_THREAT_SEARCH);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:CheckBox = null;
         while(this.numChildren)
         {
            _loc1_ = this.removeChildAt(0) as CheckBox;
            if(_loc1_)
            {
               _loc1_.removeEventListener(MouseEvent.MOUSE_OVER,this.checkBoxOveHandler);
               _loc1_.removeEventListener(MouseEvent.MOUSE_OUT,this.checkBoxOutHandler);
               _loc1_.dispose();
            }
         }
         this._toolTipMgr.hide();
         this._toolTipMgr = null;
         App.utils.data.cleanupDynamicObject(this._tooltipDataDict);
         this._tooltipDataDict = null;
         this.battleEventsCrewPerksCheckbox = null;
         this.commander_eagleEyeCheckbox = null;
         this.commander_emergencyCheckbox = null;
         this.commander_tutorCheckbox = null;
         this.commander_coordinationCheckbox = null;
         this.commander_holdLineCheckbox = null;
         this.commander_staySharpCheckbox = null;
         this.gunner_focusCheckbox = null;
         this.gunner_loneWolfCheckbox = null;
         this.driver_motorExpertCheckbox = null;
         this.driver_suspensionRepairCheckbox = null;
         this.driver_bulletproofCheckbox = null;
         this.loader_desperadoCheckbox = null;
         this.loader_intuitionCheckbox = null;
         this.loader_meleeCheckbox = null;
         this.loader_secondChanceCheckbox = null;
         this.radioman_sideBySideCheckbox = null;
         this.radioman_expertCheckbox = null;
         this.radioman_threatSearchCheckbox = null;
         super.onDispose();
      }
      
      private function initCheckBox(param1:CheckBox, param2:String, param3:String) : void
      {
         this._tooltipDataDict[param1] = param3;
         param1.label = param2;
         param1.addEventListener(MouseEvent.MOUSE_OVER,this.checkBoxOveHandler);
         param1.addEventListener(MouseEvent.MOUSE_OUT,this.checkBoxOutHandler);
      }
      
      private function checkBoxOveHandler(param1:MouseEvent) : void
      {
         var _loc2_:CheckBox = param1.currentTarget as CheckBox;
         this._toolTipMgr.showWulfTooltip(TOOLTIPS_CONSTANTS.SETTINGS_SITUATIONAL_PERK,this._tooltipDataDict[_loc2_]);
      }
      
      private function checkBoxOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
   }
}
