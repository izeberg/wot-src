package net.wg.historical_battles.gui.battle.views.consumablesPanel
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.InteractiveStates;
   import net.wg.data.constants.Time;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.buttons.interfaces.IClickButtonHandler;
   import net.wg.historical_battles.gui.battle.constants.HB_EQUIPMENT_STAGES;
   
   public class HBAbilityButton extends HBEquipmentButtonBase
   {
      
      private static const INTERACTIVE_STATES:Vector.<int> = new <int>[HB_EQUIPMENT_STAGES.READY,HB_EQUIPMENT_STAGES.PREPARING];
      
      private static const GLOW_GREEN:String = "green";
      
      private static const GLOW_RED:String = "red";
      
      private static const GLOW_NONE:String = "none";
       
      
      public var cooldownTimerTf:TextField = null;
      
      public var timeLeftTf:TextField = null;
      
      public var counterHighlight:MovieClip = null;
      
      private var _stage:int = -1;
      
      private var _currentCooldownTf:TextField;
      
      private var _clickButtonHandler:IClickButtonHandler = null;
      
      public function HBAbilityButton()
      {
         super();
      }
      
      override public function addClickCallBack(param1:IClickButtonHandler) : void
      {
         super.addClickCallBack(param1);
         this._clickButtonHandler = param1;
      }
      
      override protected function onDispose() : void
      {
         this._currentCooldownTf = null;
         this._clickButtonHandler = null;
         this.timeLeftTf = null;
         this.counterHighlight = null;
         this.cooldownTimerTf = null;
         super.onDispose();
      }
      
      override protected function drawCountdownText(param1:int) : void
      {
         if(this._currentCooldownTf == null)
         {
            return;
         }
         this._currentCooldownTf.text = param1 > 0 ? param1.toString() : Values.EMPTY_STR;
      }
      
      override protected function startCooldown(param1:Number, param2:Number, param3:Number) : void
      {
         var _loc5_:Number = NaN;
         var _loc4_:Boolean = this._stage == HB_EQUIPMENT_STAGES.COOLDOWN;
         if(_loc4_)
         {
            this._currentCooldownTf = this.cooldownTimerTf;
            this.counterHighlight.gotoAndStop(GLOW_RED);
         }
         else
         {
            this._currentCooldownTf = this.timeLeftTf;
            this.counterHighlight.gotoAndStop(GLOW_GREEN);
         }
         if(_baseDisposed)
         {
            return;
         }
         if(!_isReplay)
         {
            _scheduler.scheduleRepeatableTask(updateCountdownText,Time.MILLISECOND_IN_SECOND,param1);
            if(_loc4_)
            {
               _loc5_ = param2 / param3;
               _coolDownTimer.start(param1,this,Math.round((_cooldownEndFrame - COOLDOWN_START_FRAME) * _loc5_),TIME_SPEED,false,false);
               cooldownMc.visible = true;
            }
         }
      }
      
      override protected function endCountdown() : void
      {
         super.endCountdown();
         if(this._currentCooldownTf)
         {
            this._currentCooldownTf.text = Values.EMPTY_STR;
            this._currentCooldownTf = null;
         }
         this.counterHighlight.gotoAndStop(GLOW_NONE);
      }
      
      override protected function resolveIconTransparency() : void
      {
      }
      
      override protected function setListeners() : void
      {
         super.setListeners();
         addEventListener(MouseEvent.CLICK,this.onMouseClickHandler,false,1,true);
         addEventListener(MouseEvent.DOUBLE_CLICK,this.onMouseClickHandler,false,1,true);
      }
      
      override protected function removeListeners() : void
      {
         super.setListeners();
         removeEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         removeEventListener(MouseEvent.DOUBLE_CLICK,this.onMouseClickHandler);
      }
      
      public function setStage(param1:int) : void
      {
         if(this._stage == param1)
         {
            return;
         }
         this._stage = param1;
         state = HB_EQUIPMENT_STAGES.getState(this._stage);
         buttonMode = this.enabled = INTERACTIVE_STATES.indexOf(param1) != -1;
      }
      
      override public function set enabled(param1:Boolean) : void
      {
         super.enabled = param1;
         if(!param1)
         {
            mouseEnabled = true;
         }
      }
      
      private function onMouseClickHandler(param1:MouseEvent) : void
      {
         param1.stopImmediatePropagation();
         if(!_isEnabled && this._clickButtonHandler)
         {
            this._clickButtonHandler.onButtonClick(this);
            return;
         }
         throwLifeCycleException();
         invokeReleaseActions();
         if(!enabled)
         {
            return;
         }
         if(isClickAllowed(param1))
         {
            state = InteractiveStates.RELEASE;
            if(this._clickButtonHandler)
            {
               this._clickButtonHandler.onButtonClick(this);
            }
         }
      }
   }
}
