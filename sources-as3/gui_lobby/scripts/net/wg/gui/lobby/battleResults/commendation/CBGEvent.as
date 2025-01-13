package net.wg.gui.lobby.battleResults.commendation
{
   import flash.events.Event;
   
   public class CBGEvent extends Event
   {
      
      public static const BTN_CLICKED:String = "btnClicked";
       
      
      public var btnID:int;
      
      public function CBGEvent(param1:int)
      {
         super(BTN_CLICKED,false,false);
         this.btnID = param1;
      }
   }
}
