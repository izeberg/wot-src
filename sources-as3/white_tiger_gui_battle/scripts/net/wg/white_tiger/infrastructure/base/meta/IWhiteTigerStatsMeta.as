package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerStatsMeta extends IEventDispatcher
   {
       
      
      function as_updatePlayerStats(param1:Array) : void;
      
      function as_updateTitle(param1:String, param2:String) : void;
   }
}
