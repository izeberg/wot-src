package net.wg.infrastructure.interfaces
{
   import flash.display.DisplayObject;
   import flash.events.IEventDispatcher;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public interface ILayoutPart extends IEventDispatcher, IDisposable
   {
       
      
      function notifyAdded(param1:String, param2:uint) : void;
      
      function notifyUpdated(param1:String, param2:uint, param3:Number, param4:Number, param5:Number, param6:Number) : void;
      
      function notifyRemoved(param1:String, param2:uint) : void;
      
      function getAlgorithmTypeName() : String;
      
      function register(param1:DisplayObject) : void;
      
      function unregister(param1:DisplayObject) : void;
      
      function resendPositions() : void;
      
      function get layoutId() : uint;
      
      function get partId() : uint;
      
      function set partId(param1:uint) : void;
   }
}
