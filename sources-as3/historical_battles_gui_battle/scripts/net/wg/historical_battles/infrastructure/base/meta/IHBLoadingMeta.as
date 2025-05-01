package net.wg.historical_battles.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IHBLoadingMeta extends IEventDispatcher
   {
       
      
      function as_setData(param1:Array) : void;
      
      function as_updateProgress(param1:Number) : void;
      
      function as_loaded() : void;
   }
}
