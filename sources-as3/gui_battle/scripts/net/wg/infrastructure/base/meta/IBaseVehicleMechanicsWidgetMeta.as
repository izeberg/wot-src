package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IBaseVehicleMechanicsWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setState(param1:String, param2:Boolean) : void;
      
      function as_setHotKeys(param1:Array) : void;
      
      function as_setVisible(param1:Boolean) : void;
      
      function as_setCrosshairType(param1:int) : void;
      
      function as_setTime(param1:Number) : void;
   }
}
