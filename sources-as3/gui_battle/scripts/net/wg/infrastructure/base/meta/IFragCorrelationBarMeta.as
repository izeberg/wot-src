package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFragCorrelationBarMeta extends IEventDispatcher
   {
       
      
      function as_updateHP(param1:String, param2:String, param3:Number, param4:String, param5:Number) : void;
      
      function as_updateViewSetting(param1:int) : void;
   }
}
