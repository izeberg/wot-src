package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWidgetsPanelMeta extends IEventDispatcher
   {
       
      
      function as_addWidget(param1:String) : void;
      
      function as_updateLayout(param1:int, param2:int) : void;
      
      function as_updateCrosshairType(param1:int) : void;
      
      function as_setVisible(param1:Boolean) : void;
      
      function as_isPlayer(param1:Boolean) : void;
      
      function as_isReplay(param1:Boolean) : void;
   }
}
