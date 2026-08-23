package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWTMissileWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setRange(param1:Number) : void;
      
      function as_setAltitude(param1:Number) : void;
      
      function as_setMaxAltitude(param1:Number) : void;
      
      function as_show(param1:Boolean) : void;
      
      function as_hide(param1:Boolean) : void;
   }
}
