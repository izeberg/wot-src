package net.wg.gui.battle.random.views.teamBasesPanel
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import net.wg.utils.IScheduler;
   import scaleform.clik.motion.Tween;
   
   public class TeamCaptureBar extends SimpleDisposable
   {
      
      private static const EXIT_STATE:String = "exit";
      
      private static const DISPLAY_STATE:String = "display";
      
      private static const POINTS_2_BAR_RATIO:Number = 0.01;
      
      private static const ANIMATE_STEP_TIME:Number = 40;
      
      private static const ALPHA_FADE_SPEED:Number = 500;
      
      private static const EXIT_TWEEN_Y:int = -10;
      
      private static const EXIT_TWEEN_DELAY:Number = 4500;
      
      private static const SUPPLY_TWEEN_POSITION_DURATION:Number = 200;
      
      private static const TWEEN_EASE_IN_OUT:Array = [0,0.002,0.006,0.013,0.03,0.049,0.087,0.125,0.167,0.247,0.32,0.44,0.544,0.628,0.823,0.83,0.868,0.907,0.935,0.966,0.981,0.993,0.998,0.999,1];
      
      protected static const TWEEN_EASE_NONE:Array = [0.032,0.068,0.116,0.152,0.2,0.232,0.268,0.316,0.352,0.4,0.432,0.468,0.516,0.552,0.6,0.664,0.668,0.716,0.752,0.8,0.832,0.868,0.916,0.952,1];
      
      private static const COLOR_ALIAS_PREFIX:String = "capture_bar_";
      
      private static const DASH:String = "-";
       
      
      public var textField:TextField = null;
      
      public var tfVehiclesCount:TextField = null;
      
      public var tfTimeLeft:TextField = null;
      
      public var bg:TeamCaptureBarBg = null;
      
      public var progressBar:TeamCaptureProgress = null;
      
      public var progressBarReset:TeamCaptureProgressReset = null;
      
      public var tanksIndicator:MovieClip = null;
      
      public var supplyIndicator:MovieClip = null;
      
      private var _getColorType:String = "";
      
      private var _points:Number = -1;
      
      private var _prevDeltaPoints:Number = 0;
      
      private var _colorTypeFromVo:String = "";
      
      private var _startAnimateScale:Number = 0;
      
      private var _currentEaseArray:Array = null;
      
      private var _currentEaseLen:Number = 0;
      
      private var _currentEaseStep:Number = 0;
      
      private var _easeParam:Number = 0;
      
      private var _animateRate:Number = 10;
      
      private var _sortWeight:Number = -1;
      
      private var _id:Number = -1;
      
      private var _scheduler:IScheduler;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      private var _exitTween:Tween = null;
      
      private var _supplyIndicatorTween:Tween = null;
      
      private var _supplyIndicatorDefaultX:Number = 0;
      
      public function TeamCaptureBar()
      {
         this._scheduler = App.utils.scheduler;
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
         this.tfVehiclesCount = this.tanksIndicator.tfVehiclesCount;
         this._supplyIndicatorDefaultX = this.supplyIndicator.x;
      }
      
      override protected function onDispose() : void
      {
         stop();
         this._scheduler.cancelTask(this.animationStepHandler);
         this.textField = null;
         this.progressBar.dispose();
         this.progressBar = null;
         this.progressBarReset.dispose();
         this.progressBarReset = null;
         if(this._exitTween)
         {
            this._exitTween.dispose();
            this._exitTween = null;
         }
         this.clearSupplyIndicatorTween();
         this.bg.dispose();
         this.bg = null;
         this._getColorType = null;
         this._colorTypeFromVo = null;
         this.tfVehiclesCount = null;
         this.tfTimeLeft = null;
         this.tanksIndicator = null;
         this.supplyIndicator = null;
         this._currentEaseArray = null;
         this._scheduler = null;
         this._colorSchemeMgr = null;
         super.onDispose();
      }
      
      public function setCaptured(param1:String) : void
      {
         this.updateTitle(param1);
         this._exitTween = new Tween(ALPHA_FADE_SPEED,this,{
            "y":EXIT_TWEEN_Y,
            "alpha":0
         },{
            "delay":EXIT_TWEEN_DELAY,
            "onComplete":this.onExitCompleteCallback
         });
         gotoAndPlay(EXIT_STATE);
         this.tfTimeLeft.text = Values.EMPTY_STR;
      }
      
      public function setData(param1:Number, param2:Number, param3:String, param4:String, param5:Number, param6:String, param7:int, param8:Boolean) : void
      {
         this.sortWeight = param2;
         var _loc9_:Boolean = true;
         if(param1 != this._id)
         {
            this._id = param1;
            _loc9_ = false;
         }
         this._colorTypeFromVo = param3;
         this.updateColors();
         this.updateTitle(param4);
         gotoAndPlay(DISPLAY_STATE);
         this.updateCaptureData(param5,false,false,1,param6,param7,param4,param3,param8,_loc9_);
      }
      
      public function stopCapture(param1:Number) : void
      {
         this.updateCaptureData(param1,false,true,1,Values.EMPTY_STR,Values.ZERO,Values.EMPTY_STR,this.colorType,false);
      }
      
      public function updateCaptureData(param1:Number, param2:Boolean, param3:Boolean, param4:Number, param5:String, param6:int, param7:String, param8:String, param9:Boolean, param10:Boolean = true) : void
      {
         this.progressBar.animate(param3);
         var _loc11_:Number = this._points > 0 ? Number(param1 - this._points) : Number(0);
         if(param10)
         {
            if(_loc11_ < 0)
            {
               this.showReset(param1,_loc11_ * -1);
               param2 = false;
            }
         }
         this._points = param1;
         this.updateTitle(param7);
         if(this._colorTypeFromVo != param8)
         {
            this._colorTypeFromVo = param8;
            this.updateColors();
         }
         this.animateProgress(param1,_loc11_,param2,param4);
         this.updateIndicators(param9,param6);
         this.tfTimeLeft.text = param5;
      }
      
      public function updateColors() : void
      {
         var _loc1_:String = this._colorSchemeMgr.getAliasColor(COLOR_ALIAS_PREFIX + this._colorTypeFromVo);
         if(_loc1_ == null)
         {
            _loc1_ = this._colorTypeFromVo;
         }
         this.colorType = _loc1_;
      }
      
      private function updateIndicators(param1:Boolean, param2:int) : void
      {
         this.tfVehiclesCount.text = param2 > Values.DEFAULT_INT ? param2.toString() : DASH;
         var _loc3_:Boolean = param1 && param2 == Values.ZERO;
         this.tanksIndicator.visible = !_loc3_;
         this.supplyIndicator.visible = param1;
         var _loc4_:Number = !!_loc3_ ? Number(this.tanksIndicator.x) : Number(this._supplyIndicatorDefaultX);
         if(this.supplyIndicator.x != _loc4_)
         {
            this.clearSupplyIndicatorTween();
            this._supplyIndicatorTween = new Tween(SUPPLY_TWEEN_POSITION_DURATION,this.supplyIndicator,{"x":_loc4_},{"ease":Cubic.easeOut});
         }
      }
      
      private function clearSupplyIndicatorTween() : void
      {
         if(this._supplyIndicatorTween)
         {
            this._supplyIndicatorTween.dispose();
            this._supplyIndicatorTween = null;
         }
      }
      
      protected function updateTitle(param1:String) : void
      {
         this.textField.text = param1;
      }
      
      private function onExitCompleteCallback() : void
      {
         this._exitTween.dispose();
         this._exitTween = null;
      }
      
      private function showReset(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = this.progressBar.x + param1 * POINTS_2_BAR_RATIO * this.progressBar.getBarWidth();
         var _loc4_:Number = param2 * POINTS_2_BAR_RATIO;
         if(this.progressBarReset.isAnimating && this.progressBarReset.scaleX + _loc4_ <= 1)
         {
            _loc4_ += this.progressBarReset.scaleX;
         }
         this.progressBarReset.show(_loc3_,_loc4_);
      }
      
      protected function getEaseArray(param1:Number) : Array
      {
         return this._prevDeltaPoints != param1 ? TWEEN_EASE_IN_OUT : TWEEN_EASE_NONE;
      }
      
      private function animateProgress(param1:Number, param2:Number, param3:Boolean, param4:Number) : void
      {
         this._scheduler.cancelTask(this.animationStepHandler);
         if(!param3 || param4 == 0)
         {
            this.progressBar.scaleX = param1 * POINTS_2_BAR_RATIO;
         }
         else
         {
            this._currentEaseArray = this.getEaseArray(param2);
            this._startAnimateScale = this.progressBar.scaleX;
            this._easeParam = param1 * POINTS_2_BAR_RATIO - this._startAnimateScale;
            this._currentEaseLen = this._currentEaseArray.length;
            this._currentEaseStep = 0;
            this._animateRate = param4;
            this._scheduler.scheduleRepeatableTask(this.animationStepHandler,ANIMATE_STEP_TIME,int.MAX_VALUE);
         }
         this._prevDeltaPoints = param2;
      }
      
      private function animationStepHandler() : void
      {
         var _loc1_:int = this._currentEaseStep | 0;
         this.progressBar.scaleX = this._startAnimateScale + this._currentEaseArray[_loc1_] * this._easeParam;
         this._currentEaseStep += this._animateRate;
         if(_loc1_ >= this._currentEaseLen)
         {
            this._scheduler.cancelTask(this.animationStepHandler);
         }
      }
      
      public function get sortWeight() : Number
      {
         return this._sortWeight;
      }
      
      public function set sortWeight(param1:Number) : void
      {
         this._sortWeight = param1;
      }
      
      public function get id() : Number
      {
         return this._id;
      }
      
      public function set id(param1:Number) : void
      {
         this._id = param1;
      }
      
      public function get colorType() : String
      {
         return this._getColorType;
      }
      
      public function set colorType(param1:String) : void
      {
         this._getColorType = param1;
         this.bg.colorType = param1;
         this.progressBar.colorType = param1;
         this.progressBarReset.colorType = param1;
      }
   }
}
