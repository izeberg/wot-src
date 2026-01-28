package net.wg.gui.battle.epicBattle.views.stats.components
{
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.epicBattle.views.stats.events.EpicFullStatsEvent;
   import scaleform.clik.events.ButtonEvent;
   
   public class EpicStatsTableFilterGroup extends BattleUIComponent
   {
      
      private static const QUESTS_INDEX:uint = 2;
       
      
      public var btnTabPlayerLane:EpicStatsTableTabButton = null;
      
      public var btnTabAll:EpicStatsTableTabButton = null;
      
      public var btnQuests:EpicStatsTableTabButton = null;
      
      private var _buttons:Array = null;
      
      private var _index:uint = 0;
      
      public function EpicStatsTableFilterGroup()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.btnTabPlayerLane.removeEventListener(ButtonEvent.CLICK,this.onTabPlayerLaneFilterClickHandler);
         this.btnTabAll.removeEventListener(ButtonEvent.CLICK,this.onTabButtonAllFilterClickHandler);
         this.btnQuests.removeEventListener(ButtonEvent.CLICK,this.onTabButtonQuestsClickHandler);
         this.btnTabPlayerLane.dispose();
         this.btnTabPlayerLane = null;
         this.btnTabAll.dispose();
         this.btnTabAll = null;
         this.btnQuests.dispose();
         this.btnQuests = null;
         this._buttons = [];
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.btnTabAll.playerLane = -1;
         this.btnQuests.setQuestsPrefix();
         this._buttons = [this.btnTabPlayerLane,this.btnTabAll,this.btnQuests];
         this.btnTabPlayerLane.addEventListener(ButtonEvent.CLICK,this.onTabPlayerLaneFilterClickHandler);
         this.btnTabAll.addEventListener(ButtonEvent.CLICK,this.onTabButtonAllFilterClickHandler);
         this.btnQuests.addEventListener(ButtonEvent.CLICK,this.onTabButtonQuestsClickHandler);
      }
      
      public function setButtonTexts(param1:String, param2:String, param3:String) : void
      {
         this.btnTabPlayerLane.label = param1;
         this.btnTabAll.label = param2;
         this.btnQuests.label = param3;
      }
      
      public function toggleQuestsTab(param1:Boolean) : void
      {
         this._buttons[this._index].selected = !param1;
         this.btnQuests.selected = param1 || this._index == QUESTS_INDEX;
      }
      
      public function setPlayerLane(param1:int) : void
      {
         this.btnTabPlayerLane.playerLane = param1;
      }
      
      private function onTabPlayerLaneFilterClickHandler(param1:ButtonEvent) : void
      {
         this._index = 0;
         dispatchEvent(new EpicFullStatsEvent(EpicFullStatsEvent.FILTER_CHANGED,this.btnTabPlayerLane.playerLane));
      }
      
      private function onTabButtonAllFilterClickHandler(param1:ButtonEvent) : void
      {
         this._index = 1;
         dispatchEvent(new EpicFullStatsEvent(EpicFullStatsEvent.FILTER_CHANGED,-1));
      }
      
      private function onTabButtonQuestsClickHandler(param1:ButtonEvent) : void
      {
         this._index = 2;
         dispatchEvent(new EpicFullStatsEvent(EpicFullStatsEvent.FILTER_CHANGED,-1,false));
      }
   }
}
