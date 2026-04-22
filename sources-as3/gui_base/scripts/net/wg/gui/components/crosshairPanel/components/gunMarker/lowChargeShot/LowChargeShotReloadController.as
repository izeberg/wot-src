package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import flash.events.EventDispatcher;
   import flash.utils.clearInterval;
   import flash.utils.getTimer;
   import flash.utils.setInterval;
   import net.wg.data.constants.generated.LOW_CHARGE_SHOT_CONSTS;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class LowChargeShotReloadController extends EventDispatcher implements IDisposable
   {
      
      private static const BLOCK_STAGE_CAP:Number = 0.1;
      
      private static const RELOAD_CAP:Number = 1 - BLOCK_STAGE_CAP;
      
      private static const TIME_LEFT_EPS:Number = 2;
      
      private static const REDRAW_INTERVAL_QUICK_RELOAD:int = 90;
      
      private static const REDRAW_INTERVAL_COMMON:int = 100;
       
      
      private var _reloadingInterval:Number = 0;
      
      private var _baseTime:Number = -1;
      
      private var _almostFinishedTime:Number = -1;
      
      private var _lowChargeTime:Number = -1;
      
      private var _currentTimeLeft:Number = -1;
      
      private var _quickReloadingTime:Number = -1;
      
      private var _isDisposed:Boolean = false;
      
      private var _reloadingState:Number = -1;
      
      private var _lowChargeCap:Number = -1;
      
      public function LowChargeShotReloadController()
      {
         super();
      }
      
      public final function dispose() : void
      {
         if(!this._isDisposed)
         {
            this.clearTimer();
            this._isDisposed = true;
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setTimeLeft(param1:Number, param2:Number, param3:Boolean = false) : void
      {
         this._reloadingState = param2;
         if(param3)
         {
            if(!this.isBeforeBattle)
            {
               this.currentTimeLeft = param1;
               this.updateReloadingTimer();
            }
            else
            {
               this.tick(this.reloadingInPercent);
            }
            return;
         }
         this.currentTimeLeft = param1;
         var _loc4_:Boolean = this._reloadingState == LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE && param1 > 0;
         var _loc5_:Boolean = param1 > this.currentTimeLeft + TIME_LEFT_EPS;
         this.currentTimeLeft = _loc4_ && !_loc5_ ? Number(this.timeLeftByProgress(this.reloadingInPercent)) : Number(param1);
         this.updateReloadingTimer();
         this.clearTimer();
         if(this.isReloading)
         {
            this.startTimer();
         }
      }
      
      public function trySetInitialTime(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number = -1) : Boolean
      {
         if(this._baseTime != param1 || this._lowChargeTime != param2 || this._quickReloadingTime != param5 || this._almostFinishedTime != param3 || this._lowChargeCap != param4)
         {
            this._baseTime = param1;
            this._lowChargeTime = param2;
            this._quickReloadingTime = param5;
            this._almostFinishedTime = param3;
            this._lowChargeCap = param4;
            if(this._reloadingState == LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE)
            {
               this.currentTimeLeft = this.timeLeftByProgress(this.reloadingInPercent);
            }
            return true;
         }
         return false;
      }
      
      private function timeLeftByProgress(param1:Number) : Number
      {
         param1 = Math.max(0,Math.min(1,param1));
         var _loc2_:Number = 1 - this._lowChargeCap - BLOCK_STAGE_CAP;
         var _loc3_:Number = this._baseTime - this._lowChargeTime - this._almostFinishedTime;
         if(_loc2_ <= 0 || _loc3_ <= 0)
         {
            return Math.max(0,this.currentTimeLeft);
         }
         return this._almostFinishedTime + _loc3_ * (1 - (param1 - this._lowChargeCap) / _loc2_);
      }
      
      private function tick(param1:Number, param2:Number = -1) : void
      {
         dispatchEvent(new LowChargeShotReloadEvent(LowChargeShotReloadEvent.TICK,param2,this._reloadingState,param1));
      }
      
      private function clearTimer() : void
      {
         clearInterval(this._reloadingInterval);
      }
      
      private function updateReloadingTimer() : void
      {
         var _loc1_:Number = this.reloadingInPercent;
         if(getTimer() >= this._currentTimeLeft)
         {
            this.clearTimer();
         }
         var _loc2_:Number = this.currentTimeLeft;
         if(this._reloadingState == LOW_CHARGE_SHOT_CONSTS.INITIAL_RELOAD)
         {
            _loc2_ -= this.restChargeTime;
         }
         this.tick(_loc1_,Math.max(0,_loc2_));
      }
      
      private function startTimer() : void
      {
         var _loc1_:int = this._reloadingState == LOW_CHARGE_SHOT_CONSTS.QUICK_RELOAD ? int(REDRAW_INTERVAL_QUICK_RELOAD) : int(REDRAW_INTERVAL_COMMON);
         this._reloadingInterval = setInterval(this.updateReloadingTimer,_loc1_);
      }
      
      public function get isBeforeBattle() : Boolean
      {
         return this._reloadingState == LOW_CHARGE_SHOT_CONSTS.STATE_NONE;
      }
      
      public function get isEmpty() : Boolean
      {
         return this._reloadingState == LOW_CHARGE_SHOT_CONSTS.EMPTY;
      }
      
      public function get isReloading() : Boolean
      {
         return this._reloadingState != LOW_CHARGE_SHOT_CONSTS.FULL_CHARGE && !this.isEmpty && !this.isBeforeBattle;
      }
      
      public function get lowChargeCap() : Number
      {
         return this._lowChargeCap;
      }
      
      public function get blockStageCap() : Number
      {
         return BLOCK_STAGE_CAP;
      }
      
      public function get restChargeTime() : Number
      {
         return Math.max(this._baseTime - this._lowChargeTime,0);
      }
      
      public function get lowChargeTime() : Number
      {
         return this._lowChargeTime;
      }
      
      public function get baseTime() : Number
      {
         return this._baseTime;
      }
      
      public function get quickReloadingTime() : Number
      {
         return this._quickReloadingTime;
      }
      
      public function get currentTimeLeft() : Number
      {
         return Math.max(0,(this._currentTimeLeft - getTimer()) / CrosshairConsts.MS_IN_SECOND);
      }
      
      public function set currentTimeLeft(param1:Number) : void
      {
         this._currentTimeLeft = getTimer() + param1 * CrosshairConsts.MS_IN_SECOND;
      }
      
      public function get reloadingInPercent() : Number
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         if(this._almostFinishedTime != 0 && this._baseTime != this._almostFinishedTime && this._baseTime != 0)
         {
            if(this._reloadingState == LOW_CHARGE_SHOT_CONSTS.ALMOST_FINISHED)
            {
               return RELOAD_CAP + Math.max(0,(1 - this.currentTimeLeft / this._almostFinishedTime) * BLOCK_STAGE_CAP);
            }
            if(this._reloadingState == LOW_CHARGE_SHOT_CONSTS.INITIAL_RELOAD)
            {
               _loc1_ = this._baseTime - this._lowChargeTime;
               return (1 - (this.currentTimeLeft - _loc1_) / this._lowChargeTime) * this._lowChargeCap;
            }
            if(this._reloadingState == LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE)
            {
               _loc2_ = this._baseTime - this._lowChargeTime - this._almostFinishedTime;
               return this._lowChargeCap + (1 - (this.currentTimeLeft - this._almostFinishedTime) / _loc2_) * (1 - this._lowChargeCap - BLOCK_STAGE_CAP);
            }
            return 1 - this.currentTimeLeft / this.baseTime;
         }
         return 0;
      }
   }
}
