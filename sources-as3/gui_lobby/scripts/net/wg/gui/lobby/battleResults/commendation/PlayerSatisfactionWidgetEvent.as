package net.wg.gui.lobby.battleResults.commendation
{
   import flash.events.Event;
   
   public class PlayerSatisfactionWidgetEvent extends Event
   {
      
      public static const CREATED:String = "created";
      
      public static const DESTROYED:String = "destroyed";
       
      
      public function PlayerSatisfactionWidgetEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
   }
}
