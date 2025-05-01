package net.wg.historical_battles.gui.battle.views.respawn.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HBVehicleCardVO extends DAAPIDataClass
   {
       
      
      public var vehicleId:int = -1;
      
      public var vehicleSrc:String = "";
      
      public var emblemSrc:String = "";
      
      public var vehicleTypeSrc:String = "";
      
      public var vehicleName:String = "";
      
      public var state:uint = 0;
      
      public var frontName:String = "defence";
      
      public function HBVehicleCardVO(param1:Object)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "[HBVehicleCardVO > vehicleSrc: " + this.vehicleSrc + "]";
      }
   }
}
