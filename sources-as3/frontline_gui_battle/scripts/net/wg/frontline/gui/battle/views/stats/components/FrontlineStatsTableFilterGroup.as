package net.wg.frontline.gui.battle.views.stats.components
{
   import net.wg.data.constants.Values;
   import net.wg.frontline.gui.battle.views.stats.events.FrontlineFullStatsEvent;
   import net.wg.gui.battle.components.BattleUIComponent;
   import scaleform.clik.events.ButtonEvent;
   
   public class FrontlineStatsTableFilterGroup extends BattleUIComponent
   {
       
      
      public var btnTabPlayerLane:FrontlineStatsTableTabButton = null;
      
      public var btnTabAll:FrontlineStatsTableTabButton = null;
      
      public function FrontlineStatsTableFilterGroup()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.btnTabPlayerLane.removeEventListener(ButtonEvent.CLICK,this.onTabPlayerLaneFilterClickHandler);
         this.btnTabAll.removeEventListener(ButtonEvent.CLICK,this.onTabButtonAllFilterClickHandler);
         this.btnTabPlayerLane.dispose();
         this.btnTabPlayerLane = null;
         this.btnTabAll.dispose();
         this.btnTabAll = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.btnTabAll.playerLane = Values.DEFAULT_INT;
         this.btnTabPlayerLane.addEventListener(ButtonEvent.CLICK,this.onTabPlayerLaneFilterClickHandler);
         this.btnTabAll.addEventListener(ButtonEvent.CLICK,this.onTabButtonAllFilterClickHandler);
      }
      
      public function setButtonTexts(param1:String, param2:String) : void
      {
         this.btnTabPlayerLane.label = param1;
         this.btnTabAll.label = param2;
      }
      
      public function setPlayerLane(param1:int) : void
      {
         this.btnTabPlayerLane.playerLane = param1;
      }
      
      private function onTabPlayerLaneFilterClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new FrontlineFullStatsEvent(FrontlineFullStatsEvent.FILTER_CHANGED,this.btnTabPlayerLane.playerLane));
      }
      
      private function onTabButtonAllFilterClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new FrontlineFullStatsEvent(FrontlineFullStatsEvent.FILTER_CHANGED,-1));
      }
   }
}
