package net.wg.frontline.infrastructure.helpers.statisticsDataController
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlinePlayerStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehiclesStatsVO;
   import net.wg.frontline.infrastructure.base.meta.IFrontlineBattleStatisticDataControllerMeta;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineBattleStatisticDataControllerMeta;
   import net.wg.frontline.infrastructure.helpers.statisticsDataController.interfaces.IFrontlineBattleStatisticDataController;
   
   public class FrontlineBattleStatisticDataController extends FrontlineBattleStatisticDataControllerMeta implements IFrontlineBattleStatisticDataControllerMeta
   {
       
      
      private var _epicComponents:Vector.<IFrontlineBattleStatisticDataController> = null;
      
      public function FrontlineBattleStatisticDataController()
      {
         super();
         this._epicComponents = new Vector.<IFrontlineBattleStatisticDataController>(0);
      }
      
      override protected function setEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
         var _loc2_:IFrontlineBattleStatisticDataController = null;
         for each(_loc2_ in this._epicComponents)
         {
            _loc2_.setEpicVehiclesStats(param1);
         }
      }
      
      override protected function updateEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
         var _loc2_:IFrontlineBattleStatisticDataController = null;
         for each(_loc2_ in this._epicComponents)
         {
            _loc2_.updateEpicVehiclesStats(param1);
         }
      }
      
      override protected function updateEpicPlayerStats(param1:FrontlinePlayerStatsVO) : void
      {
         var _loc2_:IFrontlineBattleStatisticDataController = null;
         for each(_loc2_ in this._epicComponents)
         {
            _loc2_.updateEpicPlayerStats(param1);
         }
      }
      
      override protected function onDispose() : void
      {
         this._epicComponents.fixed = false;
         this._epicComponents.splice(0,this._epicComponents.length);
         this._epicComponents = null;
         super.onDispose();
      }
      
      public function registerEpicComponentController(param1:IFrontlineBattleStatisticDataController) : void
      {
         App.utils.asserter.assertNotNull(param1,"ComponentController to be added " + Errors.CANT_NULL);
         this._epicComponents.push(param1);
      }
      
      public function unregisterEpicComponentController(param1:IFrontlineBattleStatisticDataController) : void
      {
         var _loc2_:int = this._epicComponents.indexOf(param1);
         if(_loc2_ != -1)
         {
            this._epicComponents.splice(_loc2_,1);
         }
      }
   }
}
