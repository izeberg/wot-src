package net.wg.portal.gui.battle.components
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.Time;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.utils.IDateTime;
   
   public class AbilityInfoWidget extends SimpleDisposable
   {
      
      private static const SECONDS_INIT_VALUE:int = 120;
      
      private static const PRIMARY_ACTION_SHORTCUT_KEY_PADDING:int = 24;
      
      private static const SECONDARY_ACTION_SHORTCUT_KEY_PADDING:int = 18;
      
      private static const CLOCK_ICON_PADDING_EXTRA_SMALL:int = 20;
      
      private static const CLOCK_ICON_PADDING_MEDIUM:int = 48;
      
      private static const TIMER_TF_PADDING:int = 4;
      
      private static const ABILITY_PROGRESS_FILL_PADDING:int = 10;
       
      
      public var primaryActionShortcutKey:KeyShortcut = null;
      
      public var secondaryActionShortcutKey:KeyShortcut = null;
      
      public var timerTf:TextField = null;
      
      public var clockIcon:MovieClip = null;
      
      public var abilityProgressFill:AbilityProgressFill = null;
      
      public var bg:MovieClip = null;
      
      private var _dateTime:IDateTime;
      
      private var _timeRemainingSec:int = 120;
      
      private var _isExtraSmallLayout:Boolean = false;
      
      public function AbilityInfoWidget()
      {
         this._dateTime = App.utils.dateTime;
         super();
         this.initialize();
      }
      
      override protected function onDispose() : void
      {
         this.primaryActionShortcutKey.dispose();
         this.primaryActionShortcutKey = null;
         this.secondaryActionShortcutKey.dispose();
         this.secondaryActionShortcutKey = null;
         this.clearCountdown();
         this.timerTf = null;
         this.clockIcon = null;
         this.abilityProgressFill.dispose();
         this.abilityProgressFill = null;
         this.bg = null;
         this._dateTime = null;
         super.onDispose();
      }
      
      public function addPrimaryActionShortcutKey(param1:String, param2:String) : void
      {
         this.primaryActionShortcutKey.setKeyAndDesc(param1,param2);
         this.primaryActionShortcutKey.visible = true;
         this.updateLayout();
      }
      
      public function addSecondaryActionShortcutKey(param1:String, param2:String) : void
      {
         this.secondaryActionShortcutKey.setKeyAndDesc(param1,param2);
         this.secondaryActionShortcutKey.visible = true;
         this.updateLayout();
      }
      
      public function startCountdown(param1:int) : void
      {
         this.clearCountdown();
         this._timeRemainingSec = param1;
         this.updateTimerTfText();
         this.abilityProgressFill.gotoAndStop(1);
         App.utils.scheduler.scheduleRepeatableTask(this.update,Time.MILLISECOND_IN_SECOND,param1);
         this.abilityProgressFill.startCountdown(param1);
      }
      
      public function useExtraSmallLayout() : void
      {
         if(!this._isExtraSmallLayout)
         {
            this._isExtraSmallLayout = true;
            this.updateLayout();
         }
      }
      
      public function useMediumLayout() : void
      {
         if(this._isExtraSmallLayout)
         {
            this._isExtraSmallLayout = false;
            this.updateLayout();
         }
      }
      
      protected function initialize() : void
      {
         this.primaryActionShortcutKey.visible = false;
         this.secondaryActionShortcutKey.visible = false;
         this.abilityProgressFill.gotoAndStop(1);
         this.primaryActionShortcutKey.x = PRIMARY_ACTION_SHORTCUT_KEY_PADDING;
         this.updateLayout();
      }
      
      private function clearCountdown() : void
      {
         App.utils.scheduler.cancelTask(this.update);
         this.abilityProgressFill.clearProgressTween();
      }
      
      private function update() : void
      {
         --this._timeRemainingSec;
         this.updateTimerTfText();
      }
      
      private function updateTimerTfText() : void
      {
         this.timerTf.text = this._dateTime.formatSecondsToString(this._timeRemainingSec);
         App.utils.commons.updateTextFieldSize(this.timerTf,true,false);
      }
      
      private function updateLayout() : void
      {
         this.secondaryActionShortcutKey.x = this.primaryActionShortcutKey.x + this.primaryActionShortcutKey.width + SECONDARY_ACTION_SHORTCUT_KEY_PADDING | 0;
         var _loc1_:KeyShortcut = !!this.secondaryActionShortcutKey.visible ? this.secondaryActionShortcutKey : this.primaryActionShortcutKey;
         var _loc2_:uint = !!this._isExtraSmallLayout ? uint(CLOCK_ICON_PADDING_EXTRA_SMALL) : uint(CLOCK_ICON_PADDING_MEDIUM);
         this.clockIcon.x = _loc1_.x + _loc1_.width + _loc2_ | 0;
         this.timerTf.x = this.clockIcon.x + this.clockIcon.width + TIMER_TF_PADDING | 0;
         this.abilityProgressFill.x = this.timerTf.x + this.timerTf.width + ABILITY_PROGRESS_FILL_PADDING | 0;
         if(this._isExtraSmallLayout)
         {
            this.abilityProgressFill.useExtraSmallLayout();
         }
         else
         {
            this.abilityProgressFill.useMediumLayout();
         }
         this.bg.width = this.abilityProgressFill.x + this.abilityProgressFill.width + PRIMARY_ACTION_SHORTCUT_KEY_PADDING;
      }
   }
}
