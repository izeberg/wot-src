package net.wg.gui.components.crosshairPanel.components.overheatBar
{
   import fl.motion.easing.Quadratic;
   import fl.motion.easing.Quartic;
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.utils.clearInterval;
   import flash.utils.getTimer;
   import flash.utils.setInterval;
   import net.wg.data.constants.Time;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class OverheatBar extends MovieClip implements IDisposable
   {
      
      public static const X_OFFSET:int = -106;
      
      public static const Y_OFFSET:int = -104;
      
      private static const FULL_PROGRESS:Number = 1;
      
      private static const ANIM_START_FRAME:uint = 1;
      
      private static const STATE_HIDDEN:int = Values.DEFAULT_INT;
      
      private static const MiN_STATE_VALUE:Number = 0;
      
      private static const MAX_STATE_VALUE:Number = 1;
      
      private static const MARKER_FADE_TWEEN_DURATION:uint = 300;
      
      private static const DISTANCE_FADE_TWEEN_DURATION:uint = 200;
      
      private static const PROGRESS_TWEEN_DURATION:uint = 500;
      
      private static const OVERHEAT_TIMER_UPDATE_TICK:uint = 100;
      
      private static const PROGRESS_START_COLOR:uint = 16624129;
      
      private static const PROGRESS_END_COLOR:uint = 11742465;
      
      private static const DEFAULT_SEGMENT_COLOR:uint = 16777215;
      
      private static const DEFAULT_SEGMENT_ALPHA:Number = 0.2;
      
      private static const ACTIVE_SEGMENT_COLOR:uint = 16769936;
      
      private static const ACTIVE_SEGMENT_ALPHA:Number = 1;
      
      private static const ACTIVE_SEGMENT_OUTER_ALPHA:Number = 0.6;
      
      private static const SEGMENT_OUTER_RADIUS:uint = 97;
      
      private static const SEGMENT_THICKNESS:uint = 4;
      
      private static const ACTIVE_SEGMENT_OUTER_RADIUS:uint = 107;
      
      private static const ACTIVE_SEGMENT_THICKNESS:uint = 2;
      
      private static const ACTIVE_SEGMENT_EDGE_HEIGHT:uint = 6;
      
      private static const CIRCLE_PROGRESS_MIN:Number = 0.5;
      
      private static const CIRCLE_PROGRESS_MAX:Number = 0.75;
      
      private static const STATES_DELIMITER:Number = 0.005;
       
      
      public var bar:MovieClip = null;
      
      private var _progress:MovieClip = null;
      
      private var _overheatProgress:MovieClip = null;
      
      private var _staticMarkers:Vector.<Sprite> = null;
      
      private var _stateMarkers:Vector.<Sprite> = null;
      
      private var _outerStateMarkers:Vector.<Sprite> = null;
      
      private var _markersContainer:MovieClip = null;
      
      private var _outerMarkersContainer:MovieClip = null;
      
      private var _anim:MovieClip = null;
      
      private var _rangefinder:MovieClip = null;
      
      private var _timerContainer:MovieClip = null;
      
      private var _timerTF:TextField = null;
      
      private var _markerTweens:Vector.<Tween> = null;
      
      private var _progressTweenProps:OverheatBarTweenProps = null;
      
      private var _progressTween:Tween = null;
      
      private var _distanceTween:Tween = null;
      
      private var _curProgress:Number = 0;
      
      private var _overheatStates:Vector.<Number> = null;
      
      private var _disposed:Boolean = false;
      
      private var _overheatTotalTime:int = -1;
      
      private var _overheatStartTime:int = -1;
      
      private var _overheatTimeLeft:int = -1;
      
      private var _overheatIntervalId:uint = 0;
      
      private var _isOverheatIntervalPlaying:Boolean = false;
      
      private var _progressFrames:int = 0;
      
      private var _prevState:int = -1;
      
      private var _state:int = -1;
      
      private var _curStateMin:Number = 0;
      
      private var _curStateMax:Number = 0;
      
      private var _isForcedStateChange:Boolean = false;
      
      private var _isDistanceVisible:Boolean = false;
      
      public function OverheatBar()
      {
         super();
         this._staticMarkers = new Vector.<Sprite>(0);
         this._stateMarkers = new Vector.<Sprite>(0);
         this._outerStateMarkers = new Vector.<Sprite>(0);
         this._overheatStates = new Vector.<Number>(0);
         this._markerTweens = new Vector.<Tween>(0);
         this._progressTweenProps = new OverheatBarTweenProps();
         this._progressTween = new Tween(PROGRESS_TWEEN_DURATION,this._progressTweenProps,{"position":OverheatBarTweenProps.TWEEN_END},{
            "paused":true,
            "onChange":this.onProgressTweenChange,
            "ease":Quadratic.easeOut
         });
         this._progress = this.bar.progress;
         this._overheatProgress = this.bar.overheatProgress;
         this._markersContainer = this.bar.markers;
         this._outerMarkersContainer = this.bar.outerMarkers;
         this._anim = this.bar.anim;
         this._rangefinder = this.bar.rangefinder;
         this._timerContainer = this.bar.timer;
         this._timerTF = this._timerContainer.timerText.timerTF;
         this._timerContainer.visible = this._overheatProgress.visible = false;
         this._rangefinder.alpha = 0;
         this._progressFrames = this._progress.totalFrames;
         this._anim.gotoAndStop(this._anim.totalFrames - 1);
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this._progressTweenProps = null;
         this._progressTween.dispose();
         this._progressTween = null;
         this.clearDistanceTween();
         this.stopOverheatInterval();
         this.clearMarkerTweens();
         this._markerTweens = null;
         this.clearAllMarkers();
         this.bar = null;
         this._progress = null;
         this._overheatProgress = null;
         this._markersContainer = null;
         this._outerMarkersContainer = null;
         this._stateMarkers.length = 0;
         this._stateMarkers = null;
         this._outerStateMarkers.length = 0;
         this._outerStateMarkers = null;
         this._staticMarkers.length = 0;
         this._staticMarkers = null;
         this._overheatStates.length = 0;
         this._overheatStates = null;
         this._anim = null;
         this._rangefinder = null;
         this._timerTF = null;
         this._timerContainer = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function onChangeCrosshair(param1:Number, param2:Number) : void
      {
         this._curStateMin = MiN_STATE_VALUE;
         this._curStateMax = MiN_STATE_VALUE;
         this._isForcedStateChange = true;
         this.updateInfo(param1,param2,true);
      }
      
      public function setOverheatMarkers(param1:Vector.<Number>) : void
      {
         this._overheatStates.splice(0,this._overheatStates.length);
         this._overheatStates = param1.slice(0,param1.length);
         this._overheatStates.push(MAX_STATE_VALUE);
         this.clearAllMarkers();
         this.addMarkers();
      }
      
      public function updateInfo(param1:Number, param2:Number, param3:Boolean) : void
      {
         if(this._curProgress == param1 && this._overheatTimeLeft == param2)
         {
            return;
         }
         this._overheatTimeLeft = param2 * Time.MILLISECOND_IN_SECOND;
         this._curProgress = param1;
         if(this._curStateMin >= param1 || param1 > this._curStateMax || this.isOverheated)
         {
            this.updateState();
         }
         if(this._curProgress == FULL_PROGRESS)
         {
            this._anim.gotoAndPlay(ANIM_START_FRAME);
         }
         this.updateDistanceVisibility();
         this._progress.visible = !this.isOverheated;
         this._timerContainer.visible = this._overheatProgress.visible = this.isOverheated;
         var _loc4_:int = int(param1 * this._progressFrames) + 1;
         if(this.isOverheated)
         {
            this._progress.gotoAndStop(1);
            this._overheatProgress.gotoAndStop(_loc4_);
            if(param3)
            {
               this._timerTF.text = param2.toFixed(1);
            }
            else
            {
               this.updateTimerAnimation();
            }
         }
         else
         {
            this.stopOverheatInterval();
            this._overheatStartTime = this._overheatTotalTime = Values.DEFAULT_INT;
            this._overheatProgress.gotoAndStop(_loc4_);
            if(param3)
            {
               this._progress.gotoAndStop(_loc4_);
            }
            else
            {
               this.updateProgressAnimation(this._progress,_loc4_);
            }
         }
      }
      
      public function updateTimerAnimation() : void
      {
         if(this._overheatTotalTime == Values.DEFAULT_INT)
         {
            this._overheatTotalTime = this._overheatTimeLeft;
         }
         this._overheatStartTime = getTimer() - (this._overheatTotalTime - this._overheatTimeLeft);
         if(!this._isOverheatIntervalPlaying)
         {
            this._overheatIntervalId = setInterval(this.overheatTicking,OVERHEAT_TIMER_UPDATE_TICK);
            this._isOverheatIntervalPlaying = true;
         }
      }
      
      private function overheatTicking() : void
      {
         var _loc1_:int = getTimer() - this._overheatStartTime;
         var _loc2_:Number = (this._overheatTotalTime - _loc1_) / Time.MILLISECOND_IN_SECOND;
         if(_loc2_ < 0)
         {
            this.stopOverheatInterval();
         }
         else
         {
            this._timerTF.text = _loc2_.toFixed(1);
         }
      }
      
      private function stopOverheatInterval() : void
      {
         if(this._isOverheatIntervalPlaying)
         {
            clearInterval(this._overheatIntervalId);
            this._isOverheatIntervalPlaying = false;
         }
      }
      
      public function updateProgressAnimation(param1:MovieClip, param2:int) : void
      {
         this._progressTweenProps.update(param1,param2);
         this._progressTween.reset();
         this._progressTween.paused = false;
      }
      
      private function onProgressTweenChange() : void
      {
         var _loc1_:int = this._progressTweenProps.startFrame + this._progressTweenProps.delta * this._progressTweenProps.position;
         if(this._progressTweenProps.currentFrame != _loc1_)
         {
            this._progressTweenProps.target.gotoAndStop(_loc1_);
            this._progressTweenProps.currentFrame = _loc1_;
         }
      }
      
      private function normalizeMarkerValue(param1:Number, param2:Boolean = false) : Number
      {
         return (CIRCLE_PROGRESS_MAX - CIRCLE_PROGRESS_MIN) * param1 + CIRCLE_PROGRESS_MIN - (!!param2 ? STATES_DELIMITER : 0);
      }
      
      private function addMarkers() : void
      {
         var _loc4_:Sprite = null;
         var _loc5_:uint = 0;
         var _loc1_:Number = MiN_STATE_VALUE;
         var _loc2_:Number = 0;
         var _loc3_:Boolean = false;
         var _loc6_:int = this._overheatStates.length;
         var _loc7_:uint = Math.max(_loc6_ - 2,0);
         var _loc8_:Vector.<uint> = OverheatMarkersDrawer.getGradientColors(PROGRESS_START_COLOR,PROGRESS_END_COLOR,_loc7_);
         _loc5_ = 0;
         while(_loc5_ < _loc6_)
         {
            _loc2_ = this._overheatStates[_loc5_];
            if(MiN_STATE_VALUE <= _loc2_ && _loc2_ <= MAX_STATE_VALUE)
            {
               _loc3_ = _loc5_ == _loc6_ - 1;
               _loc4_ = OverheatMarkersDrawer.drawProgressSegment(SEGMENT_OUTER_RADIUS,this.normalizeMarkerValue(_loc1_),this.normalizeMarkerValue(_loc2_,!_loc3_),DEFAULT_SEGMENT_COLOR,DEFAULT_SEGMENT_ALPHA,SEGMENT_THICKNESS);
               this._staticMarkers.push(_loc4_);
               this._markersContainer.addChild(_loc4_);
               _loc4_ = OverheatMarkersDrawer.drawProgressSegment(SEGMENT_OUTER_RADIUS,this.normalizeMarkerValue(_loc1_),this.normalizeMarkerValue(_loc2_,!_loc3_),ACTIVE_SEGMENT_COLOR,ACTIVE_SEGMENT_ALPHA,SEGMENT_THICKNESS);
               OverheatMarkersDrawer.setShadowFilter(_loc4_);
               _loc4_.visible = false;
               this._stateMarkers.push(_loc4_);
               this._markersContainer.addChild(_loc4_);
               _loc4_ = OverheatMarkersDrawer.drawProgressSegment(ACTIVE_SEGMENT_OUTER_RADIUS,this.normalizeMarkerValue(_loc1_),this.normalizeMarkerValue(_loc2_,!_loc3_),_loc8_[_loc5_],ACTIVE_SEGMENT_OUTER_ALPHA,ACTIVE_SEGMENT_THICKNESS,ACTIVE_SEGMENT_EDGE_HEIGHT);
               OverheatMarkersDrawer.setShadowFilter(_loc4_);
               _loc4_.visible = false;
               this._outerStateMarkers.push(_loc4_);
               this._outerMarkersContainer.addChild(_loc4_);
               _loc1_ = _loc2_;
            }
            else
            {
               DebugUtils.LOG_ERROR("Value must be in range 0 .. 1");
            }
            _loc5_++;
         }
      }
      
      private function showCurrentStateMarkers() : void
      {
         this.clearMarkerTweens();
         if(this._prevState > Values.DEFAULT_INT)
         {
            this.showMarkerFadeTween(this._stateMarkers[this._prevState],0);
            this.showMarkerFadeTween(this._outerStateMarkers[this._prevState],0);
         }
         if(this.state == STATE_HIDDEN)
         {
            return;
         }
         var _loc1_:Sprite = this._stateMarkers[this.state];
         var _loc2_:Sprite = this._outerStateMarkers[this.state];
         _loc1_.alpha = _loc2_.alpha = 0;
         _loc1_.visible = _loc2_.visible = true;
         this.showMarkerFadeTween(_loc1_,1);
         this.showMarkerFadeTween(_loc2_,1);
      }
      
      private function clearCurrentStateMarkers() : void
      {
         var _loc1_:Sprite = null;
         for each(_loc1_ in this._stateMarkers)
         {
            if(_loc1_.filters)
            {
               _loc1_.filters.splice(0,_loc1_.filters.length);
               _loc1_.filters = null;
            }
            this._markersContainer.removeChild(_loc1_);
         }
         this._stateMarkers.splice(0,this._stateMarkers.length);
         for each(_loc1_ in this._outerStateMarkers)
         {
            this._outerMarkersContainer.removeChild(_loc1_);
         }
         this._outerStateMarkers.splice(0,this._outerStateMarkers.length);
      }
      
      private function clearAllMarkers() : void
      {
         var _loc1_:Sprite = null;
         this.clearCurrentStateMarkers();
         for each(_loc1_ in this._staticMarkers)
         {
            this._markersContainer.removeChild(_loc1_);
         }
         this._staticMarkers.splice(0,this._staticMarkers.length);
      }
      
      private function showMarkerFadeTween(param1:Sprite, param2:Number) : void
      {
         if(this._isForcedStateChange)
         {
            param1.alpha = param2;
            param1.visible = param2 > 0;
         }
         else
         {
            this._markerTweens.push(new Tween(MARKER_FADE_TWEEN_DURATION,param1,{"alpha":param2},{
               "ease":Quartic.easeOut,
               "onComplete":this.onFadeTweenComplete
            }));
         }
      }
      
      private function onFadeTweenComplete(param1:Tween) : void
      {
         var _loc2_:DisplayObject = DisplayObject(param1.target);
         _loc2_.visible = _loc2_.alpha > 0;
      }
      
      private function clearMarkerTweens() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = this._markerTweens.length;
         _loc1_ = 0;
         while(_loc1_ < _loc2_)
         {
            this._markerTweens[_loc1_].dispose();
            _loc1_++;
         }
         this._markerTweens.splice(0,_loc2_);
      }
      
      private function updateDistanceVisibility() : void
      {
         this.clearDistanceTween();
         this._distanceTween = new Tween(DISTANCE_FADE_TWEEN_DURATION,this._rangefinder,{"alpha":(!this.isOverheated && this.isDistanceVisible ? 1 : 0)},{"ease":Quartic.easeOut});
      }
      
      private function clearDistanceTween() : void
      {
         if(this._distanceTween)
         {
            this._distanceTween.dispose();
            this._distanceTween = null;
         }
      }
      
      private function updateState() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         var _loc3_:uint = 0;
         var _loc4_:int = 0;
         if(this.isOverheated)
         {
            this.state = STATE_HIDDEN;
         }
         else if(this._curProgress == MiN_STATE_VALUE)
         {
            this.state = STATE_HIDDEN;
            this._curStateMax = MiN_STATE_VALUE;
         }
         else
         {
            _loc1_ = MiN_STATE_VALUE;
            _loc4_ = this._overheatStates.length;
            _loc3_ = 0;
            while(_loc3_ < _loc4_)
            {
               if(_loc3_ != 0)
               {
                  _loc1_ = this._overheatStates[_loc3_ - 1];
               }
               _loc2_ = this._overheatStates[_loc3_];
               if(_loc1_ < this._curProgress && this._curProgress < _loc2_)
               {
                  this._curStateMin = _loc1_;
                  this._curStateMax = _loc2_;
                  this.state = _loc3_;
                  break;
               }
               _loc3_++;
            }
         }
      }
      
      public function get isOverheated() : Boolean
      {
         return this._overheatTimeLeft > 0;
      }
      
      public function get isDistanceVisible() : Boolean
      {
         return this._isDistanceVisible;
      }
      
      public function set isDistanceVisible(param1:Boolean) : void
      {
         if(this._isDistanceVisible == param1)
         {
            return;
         }
         this._isDistanceVisible = param1;
         this.updateDistanceVisibility();
      }
      
      public function get state() : int
      {
         return this._state;
      }
      
      public function set state(param1:int) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._prevState = this._state;
         this._state = param1;
         this.showCurrentStateMarkers();
         this._isForcedStateChange = false;
      }
   }
}
