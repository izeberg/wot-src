package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IDebugPanelMeta extends IEventDispatcher
   {
       
      
      function as_initReplay() : void;
      
      function as_updatePing(param1:int) : void;
      
      function as_updateFps(param1:int) : void;
      
      function as_updatePingFPS(param1:int, param2:int) : void;
      
      function as_updateAll(param1:int, param2:int, param3:Boolean) : void;
      
      function as_updateReplay(param1:int, param2:int, param3:Boolean, param4:int) : void;
   }
}
