package net.wg.historical_battles.gui.battle.views.phaseIndicator.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HBPhaseIndicatorVO extends DAAPIDataClass
   {
       
      
      public var state:String = "defence";
      
      public var phase:String = "";
      
      public var wave:String = "";
      
      public function HBPhaseIndicatorVO(param1:Object)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "[HBPhaseIndicatorVO > state: " + this.state + ", phase: " + this.phase + ", wave:" + this.wave + "]";
      }
   }
}
