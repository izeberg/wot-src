package net.wg.historical_battles.gui.battle.views.battlePage
{
   import flash.events.Event;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.historical_battles.gui.battle.views.spgPanel.HBSPGPanel;
   import net.wg.historical_battles.gui.battle.views.spgPanel.events.HBSPGPanelEvent;
   
   public class HBDefenceBattlePage extends HBBaseBattlePage
   {
      
      private static const SPG_PANEL_OFFSET_Y:int = 10;
       
      
      public var spgPanel:HBSPGPanel = null;
      
      public function HBDefenceBattlePage()
      {
         super();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerComponent(this.spgPanel,BATTLE_VIEW_ALIASES.HISTORICAL_BATTLES_SPG_PANEL);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.spgPanel.addEventListener(HBSPGPanelEvent.SIZE_CHANGE,this.onSPGPanelSizeChangeHandler);
      }
      
      override protected function onDispose() : void
      {
         this.spgPanel.removeEventListener(HBSPGPanelEvent.SIZE_CHANGE,this.onSPGPanelSizeChangeHandler);
         this.spgPanel = null;
         super.onDispose();
      }
      
      override protected function respawnVisibilityChanged(param1:Boolean, param2:Boolean) : void
      {
         super.respawnVisibilityChanged(param1,param2);
         var _loc3_:Number = param1 && param2 ? Number(COMPS_ALPHA_IN_RESPAWN) : Number(1);
         this.spgPanel.alpha = _loc3_;
      }
      
      override protected function playersPanelSizeChanged() : void
      {
         super.playersPanelSizeChanged();
         this.spgPanel.y = hbPlayersPanel.y + hbPlayersPanel.height + SPG_PANEL_OFFSET_Y | 0;
      }
      
      override protected function getPlayersPanelBottom() : int
      {
         return this.spgPanel.y + this.spgPanel.height;
      }
      
      private function onSPGPanelSizeChangeHandler(param1:Event) : void
      {
         updateBattleMessengerSwapArea();
         updateBattleDamageLogPanel();
      }
   }
}
