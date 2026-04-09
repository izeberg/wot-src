package net.wg.historical_battles.gui.battle.views.respawn.events
{
   import flash.events.Event;
   
   public class HBRespawnEvent extends Event
   {
      
      public static const VISIBILITY_CHANGE:String = "hbRespawnVisibilityChange";
       
      
      private var _isVisible:Boolean = false;
      
      private var _isRespawn:Boolean = false;
      
      public function HBRespawnEvent(param1:String, param2:Boolean, param3:Boolean, param4:Boolean = true, param5:Boolean = false)
      {
         this._isVisible = param2;
         this._isRespawn = param3;
         super(param1,param4,param5);
      }
      
      override public function clone() : Event
      {
         return new HBRespawnEvent(type,this._isVisible,this._isRespawn,bubbles,cancelable);
      }
      
      override public function toString() : String
      {
         return formatToString("HBRespawnEvent","type","isVisible","isRespawn","bubbles","cancelable","eventPhase");
      }
      
      public function get isVisible() : Boolean
      {
         return this._isVisible;
      }
      
      public function get isRespawn() : Boolean
      {
         return this._isRespawn;
      }
   }
}
