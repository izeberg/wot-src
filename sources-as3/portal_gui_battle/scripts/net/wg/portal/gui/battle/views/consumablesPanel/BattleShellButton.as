package net.wg.portal.gui.battle.views.consumablesPanel
{
   import flash.display.Sprite;
   import net.wg.gui.battle.views.consumablesPanel.BattleShellButton;
   
   public class BattleShellButton extends net.wg.gui.battle.views.consumablesPanel.BattleShellButton
   {
       
      
      public var iconInfinity:Sprite = null;
      
      public function BattleShellButton()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         glow.visible = false;
         this.iconInfinity.visible = true;
         quantityField.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.iconInfinity = null;
         super.onDispose();
      }
   }
}
