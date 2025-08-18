package net.wg.gui.battle.views.dualGunPanel
{
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import net.wg.data.constants.Time;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CROSSHAIR_CASSETTE_TYPES;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class DualGunPanelTimer extends SimpleDisposable
   {
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
      
      public static const STYLE_DEBUFF:String = "debuff";
      
      public static const STYLE_CRITICAL:String = "critical";
      
      public static const STYLE_CHARGE:String = "charge";
      
      public static const STYLE_PRIMARY_LOADING:String = "primaryLoading";
      
      public static const STYLE_SECONDARY_LOADING:String = "secondaryLoading";
      
      public static const STYLE_IDLE:String = "idle";
       
      
      public var timerReloading:TextField = null;
      
      public var timerAutoload:TextField = null;
      
      public var timerStun:TextField = null;
      
      public var timerIdle:TextField = null;
      
      public var totalTimer:TextField = null;
      
      private var _timersMap:Object;
      
      private var _currentTimer:TextField;
      
      private var _currentStyle:String = "";
      
      private var _lastValue:String = "";
      
      public function DualGunPanelTimer()
      {
         super();
         this._currentTimer = this.timerIdle;
         this._timersMap = {};
         this._timersMap[STYLE_DEBUFF] = this.timerReloading;
         this._timersMap[STYLE_CHARGE] = this.timerAutoload;
         this._timersMap[STYLE_PRIMARY_LOADING] = this.timerReloading;
         this._timersMap[STYLE_SECONDARY_LOADING] = this.timerAutoload;
         this._timersMap[STYLE_IDLE] = this.timerIdle;
         this._timersMap[STYLE_CRITICAL] = this.timerStun;
      }
      
      override protected function onDispose() : void
      {
         App.utils.data.cleanupDynamicObject(this._timersMap);
         this.timerReloading = null;
         this.timerAutoload = null;
         this.timerIdle = null;
         this.timerStun = null;
         this._currentTimer = null;
         this.totalTimer = null;
      }
      
      public function setTextStyle(param1:String) : void
      {
         if(this._currentStyle == param1)
         {
            return;
         }
         this._currentStyle = param1;
         var _loc2_:TextField = this._timersMap[param1];
         if(_loc2_)
         {
            this.switchCurrentTimers(_loc2_);
         }
      }
      
      public function updateClipType(param1:int) : void
      {
         if(CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_TYPES.indexOf(param1) != -1)
         {
            this.totalTimer.alpha = Values.ZERO;
            this.timerIdle.alpha = Values.DEFAULT_ALPHA;
         }
         else
         {
            this.totalTimer.alpha = Values.DEFAULT_ALPHA;
            this.timerIdle.alpha = Values.ZERO;
         }
      }
      
      public function updateTimerValue(param1:Number) : void
      {
         var _loc2_:String = this.convertTimerValue(param1);
         if(this._lastValue != _loc2_)
         {
            this._lastValue = _loc2_;
            this._currentTimer.text = _loc2_;
         }
      }
      
      public function updateTotalTime(param1:Number) : void
      {
         this.totalTimer.text = param1 > Values.DEFAULT_INT ? this.convertTimerValue(param1) : Values.EMPTY_STR;
      }
      
      private function switchCurrentTimers(param1:TextField) : void
      {
         this._currentTimer.visible = false;
         param1.text = this._currentTimer.text;
         this._currentTimer = param1;
         this._currentTimer.visible = true;
      }
      
      private function convertTimerValue(param1:Number) : String
      {
         var _loc2_:String = ExternalInterface.call(FRACTIONAL_FORMAT_CMD,Math.abs(param1 / Time.MILLISECOND_IN_SECOND));
         return _loc2_.slice(0,_loc2_.length - 1);
      }
   }
}
