package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlinePlayerStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehiclesStatsVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   
   public class FrontlineBattleStatisticDataControllerMeta extends BattleStatisticDataController
   {
       
      
      private var _frontlinePlayerStatsVO:FrontlinePlayerStatsVO;
      
      private var _frontlineVehiclesStatsVO:FrontlineVehiclesStatsVO;
      
      public function FrontlineBattleStatisticDataControllerMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._frontlinePlayerStatsVO)
         {
            this._frontlinePlayerStatsVO.dispose();
            this._frontlinePlayerStatsVO = null;
         }
         if(this._frontlineVehiclesStatsVO)
         {
            this._frontlineVehiclesStatsVO.dispose();
            this._frontlineVehiclesStatsVO = null;
         }
         super.onDispose();
      }
      
      public final function as_updateEpicPlayerStats(param1:Object) : void
      {
         var _loc2_:FrontlinePlayerStatsVO = this._frontlinePlayerStatsVO;
         this._frontlinePlayerStatsVO = new FrontlinePlayerStatsVO(param1);
         this.updateEpicPlayerStats(this._frontlinePlayerStatsVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_setEpicVehiclesStats(param1:Object) : void
      {
         var _loc2_:FrontlineVehiclesStatsVO = this._frontlineVehiclesStatsVO;
         this._frontlineVehiclesStatsVO = new FrontlineVehiclesStatsVO(param1);
         this.setEpicVehiclesStats(this._frontlineVehiclesStatsVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_updateEpicVehiclesStats(param1:Object) : void
      {
         var _loc2_:FrontlineVehiclesStatsVO = new FrontlineVehiclesStatsVO(param1);
         this.updateEpicVehiclesStats(_loc2_);
      }
      
      protected function updateEpicPlayerStats(param1:FrontlinePlayerStatsVO) : void
      {
         var _loc2_:String = "as_updateEpicPlayerStats" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function setEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
         var _loc2_:String = "as_setEpicVehiclesStats" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function updateEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
         var _loc2_:String = "as_updateEpicVehiclesStats" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
