package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IStagedJetBoostersWidgetMeta extends IEventDispatcher
   {
       
      
      function as_setCount(param1:int) : void;
      
      function as_setProgress(param1:Number) : void;
      
      function as_updateLayout(param1:Number, param2:Number) : void;
      
      function as_setMovementInfo(param1:String) : void;
   }
}
