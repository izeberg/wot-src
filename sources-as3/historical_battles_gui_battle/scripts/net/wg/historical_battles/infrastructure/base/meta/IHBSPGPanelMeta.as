package net.wg.historical_battles.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IHBSPGPanelMeta extends IEventDispatcher
   {
       
      
      function as_show() : void;
      
      function as_setSPGList(param1:Array) : void;
      
      function as_setSPGHp(param1:int, param2:int, param3:int) : void;
      
      function as_hideTitle() : void;
   }
}
