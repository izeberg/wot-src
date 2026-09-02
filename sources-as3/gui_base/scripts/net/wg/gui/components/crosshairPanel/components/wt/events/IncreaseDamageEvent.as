package net.wg.gui.components.crosshairPanel.components.wt.events
{
   import flash.events.Event;
   
   public class IncreaseDamageEvent extends Event
   {
      
      public static const HIDE_COMPLETE:String = "wtHideComplete";
       
      
      public function IncreaseDamageEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new IncreaseDamageEvent(type,bubbles,cancelable);
      }
   }
}
