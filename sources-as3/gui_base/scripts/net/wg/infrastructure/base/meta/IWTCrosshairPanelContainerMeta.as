package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWTCrosshairPanelContainerMeta extends IEventDispatcher
   {
       
      
      function as_showPlasmaIndicator(param1:Number, param2:Number, param3:String) : void;
      
      function as_setPlasmaSaved(param1:Number) : void;
      
      function as_showExplosiveShotIndicator(param1:Boolean) : void;
      
      function as_showBarrier(param1:Boolean, param2:String) : void;
      
      function as_showIncreaseDamage(param1:Boolean) : void;
      
      function as_hideIncreaseDamage(param1:Boolean) : void;
      
      function as_updateIncreaseDamage(param1:uint, param2:Boolean, param3:Boolean) : void;
      
      function as_showReloadBoost(param1:Boolean) : void;
      
      function as_hideReloadBoost(param1:Boolean) : void;
      
      function as_updateReloadBoost(param1:uint, param2:Boolean, param3:Boolean) : void;
      
      function as_show(param1:Boolean) : void;
      
      function as_hide(param1:Boolean) : void;
   }
}
