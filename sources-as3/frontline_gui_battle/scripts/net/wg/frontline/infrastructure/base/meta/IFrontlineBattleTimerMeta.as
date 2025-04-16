package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineBattleTimerMeta extends IEventDispatcher
   {
       
      
      function as_setTotalTimeWithSeconds(param1:String, param2:String, param3:Number) : void;
      
      function as_enableOvertime(param1:Boolean) : void;
   }
}
