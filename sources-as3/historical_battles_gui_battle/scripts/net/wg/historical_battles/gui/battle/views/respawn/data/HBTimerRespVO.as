package net.wg.historical_battles.gui.battle.views.respawn.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HBTimerRespVO extends DAAPIDataClass
   {
       
      
      public var time:int = -1;
      
      public var title:String = "";
      
      public var label:String = "";
      
      public function HBTimerRespVO(param1:Object)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "[HBTimerRespVO > time: " + this.time + ", title: " + this.title + ", label:" + this.label + "]";
      }
   }
}
