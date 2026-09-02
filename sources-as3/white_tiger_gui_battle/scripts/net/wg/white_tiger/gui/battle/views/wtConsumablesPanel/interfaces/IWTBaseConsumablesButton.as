package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces
{
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IConsumablesButton;
   
   public interface IWTBaseConsumablesButton extends IConsumablesButton
   {
       
      
      function wtShowActive(param1:int) : void;
      
      function wtSetDisabled(param1:Boolean) : void;
   }
}
