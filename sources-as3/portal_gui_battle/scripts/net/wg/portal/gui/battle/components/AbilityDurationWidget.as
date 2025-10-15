package net.wg.portal.gui.battle.components
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.Time;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.utils.IDateTime;
   
   public class AbilityDurationWidget extends SimpleDisposable
   {
      
      private static const SECONDS_INIT_VALUE:int = 120;
      
      private static const MAIN_ICON_WIDTH:uint = 44;
      
      private static const GAP:int = 2;
       
      
      public var timerTf:TextField = null;
      
      public var clockIcon:MovieClip = null;
      
      public var fillMc:AbilityProgressFill = null;
      
      private var _dateTime:IDateTime;
      
      private var _timerPrefix:String = "";
      
      private var _timeRemainingSec:int = 120;
      
      public function AbilityDurationWidget()
      {
         this._dateTime = App.utils.dateTime;
         super();
         this.initialize();
      }
      
      override protected function onDispose() : void
      {
         this.clearCountdown();
         this.timerTf = null;
         this.clockIcon = null;
         this.fillMc.dispose();
         this.fillMc = null;
         this._dateTime = null;
         super.onDispose();
      }
      
      public function startCountdown(param1:int) : void
      {
         this.clearCountdown();
         this._timeRemainingSec = param1;
         this.updateTimerTfText();
         this.fillMc.gotoAndStop(1);
         App.utils.scheduler.scheduleRepeatableTask(this.update,Time.MILLISECOND_IN_SECOND,param1);
         this.fillMc.startCountdown(param1);
      }
      
      protected function initialize() : void
      {
         this.fillMc.gotoAndStop(1);
         this.updateLayout();
      }
      
      private function clearCountdown() : void
      {
         App.utils.scheduler.cancelTask(this.update);
         this.fillMc.clearProgressTween();
      }
      
      private function update() : void
      {
         --this._timeRemainingSec;
         this.updateTimerTfText();
      }
      
      private function updateTimerTfText() : void
      {
         this.timerTf.text = this._timerPrefix;
         this.timerTf.appendText(this._dateTime.formatSecondsToString(this._timeRemainingSec));
      }
      
      private function updateLayout() : void
      {
         this.updateTimerTfText();
         App.utils.commons.updateTextFieldSize(this.timerTf,true,false);
         this.clockIcon.x = this.fillMc.width - (this.timerTf.width + this.clockIcon.width + MAIN_ICON_WIDTH + GAP) >> 1;
         this.clockIcon.x += MAIN_ICON_WIDTH;
         this.timerTf.x = this.clockIcon.x + this.clockIcon.width + GAP | 0;
      }
      
      public function set timerPrefix(param1:String) : void
      {
         this._timerPrefix = param1;
         this.updateLayout();
      }
   }
}
