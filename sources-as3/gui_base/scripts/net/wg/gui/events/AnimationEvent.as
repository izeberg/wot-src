package net.wg.gui.events
{
   import flash.events.Event;
   
   public class AnimationEvent extends Event
   {
      
      public static const ANIM_COMPLETE:String = "animComplete";
       
      
      public function AnimationEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
   }
}
