package net.wg.gui.lobby.rankedBattles19.view.rewards
{
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFormatAlign;
   import net.wg.data.constants.BaseTooltips;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.generated.RANKEDBATTLES_CONSTS;
   import net.wg.data.managers.ITooltipProps;
   import net.wg.data.managers.impl.TooltipProps;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.gui.lobby.rankedBattles19.data.RankedRewardYearItemVO;
   import net.wg.gui.lobby.rankedBattles19.data.RankedRewardsYearVO;
   import net.wg.gui.lobby.rankedBattles19.events.RewardYearEvent;
   import net.wg.gui.lobby.rankedBattles19.view.rewards.year.RankedBattlesRewardsYearBg;
   import net.wg.gui.lobby.rankedBattles19.view.rewards.year.RankedBattlesYearRewardContainer;
   import net.wg.infrastructure.base.meta.IRankedBattlesRewardsYearMeta;
   import net.wg.infrastructure.base.meta.impl.RankedBattlesRewardsYearMeta;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   import net.wg.utils.StageSizeBoundaries;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class RankedBattlesRewardsYearView extends RankedBattlesRewardsYearMeta implements IRankedBattlesRewardsYearMeta
   {
      
      private static const ICON_LEFT_GAP:int = 5;
      
      private static const TITLE_TOP_POS:int = -20;
      
      private static const COMPENSATION_TOP_POS:int = 18;
      
      private static const BG_TOP_SHIFT:int = -50;
      
      private static const TOOLTIP_MAX_WIDTH:int = 430;
      
      private static const CHOOSE_REWARD_BTN_Y_SHIFT:int = 10;
      
      private static const CHOOSE_REWARD_BTN_X_SHIFTS:Object = {};
      
      private static const NEW_COUNTER_CONTAINER_ID:String = "RankedBattlesRewardsYearView";
      
      private static const COUNTER_INVALID:String = "counterInvalid";
      
      private static const COUNTER_PROPS:CounterProps = new CounterProps(10,-2,TextFormatAlign.RIGHT);
      
      {
         CHOOSE_REWARD_BTN_X_SHIFTS[RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_SMALL] = 0;
         CHOOSE_REWARD_BTN_X_SHIFTS[RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_MEDIUM] = -42;
         CHOOSE_REWARD_BTN_X_SHIFTS[RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_BIG] = -36;
         CHOOSE_REWARD_BTN_X_SHIFTS[RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_LARGE] = -25;
      }
      
      public var titleTF:TextField = null;
      
      public var titleIcon:UILoaderAlt = null;
      
      public var titleArea:Sprite = null;
      
      public var compensationTF:TextField = null;
      
      public var rewardsContainer:RankedBattlesYearRewardContainer = null;
      
      public var chooseRewardBtn:UniversalBtn = null;
      
      public var bg:RankedBattlesRewardsYearBg = null;
      
      public var black:Sprite = null;
      
      private var _data:RankedRewardsYearVO = null;
      
      private var _counterValue:String = null;
      
      private var _counterManager:ICounterManager;
      
      private var _rewardPointsPos:int = 0;
      
      private var _tooltipMgr:ITooltipMgr = null;
      
      private var _tooltipProps:ITooltipProps = null;
      
      private var _hasCompensation:Boolean = false;
      
      public function RankedBattlesRewardsYearView()
      {
         this._counterManager = App.utils.counterManager;
         super();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this._tooltipMgr = App.toolTipMgr;
         this.titleIcon.autoSize = false;
         this.titleIcon.maintainAspectRatio = false;
         this.titleIcon.addEventListener(UILoaderEvent.COMPLETE,this.onTitleIconCompleteHandler);
         this.rewardsContainer.addEventListener(RewardYearEvent.MAIN_AWARD_SHOW,this.onRewardsContainerMainAwardShowHandler);
         this._rewardPointsPos = this.rewardsContainer.getPointsPos();
         this.titleArea.addEventListener(MouseEvent.MOUSE_OVER,this.onTitleAreaMouseOverHandler);
         this.titleArea.addEventListener(MouseEvent.MOUSE_OUT,this.onTitleAreaMouseOutHandler);
         this._tooltipProps = new TooltipProps(BaseTooltips.TYPE_INFO,0,0);
         this._tooltipProps.maxWidth = TOOLTIP_MAX_WIDTH;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.titleTF.y = TITLE_TOP_POS;
         this.compensationTF.y = COMPENSATION_TOP_POS;
         App.utils.universalBtnStyles.setStyle(this.chooseRewardBtn,UniversalBtnStylesConst.STYLE_HEAVY_GREEN);
         this.chooseRewardBtn.addEventListener(ButtonEvent.CLICK,this.onChooseRewardBtnClickHandler);
      }
      
      override protected function draw() : void
      {
         var _loc3_:uint = 0;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:int = 0;
         var _loc9_:int = 0;
         super.draw();
         var _loc1_:Boolean = isInvalid(InvalidationType.SIZE) || isInvalid(INV_VIEW_PADDING);
         var _loc2_:Boolean = isInvalid(InvalidationType.DATA);
         _loc3_ = _width - viewPadding.left >> 1;
         var _loc4_:uint = _height - viewPadding.top >> 1;
         if(this._data)
         {
            if(_loc2_)
            {
               this.rewardsContainer.setData(this._data.rewards);
               this.titleTF.text = this._data.title;
               App.utils.commons.updateTextFieldSize(this.titleTF);
               this.titleIcon.source = this._data.titleIcon;
               _loc1_ = true;
               this._hasCompensation = StringUtils.isNotEmpty(this._data.compensation);
               this.compensationTF.visible = this._hasCompensation;
               if(this._hasCompensation)
               {
                  this.compensationTF.htmlText = this._data.compensation;
                  App.utils.commons.updateTextFieldSize(this.compensationTF,true,false);
               }
               this.chooseRewardBtn.visible = this.rewardsContainer.isChooseRewardVisible;
               if(this.rewardsContainer.isChooseRewardVisible)
               {
                  this.chooseRewardBtn.label = this.rewardsContainer.selectedBtn.statusText;
               }
               if(StringUtils.isNotEmpty(this._counterValue))
               {
                  this._counterManager.disposeCountersForContainer(NEW_COUNTER_CONTAINER_ID);
                  if(this.rewardsContainer.isChooseRewardVisible && isInvalid(COUNTER_INVALID))
                  {
                     this._counterManager.setCounter(this.chooseRewardBtn,this._counterValue,NEW_COUNTER_CONTAINER_ID,COUNTER_PROPS);
                  }
               }
            }
            if(_loc1_)
            {
               this.titleTF.x = _loc3_ - (this.titleTF.width >> 1);
               if(this._hasCompensation)
               {
                  this.compensationTF.x = _loc3_ - (this.compensationTF.width >> 1);
               }
               this.titleIcon.x = this.titleTF.x + this.titleTF.width + ICON_LEFT_GAP;
               this.titleIcon.y = this.titleTF.y + (this.titleTF.height - this.titleIcon.height >> 1);
               this.titleArea.x = this.titleTF.x;
               this.titleArea.width = this.titleIcon.x + this.titleIcon.width - this.titleTF.x;
            }
         }
         if(_loc1_)
         {
            this.black.x = -viewPadding.left;
            this.black.y = -viewPadding.top;
            this.black.width = _width + viewPadding.left;
            this.black.height = _height + viewPadding.top;
            _loc5_ = App.appWidth / StageSizeBoundaries.WIDTH_1920;
            _loc6_ = App.appHeight / StageSizeBoundaries.HEIGHT_1080;
            _loc7_ = Math.min(_loc5_,_loc6_);
            _loc8_ = Math.max(0,this._rewardPointsPos * _loc7_ - (_height + viewPadding.top >> 1));
            this.bg.scaleX = this.bg.scaleY = _loc7_;
            _loc9_ = this.bg.width;
            _loc9_ += _loc9_ % 2;
            this.bg.width = _loc9_;
            _loc9_ = this.bg.height;
            _loc9_ += _loc9_ % 2;
            this.bg.height = _loc9_;
            this.bg.x = _loc3_;
            this.bg.y = _loc4_ + BG_TOP_SHIFT - _loc8_;
            this.rewardsContainer.x = _loc3_;
            this.rewardsContainer.y = this.bg.y;
            this.rewardsContainer.scale = _loc7_;
            if(this.rewardsContainer.isChooseRewardVisible)
            {
               this.chooseRewardBtn.x = this.rewardsContainer.x + this.rewardsContainer.selectedBtn.x * _loc7_ - (this.chooseRewardBtn.width >> 1) + CHOOSE_REWARD_BTN_X_SHIFTS[this.rewardsContainer.selectedBtn.id] * _loc7_ | 0;
               this.chooseRewardBtn.y = this.rewardsContainer.y + this.rewardsContainer.selectedBtn.y * _loc7_ + CHOOSE_REWARD_BTN_Y_SHIFT | 0;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.titleArea.removeEventListener(MouseEvent.MOUSE_OVER,this.onTitleAreaMouseOverHandler);
         this.titleArea.removeEventListener(MouseEvent.MOUSE_OUT,this.onTitleAreaMouseOutHandler);
         this.titleArea = null;
         this.titleTF = null;
         this.titleIcon.removeEventListener(UILoaderEvent.COMPLETE,this.onTitleIconCompleteHandler);
         this.titleIcon.dispose();
         this.titleIcon = null;
         this.rewardsContainer.removeEventListener(RewardYearEvent.MAIN_AWARD_SHOW,this.onRewardsContainerMainAwardShowHandler);
         this.rewardsContainer.dispose();
         this.rewardsContainer = null;
         this.bg.dispose();
         this.bg = null;
         this.black = null;
         this.compensationTF = null;
         this.chooseRewardBtn.removeEventListener(ButtonEvent.CLICK,this.onChooseRewardBtnClickHandler);
         this.chooseRewardBtn.dispose();
         this.chooseRewardBtn = null;
         this._counterManager.disposeCountersForContainer(NEW_COUNTER_CONTAINER_ID);
         this._counterManager = null;
         this._data = null;
         this._tooltipMgr.hide();
         this._tooltipMgr = null;
         this._tooltipProps = null;
         super.onDispose();
      }
      
      override protected function setData(param1:RankedRewardsYearVO) : void
      {
         var _loc3_:RankedRewardYearItemVO = null;
         this._data = param1;
         var _loc2_:Boolean = false;
         var _loc4_:int = param1.rewards.length;
         var _loc5_:int = 0;
         while(_loc5_ < _loc4_)
         {
            _loc3_ = param1.rewards[_loc5_];
            _loc2_ = _loc2_ || RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_MAIN_AVAILABLE_FOR.indexOf(_loc3_.id) >= 0 && (_loc3_.status == RANKEDBATTLES_CONSTS.YEAR_REWARD_STATUS_CURRENT || _loc3_.status == RANKEDBATTLES_CONSTS.YEAR_REWARD_STATUS_CURRENT_FINAL);
            _loc5_++;
         }
         this.bg.isPermanentShow = _loc2_;
         invalidateData();
      }
      
      public function as_setChooseRewardBtnCounter(param1:String) : void
      {
         if(this._counterValue != param1)
         {
            this._counterValue = param1;
            invalidate(COUNTER_INVALID);
         }
      }
      
      private function onChooseRewardBtnClickHandler(param1:ButtonEvent) : void
      {
         onChooseRewardBtnClickS();
      }
      
      private function onTitleAreaMouseOverHandler(param1:MouseEvent) : void
      {
         if(this._data)
         {
            this._tooltipMgr.showComplex(this._data.titleTooltip,this._tooltipProps);
         }
      }
      
      private function onTitleAreaMouseOutHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.hide();
      }
      
      private function onRewardsContainerMainAwardShowHandler(param1:RewardYearEvent) : void
      {
         if(param1.isShow)
         {
            this.bg.show();
         }
         else
         {
            this.bg.hide();
         }
      }
      
      private function onTitleIconCompleteHandler(param1:UILoaderEvent) : void
      {
         invalidateSize();
      }
   }
}
