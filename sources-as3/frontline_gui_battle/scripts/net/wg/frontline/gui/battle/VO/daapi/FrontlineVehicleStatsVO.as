package net.wg.frontline.gui.battle.VO.daapi
{
   import net.wg.data.VO.daapi.DAAPIVehicleStatsVO;
   
   public class FrontlineVehicleStatsVO extends DAAPIVehicleStatsVO
   {
       
      
      public var rank:int = -1;
      
      public var lane:int = -1;
      
      public var hasRespawns:Boolean = false;
      
      public function FrontlineVehicleStatsVO(param1:Object)
      {
         super(param1);
      }
   }
}
