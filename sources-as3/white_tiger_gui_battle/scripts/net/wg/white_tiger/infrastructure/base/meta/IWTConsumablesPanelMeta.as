package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWTConsumablesPanelMeta extends IEventDispatcher
   {
       
      
      function as_wtShowActive(param1:int, param2:int) : void;
      
      function as_wtSetDisabled(param1:int, param2:Boolean) : void;
      
      function as_wtShowCooldown(param1:int, param2:int) : void;
      
      function as_wtShowReady(param1:int) : void;
      
      function as_wtSetChargeProgress(param1:int, param2:int) : void;
      
      function as_wtShowPreparing(param1:int) : void;
      
      function as_wtShowDeploying(param1:int) : void;
      
      function as_wtSetLocked(param1:int, param2:Boolean) : void;
      
      function as_wtAddPassiveAbilitySlot(param1:int, param2:String, param3:String) : void;
   }
}
