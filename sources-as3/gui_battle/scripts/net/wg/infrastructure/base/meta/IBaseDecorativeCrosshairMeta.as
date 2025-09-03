package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IBaseDecorativeCrosshairMeta extends IEventDispatcher
   {
       
      
      function as_setState(param1:String, param2:Boolean) : void;
      
      function as_setVisible(param1:Boolean) : void;
   }
}
