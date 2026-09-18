package net.wg.app
{
   import flash.events.IEventDispatcher;
   import net.wg.infrastructure.managers.ISharedLayoutManager;
   
   public interface ICoreApplication extends IEventDispatcher
   {
       
      
      function get sharedLayoutMgr() : ISharedLayoutManager;
   }
}
