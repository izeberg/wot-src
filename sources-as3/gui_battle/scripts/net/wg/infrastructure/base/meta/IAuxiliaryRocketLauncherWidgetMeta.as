package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IAuxiliaryRocketLauncherWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setPreparingProgress(param1:Number) : void;
      
      function as_shootDone() : void;
   }
}
