package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IChargeShotWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setUpdateProgress(param1:uint, param2:Number) : void;
      
      function as_setShootBlock(param1:Boolean) : void;
      
      function as_setDamage(param1:uint) : void;
      
      function as_showShootBlockAnimation() : void;
   }
}
