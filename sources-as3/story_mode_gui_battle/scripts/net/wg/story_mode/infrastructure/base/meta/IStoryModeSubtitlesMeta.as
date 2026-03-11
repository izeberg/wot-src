package net.wg.story_mode.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IStoryModeSubtitlesMeta extends IEventDispatcher
   {
       
      
      function as_show(param1:String) : void;
      
      function as_hide() : void;
   }
}
