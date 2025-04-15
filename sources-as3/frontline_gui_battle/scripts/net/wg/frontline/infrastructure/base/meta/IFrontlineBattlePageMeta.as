package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineBattlePageMeta extends IEventDispatcher
   {
       
      
      function onDeactivateRadialMenuS() : void;
      
      function as_setSelectReservesAvailable(param1:Boolean) : void;
      
      function as_setVehPostProgressionEnabled(param1:Boolean) : void;
   }
}
