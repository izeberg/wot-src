package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IPillboxSiegeWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setProgress(param1:Number, param2:Number) : void;
      
      function as_setCondition(param1:String, param2:Boolean) : void;
      
      function as_setDeviceStates(param1:Array) : void;
      
      function as_setCommand(param1:String, param2:String, param3:Number) : void;
   }
}
