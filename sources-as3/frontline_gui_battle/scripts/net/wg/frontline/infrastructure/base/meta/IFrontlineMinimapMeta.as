package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineMinimapMeta extends IEventDispatcher
   {
       
      
      function onZoomModeChangedS(param1:int) : void;
      
      function as_setZoomMode(param1:Number, param2:String) : void;
      
      function as_setMapDimensions(param1:int, param2:int) : void;
      
      function as_updateSectorStateStats(param1:Object) : void;
      
      function as_setMapShortcutKeyCode(param1:Number) : void;
   }
}
