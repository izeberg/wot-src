package net.wg.white_tiger.gui.battle.VO
{
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   
   public class DAAPIHunterVehicleInfoVO extends DAAPIVehicleInfoVO
   {
       
      
      public var resurrectTimeLeft:Number = 0;
      
      public var resurrectTimeTotal:Number = 0;
      
      public var replaySpeed:Number = 1;
      
      public function DAAPIHunterVehicleInfoVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
