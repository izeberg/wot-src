package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineReinforcementPanelMeta extends IEventDispatcher
   {
       
      
      function as_setPlayerLives(param1:int) : void;
      
      function as_setTimestamp(param1:Number, param2:Number) : void;
      
      function as_setTime(param1:String) : void;
   }
}
