package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineModificationPanelMeta extends IEventDispatcher
   {
       
      
      function as_setData(param1:Object) : void;
      
      function as_setVisible(param1:Boolean) : void;
   }
}
