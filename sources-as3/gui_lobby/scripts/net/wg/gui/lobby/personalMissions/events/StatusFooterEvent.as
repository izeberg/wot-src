package net.wg.gui.lobby.personalMissions.events
{
   import flash.events.Event;
   
   public class StatusFooterEvent extends Event
   {
      
      public static const SKIP_TASK:String = "skip_task";
       
      
      public var btnID:int = 0;
      
      public function StatusFooterEvent(param1:String, param2:int, param3:Boolean = false, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this.btnID = param2;
      }
   }
}
