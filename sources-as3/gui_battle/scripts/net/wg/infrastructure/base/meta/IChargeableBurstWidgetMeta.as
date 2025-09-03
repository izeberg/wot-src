package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IChargeableBurstWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setup(param1:Number, param2:Number) : void;
      
      function as_setMode(param1:Boolean, param2:Boolean) : void;
      
      function as_setCharges(param1:Number, param2:Number, param3:Boolean) : void;
      
      function as_setShellsQuantityLeft(param1:Number) : void;
      
      function as_updateBurstReloadingState(param1:Boolean) : void;
   }
}
