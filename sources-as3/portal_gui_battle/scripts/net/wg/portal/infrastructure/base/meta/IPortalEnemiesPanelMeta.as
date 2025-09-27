package net.wg.portal.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IPortalEnemiesPanelMeta extends IEventDispatcher
   {
       
      
      function as_setCurrentPhase(param1:int) : void;
      
      function as_setPhasesCount(param1:int) : void;
      
      function as_setLaneVehicleInfo(param1:int, param2:int, param3:int, param4:int) : void;
      
      function as_setBuffStatusVisible(param1:Boolean) : void;
      
      function as_resetState() : void;
   }
}
