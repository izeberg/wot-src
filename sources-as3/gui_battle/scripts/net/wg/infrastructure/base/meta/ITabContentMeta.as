package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ITabContentMeta extends IEventDispatcher
   {
       
      
      function onTabChangedS(param1:String) : void;
   }
}
