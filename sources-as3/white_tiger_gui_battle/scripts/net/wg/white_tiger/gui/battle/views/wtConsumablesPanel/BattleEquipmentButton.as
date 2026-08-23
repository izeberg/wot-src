package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel
{
   import flash.display.MovieClip;
   import flash.geom.ColorTransform;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.KeyProps;
   import net.wg.data.constants.Time;
   import net.wg.gui.battle.components.CoolDownTimer;
   import net.wg.gui.battle.components.interfaces.ICoolDownCompleteHandler;
   import net.wg.gui.battle.views.consumablesPanel.constants.COLOR_STATES;
   import net.wg.utils.IScheduler;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.components.EquipmentButtonBackground;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.constants.WT_ABILITY_STATES;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces.IWTConsumablesButton;
   
   public class BattleEquipmentButton extends BaseConsumablesButton implements IWTConsumablesButton, ICoolDownCompleteHandler
   {
      
      private static const KEY_VALIDATION:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 3;
      
      private static const COOLDOWN_START_FRAME:int = 1;
      
      private static const COOLDOWN_END_FRAME:int = 49;
      
      private static const DEFAULT_TIME_COEF:int = 1;
      
      private static const COOLDOWN_COUNTER_BG_ORANGE:String = "orange";
      
      private static const COOLDOWN_COUNTER_BG_BLUE:String = "blue";
      
      private static const MAX_CHARGE_PROGRESS:int = 100;
      
      private static const ORANGE_PROGRESS_TEXT_COLOR:uint = 16768409;
      
      private static const BLUE_PROGRESS_TEXT_COLOR:uint = 15921911;
      
      private static const BLUE_COOLDOWN_COLOR_TRANSFORM:ColorTransform = new ColorTransform(1,1,1,1,-90,-10,70,0);
       
      
      public var progressBar:MovieClip = null;
      
      public var hit:MovieClip = null;
      
      public var cooldownTimerTf:TextField = null;
      
      public var counterBg:MovieClip = null;
      
      public var glow:BattleEquipmentButtonGlow = null;
      
      public var cooldownMc:MovieClip = null;
      
      public var background:EquipmentButtonBackground = null;
      
      private var _bindSfKeyCode:Number;
      
      private var _coolDownTimer:CoolDownTimer = null;
      
      private var _chargeProgress:int;
      
      private var _scheduler:IScheduler;
      
      private var _cooldownTime:int;
      
      private var _isLocked:Boolean = false;
      
      public function BattleEquipmentButton()
      {
         this._scheduler = App.utils.scheduler;
         super();
         this._coolDownTimer = new CoolDownTimer(this.cooldownMc);
      }
      
      override public function wtShowActive(param1:int) : void
      {
         if(wtState != WT_ABILITY_STATES.ACTIVE)
         {
            wtState = WT_ABILITY_STATES.ACTIVE;
            this._cooldownTime = param1;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.progressBar.visible = false;
         this.cooldownMc.visible = false;
         this.hit.mouseEnabled = false;
         hitArea = this.hit;
         this._coolDownTimer.setFrames(COOLDOWN_START_FRAME,COOLDOWN_END_FRAME);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(KEY_VALIDATION))
         {
            this.setBindKeyText();
         }
      }
      
      override protected function updateWtState() : void
      {
         var _loc1_:Boolean = wtState == WT_ABILITY_STATES.COOLDOWN && this._cooldownTime > 0;
         var _loc2_:Boolean = wtState == WT_ABILITY_STATES.ACTIVE && this._cooldownTime > 0;
         this._scheduler.cancelTask(this.intervalRun);
         if(_loc1_ || _loc2_)
         {
            this._scheduler.scheduleRepeatableTask(this.intervalRun,Time.SECOND,this._cooldownTime);
         }
         if(this._isLocked)
         {
            buttonMode = useHandCursor = false;
            this.background.updateWtState(WT_ABILITY_STATES.DISABLED);
            this.setIconColorTransform(COLOR_STATES.DARK_COLOR_TRANSFORM);
            this.glow.visible = false;
            this.cooldownMc.visible = false;
            this.cooldownTimerTf.visible = this.counterBg.visible = false;
            this.progressBar.visible = false;
            return;
         }
         var _loc3_:Boolean = wtState == WT_ABILITY_STATES.DISABLED;
         var _loc4_:Boolean = wtState == WT_ABILITY_STATES.CHARGE;
         var _loc5_:Boolean = wtState == WT_ABILITY_STATES.READY;
         var _loc6_:Boolean = wtState == WT_ABILITY_STATES.DEPLOYING || wtState == WT_ABILITY_STATES.ACTIVE && this._cooldownTime <= 0;
         var _loc7_:Boolean = wtState == WT_ABILITY_STATES.PREPARING;
         useHandCursor = buttonMode = _loc5_;
         this.background.updateWtState(wtState);
         if(_loc3_ || _loc1_ || _loc4_ || _loc7_)
         {
            this.setIconColorTransform(COLOR_STATES.DARK_COLOR_TRANSFORM);
         }
         else
         {
            this.setIconColorTransform(COLOR_STATES.NORMAL_COLOR_TRANSFORM);
         }
         this.glow.visible = !_loc3_;
         this.cooldownMc.visible = _loc1_ || _loc4_ || _loc2_ || _loc6_;
         this.cooldownTimerTf.visible = this.counterBg.visible = _loc1_ || _loc4_ || _loc2_;
         this.progressBar.visible = _loc4_;
         if(_loc5_)
         {
            this.glow.glowBlue();
         }
         else if(!_loc3_)
         {
            this.glow.hideGlow();
         }
         this._coolDownTimer.end();
         if(_loc1_ || _loc4_)
         {
            this.cooldownMc.transform.colorTransform = COLOR_STATES.ORANGE_COOLDOWN_COLOR_TRANSFORM;
            this.counterBg.gotoAndStop(COOLDOWN_COUNTER_BG_ORANGE);
            this.cooldownTimerTf.textColor = ORANGE_PROGRESS_TEXT_COLOR;
         }
         if(_loc1_)
         {
            this.cooldownTimerTf.text = this._cooldownTime.toString();
            this._coolDownTimer.start(this._cooldownTime,this,0,DEFAULT_TIME_COEF);
         }
         if(_loc4_)
         {
            this.progressBar.gotoAndStop(this._chargeProgress);
            this.cooldownTimerTf.text = this._chargeProgress + "%";
            this._coolDownTimer.setPositionAsPercent(this._chargeProgress);
         }
         if(_loc6_)
         {
            this.cooldownMc.transform.colorTransform = BLUE_COOLDOWN_COLOR_TRANSFORM;
            this._coolDownTimer.setPositionAsPercent(MAX_CHARGE_PROGRESS - 1);
         }
         if(_loc2_)
         {
            this.cooldownMc.transform.colorTransform = BLUE_COOLDOWN_COLOR_TRANSFORM;
            this.counterBg.gotoAndStop(COOLDOWN_COUNTER_BG_BLUE);
            this.cooldownTimerTf.textColor = BLUE_PROGRESS_TEXT_COLOR;
            this.cooldownTimerTf.text = this._cooldownTime.toString();
            this._coolDownTimer.start(this._cooldownTime,this,COOLDOWN_END_FRAME - 1,DEFAULT_TIME_COEF,true);
         }
      }
      
      override protected function onDispose() : void
      {
         this._scheduler.cancelTask(this.intervalRun);
         this._scheduler = null;
         this.glow.dispose();
         this.glow = null;
         this._coolDownTimer.dispose();
         this._coolDownTimer = null;
         this.progressBar = null;
         this.hit = null;
         this.cooldownTimerTf = null;
         this.counterBg = null;
         this.cooldownMc = null;
         this.background = null;
         super.onDispose();
      }
      
      public function onCoolDownComplete() : void
      {
      }
      
      public function wtSetCharge(param1:int) : void
      {
         if(wtState != WT_ABILITY_STATES.CHARGE || this._chargeProgress != param1)
         {
            wtState = WT_ABILITY_STATES.CHARGE;
            this._chargeProgress = param1;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      public function wtSetLocked(param1:Boolean) : void
      {
         if(this._isLocked != param1)
         {
            this._isLocked = param1;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      public function wtShowCooldown(param1:int) : void
      {
         if(wtState != WT_ABILITY_STATES.COOLDOWN)
         {
            wtState = WT_ABILITY_STATES.COOLDOWN;
            this._cooldownTime = param1;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      public function wtShowDeploying() : void
      {
         if(wtState != WT_ABILITY_STATES.DEPLOYING)
         {
            wtState = WT_ABILITY_STATES.DEPLOYING;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      public function wtShowPreparing() : void
      {
         if(wtState != WT_ABILITY_STATES.PREPARING)
         {
            wtState = WT_ABILITY_STATES.PREPARING;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      public function wtShowReady() : void
      {
         if(wtState != WT_ABILITY_STATES.READY)
         {
            wtState = WT_ABILITY_STATES.READY;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      private function setBindKeyText() : void
      {
         if(this._bindSfKeyCode == KeyProps.KEY_NONE)
         {
            this.glow.setBindKeyText(App.utils.locale.makeString(READABLE_KEY_NAMES.KEY_NONE_ALT));
         }
         else
         {
            this.glow.setBindKeyText(App.utils.commons.keyToString(this._bindSfKeyCode).keyName);
         }
      }
      
      private function intervalRun() : void
      {
         this._cooldownTime -= 1;
         this.cooldownTimerTf.text = this._cooldownTime.toString();
      }
      
      private function setIconColorTransform(param1:ColorTransform) : void
      {
         iconLoader.transform.colorTransform = param1;
      }
      
      override public function set key(param1:Number) : void
      {
         if(this._bindSfKeyCode == param1)
         {
            return;
         }
         this._bindSfKeyCode = param1;
         invalidate(KEY_VALIDATION);
      }
   }
}
