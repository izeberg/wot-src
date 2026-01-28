package net.wg.gui.battle.views.consumablesPanel
{
   import fl.motion.easing.Linear;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.generated.CONSUMABLES_PANEL_SETTINGS;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.utils.ICommons;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.events.ComponentEvent;
   import scaleform.clik.motion.Tween;
   
   public class ContextHint extends BattleUIComponent
   {
      
      private static const TEXT_FIELD_Y_OFFSET:int = -116;
      
      private static const TEXT_FIELD_NO_KEY_Y_OFFSET:int = -92;
      
      private static const KEY_Y:int = -110;
      
      private static const Y_OFFSET:int = 16;
      
      private static const IDLE_STATE:String = "idle";
      
      private static const SHOW_STATE:String = "show";
      
      private static const HIDE_STATE:String = "hide";
      
      private static const HIDE_GREEN_STATE:String = "hide_green";
      
      private static const HIDE_END_FRAME:uint = 79;
      
      private static const HIDE_GREEN_END_FRAME:uint = 95;
      
      private static const SHOW_FIRST_STEP_TWEEN_DURATION:uint = 85;
      
      private static const SHOW_SECOND_STEP_TWEEN_DURATION:uint = 300;
      
      private static const HIDE_TWEEN_DURATION:uint = 200;
      
      private static const HIDE_GREEN_TWEEN_DURATION:uint = 50;
       
      
      public var tfContainer:MovieClip = null;
      
      public var key:MovieClip = null;
      
      private var _textField:TextField = null;
      
      private var _keyTextField:TextField = null;
      
      private var _label:String = null;
      
      private var _commons:ICommons;
      
      private var _tweens:Vector.<Tween>;
      
      private var _keyVisible:Boolean = false;
      
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
         this.tfContainer.visible = false;
         this.key.visible = false;
         this._textField = this.tfContainer.textField;
         this._keyTextField = this.key.textField;
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
         this._textField = null;
         this._keyTextField = null;
         this.tfContainer = null;
         this.key = null;
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
         this._tweens.push(new Tween(_loc2_,this.tfContainer,{
            "alpha":0,
            "y":this._textFieldY + Y_OFFSET
         },{"ease":Linear.easeIn}));
         if(this._keyVisible)
         {
            this._tweens.push(new Tween(_loc2_,this.key,{
               "alpha":0,
               "y":KEY_Y + Y_OFFSET
            },{"ease":Linear.easeIn}));
         }
      }
      
      public function setKeyParams(param1:Boolean, param2:String) : void
      {
         this._keyVisible = param1;
         if(param1)
         {
            this._keyTextField.text = param2;
         }
      }
      
      public function setLabel(param1:String) : void
      {
         if(this._label != param1 && StringUtils.isNotEmpty(param1))
         {
            this._label = param1;
            this._textField.text = this._label;
            this._commons.updateTextFieldSize(this._textField,false,true);
         }
      }
      
      public function show() : void
      {
         this.tfContainer.alpha = 0;
         this.tfContainer.visible = true;
         this.key.alpha = 0;
         this.key.visible = this._keyVisible;
         gotoAndPlay(SHOW_STATE);
         this.clearTweens();
         this._textFieldY = (!!this._keyVisible ? TEXT_FIELD_Y_OFFSET : TEXT_FIELD_NO_KEY_Y_OFFSET) - this._textField.height | 0;
         this.tfContainer.y = this._textFieldY - Y_OFFSET;
         this._tweens.push(new Tween(SHOW_SECOND_STEP_TWEEN_DURATION,this.tfContainer,{
            "alpha":1,
            "y":this._textFieldY
         },{"ease":Linear.easeOut}));
         if(this._keyVisible)
         {
            this.key.y = KEY_Y + Y_OFFSET;
            this._tweens.push(new Tween(SHOW_FIRST_STEP_TWEEN_DURATION,this.key,{
               "alpha":1,
               "y":KEY_Y
            },{"ease":Linear.easeOut}));
         }
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
         this.tfContainer.visible = false;
         this.key.visible = false;
         dispatchEvent(new ComponentEvent(ComponentEvent.HIDE));
      }
   }
}
