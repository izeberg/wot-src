package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ITemperatureGunOverheatWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setupThresholds(param1:Number, param2:Number) : void;
      
      function as_setTemperature(param1:Number) : void;
   }
}
