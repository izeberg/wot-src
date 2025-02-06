package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IPlayerSatisfactionWidgetMeta extends IEventDispatcher
   {
       
      
      function selectedChoiceS(param1:int) : void;
      
      function as_setInitData(param1:Array, param2:Array, param3:int) : void;
   }
}
