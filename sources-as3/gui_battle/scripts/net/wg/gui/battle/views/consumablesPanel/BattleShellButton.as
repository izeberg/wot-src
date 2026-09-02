package net.wg.gui.battle.views.consumablesPanel
{
   import flash.display.MovieClip;
   import flash.geom.ColorTransform;
   import flash.text.TextField;
   import net.wg.data.constants.InteractiveStates;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.KeyProps;
   import net.wg.data.constants.generated.BATTLE_ITEM_STATES;
   import net.wg.data.constants.generated.MECHANIC_SHELL_MODE_CONSTS;
   import net.wg.gui.battle.components.CoolDownTimer;
   import net.wg.gui.battle.components.buttons.BattleToolTipButton;
   import net.wg.gui.battle.views.consumablesPanel.VO.ConsumablesVO;
   import net.wg.gui.battle.views.consumablesPanel.constants.COLOR_STATES;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IBattleEquipmentButtonGlow;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IBattleShellButton;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.utils.FramesCollection;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import scaleform.gfx.TextFieldEx;
   
   public class BattleShellButton extends BattleToolTipButton implements IBattleShellButton
   {
      
      private static const FIRST_FRAME:int = 0;
      
      private static const START_FRAME:int = 51;
      
      private static const END_FRAME:int = 101;
      
      private static const END_RELOADING_FRAME:int = 142;
      
      private static const DEFAULT_TIME_COEF:Number = 1;
      
      private static const KEY_VALIDATION:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const QUANTITY_VALIDATION:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 3;
      
      private static const SELECTED_INDICATOR_VISIBILITY:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 4;
      
      private static const CRITICAL_QUANTITY_VALIDATION:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 5;
      
      private static const SPG_SHOT_RED_FRAME_LBL:String = "red";
      
      private static const SPG_SHOT_PURPLE_FRAME_LBL:String = "purple";
      
      private static const SPG_SHOT_RESULT_FALSE_STATE:int = 0;
      
      private static const CRITICAL_QUANTITY_ANIMATION_RATE:int = 200;
      
      private static const CRITICAL_QUANTITY_ICON_ALPHA:Number = 0.5;
      
      private static const SHELL_MODE_ON:String = "_on";
      
      private static const SHELL_MODE_OFF:String = "_off";
       
      
      public var shellModeIndicator:MovieClip = null;
      
      public var spgShotResultIndicator:MovieClip = null;
      
      public var quantityField:TextField = null;
      
      public var infinity:MovieClip = null;
      
      public var nextIndicator:MovieClip = null;
      
      public var selectedIndicator:MovieClip = null;
      
      public var iconLoader:UILoaderAlt = null;
      
      public var glow:IBattleEquipmentButtonGlow = null;
      
      private var _isCurrent:Boolean;
      
      private var _isNext:Boolean;
      
      private var _isReloading:Boolean;
      
      private var _bindSfKeyCode:Number;
      
      private var _quantity:int;
      
      private var _criticalQuantity:int = -1;
      
      private var _quantityAnimationEnabled:Boolean = false;
      
      private var _isEmpty:Boolean = true;
      
      private var _isAfterCoolDown:Boolean;
      
      private var _isSelectedIndicatorVisible:Boolean = false;
      
      private var _coolDownTimer:CoolDownTimer = null;
      
      private var _consumablesVO:ConsumablesVO;
      
      private var _spgShotResult:int = -1;
      
      private var _isColorBlindMode:Boolean = false;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      private var _shellMode:String = null;
      
      private var _shellModeIsActive:Boolean = false;
      
      private var _shellModeFrameHelper:FramesCollection = null;
      
      public function BattleShellButton()
      {
         this._consumablesVO = new ConsumablesVO();
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
         this._coolDownTimer = new CoolDownTimer(this);
         this._coolDownTimer.setFrames(START_FRAME,END_FRAME);
         this._isColorBlindMode = this._colorSchemeMgr.getIsColorBlindS();
         this.shellModeIndicator.visible = false;
         this.spgShotResultIndicator.visible = false;
         isAllowedToShowToolTipOnDisabledState = true;
         hideToolTipOnClickActions = false;
         addFrameScript(END_RELOADING_FRAME,this.reloadingEnd);
         if(this.quantityField)
         {
            TextFieldEx.setNoTranslate(this.quantityField,true);
         }
         if(this.infinity)
         {
            this.infinity.visible = false;
         }
         this._shellModeFrameHelper = new FramesCollection(this.shellModeIndicator);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.nextIndicator.visible = this._isNext;
         this._colorSchemeMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         var _loc1_:Boolean = isInvalid(QUANTITY_VALIDATION);
         var _loc2_:Boolean = isInvalid(SELECTED_INDICATOR_VISIBILITY);
         if(isInvalid(KEY_VALIDATION))
         {
            this.setBindKeyText();
         }
         if(this.quantityField && _loc1_)
         {
            this.quantityField.text = this._quantity.toString();
         }
         if(_loc2_)
         {
            this.selectedIndicator.visible = this._isSelectedIndicatorVisible;
         }
         if(_loc1_ || _loc2_ || isInvalid(CRITICAL_QUANTITY_VALIDATION))
         {
            this.startCriticalAnimation();
         }
      }
      
      override protected function onDispose() : void
      {
         this._colorSchemeMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
         this._colorSchemeMgr = null;
         addFrameScript(END_RELOADING_FRAME,null);
         this._coolDownTimer.dispose();
         this._coolDownTimer = null;
         this.stopCriticalAnimation();
         this.iconLoader.dispose();
         this.iconLoader = null;
         this.glow.dispose();
         this.glow = null;
         this.selectedIndicator = null;
         this.infinity = null;
         this.nextIndicator = null;
         this.quantityField = null;
         this.spgShotResultIndicator = null;
         this.shellModeIndicator = null;
         this._consumablesVO = null;
         this._shellModeFrameHelper.dispose();
         this._shellModeFrameHelper = null;
         super.onDispose();
      }
      
      public function clearColorTransform() : void
      {
         this.iconLoader.transform.colorTransform = COLOR_STATES.NORMAL_COLOR_TRANSFORM;
      }
      
      public function clearCoolDownTime() : void
      {
         this._isReloading = false;
         this._coolDownTimer.end();
         this.state = InteractiveStates.UP;
      }
      
      public function hideGlow() : void
      {
         this.glow.hideGlow();
      }
      
      public function onCoolDownComplete() : void
      {
      }
      
      public function setColorTransform(param1:ColorTransform) : void
      {
         if(param1)
         {
            this.iconLoader.transform.colorTransform = param1;
         }
      }
      
      public function setCoolDownPosAsPercent(param1:Number) : void
      {
         this._isReloading = true;
         if(param1 < 100)
         {
            this._isSelectedIndicatorVisible = false;
            invalidate(SELECTED_INDICATOR_VISIBILITY);
            this._coolDownTimer.setPositionAsPercent(param1);
         }
         else
         {
            this.setCoolDownTime(0,0,0);
         }
      }
      
      public function setCoolDownTime(param1:Number, param2:Number, param3:Number, param4:int = 1) : void
      {
         var _loc5_:Number = NaN;
         this._isAfterCoolDown = false;
         if(param1 > 0 && param2 != -1)
         {
            this._isSelectedIndicatorVisible = false;
            invalidate(SELECTED_INDICATOR_VISIBILITY);
         }
         if(param1 > 0)
         {
            _loc5_ = param3 / param2;
            this.state = BATTLE_ITEM_STATES.COOLDOWN;
            this._isReloading = true;
            this._coolDownTimer.start(param1,this,(END_FRAME - START_FRAME) * _loc5_,DEFAULT_TIME_COEF);
         }
         else
         {
            this._coolDownTimer.end();
            if(param1 == 0 && this._isReloading)
            {
               this._isReloading = false;
               this.state = BATTLE_ITEM_STATES.RELOADED;
               this._isAfterCoolDown = true;
            }
            else
            {
               this._coolDownTimer.moveToFrame(FIRST_FRAME);
            }
         }
      }
      
      public function setCurrent(param1:Boolean, param2:Boolean = false) : void
      {
         if(param2 || param1 != this._isCurrent)
         {
            this._isCurrent = param1;
            if(this.selectedIndicator)
            {
               if(param1)
               {
                  this._isSelectedIndicatorVisible = true;
                  this.selectedIndicator.gotoAndPlay(BATTLE_ITEM_STATES.SHOW);
               }
               else
               {
                  this._isSelectedIndicatorVisible = false;
                  this.selectedIndicator.gotoAndStop(BATTLE_ITEM_STATES.NORMAL);
                  this._isAfterCoolDown = false;
                  this.state = InteractiveStates.UP;
               }
               invalidate(SELECTED_INDICATOR_VISIBILITY);
            }
         }
      }
      
      public function setEmpty(param1:Boolean, param2:Boolean = false) : void
      {
         if(!param2 && this._isEmpty == param1)
         {
            return;
         }
         this._isEmpty = param1;
         if(param1)
         {
            this.clearCoolDownTime();
            this.icon = this._consumablesVO.noShellIconPath;
            enabled = false;
            this.state = InteractiveStates.EMPTY_UP;
         }
         else
         {
            this.icon = this._consumablesVO.shellIconPath;
            enabled = true;
            this.state = InteractiveStates.UP;
         }
      }
      
      public function setInfinity(param1:Boolean = false) : void
      {
         if(this.infinity)
         {
            this.infinity.visible = param1;
            this.quantityField.visible = !param1;
         }
      }
      
      public function setNext(param1:Boolean, param2:Boolean = false, param3:Boolean = true) : void
      {
         var _loc4_:Boolean = false;
         var _loc5_:Boolean = false;
         if(param2 || param1 != this._isNext)
         {
            _loc4_ = param1 == this._isNext;
            this._isNext = param1;
            if(this.nextIndicator && !this._isCurrent)
            {
               if(this._isEmpty || !param1)
               {
                  this.nextIndicator.visible = false;
                  this.nextIndicator.stop();
               }
               else
               {
                  this.nextIndicator.visible = true;
                  _loc5_ = param3 && !(this._shellModeIsActive && MECHANIC_SHELL_MODE_CONSTS.SUPPRESS_NEXT_SHELL_ANIMATION.indexOf(this._shellMode) != -1);
                  if(_loc5_)
                  {
                     if(!_loc4_ || this.nextIndicator.currentFrameLabel == BATTLE_ITEM_STATES.NORMAL)
                     {
                        this.nextIndicator.gotoAndPlay(BATTLE_ITEM_STATES.SHOW);
                     }
                  }
                  else
                  {
                     this.nextIndicator.gotoAndStop(BATTLE_ITEM_STATES.NORMAL);
                  }
               }
            }
         }
      }
      
      public function setQuantity(param1:int, param2:Boolean = false) : void
      {
         if(!param2 && this._quantity == param1)
         {
            return;
         }
         this._quantity = param1;
         if(this._quantity > 0)
         {
            this.setEmpty(false,param2);
         }
         else if(this._quantity == 0)
         {
            this.setEmpty(true,param2);
         }
         invalidate(QUANTITY_VALIDATION);
      }
      
      public function setShellMode(param1:String, param2:Boolean) : void
      {
         var _loc3_:String = null;
         this._shellMode = param1;
         this._shellModeIsActive = param2;
         if(this._isNext)
         {
            this.setNext(this._isNext,true,!this._shellModeIsActive);
         }
         if(param1)
         {
            _loc3_ = this.getShellModeFrame(param1,param2);
            if(this._shellModeFrameHelper.hasFrameLabel(_loc3_))
            {
               this.shellModeIndicator.visible = true;
               this.shellModeIndicator.gotoAndStop(_loc3_);
            }
            else
            {
               this.shellModeIndicator.visible = false;
            }
         }
         else
         {
            this.shellModeIndicator.visible = false;
         }
      }
      
      public function setSpgShotResult(param1:int) : void
      {
         if(param1 == SPG_SHOT_RESULT_FALSE_STATE)
         {
            this.spgShotResultIndicator.visible = true;
            this.spgShotResultIndicator.gotoAndStop(!!this._isColorBlindMode ? SPG_SHOT_PURPLE_FRAME_LBL : SPG_SHOT_RED_FRAME_LBL);
         }
         else
         {
            this.spgShotResultIndicator.visible = false;
         }
         this._spgShotResult = param1;
      }
      
      public function setTimerSnapshot(param1:int, param2:Boolean) : void
      {
      }
      
      public function showGlow(param1:int) : void
      {
         this.glow.showGlow(param1);
      }
      
      protected function setBindKeyText() : void
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
      
      protected function reloadingEnd() : void
      {
         this._isSelectedIndicatorVisible = this._quantity > 0;
         invalidate(SELECTED_INDICATOR_VISIBILITY);
         this.selectedIndicator.gotoAndStop(BATTLE_ITEM_STATES.NORMAL);
         this._isAfterCoolDown = false;
         validateNow();
      }
      
      protected function getQuantity() : int
      {
         return this._quantity;
      }
      
      protected function getCoolDownTimer() : CoolDownTimer
      {
         return this._coolDownTimer;
      }
      
      private function getShellModeFrame(param1:String, param2:Boolean) : String
      {
         return param1 + (!!param2 ? SHELL_MODE_ON : SHELL_MODE_OFF);
      }
      
      private function startCriticalAnimation() : void
      {
         if(this._quantity > 0 && this._quantity <= this._criticalQuantity)
         {
            if(this._isCurrent && !this._quantityAnimationEnabled)
            {
               this.changeIconAlpha();
               App.utils.scheduler.scheduleRepeatableTask(this.changeIconAlpha,CRITICAL_QUANTITY_ANIMATION_RATE,int.MAX_VALUE);
               this._quantityAnimationEnabled = true;
            }
            else if(!this._isCurrent && this._quantityAnimationEnabled)
            {
               this.stopCriticalAnimation();
            }
         }
         else if(this._quantityAnimationEnabled)
         {
            this.stopCriticalAnimation();
         }
      }
      
      private function changeIconAlpha() : void
      {
         this.iconLoader.alpha = this.iconLoader.alpha == 1 ? Number(CRITICAL_QUANTITY_ICON_ALPHA) : Number(1);
      }
      
      private function stopCriticalAnimation() : void
      {
         App.utils.scheduler.cancelTask(this.changeIconAlpha);
         this.iconLoader.alpha = 1;
         this._quantityAnimationEnabled = false;
      }
      
      override public function set state(param1:String) : void
      {
         if(!this._isReloading && !this._isAfterCoolDown)
         {
            super.state = param1;
         }
      }
      
      public function set activated(param1:Boolean) : void
      {
      }
      
      public function get consumablesVO() : ConsumablesVO
      {
         return this._consumablesVO;
      }
      
      public function set icon(param1:String) : void
      {
         this.iconLoader.source = param1;
      }
      
      public function get bindSfKeyCode() : Number
      {
         return this._bindSfKeyCode;
      }
      
      public function set key(param1:Number) : void
      {
         if(this._bindSfKeyCode == param1)
         {
            return;
         }
         this._bindSfKeyCode = param1;
         invalidate(KEY_VALIDATION);
      }
      
      public function set quantity(param1:int) : void
      {
         this.setQuantity(param1);
      }
      
      public function set criticalQuantity(param1:int) : void
      {
         if(this._criticalQuantity == param1)
         {
            return;
         }
         this._criticalQuantity = param1;
         invalidate(CRITICAL_QUANTITY_VALIDATION);
      }
      
      public function get reloading() : Boolean
      {
         return this._isReloading;
      }
      
      public function get coolDownCurrentFrame() : int
      {
         return this._coolDownTimer.currentFrame;
      }
      
      public function get empty() : Boolean
      {
         return this._isEmpty;
      }
      
      public function set empty(param1:Boolean) : void
      {
         this.setEmpty(param1);
      }
      
      public function set isReplay(param1:Boolean) : void
      {
      }
      
      protected function get isCurrent() : Boolean
      {
         return this._isCurrent;
      }
      
      protected function get isSelectedIndicatorVisible() : Boolean
      {
         return this._isSelectedIndicatorVisible;
      }
      
      private function onColorSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this._isColorBlindMode = this._colorSchemeMgr.getIsColorBlindS();
         this.setSpgShotResult(this._spgShotResult);
      }
   }
}
