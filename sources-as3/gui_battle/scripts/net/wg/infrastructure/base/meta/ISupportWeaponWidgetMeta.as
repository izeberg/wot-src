package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ISupportWeaponWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setActiveProgress(param1:Number) : void;
      
      function as_setPreparingProgress(param1:Number) : void;
      
      function as_shootDone() : void;
   }
}
