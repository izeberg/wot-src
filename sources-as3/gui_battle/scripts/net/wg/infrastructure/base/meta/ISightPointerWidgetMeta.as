package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ISightPointerWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setProgress(param1:Number, param2:Number) : void;
      
      function as_setTankIconState(param1:String) : void;
      
      function as_triggerHighlightLamp() : void;
   }
}
