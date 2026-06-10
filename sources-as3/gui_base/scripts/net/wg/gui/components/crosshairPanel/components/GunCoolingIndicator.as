package net.wg.gui.components.crosshairPanel.components
{
   import flash.display.MovieClip;
   import flash.filters.DropShadowFilter;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.base.SimpleContainer;
   import scaleform.clik.constants.InvalidationType;
   
   public class GunCoolingIndicator extends SimpleContainer
   {
      
      private static const TIMER_PRECISION:int = 1;
      
      private static const INVALID_IDLE_ANIMATIONS:String = "invalidIdleAnimations";
      
      private static const ACTIVATE_LABEL:String = "activate";
      
      private static const DEACTIVATE_LABEL:String = "deactivate";
      
      private static const NORMAL_LABEL:String = "normal";
      
      private static const DISABLED_LABEL:String = "disabled";
      
      private static const NORMAL_TEXT_COLOR:uint = 16773612;
      
      private static const DISABLED_TEXT_COLOR:uint = 0;
      
      private static const DISABLED_TEXT_ALPHA:Number = 0.5;
      
      private static const NORMAL_TEXT_FILTER:DropShadowFilter = new DropShadowFilter(0,0,16745238,1,8,8,1.2);
      
      private static const DISABLED_TEXT_FILTER:DropShadowFilter = new DropShadowFilter(0,0,16777215,1,4,4,1);
       
      
      public var valueMC:MovieClip = null;
      
      public var idle:MovieClip = null;
      
      public var anim1:MovieClip = null;
      
      public var anim2:MovieClip = null;
      
      private var _idleNormal:MovieClip = null;
      
      private var _valueWrapper:MovieClip = null;
      
      private var _valueTF:TextField = null;
      
      private var _secondsLeft:Number = 0;
      
      private var _isActive:Boolean = true;
      
      private var _currentAnimationLabel:String = "";
      
      public function GunCoolingIndicator()
      {
         super();
         this.idle.stop();
         this.anim1.stop();
         this.anim2.stop();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._idleNormal = this.idle.normal;
         this._idleNormal.stop();
         this._valueWrapper = this.valueMC.valueWrapper;
         this._valueTF = this._valueWrapper.valueTF;
         this._currentAnimationLabel = DEACTIVATE_LABEL;
      }
      
      override protected function onDispose() : void
      {
         this._idleNormal = null;
         this._valueWrapper = null;
         this._valueTF.filters = null;
         this._valueTF = null;
         this.valueMC = null;
         this.idle = null;
         this.anim1 = null;
         this.anim2 = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         var _loc2_:uint = 0;
         var _loc3_:DropShadowFilter = null;
         var _loc4_:Number = NaN;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.updateAnimation(this._secondsLeft > Values.ZERO ? ACTIVATE_LABEL : DEACTIVATE_LABEL);
            this._valueTF.text = this._secondsLeft.toFixed(TIMER_PRECISION);
         }
         if(isInvalid(InvalidationType.STATE))
         {
            _loc1_ = !!this._isActive ? NORMAL_LABEL : DISABLED_LABEL;
            _loc2_ = !!this._isActive ? uint(NORMAL_TEXT_COLOR) : uint(DISABLED_TEXT_COLOR);
            _loc3_ = !!this._isActive ? NORMAL_TEXT_FILTER : DISABLED_TEXT_FILTER;
            _loc4_ = !!this._isActive ? Number(Values.DEFAULT_ALPHA) : Number(DISABLED_TEXT_ALPHA);
            this.idle.gotoAndStop(_loc1_);
            this.anim1.gotoAndStop(_loc1_);
            this._valueTF.filters = [_loc3_];
            this._valueTF.textColor = _loc2_;
            this._valueWrapper.alpha = _loc4_;
            if(this._isActive)
            {
               this.anim2.gotoAndStop(NORMAL_LABEL);
            }
            else
            {
               this.anim2.gotoAndPlay(DISABLED_LABEL);
            }
         }
         if(isInvalid(INVALID_IDLE_ANIMATIONS))
         {
            if(this._currentAnimationLabel == ACTIVATE_LABEL && this._isActive)
            {
               this._idleNormal.gotoAndPlay(1);
            }
            else
            {
               this._idleNormal.stop();
            }
         }
      }
      
      private function updateAnimation(param1:String) : void
      {
         if(this._currentAnimationLabel == param1)
         {
            return;
         }
         this._currentAnimationLabel = param1;
         gotoAndStop(this._currentAnimationLabel);
         play();
         invalidate(INVALID_IDLE_ANIMATIONS);
      }
      
      public function updateTime(param1:Boolean, param2:Number) : void
      {
         if(this._secondsLeft != param2)
         {
            this._secondsLeft = param2;
            invalidateData();
         }
         if(this._isActive != param1)
         {
            this._isActive = param1;
            invalidateState();
            invalidate(INVALID_IDLE_ANIMATIONS);
         }
      }
   }
}
