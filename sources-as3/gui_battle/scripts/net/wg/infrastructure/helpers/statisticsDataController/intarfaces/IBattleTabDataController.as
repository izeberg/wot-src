package net.wg.infrastructure.helpers.statisticsDataController.intarfaces
{
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   
   public interface IBattleTabDataController
   {
       
      
      function setArenaInfo(param1:IDAAPIDataClass) : void;
      
      function setQuestStatus(param1:IDAAPIDataClass) : void;
   }
}
