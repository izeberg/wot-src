package net.wg.gui.components.crosshairPanel.components.autoloader
{
   import flash.display.MovieClip;
   import flash.geom.Rectangle;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class AutoloaderShellsCassette extends SimpleContainer
   {
      
      private static const RELOADING_FRAMES:int = 100;
      
      private static const AUTOLOADING_START_FRAME:int = 14;
      
      private static const AUTOLOADING_FRAMES:int = 83;
      
      private static const STATUS_RELOAD_IDLE_STATE:int = 11;
      
      private static const STATUS_RELOAD_COMPLETE_STATE:int = 2;
      
      private static const STATUS_RELOAD_COMPLETE_IDLE:int = 1;
      
      private static const TIMER_STATE_INVALID:String = "TIMER_STATE_INVALID";
      
      private static const TIMER_COMPONENT_NAME:String = "timer";
      
      private static const IDLE_STATE:int = 0;
      
      protected static const GUN_RELOADING_COMPLETE_STATE:int = 1;
      
      protected static const SHELL_STATE_COMEIN:String = "comeIn";
      
      protected static const SHELL_STATE_READY:String = "ready";
      
      protected static const SHELL_STATE_RELOADING:String = "reloading";
      
      protected static const SHELL_STATE_ON_READY:String = "onReady";
      
      protected static const SHELL_STATE_CLEAR:String = "clear";
       
      
      public var shell_1:MovieClip = null;
      
      public var shell_2:MovieClip = null;
      
      public var shell_3:MovieClip = null;
      
      public var shell_4:MovieClip = null;
      
      public var shell_5:MovieClip = null;
      
      public var shell_6:MovieClip = null;
      
      public var shell_7:MovieClip = null;
      
      public var shell_8:MovieClip = null;
      
      public var shell_9:MovieClip = null;
      
      public var shell_10:MovieClip = null;
      
      public var shell_11:MovieClip = null;
      
      public var shell_12:MovieClip = null;
      
      public var shell_13:MovieClip = null;
      
      public var shell_14:MovieClip = null;
      
      public var shell_15:MovieClip = null;
      
      public var shell_16:MovieClip = null;
      
      public var shell_17:MovieClip = null;
      
      public var shell_18:MovieClip = null;
      
      public var shell_19:MovieClip = null;
      
      public var statusMc:MovieClip = null;
      
      public var background:MovieClip = null;
      
      public var backgroundCritical:MovieClip = null;
      
      public var timerMc:MovieClip = null;
      
      private var _timer:AutoloaderTimer = null;
      
      private var _totalAmmo:int = -1;
      
      private var _isAutoloadInProgress:Boolean = false;
      
      private var _isCritical:Boolean = false;
      
      private var _isTimerRed:Boolean = false;
      
      private var _isTimerOn:Boolean = false;
      
      private var _lastShell:MovieClip = null;
      
      private var _currentAutoloadProgress:Number = -1;
      
      protected var _currentReloadingPercent:Number = -1;
      
      protected var _shells:Vector.<MovieClip> = null;
      
      protected var _currentAmmo:int = -1;
      
      protected var _isAnimationInProgress:Boolean = false;
      
      protected var _lastLoadedShell:MovieClip = null;
      
      public function AutoloaderShellsCassette()
      {
         super();
         this._shells = new <MovieClip>[this.shell_1,this.shell_2,this.shell_3,this.shell_4,this.shell_5,this.shell_6,this.shell_7,this.shell_8,this.shell_9,this.shell_10,this.shell_11,this.shell_12,this.shell_13,this.shell_14,this.shell_15,this.shell_16,this.shell_17,this.shell_18,this.shell_19];
         if(this.timerMc)
         {
            this._timer = this.timerMc.getChildByName(TIMER_COMPONENT_NAME) as AutoloaderTimer;
         }
         this.backgroundCritical.visible = this._isCritical;
      }
      
      override protected function onDispose() : void
      {
         this.shell_1 = null;
         this.shell_2 = null;
         this.shell_3 = null;
         this.shell_4 = null;
         this.shell_5 = null;
         this.shell_6 = null;
         this.shell_7 = null;
         this.shell_8 = null;
         this.shell_9 = null;
         this.shell_10 = null;
         this.shell_11 = null;
         this.shell_12 = null;
         this.shell_13 = null;
         this.shell_14 = null;
         this.shell_15 = null;
         this.shell_16 = null;
         this.shell_17 = null;
         this.shell_18 = null;
         this.shell_19 = null;
         this.background = null;
         this.backgroundCritical = null;
         this.timerMc = null;
         this.statusMc = null;
         this._lastShell = null;
         this._lastLoadedShell = null;
         this._shells.splice(0,this._shells.length);
         this._shells = null;
         if(this._timer)
         {
            this._timer.dispose();
            this._timer = null;
         }
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(TIMER_STATE_INVALID))
         {
            if(this._timer)
            {
               this._timer.updateTimerColor(this._isTimerRed,this._isCritical,this._isAutoloadInProgress);
            }
            this.updateStatusMC();
         }
      }
      
      public function autoloadProgress(param1:Number, param2:Number, param3:Boolean, param4:Boolean, param5:Boolean = false) : void
      {
         if((param5 || !this._isAnimationInProgress) && this._lastLoadedShell && param1 != this._currentAutoloadProgress)
         {
            this._currentAutoloadProgress = param1;
            if(!this._isAutoloadInProgress && param1 > 0)
            {
               this._isAutoloadInProgress = true;
               invalidate(TIMER_STATE_INVALID);
            }
            if(this._isAutoloadInProgress)
            {
               this._lastLoadedShell.gotoAndStop(AUTOLOADING_START_FRAME + param1 * AUTOLOADING_FRAMES);
            }
         }
         if(this._currentReloadingPercent >= GUN_RELOADING_COMPLETE_STATE)
         {
            this.setTimerRed(param4);
         }
         if(this._timer)
         {
            this._isTimerOn = param3;
            this._timer.updateTimer(param2,this._isTimerOn);
         }
      }
      
      public function getTimerRect() : Rectangle
      {
         return this._timer != null ? new Rectangle(this._timer.x,this._timer.y,this._timer.width,this._timer.height) : null;
      }
      
      public function reloadingPercent(param1:Number) : void
      {
         if(param1 != this._currentReloadingPercent)
         {
            this._currentReloadingPercent = param1;
            if(param1 < GUN_RELOADING_COMPLETE_STATE)
            {
               this.reloadingInProgress(param1);
               this.setTimerRed(true);
            }
            else
            {
               this.reloadingComplete();
               this.setTimerRed(false);
            }
         }
      }
      
      public function resetLastLoadedShell() : void
      {
         if(this._isAutoloadInProgress)
         {
            if(this._lastLoadedShell)
            {
               this._lastLoadedShell.gotoAndStop(AUTOLOADING_START_FRAME + AUTOLOADING_FRAMES);
            }
            if(this._timer)
            {
               this._timer.updateTimer(0,this._isTimerOn);
            }
         }
      }
      
      public function updateCritical(param1:Boolean) : void
      {
         this._isCritical = param1;
         this.backgroundCritical.visible = this._isCritical;
         this.background.visible = !this._isCritical;
         invalidate(TIMER_STATE_INVALID);
      }
      
      private function updateTotalAmmoState() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:int = this._shells.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            _loc1_ = this._shells[_loc3_];
            if(_loc1_)
            {
               _loc1_.visible = _loc3_ < this._totalAmmo;
            }
            _loc3_++;
         }
         var _loc4_:int = this._totalAmmo - 1;
         this._lastShell = this._shells[_loc4_];
         this.background.gotoAndStop(_loc4_);
         this.backgroundCritical.gotoAndStop(_loc4_);
         if(this.timerMc)
         {
            this.timerMc.gotoAndStop(_loc4_);
         }
      }
      
      protected function updateCurrentAmmoStates(param1:int) : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:String = null;
         var _loc4_:int = 0;
         _loc4_ = 0;
         while(_loc4_ < this._totalAmmo)
         {
            _loc3_ = _loc4_ < param1 ? SHELL_STATE_READY : SHELL_STATE_CLEAR;
            _loc2_ = this._shells[_loc4_];
            if(_loc2_)
            {
               if(_loc2_.currentLabel == SHELL_STATE_RELOADING && _loc4_ < param1)
               {
                  _loc2_.gotoAndPlay(SHELL_STATE_ON_READY);
               }
               else
               {
                  _loc2_.gotoAndStop(_loc3_);
               }
            }
            _loc4_++;
         }
         this._currentAutoloadProgress = 0;
         this._isAutoloadInProgress = false;
         invalidate(TIMER_STATE_INVALID);
         this._lastLoadedShell = this._shells[this._currentAmmo];
      }
      
      protected function reloadingComplete() : void
      {
         var _loc1_:Boolean = this._isAnimationInProgress;
         this._isAnimationInProgress = false;
         invalidate(TIMER_STATE_INVALID);
         gotoAndStop(IDLE_STATE);
         this.updateCurrentAmmoStates(this._currentAmmo);
         if(this._lastShell && _loc1_ && this._currentAmmo < this._totalAmmo)
         {
            this._lastShell.gotoAndPlay(SHELL_STATE_COMEIN);
         }
      }
      
      protected function reloadingInProgress(param1:Number) : void
      {
         if(!this._isAnimationInProgress)
         {
            this._isAnimationInProgress = true;
            invalidate(TIMER_STATE_INVALID);
         }
         gotoAndStop(param1 * RELOADING_FRAMES);
      }
      
      private function setTimerRed(param1:Boolean) : void
      {
         if(this._isTimerRed != param1)
         {
            this._isTimerRed = param1;
            invalidate(TIMER_STATE_INVALID);
         }
      }
      
      private function updateStatusMC() : void
      {
         if(this.statusMc == null || this.statusMc.totalFrames == 1)
         {
            return;
         }
         if(this._isTimerRed)
         {
            this.statusMc.gotoAndStop(STATUS_RELOAD_COMPLETE_IDLE);
         }
         else if(this.statusMc.currentFrame != STATUS_RELOAD_IDLE_STATE)
         {
            this.statusMc.gotoAndPlay(STATUS_RELOAD_COMPLETE_STATE);
         }
      }
      
      public function set totalAmmo(param1:int) : void
      {
         if(this._totalAmmo == param1)
         {
            return;
         }
         this._totalAmmo = param1;
         this.updateTotalAmmoState();
      }
      
      public function set currentAmmo(param1:int) : void
      {
         this._currentAmmo = param1;
         var _loc2_:int = this._currentAmmo;
         if(this._isAnimationInProgress)
         {
            _loc2_ += 1;
         }
         this.updateCurrentAmmoStates(_loc2_);
      }
   }
}
