package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IDailyQuestMeta extends IEventDispatcher
   {
       
      
      function updateWidgetLayoutS(param1:int) : void;
      
      function as_setEnabled(param1:Boolean) : void;
   }
}
