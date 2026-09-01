package net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel
{
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IConsumablesButton;
   
   public interface IWhiteTigerConsumablesButton extends IConsumablesButton
   {
       
      
      function setCharge(param1:int, param2:Number, param3:Boolean) : void;
      
      function setSelected(param1:Boolean) : void;
      
      function setDebuffView(param1:Boolean) : void;
      
      function setStage(param1:int) : void;
   }
}
