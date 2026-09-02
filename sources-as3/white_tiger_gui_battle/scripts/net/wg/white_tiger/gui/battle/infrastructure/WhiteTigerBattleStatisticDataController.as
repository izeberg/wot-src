package net.wg.white_tiger.gui.battle.infrastructure
{
   import flash.display.DisplayObjectContainer;
   import net.wg.data.VO.daapi.DAAPIVehiclesDataVO;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   import net.wg.white_tiger.gui.battle.VO.DAAPIHunterVehiclesDataVO;
   
   public class WhiteTigerBattleStatisticDataController extends BattleStatisticDataController
   {
       
      
      public function WhiteTigerBattleStatisticDataController(param1:DisplayObjectContainer)
      {
         super(param1);
      }
      
      override protected function getDAAPIVehiclesDataVOForVehData(param1:Object) : DAAPIVehiclesDataVO
      {
         return new DAAPIHunterVehiclesDataVO(param1);
      }
   }
}
