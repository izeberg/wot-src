package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IAutoreloaderSurgeWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setStagesProgress(param1:Array) : void;
      
      function as_setAvailable(param1:Boolean) : void;
      
      function as_setChargeCount(param1:Number) : void;
      
      function as_setSectorCount(param1:int) : void;
      
      function as_setBoostedCharge(param1:Boolean) : void;
   }
}
