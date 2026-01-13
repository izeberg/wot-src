package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IBattleTankCarouselMeta extends IEventDispatcher
   {
       
      
      function setFilterS(param1:int) : void;
      
      function resetPlaylistAndFiltersS() : void;
      
      function as_useExtendedCarousel(param1:Boolean) : void;
      
      function as_scrollToSlot(param1:int) : void;
   }
}
