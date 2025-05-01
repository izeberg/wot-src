package net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components
{
   public class HBEndGameMessageVictory extends HBEndGameMessage
   {
       
      
      public var flare:HBVictoryFlare;
      
      public function HBEndGameMessageVictory()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.flare.dispose();
         this.flare = null;
         super.onDispose();
      }
      
      override protected function updateLayout() : void
      {
         super.updateLayout();
         this.flare.updateLayout(App.stageSizeMgr.currentBreakPoint);
      }
   }
}
