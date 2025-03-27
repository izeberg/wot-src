package net.wg.gui.battle.random.views.stats.components.tabScreen
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.data.VO.daapi.DAAPIArenaInfoVO;
   import net.wg.data.VO.daapi.DAAPIQuestStatusVO;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.LobbyMetrics;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.FullStatsHeader;
   import net.wg.gui.battle.components.FullStatsTitle;
   import net.wg.gui.battle.interfaces.ITabScreen;
   import net.wg.gui.battle.views.questProgress.data.QPProgressTrackingVO;
   import net.wg.gui.battle.views.questProgress.data.QPTrackingDataItemVO;
   import net.wg.gui.battle.views.questProgress.data.QuestProgressPerformVO;
   import net.wg.gui.battle.views.questProgress.events.QuestProgressTabEvent;
   import net.wg.gui.battle.views.questProgress.interfaces.IQuestProgressView;
   import net.wg.gui.battle.views.questProgress.interfaces.IQuestProgressViewOperationSelector;
   import net.wg.gui.battle.views.tabContent.TabContent;
   import net.wg.gui.components.advanced.ContentTabBar;
   import net.wg.gui.lobby.settings.vo.TabsDataVo;
   import net.wg.infrastructure.base.meta.ITabScreenMeta;
   import net.wg.infrastructure.base.meta.impl.TabScreenMeta;
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.IndexEvent;
   
   public class TabScreen extends TabScreenMeta implements ITabScreenMeta, ITabScreen
   {
      
      private static const MIN_HEIGHT:int = 880;
      
      private static const NO_QUEST_TF_GAP:int = 12;
      
      private static const TAB_RESERVES_Y_SHIFT:int = 13;
      
      private static const MIN_TABS_RENDERER_WIDTH:int = 134;
      
      private static const TABS_Y:int = 141;
      
      private static const TABS_SMALL_Y:int = 98;
      
      private static const TITLE_SMALL_Y_SHIFT:int = 58;
      
      private static const QUEST_SMALL_Y_SHIFT:int = -30;
      
      private static const QUEST_Y_SHIFT:int = 103;
      
      private static const STATS_TAB_ALIAS:String = "stats";
      
      private static const QUEST_TAB_ALIAS:String = "quests_progress";
       
      
      public var modalBgSpr:Sprite = null;
      
      public var title:FullStatsTitle = null;
      
      public var header:FullStatsHeader = null;
      
      public var tabs:ContentTabBar = null;
      
      public var tabQuest:IQuestProgressViewOperationSelector = null;
      
      public var tabContent:TabContent = null;
      
      public var noQuestTitleTF:TextField = null;
      
      public var noQuestDescrTF:TextField = null;
      
      private var _arenaData:DAAPIArenaInfoVO = null;
      
      private var emptyStatusVO:DAAPIQuestStatusVO = null;
      
      private var _lastSelectedTabIndex:int = 0;
      
      private var _currentMissionName:String = null;
      
      private var _questStatusData:DAAPIQuestStatusVO = null;
      
      private var _hasQuestToPerform:Boolean = false;
      
      private var _stageWidth:int = 0;
      
      private var _stageHeight:int = 0;
      
      public function TabScreen()
      {
         super();
         this.header.setMinHeight(MIN_HEIGHT);
         this.visible = false;
         this.emptyStatusVO = new DAAPIQuestStatusVO({"status":Values.EMPTY_STR});
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.initTitle();
         this.tabs.itemRendererName = Linkages.CONTENT_TAB_RENDERER;
         this.tabs.minRendererWidth = MIN_TABS_RENDERER_WIDTH;
         this.tabs.addEventListener(IndexEvent.INDEX_CHANGE,this.onTabsIndexChangeHandler);
         if(this.tabQuest)
         {
            this.tabQuest.addEventListener(QuestProgressTabEvent.QUEST_SELECT,this.onProgressTrackingQuestSelectHandler);
         }
      }
      
      private function initTitle() : void
      {
         this.title.setStatus(this.emptyStatusVO);
         this.setTitle();
      }
      
      private function setTitle() : void
      {
         this.title.setStatus(this._questStatusData == null ? this.emptyStatusVO : this._questStatusData);
         if(this.tabQuest && this.tabQuest.visible)
         {
            this.title.setTitle(this._currentMissionName);
         }
      }
      
      override protected function onDispose() : void
      {
         if(this.tabQuest)
         {
            this.tabQuest.removeEventListener(QuestProgressTabEvent.QUEST_SELECT,this.onProgressTrackingQuestSelectHandler);
            this.tabQuest.dispose();
            this.tabQuest = null;
         }
         if(this.tabContent)
         {
            this.tabContent = null;
         }
         this.tabs.removeEventListener(IndexEvent.INDEX_CHANGE,this.onTabsIndexChangeHandler);
         this.tabs.dispose();
         this.tabs = null;
         this.noQuestTitleTF = null;
         this.noQuestDescrTF = null;
         this._questStatusData = null;
         this.modalBgSpr = null;
         this.header.dispose();
         this.header = null;
         this.emptyStatusVO.dispose();
         this.emptyStatusVO = null;
         super.onDispose();
      }
      
      private function onTabsIndexChangeHandler(param1:IndexEvent) : void
      {
         var _loc2_:String = this.getTabDataAlias(param1.index);
         this.tabContent.onTabChangedS(_loc2_);
         this.updateCurrentTab();
         this.updateStage();
      }
      
      protected function updateCurrentTab() : void
      {
         var _loc3_:Boolean = false;
         var _loc1_:* = this.getTabDataAlias(this.tabs.selectedIndex);
         var _loc2_:Boolean = _loc1_ == STATS_TAB_ALIAS;
         if(visible)
         {
            onStatsTableVisibiltyToggledS(_loc2_);
         }
         _loc3_ = _loc1_ == QUEST_TAB_ALIAS;
         var _loc4_:Boolean = _loc3_ && this._hasQuestToPerform;
         if(this.tabContent)
         {
            this.tabContent.visible = !_loc3_;
         }
         if(this.tabQuest)
         {
            this.tabQuest.visible = _loc4_;
         }
         this.title.visible = _loc4_;
         if(_loc4_)
         {
            this.setTitle();
         }
         this.noQuestTitleTF.visible = this.noQuestDescrTF.visible = !this._hasQuestToPerform && _loc3_;
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(param1 && this.title.visible)
         {
            this.title.validateNow();
         }
         super.visible = param1;
         if(!initialized)
         {
            return;
         }
         var _loc2_:Boolean = this.getTabDataAlias(this.tabs.selectedIndex) == STATS_TAB_ALIAS;
         if(visible)
         {
            onStatsTableVisibiltyToggledS(_loc2_);
         }
         else
         {
            onStatsTableVisibiltyToggledS(false);
         }
      }
      
      private function getTabDataAlias(param1:int) : String
      {
         if(param1 < 0)
         {
            return Values.EMPTY_STR;
         }
         var _loc2_:TabsDataVo = this.tabs.dataProvider[param1];
         return _loc2_.alias;
      }
      
      private function onProgressTrackingQuestSelectHandler(param1:QuestProgressTabEvent) : void
      {
         onSelectQuestS(param1.questID);
      }
      
      override protected function questProgressPerform(param1:QuestProgressPerformVO) : void
      {
         this.noQuestTitleTF.htmlText = param1.noQuestTitle;
         this.noQuestDescrTF.htmlText = param1.noQuestDescr;
         if(this._hasQuestToPerform != param1.hasQuestToPerform)
         {
            this._hasQuestToPerform = param1.hasQuestToPerform;
            this.updateCurrentTab();
         }
      }
      
      override protected function updateTabs(param1:DataProvider) : void
      {
         this.tabs.dataProvider = param1;
      }
      
      override protected function updateProgressTracking(param1:QPProgressTrackingVO) : void
      {
         var _loc2_:QPTrackingDataItemVO = null;
         if(this.tabQuest)
         {
            this.tabQuest.updateProgressTracking(param1);
         }
         for each(_loc2_ in param1.trackingData)
         {
            if(_loc2_.selected)
            {
               this._currentMissionName = _loc2_.fullMissionName;
               break;
            }
         }
      }
      
      public function as_setActiveTab(param1:Number) : void
      {
         this._lastSelectedTabIndex = this.tabs.selectedIndex;
         this.tabs.selectedIndex = param1;
      }
      
      public function as_resetActiveTab() : void
      {
         this.tabs.selectedIndex = this._lastSelectedTabIndex;
      }
      
      public function getStatsProgressView() : IQuestProgressView
      {
         return this.tabQuest;
      }
      
      public function getTabContentView() : IDAAPIModule
      {
         return this.tabContent;
      }
      
      public function updateStageSize(param1:Number, param2:Number) : void
      {
         this._stageWidth = param1;
         this._stageHeight = param2;
         this.updateStage();
      }
      
      public function updateStage() : *
      {
         var _loc1_:int = this._stageWidth >> 1;
         var _loc2_:int = 0;
         x = _loc1_;
         y = _loc2_;
         this.modalBgSpr.visible = false;
         this.modalBgSpr.x = -_loc1_;
         this.modalBgSpr.y = _loc2_;
         this.modalBgSpr.width = this._stageWidth;
         this.modalBgSpr.height = this._stageHeight;
         this.modalBgSpr.visible = true;
         this.doUpdateSizeTop(this._stageWidth,this._stageHeight);
         this.doUpdateSizeTable(this._stageWidth,this._stageHeight);
      }
      
      private function doUpdateSizeTop(param1:Number, param2:Number) : void
      {
         this.header.updateSize(param1,param2);
         this.tabs.y = param2 < MIN_HEIGHT ? Number(TABS_SMALL_Y) : Number(TABS_Y);
      }
      
      private function doUpdateSizeTable(param1:Number, param2:Number) : void
      {
         var _loc4_:int = 0;
         var _loc3_:int = param2 - LobbyMetrics.MIN_STAGE_HEIGHT >> 2;
         this.title.y = this.tabs.y + TITLE_SMALL_Y_SHIFT + _loc3_;
         if(this.tabQuest != null)
         {
            _loc4_ = param2 < MIN_HEIGHT ? int(QUEST_SMALL_Y_SHIFT) : int(0);
            this.tabQuest.y = this.title.y + QUEST_Y_SHIFT + _loc4_;
         }
         if(this.tabContent)
         {
            this.tabContent.y = this.tabs.y + TAB_RESERVES_Y_SHIFT;
            this.tabContent.width = param1;
            this.tabContent.height = param2 - this.tabContent.y;
            this.tabContent.x = -this.tabContent.width >> 1;
         }
         this.noQuestTitleTF.y = param2 - (this.noQuestTitleTF.height + this.noQuestTitleTF.height + NO_QUEST_TF_GAP) >> 1;
         this.noQuestDescrTF.y = this.noQuestTitleTF.y + this.noQuestTitleTF.height + NO_QUEST_TF_GAP | 0;
      }
      
      public function setArenaInfo(param1:IDAAPIDataClass) : void
      {
         if(this._arenaData != param1 && param1)
         {
            this._arenaData = DAAPIArenaInfoVO(param1);
            this.header.update(this._arenaData);
         }
      }
      
      public function setQuestStatus(param1:IDAAPIDataClass) : void
      {
         this._questStatusData = DAAPIQuestStatusVO(param1);
         if(visible)
         {
            this.updateCurrentTab();
         }
      }
   }
}
