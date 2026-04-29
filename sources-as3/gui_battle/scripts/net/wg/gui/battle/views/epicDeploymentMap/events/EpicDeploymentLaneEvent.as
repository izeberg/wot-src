package net.wg.gui.battle.views.epicDeploymentMap.events
{
   import flash.events.Event;
   
   public class EpicDeploymentLaneEvent extends Event
   {
      
      public static const CHANGED:String = "laneChanged";
       
      
      private var _warningValue:String = "";
      
      public function EpicDeploymentLaneEvent(param1:String, param2:String, param3:Boolean = false, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this._warningValue = param2;
      }
      
      override public function clone() : Event
      {
         return new EpicDeploymentLaneEvent(type,this._warningValue,bubbles,cancelable);
      }
      
      public function get warningValue() : String
      {
         return this._warningValue;
      }
   }
}
