package net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.consumablesPanel.BattleShellButton;
   
   public class WhiteTigerBattleShellButton extends BattleShellButton implements IWhiteTigerBattleShellButton
   {
       
      
      public var hit:MovieClip = null;
      
      public var inspired:MovieClip = null;
      
      public function WhiteTigerBattleShellButton()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         hitArea = this.hit;
         this.inspired.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.hit = null;
         this.inspired = null;
         super.onDispose();
      }
      
      public function setInspired(param1:Boolean = false) : void
      {
         this.inspired.visible = param1;
      }
   }
}
