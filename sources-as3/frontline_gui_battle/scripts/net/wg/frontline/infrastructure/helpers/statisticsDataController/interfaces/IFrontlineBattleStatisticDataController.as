package net.wg.frontline.infrastructure.helpers.statisticsDataController.interfaces
{
   import net.wg.frontline.gui.battle.VO.daapi.FrontlinePlayerStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehiclesStatsVO;
   
   public interface IFrontlineBattleStatisticDataController
   {
       
      
      function setEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void;
      
      function updateEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void;
      
      function updateEpicPlayerStats(param1:FrontlinePlayerStatsVO) : void;
   }
}
