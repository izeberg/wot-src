package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces
{
   public interface IWTConsumablesButton extends IWTBaseConsumablesButton
   {
       
      
      function wtShowCooldown(param1:int) : void;
      
      function wtShowReady() : void;
      
      function wtSetCharge(param1:int) : void;
      
      function wtShowPreparing() : void;
      
      function wtShowDeploying() : void;
      
      function wtSetLocked(param1:Boolean) : void;
   }
}
