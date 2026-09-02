package net.wg.gui.lobby.settings.events
{
   import flash.events.Event;
   
   public class BattleContextHintSettingsEvent extends Event
   {
      
      public static const RESET:String = "reset";
       
      
      public function BattleContextHintSettingsEvent(param1:String, param2:Boolean = true, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new BattleContextHintSettingsEvent(type,bubbles,cancelable);
      }
      
      override public function toString() : String
      {
         return formatToString("BattleContextHintSettingsEvent","type","bubbles","cancelable","eventPhase");
      }
   }
}
