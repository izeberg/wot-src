package net.wg.infrastructure.managers
{
   import flash.events.IEventDispatcher;
   import net.wg.infrastructure.interfaces.ILayoutPart;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public interface ISharedLayoutManager extends IEventDispatcher, IDisposable
   {
       
      
      function registerLayout(param1:ILayoutPart) : void;
      
      function unregisterLayout(param1:ILayoutPart) : void;
      
      function notifyLayoutKilled(param1:uint) : void;
   }
}
