package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWheeledDashWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setPreparingProgress(param1:Number) : void;
      
      function as_setActiveProgress(param1:Number) : void;
      
      function as_isReducedCooldown(param1:Boolean) : void;
   }
}
