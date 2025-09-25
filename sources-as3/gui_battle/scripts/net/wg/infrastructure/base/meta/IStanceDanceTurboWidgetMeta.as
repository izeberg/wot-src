package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IStanceDanceTurboWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setProgress(param1:Boolean, param2:Number) : void;
      
      function as_setSpeed(param1:Number, param2:Boolean) : void;
      
      function as_setParams(param1:Number, param2:Number, param3:Number, param4:Number) : void;
      
      function as_switchTimer(param1:Number) : void;
      
      function as_keysVisible(param1:Boolean) : void;
   }
}
