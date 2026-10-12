package net.wg.gui.components.crosshairPanel.components.autoloader
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.external.ExternalInterface;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class AutoloaderTimer extends MovieClip implements IDisposable
   {
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
       
      
      public var timerReloading:AutoloaderTimerText = null;
      
      public var timerAutoload:AutoloaderTimerText = null;
      
      public var timerStun:AutoloaderTimerText = null;
      
      public var timerIdle:AutoloaderTimerText = null;
      
      public var autoreloaderSurge:AutoloaderTimerText = null;
      
      public var autoreloaderSurgeRed:AutoloaderTimerText = null;
      
      public var reloadingBg:Sprite = null;
      
      private var _currentTimer:AutoloaderTimerText = null;
      
      private var _currentLabel:String = "";
      
      private var _disposed:Boolean = false;
      
      private var _isReloading:Boolean = false;
      
      private var _lastTenths:int = -2147483648;
      
      private var _lastIsTimerOn:Boolean = false;
      
      public function AutoloaderTimer()
      {
         super();
         this._currentTimer = this.timerIdle;
         this.autoreloaderSurgeRed.noTranslateTextfield = true;
         this.autoreloaderSurge.noTranslateTextfield = true;
         this.timerReloading.noTranslateTextfield = true;
         this.timerAutoload.noTranslateTextfield = true;
         this.timerStun.noTranslateTextfield = true;
         this.timerIdle.noTranslateTextfield = true;
         this.reloadingBg.visible = false;
      }
      
      public function dispose() : void
      {
         this._disposed = true;
         this.autoreloaderSurge.dispose();
         this.autoreloaderSurge = null;
         this.autoreloaderSurgeRed.dispose();
         this.autoreloaderSurgeRed = null;
         this.timerReloading.dispose();
         this.timerReloading = null;
         this.timerAutoload.dispose();
         this.timerAutoload = null;
         this.timerStun.dispose();
         this.timerStun = null;
         this.timerIdle.dispose();
         this.timerIdle = null;
         this._currentTimer = null;
         this.reloadingBg = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function updateTimer(param1:Number, param2:Boolean) : void
      {
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc3_:Number = Math.abs(param1);
         var _loc4_:int = !!param2 ? int(int(_loc3_ * 10)) : int(int.MIN_VALUE);
         if(_loc4_ == this._lastTenths && param2 == this._lastIsTimerOn)
         {
            return;
         }
         this._lastTenths = _loc4_;
         this._lastIsTimerOn = param2;
         if(param2)
         {
            _loc6_ = ExternalInterface.call(FRACTIONAL_FORMAT_CMD,_loc3_);
            _loc5_ = _loc6_.slice(0,_loc6_.length - 1);
            this.reloadingBg.visible = this._isReloading;
         }
         else
         {
            this.reloadingBg.visible = false;
            _loc5_ = Values.EMPTY_STR;
         }
         this._currentLabel = _loc5_;
         this._currentTimer.label = this._currentLabel;
      }
      
      public function updateTimerColor(param1:Boolean, param2:Boolean, param3:Boolean, param4:Boolean = false, param5:Boolean = true) : void
      {
         this._isReloading = param1;
         this.reloadingBg.visible = param1 && param5;
         if(param1)
         {
            if(param4)
            {
               this.switchCurrentTimers(this.autoreloaderSurgeRed);
            }
            else
            {
               this.switchCurrentTimers(this.timerReloading);
            }
         }
         else if(param2)
         {
            this.switchCurrentTimers(this.timerStun);
         }
         else if(param3)
         {
            if(param4)
            {
               this.switchCurrentTimers(this.autoreloaderSurge);
            }
            else
            {
               this.switchCurrentTimers(this.timerAutoload);
            }
         }
         else
         {
            this.switchCurrentTimers(this.timerIdle);
         }
      }
      
      private function switchCurrentTimers(param1:AutoloaderTimerText) : void
      {
         this._currentTimer.visible = false;
         param1.label = this._currentLabel;
         this._currentTimer = param1;
         this._currentTimer.visible = true;
      }
   }
}
