package net.wg.historical_battles.gui.battle.views.respawn.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HBDivisionVO extends DAAPIDataClass
   {
       
      
      public var name:String = "";
      
      public var emblemSrc:String = "";
      
      public function HBDivisionVO(param1:Object)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "[HBDivisionVO > name: " + this.name + ", emblemSrc: " + this.emblemSrc + "]";
      }
   }
}
