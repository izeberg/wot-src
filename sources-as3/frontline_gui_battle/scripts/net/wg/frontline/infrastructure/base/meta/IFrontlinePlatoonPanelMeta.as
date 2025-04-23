package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlinePlatoonPanelMeta extends IEventDispatcher
   {
       
      
      function as_setPlatoonTitle(param1:String) : void;
      
      function as_setMaxDisplayedInviteMessages(param1:int) : void;
   }
}
