package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.MovieClip;
   import flash.events.TimerEvent;
   import flash.utils.Timer;
   import flash.utils.getTimer;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class SmoothFrameProgress implements IDisposable
   {
      
      private static const INCLUDED_LAST_FRAME:uint = 1;
       
      
      private var _target:MovieClip = null;
      
      private var _progressFrame:uint = 0;
      
      private var _progressFrameMax:uint = 0;
      
      private var _progress:Number = 0;
      
      private var _lastTimePoint:Number = 0;
      
      private var _firstFrame:uint = 0;
      
      private var _framesLength:uint = 0;
      
      private var _timer:flash.utils.Timer = null;
      
      private var _isActive:Boolean = false;
      
      private var _isDisposed:Boolean = false;
      
      public function SmoothFrameProgress(param1:MovieClip, param2:uint, param3:uint)
      {
         super();
         this.setup(param1,param2,param3);
      }
      
      private function setup(param1:MovieClip, param2:uint, param3:uint) : void
      {
         this._target = param1;
         this._firstFrame = param2;
         this._framesLength = param3 - param2 + INCLUDED_LAST_FRAME;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.removeTimer();
         this._target = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function changeTarget(param1:MovieClip, param2:uint, param3:uint) : void
      {
         var _loc4_:Number = NaN;
         if(this._isDisposed)
         {
            return;
         }
         if(this._isActive)
         {
            this.removeTimer();
            _loc4_ = this._progressFrame / this._framesLength;
            this.setup(param1,param2,param3);
            this._progressFrame = this._framesLength * _loc4_;
            this._target.gotoAndStop(this._progressFrame);
            this.applyProgress(this._progress);
         }
         else
         {
            this.setup(param1,param2,param3);
         }
      }
      
      private function getFrameByProgress(param1:Number) : uint
      {
         return this._firstFrame + param1 * this._framesLength;
      }
      
      public function set isActive(param1:Boolean) : void
      {
         if(this._isActive == param1)
         {
            return;
         }
         if(param1)
         {
            this._lastTimePoint = getTimer();
            this._progress = Values.ZERO;
            this._progressFrame = this.getFrameByProgress(this._progress);
         }
         this._isActive = param1;
      }
      
      public function set progress(param1:Number) : void
      {
         this.applyProgress(param1);
         this._progress = param1;
      }
      
      private function applyProgress(param1:Number) : void
      {
         if(!this._isActive)
         {
            return;
         }
         var _loc2_:Number = getTimer();
         var _loc3_:Number = _loc2_ - this._lastTimePoint;
         this._lastTimePoint = _loc2_;
         this._progressFrameMax = this.getFrameByProgress(param1);
         var _loc4_:uint = this._progressFrameMax - this._target.currentFrame;
         var _loc5_:Number = _loc4_ > Values.ZERO ? Number(_loc3_ / _loc4_) : Number(Values.ZERO);
         if(_loc4_ > 0)
         {
            this.removeTimer();
            this.increaseProgressFrame();
            this._timer = new flash.utils.Timer(_loc5_,_loc4_ - 1);
            this._timer.addEventListener(TimerEvent.TIMER_COMPLETE,this.onTimerCompleteHandler);
            this._timer.addEventListener(TimerEvent.TIMER,this.onUpdateTimerHandler,false,0,true);
            this._timer.reset();
            this._timer.start();
         }
         else
         {
            this._target.gotoAndStop(this._progressFrame);
         }
      }
      
      private function removeTimer() : void
      {
         if(this._timer)
         {
            this._timer.stop();
            this._timer.removeEventListener(TimerEvent.TIMER_COMPLETE,this.onTimerCompleteHandler);
            this._timer.removeEventListener(TimerEvent.TIMER,this.onUpdateTimerHandler,false);
            this._timer = null;
         }
      }
      
      private function onUpdateTimerHandler(param1:TimerEvent) : void
      {
         this.increaseProgressFrame();
      }
      
      private function onTimerCompleteHandler(param1:TimerEvent) : void
      {
         this.removeTimer();
      }
      
      private function increaseProgressFrame() : void
      {
         if(this._progressFrame < this._progressFrameMax)
         {
            this._target.gotoAndStop(this._progressFrame++);
         }
      }
   }
}
