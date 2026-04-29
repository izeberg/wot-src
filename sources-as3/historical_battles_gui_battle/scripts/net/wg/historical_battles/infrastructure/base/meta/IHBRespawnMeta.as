package net.wg.historical_battles.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IHBRespawnMeta extends IEventDispatcher
   {
       
      
      function onPickVehicleS(param1:int) : void;
      
      function onSelectVehicleS() : void;
      
      function as_updateGoalTime(param1:String) : void;
      
      function as_setData(param1:Object) : void;
      
      function as_setTimerData(param1:Object) : void;
      
      function as_setVisibility(param1:Boolean, param2:Boolean) : void;
   }
}
