package net.wg.gui.battle.bob.data
{
   import flash.display.DisplayObjectContainer;
   import net.wg.data.VO.daapi.DAAPIVehiclesDataVO;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   
   public class BobBattleStatisticDataController extends BattleStatisticDataController
   {
       
      
      public function BobBattleStatisticDataController(param1:DisplayObjectContainer = null)
      {
         super(param1);
      }
      
      override protected function getDAAPIVehiclesDataVOForVehData(param1:Object) : DAAPIVehiclesDataVO
      {
         return new BobDAAPIVehiclesDataVO(param1);
      }
      
      override protected function getDAAPIVehiclesDataVOForVehInfo(param1:Object) : DAAPIVehiclesDataVO
      {
         return this.getDAAPIVehiclesDataVOForVehData(param1);
      }
      
      override protected function getDAAPIVehiclesDataVOForUpVehInfo(param1:Object) : DAAPIVehiclesDataVO
      {
         return this.getDAAPIVehiclesDataVOForVehData(param1);
      }
   }
}
