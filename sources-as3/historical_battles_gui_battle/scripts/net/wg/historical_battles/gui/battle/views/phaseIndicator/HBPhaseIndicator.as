package net.wg.historical_battles.gui.battle.views.phaseIndicator
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.historical_battles.data.constants.generated.HB_PHASE_INDICATOR_STATE;
   import net.wg.historical_battles.gui.battle.views.phaseIndicator.data.HBPhaseIndicatorVO;
   import net.wg.historical_battles.infrastructure.base.meta.IHBPhaseIndicatorMeta;
   import net.wg.historical_battles.infrastructure.base.meta.impl.HBPhaseIndicatorMeta;
   import net.wg.utils.StageBreakPoint;
   import net.wg.utils.StageBreakPointList;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class HBPhaseIndicator extends HBPhaseIndicatorMeta implements IHBPhaseIndicatorMeta
   {
      
      private static const PHASE_TF_Y_GAP_SMALL:int = 5;
      
      private static const PHASE_TF_Y_GAP_MEDIUM:int = 4;
      
      private static const PHASE_TF_Y_GAP_LARGE:int = 4;
      
      private static const LAYOUT_INV:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const VISIBLE_INV:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const SMALL_SIZE_POSTFIX:String = "Small";
      
      private static const MEDIUM_SIZE_POSTFIX:String = "Medium";
      
      private static const LARGE_SIZE_POSTFIX:String = "Large";
      
      private static const TF_BORDER:uint = 4;
      
      private static const PHASE_TF_MAX_TEXT_LENGTH:uint = 25;
       
      
      public var phaseTf:TextField = null;
      
      public var waveTf:TextField = null;
      
      public var background:MovieClip = null;
      
      private var _isVisible:Boolean = false;
      
      private var _data:HBPhaseIndicatorVO = null;
      
      private var _offsetX:int = 0;
      
      public function HBPhaseIndicator()
      {
         super();
         this.initialize();
      }
      
      override protected function initialize() : void
      {
         super.visible = false;
         gotoAndStop(HB_PHASE_INDICATOR_STATE.DEFENCE + this.getSizePostfixNewVal());
      }
      
      override protected function onDispose() : void
      {
         this.phaseTf = null;
         this.waveTf = null;
         this.background = null;
         this._data = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         super.draw();
         if(this._data != null)
         {
            if(isInvalid(VISIBLE_INV))
            {
               super.visible = this._isVisible;
            }
            if(isInvalid(InvalidationType.DATA))
            {
               _loc1_ = this._data.state + this.getSizePostfixNewVal();
               gotoAndStop(_loc1_);
               this.phaseTf.wordWrap = StringUtils.isEmpty(this._data.wave) && this.phaseTf.text.length > PHASE_TF_MAX_TEXT_LENGTH;
               this.phaseTf.text = this._data.phase;
               this.waveTf.text = this._data.wave;
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               this.updateSize();
            }
            if(this._isVisible && isInvalid(LAYOUT_INV))
            {
               this.updateLayout();
            }
         }
      }
      
      override protected function setData(param1:HBPhaseIndicatorVO) : void
      {
         if(this._data != param1 && param1 != null)
         {
            this._data = param1;
            invalidateData();
            invalidate(LAYOUT_INV);
            if(this._isVisible != visible)
            {
               invalidate(VISIBLE_INV);
            }
         }
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         if(this._isVisible != param1)
         {
            this._isVisible = param1;
            if(!this._data)
            {
               return;
            }
            invalidate(VISIBLE_INV);
         }
      }
      
      public function updateStage() : void
      {
         this.updateSize();
         this.updateLayout();
      }
      
      private function updateSize() : void
      {
         if(!this._data)
         {
            return;
         }
         var _loc1_:String = this._data.state + this.getSizePostfixNewVal();
         var _loc2_:Boolean = this.phaseTf.wordWrap;
         var _loc3_:String = this.phaseTf.text;
         var _loc4_:String = this.waveTf.text;
         gotoAndStop(_loc1_);
         this.phaseTf.wordWrap = _loc2_;
         this.phaseTf.text = _loc3_;
         this.waveTf.text = _loc4_;
      }
      
      private function updateLayout() : void
      {
         var _loc1_:int = 0;
         var _loc2_:Boolean = false;
         if(!this._data)
         {
            return;
         }
         if(StringUtils.isEmpty(this._data.wave))
         {
            App.utils.commons.updateTextFieldSize(this.phaseTf,false,true);
            this.phaseTf.y = height - this.phaseTf.height >> 1;
         }
         else
         {
            this.phaseTf.y = this.waveTf.y - this.phaseTf.height + this.getPhaseTfYGap() | 0;
            _loc1_ = this.phaseTf.x + this.phaseTf.textWidth + TF_BORDER - this.background.width | 0;
            _loc2_ = _loc1_ > 0;
            if(_loc2_)
            {
               this.phaseTf.x -= _loc1_;
               this.waveTf.x -= _loc1_;
               this.background.x -= _loc1_;
               this.background.width += _loc1_;
               this.phaseTf.width += _loc1_;
               this._offsetX = _loc1_;
            }
         }
      }
      
      private function getSizePostfixNewVal() : String
      {
         var _loc1_:StageBreakPoint = App.stageSizeMgr.currentBreakPoint;
         if(_loc1_ == StageBreakPointList.EXTRA_SMALL || _loc1_ == StageBreakPointList.SMALL)
         {
            return SMALL_SIZE_POSTFIX;
         }
         if(_loc1_ == StageBreakPointList.MEDIUM || _loc1_ == StageBreakPointList.LARGE)
         {
            return MEDIUM_SIZE_POSTFIX;
         }
         return LARGE_SIZE_POSTFIX;
      }
      
      private function getPhaseTfYGap() : int
      {
         var _loc1_:StageBreakPoint = App.stageSizeMgr.currentBreakPoint;
         if(_loc1_ == StageBreakPointList.EXTRA_SMALL || _loc1_ == StageBreakPointList.SMALL)
         {
            return PHASE_TF_Y_GAP_SMALL;
         }
         if(_loc1_ == StageBreakPointList.MEDIUM || _loc1_ == StageBreakPointList.LARGE)
         {
            return PHASE_TF_Y_GAP_MEDIUM;
         }
         return PHASE_TF_Y_GAP_LARGE;
      }
      
      override public function set visible(param1:Boolean) : void
      {
      }
      
      public function get offsetX() : int
      {
         return this._offsetX;
      }
   }
}
