package net.wg.gui.battle.epicBattle.views.stats.events
{
   import flash.events.Event;
   
   public class EpicFullStatsEvent extends Event
   {
      
      public static const FILTER_CHANGED:String = "filterChanged";
       
      
      public var lane:int = -1;
      
      public var visible:Boolean = true;
      
      public function EpicFullStatsEvent(param1:String, param2:int, param3:Boolean = true, param4:Boolean = false, param5:Boolean = false)
      {
         super(param1,param4,param5);
         this.lane = param2;
         this.visible = param3;
      }
      
      override public function clone() : Event
      {
         return new EpicFullStatsEvent(type,this.lane,bubbles,cancelable);
      }
   }
}
