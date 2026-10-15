package net.wg.gui.lobby.settings.components.evnts
{
   import flash.events.Event;
   
   public class WarningMessageEvent extends Event
   {
      
      public static const TURN_OFF_LIMITED_UI:String = "turnOffLimitedUI";
      
      public static const FIX_MIXER_SOUND:String = "fixMixerSound";
       
      
      public function WarningMessageEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new WarningMessageEvent(type,bubbles,cancelable);
      }
      
      override public function toString() : String
      {
         return formatToString("WarningMessageEvent","type","bubbles","cancelable","eventPhase");
      }
   }
}
