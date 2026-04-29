package net.wg.historical_battles.gui.battle.views.spgPanel.events
{
   import flash.events.Event;
   
   public class HBSPGPanelEvent extends Event
   {
      
      public static const SIZE_CHANGE:String = "spgPanelSizeChanged";
       
      
      public function HBSPGPanelEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new HBSPGPanelEvent(type,bubbles,cancelable);
      }
   }
}
