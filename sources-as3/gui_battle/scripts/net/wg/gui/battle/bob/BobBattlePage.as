package net.wg.gui.battle.bob
{
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.gui.battle.bob.data.BobBattleStatisticDataController;
   import net.wg.gui.battle.bob.stats.components.playersPanel.list.BobPlayersPanelListLeft;
   import net.wg.gui.battle.components.StatusNotificationsPanel;
   import net.wg.gui.battle.components.pointsOfInterestNotificationPanel.PointsOfInterestNotificationPanel;
   import net.wg.gui.battle.random.views.BattlePage;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   
   public class BobBattlePage extends BattlePage
   {
      
      private static const MESSANGER_SWAP_AREA_TOP_OFFSET:Number = 86;
       
      
      public var pointsOfInterestNotificationPanel:PointsOfInterestNotificationPanel = null;
      
      public var statusNotificationsPanel:StatusNotificationsPanel = null;
      
      public function BobBattlePage()
      {
         super();
      }
      
      override protected function createStatisticsController() : BattleStatisticDataController
      {
         return new BobBattleStatisticDataController(this);
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         if(isDisposed())
         {
            return;
         }
         super.updateStage(param1,param2);
         this.pointsOfInterestNotificationPanel.updateStage(param1,param2);
         this.statusNotificationsPanel.updateStage(param1,param2);
         invalidateLayout();
      }
      
      override protected function onPopulate() : void
      {
         registerComponent(this.pointsOfInterestNotificationPanel,BATTLE_VIEW_ALIASES.POINT_OF_INTEREST_NOTIFICATIONS_PANEL);
         registerComponent(this.statusNotificationsPanel,BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL);
         super.onPopulate();
      }
      
      override protected function onDispose() : void
      {
         this.pointsOfInterestNotificationPanel = null;
         this.statusNotificationsPanel = null;
         super.onDispose();
      }
      
      override protected function updateBattleMessengerSwapArea() : void
      {
         var _loc1_:BobPlayersPanelListLeft = BobPlayersPanelListLeft(playersPanel.listLeft);
         var _loc2_:int = _loc1_.getRenderersVisibleHeight();
         battleMessenger.updateSwapAreaHeight(damagePanel.y - (playersPanel.y + _loc2_) + MESSANGER_SWAP_AREA_TOP_OFFSET);
      }
   }
}
