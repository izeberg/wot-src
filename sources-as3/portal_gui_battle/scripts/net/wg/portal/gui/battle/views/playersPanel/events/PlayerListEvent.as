package net.wg.portal.gui.battle.views.playersPanel.events
{
   import flash.events.Event;
   
   public class PlayerListEvent extends Event
   {
      
      public static const SIZE_CHANGE:String = "sizeChanged";
       
      
      public function PlayerListEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
   }
}
