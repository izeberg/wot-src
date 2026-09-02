package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerHunterRespawnViewMeta extends IEventDispatcher
   {
       
      
      function onRespawnPointClickS(param1:String) : void;
      
      function as_updateTimer(param1:Number, param2:Number, param3:Boolean, param4:Number) : void;
   }
}
