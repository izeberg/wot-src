package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IAccuracyStackDecorativeCrosshairMeta extends IEventDispatcher
   {
       
      
      function as_setInitData(param1:int, param2:int) : void;
      
      function as_setStacksProgres(param1:int, param2:Number) : void;
      
      function as_setGainingActive(param1:Boolean) : void;
      
      function as_setSpeedLimitActive(param1:Boolean) : void;
   }
}
