package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ILowChargeShotWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setInitialTime(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number) : void;
      
      function as_setTimeLeft(param1:Number, param2:Number, param3:Boolean) : void;
   }
}
