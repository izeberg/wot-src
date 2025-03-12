package net.wg.gui.battle.fep.views
{
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.gui.battle.components.StatusNotificationsPanel;
   import net.wg.gui.battle.random.views.BattlePage;
   
   public class FepBattlePage extends BattlePage
   {
       
      
      public var statusNotificationsPanel:StatusNotificationsPanel = null;
      
      public function FepBattlePage()
      {
         super();
         excludedComponentAliases.push(BATTLE_VIEW_ALIASES.TIMERS_PANEL);
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         this.statusNotificationsPanel.updateStage(param1,param2);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerComponent(this.statusNotificationsPanel,BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL);
      }
      
      override protected function onDispose() : void
      {
         this.statusNotificationsPanel = null;
         super.onDispose();
      }
   }
}
