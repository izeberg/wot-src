package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IStanceDanceFightWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setProgress(param1:Boolean, param2:Number) : void;
      
      function as_energyBoost() : void;
      
      function as_switchTimer(param1:Number) : void;
      
      function as_keysVisible(param1:Boolean) : void;
      
      function as_pauseReplay(param1:Boolean) : void;
   }
}
