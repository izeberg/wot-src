package net.wg.gui.battle.views.widgetsPanel.pillbox
{
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.events.TimerEvent;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   import flash.utils.Timer;
   import flash.utils.getTimer;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.PILLBOX_SIEGE_WIDGET_CONST;
   import net.wg.gui.utils.FrameHelper;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PillboxAnim extends MovieClip implements IDisposable
   {
      
      private static const FRAME_POSTFIX_FIRST:String = "_first";
      
      private static const FRAME_POSTFIX_LAST:String = "_last";
      
      private static const FRAME_POSTFIX_FINISH:String = "_finish";
      
      private static const TIME_LEFT_UNAVAILABLE:String = "- -";
      
      private static const MIN_VISIBLE_TIME_VALUE:Number = 0.1;
       
      
      public var progressTf:TextField = null;
      
      private var _frameHelper:FrameHelper = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _animLength:int = 0;
      
      private var _animStart:int = 0;
      
      private var _frames:Dictionary = null;
      
      private var _isInTransition:Boolean = false;
      
      private var _lastTimePoint:Number = 0;
      
      private var _progress:Number = 0;
      
      private var _timeLeft:Number = 0;
      
      private var _skippedProgress:Number = 0;
      
      private var _progressLength:Number = 0;
      
      private var _timer:Timer = null;
      
      private var _animProgressFromFrame:int = 0;
      
      private var _animProgressToFrame:int = 0;
      
      private var _allowProgress:Boolean = false;
      
      private var _state:String = "";
      
      private var _isUpdatable:Boolean = true;
      
      private var _isInPlay:Boolean = false;
      
      private var _inStartTransition:Boolean = false;
      
      private var _isWidgetVisible:Boolean = true;
      
      public function PillboxAnim()
      {
         var _loc3_:FrameLabel = null;
         super();
         this._frameHelper = new FrameHelper(this);
         this._frames = new Dictionary();
         var _loc1_:Array = this.currentLabels;
         var _loc2_:int = _loc1_.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc2_)
         {
            _loc3_ = _loc1_[_loc4_];
            this._frames[_loc3_.name] = _loc3_.frame;
            if(_loc3_.name.indexOf(FRAME_POSTFIX_FIRST) != -1)
            {
               addFrameScript(_loc3_.frame - 1,this.onProgressStart);
            }
            else if(_loc3_.name.indexOf(FRAME_POSTFIX_LAST) != -1)
            {
               addFrameScript(_loc3_.frame - 1,this.onProgressFinish);
            }
            else if(_loc3_.name.indexOf(FRAME_POSTFIX_FINISH) != -1)
            {
               addFrameScript(_loc3_.frame - 1,this.onTransitionFinish);
            }
            _loc4_++;
         }
         this.progressTf.visible = false;
      }
      
      override public function gotoAndPlay(param1:Object, param2:String = null) : void
      {
         this._isInPlay = true;
         super.gotoAndPlay(param1,param2);
      }
      
      override public function gotoAndStop(param1:Object, param2:String = null) : void
      {
         this._isInPlay = false;
         super.gotoAndStop(param1,param2);
      }
      
      override public function play() : void
      {
         this._isInPlay = true;
         super.play();
      }
      
      override public function stop() : void
      {
         this._isInPlay = false;
         super.stop();
      }
      
      public function applyProgress(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:int = 0;
         var _loc6_:Number = NaN;
         if(!this._isInTransition)
         {
            return;
         }
         if(!this._isUpdatable)
         {
            this.progressTf.text = TIME_LEFT_UNAVAILABLE;
            return;
         }
         if(!this._allowProgress)
         {
            this._skippedProgress = param1;
            return;
         }
         if(this._isInTransition)
         {
            _loc3_ = getTimer();
            _loc4_ = _loc3_ - this._lastTimePoint;
            this._lastTimePoint = _loc3_;
            this._timeLeft = param2;
            param1 = (param1 - this._skippedProgress) / this._progressLength;
            this._animProgressFromFrame = this._animStart + Math.round(this._animLength * this._progress);
            this._animProgressToFrame = this._animStart + Math.round(this._animLength * param1);
            _loc5_ = this._animProgressToFrame - this._animProgressFromFrame - 1;
            _loc6_ = _loc5_ > Values.ZERO ? Number(_loc4_ / _loc5_) : Number(Values.ZERO);
            this._progress = param1;
            if(_loc5_ > 0)
            {
               this.removeTimer();
               this.increaseAnimFrame();
               this._timer = new Timer(_loc6_,_loc5_);
               this._timer.addEventListener(TimerEvent.TIMER_COMPLETE,this.onTimerCompleteHandler);
               this._timer.addEventListener(TimerEvent.TIMER,this.onTimerUpdateHandler,false,0,true);
               this._timer.reset();
               this._timer.start();
            }
            else
            {
               this.gotoAndStop(this._animProgressToFrame);
            }
            this.progressTf.text = param2 >= MIN_VISIBLE_TIME_VALUE ? param2.toFixed(1) : Values.EMPTY_STR;
         }
      }
      
      public function applyState(param1:String, param2:Boolean) : void
      {
         var _loc3_:String = null;
         var _loc4_:int = 0;
         if(!this._isUpdatable)
         {
            return;
         }
         this._isInTransition = PILLBOX_SIEGE_WIDGET_CONST.PILLBOX_SIEGE_TRANSITIONS_STATE.indexOf(param1) != -1;
         if(this._isInTransition)
         {
            this._inStartTransition = true;
            this._allowProgress = false;
            this.removeTimer();
            this.gotoAndPlay(param1);
         }
         else if(this._inStartTransition && this._skippedProgress == 1 || param2)
         {
            this.applyStateInstantly(param1);
         }
         else if(this._inStartTransition || !this._allowProgress)
         {
            this._inStartTransition = false;
            this.removeTimer();
            if(this._state.indexOf(param1) == -1)
            {
               this.gotoAndStop(param1);
            }
            else
            {
               _loc3_ = this._state + FRAME_POSTFIX_LAST;
               _loc4_ = this._frameHelper.getFrameByLabel(_loc3_);
               if(_loc4_ > 1 && this._isWidgetVisible)
               {
                  if(this.currentLabel != _loc3_ && !this._isInPlay)
                  {
                     this.gotoAndPlay(_loc4_ + 1);
                  }
               }
               else
               {
                  _loc3_ = this._state + FRAME_POSTFIX_FINISH;
                  _loc4_ = this._frameHelper.getFrameByLabel(_loc3_);
                  if(_loc4_ > 1)
                  {
                     this.gotoAndStop(_loc3_);
                  }
                  else
                  {
                     this.gotoAndStop(param1);
                  }
               }
            }
         }
         this._state = param1;
      }
      
      private function applyStateInstantly(param1:String) : void
      {
         this._inStartTransition = false;
         this._allowProgress = false;
         this.removeTimer();
         this.gotoAndStop(param1);
      }
      
      public function clear() : void
      {
         this.removeTimer();
         this.gotoAndStop(PILLBOX_SIEGE_WIDGET_CONST.EMPTY);
         this.progressTf.text = Values.EMPTY_STR;
      }
      
      public final function dispose() : void
      {
         var _loc1_:* = null;
         this.removeTimer();
         this.stop();
         for(_loc1_ in this._frames)
         {
            if(_loc1_.indexOf(FRAME_POSTFIX_FIRST) != -1 || _loc1_.indexOf(FRAME_POSTFIX_LAST) != -1 || _loc1_.indexOf(FRAME_POSTFIX_FINISH) != -1)
            {
               addFrameScript(this._frames[_loc1_] - 1,null);
            }
         }
         App.utils.data.cleanupDynamicObject(this._frames);
         this._frameHelper.dispose();
         this._frameHelper = null;
         this.progressTf = null;
         this._frames = null;
         this._isDisposed = true;
      }
      
      public function getSnapshot() : AnimSnapshot
      {
         return new AnimSnapshot(this._state,this._isInTransition,this._inStartTransition,this._allowProgress,this._isUpdatable,this._progress,this._timeLeft,this._skippedProgress,this._animProgressFromFrame,this._animProgressToFrame,currentFrame,this._isInPlay);
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setSnapshot(param1:AnimSnapshot) : void
      {
         this._state = param1.state;
         this._isInTransition = param1.isInTransition;
         this._inStartTransition = param1.inStartTransition;
         this._allowProgress = param1.allowProgress;
         this._isUpdatable = param1.isUpdatable;
         this._progress = param1.progress;
         this._skippedProgress = param1.skippedProgress;
         this._animProgressFromFrame = param1.animProgressFromFrame;
         this._animProgressToFrame = param1.animProgressToFrame;
         this._timeLeft = param1.timeLeft;
         this.progressTf.visible = this._allowProgress;
         if(param1.isInPlay)
         {
            this.gotoAndPlay(param1.currentFrame);
         }
         else
         {
            this.gotoAndStop(param1.currentFrame);
         }
         this.calcAnimData();
      }
      
      public function setWidgetVisible(param1:Boolean) : void
      {
         this._isWidgetVisible = param1;
      }
      
      private function onProgressStart() : void
      {
         this._inStartTransition = false;
         this.allowProgress = true;
         this.calcAnimData();
         this.stop();
      }
      
      private function calcAnimData() : void
      {
         this._animLength = this.getAnimLength(this._state);
         this._animStart = this._frames[this._state + FRAME_POSTFIX_FIRST];
         this._progressLength = 1 - this._skippedProgress;
         this._lastTimePoint = getTimer();
      }
      
      private function onProgressFinish() : void
      {
         this.allowProgress = false;
         this.removeTimer();
         this.play();
      }
      
      private function onTransitionFinish() : void
      {
         this.stop();
      }
      
      private function removeTimer() : void
      {
         if(this._timer)
         {
            this._timer.stop();
            this._timer.removeEventListener(TimerEvent.TIMER_COMPLETE,this.onTimerCompleteHandler);
            this._timer.removeEventListener(TimerEvent.TIMER,this.onTimerUpdateHandler,false);
            this._timer = null;
         }
      }
      
      private function increaseAnimFrame() : void
      {
         if(this._animProgressFromFrame < this._animProgressToFrame)
         {
            ++this._animProgressFromFrame;
            this.gotoAndStop(this._animProgressFromFrame);
         }
      }
      
      private function getAnimLength(param1:String) : int
      {
         var _loc2_:String = param1 + FRAME_POSTFIX_FIRST;
         var _loc3_:String = param1 + FRAME_POSTFIX_LAST;
         if(this._frames.hasOwnProperty(_loc3_) && this._frames.hasOwnProperty(_loc2_))
         {
            return this._frames[_loc3_] - this._frames[_loc2_];
         }
         return Values.ZERO;
      }
      
      public function get isInProgress() : Boolean
      {
         return this._inStartTransition || this._allowProgress;
      }
      
      public function set isUpdatable(param1:Boolean) : void
      {
         this._isUpdatable = param1;
      }
      
      private function set allowProgress(param1:Boolean) : void
      {
         this._allowProgress = param1;
         this.progressTf.visible = this._allowProgress;
      }
      
      private function onTimerUpdateHandler(param1:TimerEvent) : void
      {
         this.increaseAnimFrame();
      }
      
      private function onTimerCompleteHandler(param1:TimerEvent) : void
      {
         this.increaseAnimFrame();
         this.removeTimer();
      }
   }
}
