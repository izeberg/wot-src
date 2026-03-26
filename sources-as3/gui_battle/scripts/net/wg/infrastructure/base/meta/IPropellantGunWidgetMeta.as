package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IPropellantGunWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setChargeValues(param1:Number, param2:Number) : void;
      
      function as_setupThreshold(param1:Number) : void;
      
      function as_showHotKeys(param1:Boolean) : void;
      
      function as_activateHotKey(param1:String) : void;
   }
}
