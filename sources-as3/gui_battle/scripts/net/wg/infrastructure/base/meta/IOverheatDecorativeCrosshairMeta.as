package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IOverheatDecorativeCrosshairMeta extends IEventDispatcher
   {
       
      
      function as_setStacksProgres(param1:Number, param2:int) : void;
      
      function as_setHeatProgres(param1:Number) : void;
      
      function as_updateState(param1:int) : void;
      
      function as_setInitData(param1:int, param2:int, param3:Number, param4:Number, param5:Boolean) : void;
      
      function as_setDamageData(param1:int, param2:int) : void;
   }
}
