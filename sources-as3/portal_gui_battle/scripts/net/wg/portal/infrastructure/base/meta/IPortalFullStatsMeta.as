package net.wg.portal.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IPortalFullStatsMeta extends IEventDispatcher
   {
       
      
      function as_setData(param1:Object) : void;
      
      function as_updateScore(param1:int, param2:int, param3:String) : void;
   }
}
