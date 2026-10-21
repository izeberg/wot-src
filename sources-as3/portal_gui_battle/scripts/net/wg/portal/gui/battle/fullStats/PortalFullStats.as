package net.wg.portal.gui.battle.fullStats
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import flash.events.Event;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.interfaces.IFullStats;
   import net.wg.gui.battle.interfaces.ITabbedFullStatsTableController;
   import net.wg.gui.battle.views.questProgress.interfaces.IQuestProgressView;
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   import net.wg.portal.data.VO.fullStats.PortalFullStatsVO;
   import net.wg.portal.gui.battle.fullStats.components.Header;
   import net.wg.portal.gui.battle.fullStats.components.MinimapItemsInfo;
   import net.wg.portal.gui.battle.fullStats.components.ScoreBlock;
   import net.wg.portal.infrastructure.base.meta.IPortalFullStatsMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalFullStatsMeta;
   import net.wg.utils.StageBreakPoint;
   import net.wg.utils.StageBreakPointList;
   import scaleform.clik.data.DataProvider;
   
   public class PortalFullStats extends PortalFullStatsMeta implements IPortalFullStatsMeta, IFullStats
   {
      
      private static const PADDING_LEFT_EXTRA_SMALL:uint = 40;
      
      private static const PADDING_LEFT_MEDIUM:uint = 32;
      
      private static const PADDING_LEFT_LARGE:uint = 72;
      
      private static const PADDING_LEFT_EXTRA_LARGE:uint = 88;
      
      private static const PADDING_TOP_EXTRA_SMALL:uint = 4;
      
      private static const PADDING_TOP_MEDIUM:uint = 0;
      
      private static const PADDING_TOP_LARGE:uint = 0;
      
      private static const PADDING_TOP_EXTRA_LARGE:uint = 0;
       
      
      public var bg:Sprite = null;
      
      public var header:Header = null;
      
      public var minimapItems:MinimapItemsInfo = null;
      
      public var score:ScoreBlock = null;
      
      private var _anchorDO:DisplayObject = null;
      
      public function PortalFullStats()
      {
         super();
      }
      
      override protected function draw() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:StageBreakPoint = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            _loc1_ = App.stage.stageHeight;
            _loc2_ = App.stage.stageWidth;
            _loc3_ = App.stageSizeMgr.currentBreakPoint;
            _loc4_ = this.getPaddingLeft(_loc3_);
            this.bg.width = _loc2_;
            this.bg.height = _loc1_;
            this.bg.x = -_loc2_ >> 1;
            this.score.x = _loc4_;
            this.minimapItems.x = _loc4_;
            if(this._anchorDO)
            {
               _loc5_ = this.getPaddingTop(_loc3_);
               this.score.y = this._anchorDO.y + _loc5_;
               this.minimapItems.y = this._anchorDO.y + this._anchorDO.height - this.minimapItems.height + _loc5_;
            }
         }
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.minimapItems.addEventListener(Event.RESIZE,this.onResizeHandler);
      }
      
      override protected function onDispose() : void
      {
         this.minimapItems.removeEventListener(Event.RESIZE,this.onResizeHandler);
         this.minimapItems.dispose();
         this.minimapItems = null;
         this.score.dispose();
         this.score = null;
         this.header.dispose();
         this.header = null;
         this.bg = null;
         this._anchorDO = null;
         super.onDispose();
      }
      
      override protected function setData(param1:PortalFullStatsVO) : void
      {
         this.header.setData(param1.header);
         this.score.setData(param1);
         this.minimapItems.dataProvider = new DataProvider(param1.minimapItems);
      }
      
      public function addVehiclesInfo(param1:IDAAPIDataClass) : void
      {
      }
      
      public function as_updateScore(param1:int, param2:int, param3:String) : void
      {
         this.score.update(param2,param1);
      }
      
      public function getStatsProgressView() : IQuestProgressView
      {
         return undefined;
      }
      
      public function getTableCtrl() : ITabbedFullStatsTableController
      {
         return undefined;
      }
      
      public function resetFrags() : void
      {
      }
      
      public function setAnchorDO(param1:DisplayObject) : void
      {
         this._anchorDO = param1;
      }
      
      public function setArenaInfo(param1:IDAAPIDataClass) : void
      {
      }
      
      public function setFrags(param1:IDAAPIDataClass) : void
      {
      }
      
      public function setPersonalStatus(param1:uint) : void
      {
      }
      
      public function setQuestStatus(param1:IDAAPIDataClass) : void
      {
      }
      
      public function setUserTags(param1:IDAAPIDataClass) : void
      {
      }
      
      public function setVehiclesData(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateInvitationsStatuses(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateLayout() : void
      {
         invalidateSize();
      }
      
      public function updatePersonalStatus(param1:uint, param2:uint) : void
      {
      }
      
      public function updatePlayerStatus(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateStageSize(param1:Number, param2:Number) : void
      {
         this.header.updateStage(param1,param2);
         this.score.updateStageSize(param1,param2);
         this.minimapItems.updateStageSize(param1,param2);
         invalidateSize();
      }
      
      public function updateTriggeredChatCommands(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateUserTags(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateVehicleStatus(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateVehiclesData(param1:IDAAPIDataClass) : void
      {
      }
      
      public function updateVehiclesStat(param1:IDAAPIDataClass) : void
      {
      }
      
      private function getPaddingLeft(param1:StageBreakPoint) : uint
      {
         switch(param1)
         {
            case StageBreakPointList.SMALL:
               return PADDING_LEFT_EXTRA_SMALL;
            case StageBreakPointList.MEDIUM:
               return PADDING_LEFT_MEDIUM;
            case StageBreakPointList.LARGE:
               return PADDING_LEFT_LARGE;
            case StageBreakPointList.EXTRA_LARGE:
               return PADDING_LEFT_EXTRA_LARGE;
            default:
               return PADDING_LEFT_EXTRA_SMALL;
         }
      }
      
      private function getPaddingTop(param1:StageBreakPoint) : uint
      {
         switch(param1)
         {
            case StageBreakPointList.SMALL:
               return PADDING_TOP_EXTRA_SMALL;
            case StageBreakPointList.MEDIUM:
               return PADDING_TOP_MEDIUM;
            case StageBreakPointList.LARGE:
               return PADDING_TOP_LARGE;
            case StageBreakPointList.EXTRA_LARGE:
               return PADDING_TOP_EXTRA_LARGE;
            default:
               return PADDING_TOP_EXTRA_SMALL;
         }
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(param1 != visible)
         {
            dispatchEvent(new Event(!!param1 ? Event.OPEN : Event.CLOSE));
         }
         super.visible = param1;
      }
      
      public function get headerHeight() : uint
      {
         return this.header.getContentHeight();
      }
      
      private function onResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
   }
}
