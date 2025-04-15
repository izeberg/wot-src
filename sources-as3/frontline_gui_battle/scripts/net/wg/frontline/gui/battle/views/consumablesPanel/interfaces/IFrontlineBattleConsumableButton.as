package net.wg.frontline.gui.battle.views.consumablesPanel.interfaces
{
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IConsumablesButton;
   
   public interface IFrontlineBattleConsumableButton extends IConsumablesButton
   {
       
      
      function updateLockedInformation(param1:int, param2:String, param3:Boolean) : void;
      
      function updateLevelInformation(param1:int) : void;
      
      function showPossibleStacks(param1:int) : void;
      
      function updateStacks(param1:int) : void;
   }
}
