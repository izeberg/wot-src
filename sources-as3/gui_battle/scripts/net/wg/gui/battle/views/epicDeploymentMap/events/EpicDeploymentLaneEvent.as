package net.wg.gui.battle.views.epicDeploymentMap.events
{
   import flash.events.Event;
   
   public class EpicDeploymentLaneEvent extends Event
   {
      
      public static const CHANGED:String = "laneChanged";
       
      
      private var _currentLane:String = "";
      
      private var _selectedLane:String = "";
      
      public function EpicDeploymentLaneEvent(param1:String, param2:String, param3:String, param4:Boolean = false, param5:Boolean = false)
      {
         super(param1,param4,param5);
         this._currentLane = param2;
         this._selectedLane = param3;
      }
      
      override public function clone() : Event
      {
         return new EpicDeploymentLaneEvent(type,this._currentLane,this._selectedLane,bubbles,cancelable);
      }
      
      public function get currentLane() : String
      {
         return this._currentLane;
      }
      
      public function get selectedLane() : String
      {
         return this._selectedLane;
      }
   }
}
