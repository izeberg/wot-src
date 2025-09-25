package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IUserMissionsHubContainerViewMeta extends IEventDispatcher
   {
       
      
      function resetFiltersS() : void;
      
      function onCloseS() : void;
      
      function as_showFilterCounter(param1:String, param2:Boolean) : void;
      
      function as_blinkFilterCounter() : void;
      
      function as_updateCommonMissionsTabVisibility(param1:Boolean) : void;
      
      function as_updateCommonMissionsTabPosition(param1:Number, param2:Number) : void;
      
      function as_setBackground(param1:String) : void;
   }
}
