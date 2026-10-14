package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFortVehicleSelectPopoverMeta extends IEventDispatcher
   {
       
      
      function onFilterChangeS(param1:int, param2:Boolean) : void;
      
      function onFrozenChangeS(param1:Boolean) : void;
   }
}
