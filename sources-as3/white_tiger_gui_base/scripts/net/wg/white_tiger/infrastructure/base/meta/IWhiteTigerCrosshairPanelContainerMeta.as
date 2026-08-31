package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerCrosshairPanelContainerMeta extends IEventDispatcher
   {
       
      
      function as_showPlasmaIndicator(param1:Number, param2:Boolean, param3:String) : void;
      
      function as_showExplosiveShotIndicator(param1:Boolean) : void;
   }
}
