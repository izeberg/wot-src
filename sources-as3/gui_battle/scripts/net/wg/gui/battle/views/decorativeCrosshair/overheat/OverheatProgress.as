package net.wg.gui.battle.views.decorativeCrosshair.overheat
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.utils.getTimer;
   import net.wg.gui.battle.views.decorativeCrosshair.OverheatDecorativeCrosshair;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class OverheatProgress extends MovieClip implements IDisposable
   {
      
      private static const MAIN_PROGRESS_FRAMES:uint = 400;
      
      private static const EMPTY_PROGRESS_FRAMES:uint = 100;
      
      private static const FRAMES_REACTION_THRESHOLD:uint = 50;
      
      private static const LERP_ALPHA:Number = 0.25;
      
      private static const MS_IN_SEC:uint = 1000;
      
      private static const DAMAGE_SNAP:int = 5;
      
      private static const DEFAULT_REPLAY_SPEED:int = 1;
      
      private static const STATE_SHOW:String = "show";
      
      private static const STATE_HIDE:String = "hide";
      
      private static const STATE_SHAKE_AND_HIDE:String = "shakeAndHide";
       
      
      public var empty:MovieClip = null;
      
      public var pointer:MovieClip = null;
      
      public var pointerGlow:MovieClip = null;
      
      private var _currentFrame:Number = 0;
      
      private var _targetFrame:Number = 0;
      
      private var _pointerShown:Boolean = false;
      
      private var _heatProgress:Number = 0;
      
      private var _fullTimeMs:uint = 19000.0;
      
      private var _fullCoolingTimeMs:uint = 45000.0;
      
      private var _maxLevel:Number = 1;
      
      private var _isDisposed:Boolean = false;
      
      private var _isGaining:Boolean = false;
      
      private var _isCooling:Boolean = false;
      
      private var _baseDamage:int = 0;
      
      private var _maxExtraDamage:int = 0;
      
      private var _currentDamage:int = 0;
      
      private var _counterValue:int = 0;
      
      private var _interpolation:Boolean = true;
      
      private var _stopTimerTime:Number = 0;
      
      private var _counter:OverheatCounter = null;
      
      private var _lastUpdateFromServerTime:int = 0;
      
      private var _lastServerProgress:Number = 0;
      
      private var _lerp:Number = 0.25;
      
      public function OverheatProgress()
      {
         super();
         App.stage.addEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
         this.updateProgressVisible();
      }
      
      private static function snapDownToFive(param1:Number) : int
      {
         return int(Math.floor(param1 / DAMAGE_SNAP) * DAMAGE_SNAP);
      }
      
      public function setProgress(param1:Number, param2:int) : void
      {
         this._lastServerProgress = (param2 + param1) / this._maxLevel;
         this._lastUpdateFromServerTime = getTimer();
         this.recalcTargetFrame();
         this.updateProgressVisible();
         if(!this._interpolation)
         {
            this._currentFrame = this._targetFrame;
            this.setCounter(this._currentDamage);
            gotoAndStop(this._currentFrame);
         }
      }
      
      private function onEnterFrameHandler(param1:Event) : void
      {
         this.recalcTargetFrame();
         this._currentFrame += (this._targetFrame - this._currentFrame) * this._lerp;
         this.setCounter(this._currentDamage);
         gotoAndStop(this._currentFrame);
      }
      
      private function recalcTargetFrame() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:int = getTimer() - this._lastUpdateFromServerTime;
         if(this._isGaining)
         {
            _loc1_ = this._lastServerProgress + _loc2_ / this._fullTimeMs;
            if(_loc1_ > 1)
            {
               _loc1_ = 1;
            }
         }
         else if(this._isCooling)
         {
            _loc1_ = this._lastServerProgress - _loc2_ / this._fullCoolingTimeMs;
            if(_loc1_ < 0)
            {
               _loc1_ = 0;
            }
         }
         else
         {
            _loc1_ = this._lastServerProgress;
         }
         this._targetFrame = _loc1_ * MAIN_PROGRESS_FRAMES;
         var _loc3_:Number = this._baseDamage + _loc1_ * this._maxExtraDamage;
         var _loc4_:int = this._baseDamage + this._maxExtraDamage;
         if(_loc3_ >= _loc4_)
         {
            this._currentDamage = _loc4_;
         }
         else
         {
            this._currentDamage = snapDownToFive(_loc3_);
         }
      }
      
      private function setCounter(param1:int) : void
      {
         if(this._counter)
         {
            if(this._counterValue != param1)
            {
               this._counterValue = param1;
               this._counter.setCount(param1);
            }
         }
      }
      
      public function setHeatProgress(param1:Number) : void
      {
         this._heatProgress = param1;
         this.updateProgressVisible();
      }
      
      public function setState(param1:uint) : void
      {
         this._isGaining = false;
         this._isCooling = false;
         switch(param1)
         {
            case OverheatDecorativeCrosshair.STATE_CHARGE_MAX:
            case OverheatDecorativeCrosshair.STATE_STACK_GAIN:
               this._isGaining = true;
               break;
            case OverheatDecorativeCrosshair.STATE_STACK_LOOSE:
               this._isCooling = true;
         }
      }
      
      private function updateProgressVisible() : void
      {
         var _loc2_:Boolean = false;
         if(this._targetFrame > 0)
         {
            this.empty.gotoAndStop(EMPTY_PROGRESS_FRAMES);
         }
         else if(this._heatProgress == 0 && this.empty.currentFrame == EMPTY_PROGRESS_FRAMES)
         {
            this.empty.gotoAndPlay(STATE_HIDE);
         }
         else
         {
            this.empty.gotoAndStop(EMPTY_PROGRESS_FRAMES * this._heatProgress);
         }
         var _loc1_:Boolean = this._targetFrame > 0;
         if(_loc1_ != this._pointerShown)
         {
            this._pointerShown = _loc1_;
            if(this._pointerShown)
            {
               this.pointer.gotoAndPlay(STATE_SHOW);
               this.pointerGlow.gotoAndPlay(STATE_SHOW);
            }
            else
            {
               _loc2_ = this._currentFrame >= FRAMES_REACTION_THRESHOLD;
               this.pointer.gotoAndPlay(!!_loc2_ ? STATE_SHAKE_AND_HIDE : STATE_HIDE);
               this.pointerGlow.gotoAndPlay(STATE_HIDE);
            }
         }
      }
      
      public function dispose() : void
      {
         App.stage.removeEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
         this._counter = null;
         this.pointer = null;
         this.pointerGlow = null;
         this.empty = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setInitData(param1:int, param2:Number, param3:Number, param4:Boolean) : void
      {
         this._fullTimeMs = param2 * MS_IN_SEC;
         this._fullCoolingTimeMs = param3 * MS_IN_SEC;
         this._maxLevel = param1;
         this._lerp = LERP_ALPHA;
         if(this._interpolation && param4)
         {
            this._stopTimerTime = getTimer() - this._lastUpdateFromServerTime;
            App.stage.removeEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
            this._interpolation = false;
         }
         else if(!this._interpolation && !param4)
         {
            this._lastUpdateFromServerTime = getTimer() - this._stopTimerTime;
            App.stage.addEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
            this._interpolation = true;
         }
      }
      
      public function setDependency(param1:OverheatCounter) : void
      {
         this._counter = param1;
      }
      
      public function setDamageData(param1:int, param2:int) : void
      {
         this._baseDamage = param1;
         this._maxExtraDamage = param2 - param1;
      }
   }
}
