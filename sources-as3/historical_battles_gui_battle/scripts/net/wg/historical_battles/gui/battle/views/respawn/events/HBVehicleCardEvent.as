package net.wg.historical_battles.gui.battle.views.respawn.events
{
   import flash.events.Event;
   
   public class HBVehicleCardEvent extends Event
   {
      
      public static const VEHICLE_PICK:String = "vehiclePick";
      
      public static const VEHICLE_SELECT:String = "vehicleSelect";
       
      
      private var _vehicleId:int = -1;
      
      public function HBVehicleCardEvent(param1:String, param2:int, param3:Boolean = true, param4:Boolean = false)
      {
         this._vehicleId = param2;
         super(param1,param3,param4);
      }
      
      override public function clone() : Event
      {
         return new HBVehicleCardEvent(type,this._vehicleId,bubbles,cancelable);
      }
      
      override public function toString() : String
      {
         return formatToString("HBVehicleCardEvent","type","vehicleId","bubbles","cancelable","eventPhase");
      }
      
      public function get vehicleId() : int
      {
         return this._vehicleId;
      }
   }
}
