package net.wg.gui.battle.views.consumablesPanel
{
   import fl.motion.easing.Linear;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.generated.CONSUMABLES_PANEL_SETTINGS;
   import net.wg.data.constants.generated.CONTEXT_HINT_STATE;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.utils.ICommons;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.events.ComponentEvent;
   import scaleform.clik.motion.Tween;
   
   public class ContextHint extends BattleUIComponent
   {
      
      private static const TEXT_FIELD_Y_OFFSET:int = -116;
      
      private static const TEXT_FIELD_NO_KEY_Y_OFFSET:int = -92;
      
      private static const KEY_ANIMATION_Y:int = -110;
      
      private static const KEY_STATIC_Y:int = -87;
      
      private static const Y_OFFSET:int = 16;
      
      private static const IDLE_STATE:String = "idle";
      
      private static const SHOW_STATE:String = "show";
      
      private static const SELECTED_STATE:String = "selected";
      
      private static const HIDE_STATE:String = "hide";
      
      private static const HIDE_GREEN_STATE:String = "hide_green";
      
      private static const HIDE_END_FRAME:uint = 172;
      
      private static const HIDE_GREEN_END_FRAME:uint = 187;
      
      private static const SHOW_FIRST_STEP_TWEEN_DURATION:uint = 85;
      
      private static const SHOW_SECOND_STEP_TWEEN_DURATION:uint = 300;
      
      private static const TWEEN_DELAY:uint = 100;
      
      private static const HIDE_TWEEN_DURATION:uint = 200;
      
      private static const HIDE_GREEN_TWEEN_DURATION:uint = 50;
       
      
      public var mainTfContainer:MovieClip = null;
      
      public var secondaryTfContainer:MovieClip = null;
      
      public var keyAnimation:MovieClip = null;
      
      public var keyStatic:MovieClip = null;
      
      private var _mainTextField:TextField = null;
      
      private var _secondaryTextField:TextField = null;
      
      private var _keyAnimationTextField:TextField = null;
      
      private var _keyStaticTextField:TextField = null;
      
      private var _label:String = null;
      
      private var _commons:ICommons;
      
      private var _tweens:Vector.<Tween>;
      
      private var _isAnimatedKeyVisible:Boolean = false;
      
      private var _isStaticKeyVisible:Boolean = false;
      
      private var _textFieldY:int = 0;
      
      public function ContextHint()
      {
         this._commons = App.utils.commons;
         this._tweens = new Vector.<Tween>();
         super();
         addFrameScript(HIDE_END_FRAME,this.onAnimationComplete);
         addFrameScript(HIDE_GREEN_END_FRAME,this.onAnimationComplete);
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.mainTfContainer.visible = false;
         this.secondaryTfContainer.visible = false;
         this.keyAnimation.visible = this._isAnimatedKeyVisible;
         this.keyAnimation.animPulse.visible = false;
         this.keyAnimation.animKeyBorder.visible = true;
         this.keyStatic.visible = this._isStaticKeyVisible;
         this._mainTextField = this.mainTfContainer.textField;
         this._secondaryTextField = this.secondaryTfContainer.textField;
         this._keyAnimationTextField = this.keyAnimation.textField;
         this._keyStaticTextField = this.keyStatic.textField;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseEnabled = mouseChildren = false;
      }
      
      override protected function onDispose() : void
      {
         addFrameScript(HIDE_END_FRAME,null);
         addFrameScript(HIDE_GREEN_END_FRAME,null);
         this.clearTweens();
         this._tweens = null;
         this._commons = null;
         this._mainTextField = null;
         this._secondaryTextField = null;
         this._keyAnimationTextField = null;
         this._keyStaticTextField = null;
         this.mainTfContainer = null;
         this.secondaryTfContainer = null;
         this.keyAnimation = null;
         this.keyStatic = null;
         super.onDispose();
      }
      
      public function hide(param1:int) : void
      {
         var _loc2_:uint = 0;
         switch(param1)
         {
            case CONSUMABLES_PANEL_SETTINGS.CONTEXT_HINT_ANIM_ID_NONE:
               _loc2_ = HIDE_TWEEN_DURATION;
               gotoAndPlay(HIDE_STATE);
               break;
            case CONSUMABLES_PANEL_SETTINGS.CONTEXT_HINT_ANIM_ID_GREEN:
               _loc2_ = HIDE_GREEN_TWEEN_DURATION;
               gotoAndPlay(HIDE_GREEN_STATE);
               break;
            default:
               _loc2_ = HIDE_GREEN_TWEEN_DURATION;
               gotoAndStop(IDLE_STATE);
         }
         this.clearTweens();
         this._tweens.push(new Tween(_loc2_,this.mainTfContainer,{
            "alpha":0,
            "y":this._textFieldY + Y_OFFSET
         },{"ease":Linear.easeIn}));
         this._tweens.push(new Tween(_loc2_,this.secondaryTfContainer,{
            "alpha":0,
            "y":this._textFieldY + Y_OFFSET
         },{"ease":Linear.easeIn}));
         var _loc3_:MovieClip = !!this._isAnimatedKeyVisible ? this.keyAnimation : this.keyStatic;
         var _loc4_:int = !!this._isAnimatedKeyVisible ? int(KEY_ANIMATION_Y) : int(KEY_STATIC_Y);
         this._tweens.push(new Tween(_loc2_,_loc3_,{
            "alpha":0,
            "y":_loc4_ + Y_OFFSET
         },{"ease":Linear.easeIn}));
      }
      
      public function setAnimatedKeyParams(param1:Boolean, param2:Boolean, param3:String) : void
      {
         this._isAnimatedKeyVisible = param1;
         this._isStaticKeyVisible = param2;
         this._keyAnimationTextField.text = param3;
         this._keyStaticTextField.text = param3;
      }
      
      public function setLabel(param1:String) : void
      {
         if(this._label != param1 && StringUtils.isNotEmpty(param1))
         {
            this._label = param1;
            this.updateLabel(this._label,this._mainTextField);
         }
      }
      
      public function setStateAndLabel(param1:String, param2:String = "") : void
      {
         if(param1 == CONTEXT_HINT_STATE.SELECTED)
         {
            gotoAndPlay(SELECTED_STATE);
            this.playLabelSwitchAnimation(param2);
            if(this.keyAnimation.visible)
            {
               this.keyAnimation.alpha = 1;
               this.keyAnimation.y = KEY_ANIMATION_Y;
            }
            if(this.keyStatic.visible)
            {
               this.keyStatic.alpha = 1;
               this.keyStatic.y = KEY_STATIC_Y;
            }
         }
      }
      
      public function show() : void
      {
         this.keyAnimation.alpha = 0;
         this.keyAnimation.visible = this._isAnimatedKeyVisible;
         this.keyStatic.alpha = 0;
         this.keyStatic.visible = this._isStaticKeyVisible;
         gotoAndPlay(SHOW_STATE);
         this.clearTweens();
         this.mainTfContainer.alpha = 0;
         this.mainTfContainer.visible = true;
         this.secondaryTfContainer.alpha = 0;
         this.secondaryTfContainer.visible = true;
         this._textFieldY = (!!this._isAnimatedKeyVisible ? TEXT_FIELD_Y_OFFSET : TEXT_FIELD_NO_KEY_Y_OFFSET) - this._mainTextField.height | 0;
         this.mainTfContainer.y = this._textFieldY - Y_OFFSET;
         this._tweens.push(new Tween(SHOW_SECOND_STEP_TWEEN_DURATION,this.mainTfContainer,{
            "alpha":1,
            "y":this._textFieldY
         },{"ease":Linear.easeOut}));
         var _loc1_:MovieClip = !!this._isAnimatedKeyVisible ? this.keyAnimation : this.keyStatic;
         var _loc2_:int = !!this._isAnimatedKeyVisible ? int(KEY_ANIMATION_Y) : int(KEY_STATIC_Y);
         this.keyAnimation.y = _loc2_ + Y_OFFSET;
         this._tweens.push(new Tween(SHOW_FIRST_STEP_TWEEN_DURATION,_loc1_,{
            "alpha":1,
            "y":_loc2_
         },{"ease":Linear.easeOut}));
      }
      
      private function playLabelSwitchAnimation(param1:String) : void
      {
         this.clearTweens();
         this.updateLabel(param1,this._secondaryTextField);
         this.secondaryTfContainer.alpha = 0;
         this.secondaryTfContainer.visible = true;
         this.secondaryTfContainer.y = (!!this._isAnimatedKeyVisible ? TEXT_FIELD_Y_OFFSET : TEXT_FIELD_NO_KEY_Y_OFFSET) - this._secondaryTextField.height | 0;
         this._tweens.push(new Tween(SHOW_SECOND_STEP_TWEEN_DURATION,this.mainTfContainer,{"alpha":0},{"ease":Linear.easeOut}));
         this._tweens.push(new Tween(SHOW_SECOND_STEP_TWEEN_DURATION,this.secondaryTfContainer,{"alpha":1},{
            "delay":TWEEN_DELAY,
            "ease":Linear.easeOut
         }));
      }
      
      private function updateLabel(param1:String, param2:TextField) : void
      {
         param2.text = param1;
         this._commons.updateTextFieldSize(param2,false,true);
      }
      
      private function clearTweens() : void
      {
         var _loc1_:Tween = null;
         if(this._tweens != null && this._tweens.length > 0)
         {
            for each(_loc1_ in this._tweens)
            {
               _loc1_.dispose();
               _loc1_ = null;
            }
            this._tweens.length = 0;
         }
      }
      
      private function onAnimationComplete() : void
      {
         gotoAndStop(IDLE_STATE);
         this.mainTfContainer.visible = false;
         this.secondaryTfContainer.visible = false;
         this.keyAnimation.visible = false;
         this.keyStatic.visible = false;
         dispatchEvent(new ComponentEvent(ComponentEvent.HIDE));
      }
      
      public function set usePulseAnimation(param1:Boolean) : void
      {
         this.keyAnimation.animPulse.visible = param1;
         this.keyAnimation.animKeyBorder.visible = !param1;
      }
   }
}
