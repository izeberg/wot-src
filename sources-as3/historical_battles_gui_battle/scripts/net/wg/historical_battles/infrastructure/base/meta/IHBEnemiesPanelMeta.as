package net.wg.historical_battles.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IHBEnemiesPanelMeta extends IEventDispatcher
   {
       
      
      function as_getEnemyInfoDP() : Object;
      
      function as_setEnemyHp(param1:int, param2:int, param3:int) : void;
      
      function as_setChatCommand(param1:int, param2:String, param3:uint) : void;
      
      function as_setChatCommandsVisibility(param1:Boolean) : void;
   }
}
