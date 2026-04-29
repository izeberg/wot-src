package net.wg.historical_battles.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IHBPhaseIndicatorMeta extends IEventDispatcher
   {
       
      
      function as_setData(param1:Object) : void;
      
      function as_setVisible(param1:Boolean) : void;
   }
}
