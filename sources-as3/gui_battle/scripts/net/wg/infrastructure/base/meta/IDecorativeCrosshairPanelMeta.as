package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IDecorativeCrosshairPanelMeta extends IEventDispatcher
   {
       
      
      function as_addDecorCrosshair(param1:String) : void;
      
      function as_setVisible(param1:Boolean) : void;
      
      function as_updateLayout(param1:int, param2:int) : void;
      
      function as_updateCrosshairType(param1:int) : void;
   }
}
