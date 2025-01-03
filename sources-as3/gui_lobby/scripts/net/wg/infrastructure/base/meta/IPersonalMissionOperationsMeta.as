package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IPersonalMissionOperationsMeta extends IEventDispatcher
   {
       
      
      function closeViewS() : void;
      
      function onTabSelectedS(param1:int) : void;
      
      function as_setSelectedTab(param1:int) : void;
   }
}
