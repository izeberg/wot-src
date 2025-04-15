package net.wg.frontline.gui.battle.battleLoading.events
{
   import flash.events.Event;
   
   public class FrontlineBattleLoadingEvent extends Event
   {
      
      public static const VISIBILITY_CHANGED:String = "onVisibilityChanged";
       
      
      public function FrontlineBattleLoadingEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new FrontlineBattleLoadingEvent(type,bubbles,cancelable);
      }
   }
}
