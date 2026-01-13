package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineCarouselFilterPopoverMeta extends IEventDispatcher
   {
       
      
      function onPlayListsChangeS(param1:String) : void;
      
      function as_updatePlayLists(param1:Object) : void;
   }
}
