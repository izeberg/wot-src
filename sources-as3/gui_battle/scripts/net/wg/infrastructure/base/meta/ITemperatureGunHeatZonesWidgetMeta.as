package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ITemperatureGunHeatZonesWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setHeatZonesValues(param1:Number, param2:Number) : void;
      
      function as_setTemperature(param1:Number) : void;
   }
}
