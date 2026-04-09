package net.wg.historical_battles.gui.battle.views.respawn.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HBRespawnVO extends DAAPIDataClass
   {
      
      private static const DIVISION_FIELD_NAME:String = "division";
      
      private static const VEHICLE_CARDS_FIELD_NAME:String = "vehicleCards";
       
      
      public var divisionVO:HBDivisionVO = null;
      
      public var vehicleCards:Vector.<HBVehicleCardVO> = null;
      
      public var mapName:String = "";
      
      public function HBRespawnVO(param1:Object)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "[HBRespawnVO > divisionVO: " + this.divisionVO + ", vehicleCards: " + this.vehicleCards + "]";
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         switch(param1)
         {
            case DIVISION_FIELD_NAME:
               this.divisionVO = new HBDivisionVO(param2);
               return false;
            case VEHICLE_CARDS_FIELD_NAME:
               this.vehicleCards = Vector.<HBVehicleCardVO>(App.utils.data.convertVOArrayToVector(param1,param2,HBVehicleCardVO));
               return false;
            default:
               return super.onDataWrite(param1,param2);
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:HBVehicleCardVO = null;
         if(this.divisionVO)
         {
            this.divisionVO.dispose();
            this.divisionVO = null;
         }
         if(this.vehicleCards)
         {
            for each(_loc1_ in this.vehicleCards)
            {
               _loc1_.dispose();
            }
            this.vehicleCards.splice(0,this.vehicleCards.length);
            this.vehicleCards = null;
         }
         super.onDispose();
      }
   }
}
