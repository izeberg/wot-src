package net.wg.gui.battle.cosmic.battleloading
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.battleloading.vo.VisualTipInfoVO;
   import net.wg.infrastructure.base.meta.ICosmicBattleLoadingMeta;
   import net.wg.infrastructure.base.meta.impl.CosmicBattleLoadingMeta;
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   import net.wg.infrastructure.managers.IStageSizeManager;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.controls.StatusIndicator;
   
   public class CosmicBattleLoading extends CosmicBattleLoadingMeta implements ICosmicBattleLoadingMeta
   {
      
      private static const TIPS_COUNT:uint = 3;
      
      private static const TITLE_SIZE:Object = {};
      
      private static const TIPS_SIZE:Object = {};
      
      private static const TIPS_LEFT:Object = {};
      
      private static const TITLE_BOTTOM:Object = {};
      
      private static const TIPS_BOTTOM:Object = {};
      
      private static const LOADING_BAR_BOTTOM:Object = {};
      
      public static const PROGRESS:int = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      {
         TITLE_SIZE[StageSizeBoundaries.WIDTH_1024] = 18;
         TITLE_SIZE[StageSizeBoundaries.WIDTH_1366] = 18;
         TITLE_SIZE[StageSizeBoundaries.WIDTH_1600] = 24;
         TITLE_SIZE[StageSizeBoundaries.WIDTH_1920] = 28;
         TITLE_SIZE[StageSizeBoundaries.WIDTH_2560] = 36;
         TIPS_SIZE[StageSizeBoundaries.WIDTH_1024] = 16;
         TIPS_SIZE[StageSizeBoundaries.WIDTH_1366] = 16;
         TIPS_SIZE[StageSizeBoundaries.WIDTH_1600] = 20;
         TIPS_SIZE[StageSizeBoundaries.WIDTH_1920] = 24;
         TIPS_SIZE[StageSizeBoundaries.WIDTH_2560] = 32;
         TIPS_LEFT[StageSizeBoundaries.WIDTH_1024] = 120;
         TIPS_LEFT[StageSizeBoundaries.WIDTH_1366] = 120;
         TIPS_LEFT[StageSizeBoundaries.WIDTH_1600] = 140;
         TIPS_LEFT[StageSizeBoundaries.WIDTH_1920] = 160;
         TIPS_LEFT[StageSizeBoundaries.WIDTH_2560] = 240;
         TITLE_BOTTOM[StageSizeBoundaries.WIDTH_1024] = 15;
         TITLE_BOTTOM[StageSizeBoundaries.WIDTH_1366] = 15;
         TITLE_BOTTOM[StageSizeBoundaries.WIDTH_1600] = 18;
         TITLE_BOTTOM[StageSizeBoundaries.WIDTH_1920] = 24;
         TITLE_BOTTOM[StageSizeBoundaries.WIDTH_2560] = 27;
         TIPS_BOTTOM[StageSizeBoundaries.WIDTH_1024] = [7,7,24];
         TIPS_BOTTOM[StageSizeBoundaries.WIDTH_1366] = [7,7,24];
         TIPS_BOTTOM[StageSizeBoundaries.WIDTH_1600] = [11,11,52];
         TIPS_BOTTOM[StageSizeBoundaries.WIDTH_1920] = [16,16,58];
         TIPS_BOTTOM[StageSizeBoundaries.WIDTH_2560] = [18,19,79];
         LOADING_BAR_BOTTOM[StageSizeBoundaries.WIDTH_1024] = 46;
         LOADING_BAR_BOTTOM[StageSizeBoundaries.WIDTH_1366] = 46;
         LOADING_BAR_BOTTOM[StageSizeBoundaries.WIDTH_1600] = 46;
         LOADING_BAR_BOTTOM[StageSizeBoundaries.WIDTH_1920] = 60;
         LOADING_BAR_BOTTOM[StageSizeBoundaries.WIDTH_2560] = 60;
      }
      
      public var loadingBar:StatusIndicator = null;
      
      public var title:TextField = null;
      
      public var tip1:TextField = null;
      
      public var tip2:TextField = null;
      
      public var tip3:TextField = null;
      
      private var _height:int = 0;
      
      private var _width:int = 0;
      
      private var _title:String = null;
      
      private var _tips:Vector.<TextField> = null;
      
      private var _tipsData:Vector.<String> = null;
      
      private var _progress:Number = 0;
      
      private var _stageSizeMgr:IStageSizeManager;
      
      public function CosmicBattleLoading()
      {
         this._stageSizeMgr = App.stageSizeMgr;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._tips = new <TextField>[this.tip1,this.tip2,this.tip3];
         this.title.wordWrap = this.tip1.wordWrap = this.tip2.wordWrap = this.tip3.wordWrap = true;
         this.title.autoSize = this.tip1.autoSize = this.tip2.autoSize = this.tip3.autoSize = TextFieldAutoSize.LEFT;
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         var _loc3_:Number = NaN;
         var _loc4_:TextFormat = null;
         var _loc5_:TextField = null;
         var _loc6_:Number = NaN;
         var _loc7_:int = 0;
         super.draw();
         if(this._progress > 0 && isInvalid(PROGRESS))
         {
            this.loadingBar.position = this._progress;
         }
         if(this._width > 0)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.title.text = this._title;
               _loc1_ = 0;
               while(_loc1_ < TIPS_COUNT)
               {
                  this._tips[_loc1_].text = this._tipsData[_loc1_];
                  _loc1_++;
               }
               invalidateSize();
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               _loc2_ = this._stageSizeMgr.currentBreakPoint.width;
               _loc3_ = this._height - LOADING_BAR_BOTTOM[_loc2_];
               this.loadingBar.y = _loc3_;
               this.loadingBar.x = this._width - this.loadingBar.width >> 1;
               _loc6_ = _loc3_;
               _loc7_ = TIPS_COUNT - 1;
               while(_loc7_ >= 0)
               {
                  _loc5_ = this._tips[_loc7_];
                  _loc4_ = _loc5_.getTextFormat();
                  _loc4_.size = TIPS_SIZE[_loc2_];
                  _loc5_.setTextFormat(_loc4_);
                  _loc5_.width = this._width - TIPS_LEFT[_loc2_] * 2 | 0;
                  _loc5_.x = TIPS_LEFT[_loc2_];
                  _loc5_.y = _loc6_ - _loc5_.height - TIPS_BOTTOM[_loc2_][_loc7_];
                  _loc6_ = _loc5_.y;
                  _loc7_--;
               }
               _loc4_ = this.title.getTextFormat();
               _loc4_.size = TITLE_SIZE[_loc2_];
               this.title.setTextFormat(_loc4_);
               this.title.width = this._width - TIPS_LEFT[_loc2_] * 2 | 0;
               this.title.x = TIPS_LEFT[_loc2_];
               this.title.y = _loc6_ - this.title.height - TITLE_BOTTOM[_loc2_];
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.loadingBar.dispose();
         this.loadingBar = null;
         this.title = null;
         this.tip1 = null;
         this.tip2 = null;
         this.tip3 = null;
         this._tips.length = 0;
         this._tips = null;
         this._title = null;
         this._tipsData = null;
         this._stageSizeMgr = null;
         super.onDispose();
      }
      
      override public function as_setProgress(param1:Number) : void
      {
         if(param1 != this._progress)
         {
            this._progress = param1;
            invalidate(PROGRESS);
         }
      }
      
      override public function getContentY() : int
      {
         return this.loadingBar.y;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         if(this._width != param1 || this._height != param2)
         {
            this._width = param1;
            this._height = param2;
            invalidateSize();
         }
      }
      
      override public function as_setTipTitle(param1:String) : void
      {
         if(this._title != param1)
         {
            this._title = param1;
            invalidateData();
         }
      }
      
      override protected function setTips(param1:Vector.<String>) : void
      {
         if(this._tipsData != param1 && param1 != null)
         {
            this._tipsData = param1;
            invalidateData();
         }
      }
      
      override public function addVehiclesInfo(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function as_setMapIcon(param1:String) : void
      {
      }
      
      override public function as_setTip(param1:String) : void
      {
      }
      
      override public function setArenaInfo(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function setFrags(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function setPersonalStatus(param1:uint) : void
      {
      }
      
      override public function setQuestStatus(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function setUserTags(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function setVehiclesData(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updateInvitationsStatuses(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updatePersonalStatus(param1:uint, param2:uint) : void
      {
      }
      
      override public function updatePlayerStatus(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updateUserTags(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updateVehicleStatus(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updateVehiclesData(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updateVehiclesStat(param1:IDAAPIDataClass) : void
      {
      }
      
      override public function updateTriggeredChatCommands(param1:IDAAPIDataClass) : void
      {
      }
      
      override protected function setVisualTipInfo(param1:VisualTipInfoVO) : void
      {
      }
      
      override public function hasAmmunitionPanel(param1:Boolean) : void
      {
      }
   }
}
