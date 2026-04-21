package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import flash.events.Event;
   
   public class LowChargeShotReloadEvent extends Event
   {
      
      public static const TICK:String = "tick";
      
      public static const QUICK_RELOAD_CHANGED:String = "quickReloadChanged";
       
      
      private var _time:Number = -1;
      
      private var _state:Number = -1;
      
      private var _progress:Number = -1;
      
      public function LowChargeShotReloadEvent(param1:String, param2:Number = -1, param3:Number = -1, param4:Number = -1, param5:Boolean = false, param6:Boolean = false)
      {
         super(param1,param5,param6);
         this._time = param2;
         this._state = param3;
         this._progress = param4;
      }
      
      public function get time() : Number
      {
         return this._time;
      }
      
      public function get progress() : Number
      {
         return this._progress;
      }
      
      public function get state() : Number
      {
         return this._state;
      }
   }
}
