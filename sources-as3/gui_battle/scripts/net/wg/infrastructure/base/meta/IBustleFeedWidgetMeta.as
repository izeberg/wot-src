package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IBustleFeedWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setProgress(param1:Number, param2:Number) : void;
      
      function as_setLock(param1:Boolean) : void;
      
      function as_setAvailability(param1:Boolean) : void;
      
      function as_setCommand(param1:String) : void;
   }
}
