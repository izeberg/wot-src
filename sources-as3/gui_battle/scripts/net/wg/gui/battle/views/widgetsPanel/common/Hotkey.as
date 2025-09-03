package net.wg.gui.battle.views.widgetsPanel.common
{
   import fl.motion.easing.Cubic;
   import fl.motion.easing.Linear;
   import fl.transitions.easing.Elastic;
   import flash.display.BlendMode;
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.utils.getTimer;
   import net.wg.data.constants.KeyProps;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANIC_WIDGET_HOTKEY_CONST;
   import net.wg.gui.battle.views.widgetsPanel.vo.HotKeyVo;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.motion.Tween;
   
   public class Hotkey extends MovieClip implements IDisposable
   {
      
      private static const ADDITIONAL_TEXT_WIDTH:int = 4;
      
      private static const WIDTH_ADD:int = 16;
      
      private static const LABEL_X:int = 8;
      
      private static const MIN_BG_W:int = 28;
      
      private static const INVALID_KAY_NAME:String = "- -";
      
      private static const MIN_FILL_HEIGHT:int = 1;
      
      private static const FILL_HEIGHT:int = 20;
      
      private static const FILLED_MASK_WIDTH_CORRECTION:int = -6;
      
      private static const START_SHAKE_DURATION:int = 60;
      
      private static const CONTINUE_SHAKE_DURATION:int = 600;
      
      private static const SHAKE_MAX_SHIFT_X:int = -4;
       
      
      public var bg:Sprite;
      
      public var label:TextField;
      
      public var lid:MovieClip;
      
      public var maskMc:HotkeyMask;
      
      public var fillMaskMc:MovieClip;
      
      public var filledBg:HotkeyFilledBgContainer;
      
      public var filledLabel:TextField;
      
      private var _disposed:Boolean = false;
      
      private var _isValid:Boolean = false;
      
      private var _isLongKey:Boolean = false;
      
      private var _state:String = "normal";
      
      private var _label:String = "";
      
      private var _command:String = "";
      
      private var _visibilityTween:Tween = null;
      
      private var _fillTween:Tween = null;
      
      private var _fillStartTime:int = 0;
      
      private var _shakeTween:Tween = null;
      
      private var _x:int = 0;
      
      public function Hotkey()
      {
         super();
         stop();
         this.label.autoSize = TextFieldAutoSize.LEFT;
         this.filledLabel.autoSize = TextFieldAutoSize.LEFT;
         this.maskMc.visible = false;
         this.renewBlendMod();
      }
      
      public final function dispose() : void
      {
         this.removeShake();
         this.removeVisibilityTween();
         this.removeFillTween();
         stop();
         this.label = null;
         this.bg.mask = null;
         this.bg = null;
         this.lid = null;
         this.fillMaskMc = null;
         this.filledLabel = null;
         this.filledBg.dispose();
         this.filledBg = null;
         this.maskMc.dispose();
         this.maskMc = null;
         this._disposed = true;
      }
      
      public function hide(param1:Number) : void
      {
         if(this._visibilityTween != null && this.alpha != Values.DEFAULT_ALPHA)
         {
            return;
         }
         this.removeVisibilityTween();
         if(param1 != Values.ZERO)
         {
            this._visibilityTween = new Tween(param1,this,{"alpha":Values.ZERO},{
               "ease":Cubic.easeIn,
               "onComplete":this.onHideComplete
            });
         }
         else
         {
            this.alpha = Values.ZERO;
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function onPress(param1:Number) : void
      {
         this.removeFillTween();
         if(param1 == 0)
         {
            this.fillMaskMc.height = FILL_HEIGHT;
         }
         else
         {
            this._fillTween = new Tween(param1,this.fillMaskMc,{"height":FILL_HEIGHT},{
               "ease":Linear.easeNone,
               "onComplete":this.onFillComplete
            });
            this._fillStartTime = getTimer();
         }
      }
      
      public function onRelease() : void
      {
         this.removeFillTween();
         if(this._fillStartTime != Values.ZERO)
         {
            this._fillTween = new Tween(getTimer() - this._fillStartTime >> 1,this.fillMaskMc,{"height":MIN_FILL_HEIGHT},{
               "ease":Cubic.easeOut,
               "onComplete":this.onFillComplete
            });
         }
         else
         {
            this.fillMaskMc.height = MIN_FILL_HEIGHT;
         }
         this._fillStartTime = Values.ZERO;
      }
      
      public function setPosition(param1:int, param2:int) : void
      {
         this.x = param1;
         this.y = param2;
         this._x = param1;
      }
      
      public function setState(param1:String) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         this.invalidateAll();
      }
      
      public function setup(param1:HotKeyVo) : void
      {
         var _loc2_:uint = param1.keyCode;
         this._isValid = _loc2_ != KeyProps.KEY_NONE;
         this._label = App.utils.commons.keyToString(_loc2_).keyName;
         this._isLongKey = param1.isLong;
         this._command = param1.command;
         this.filledBg.isLong = this._isLongKey;
         this.invalidateAll();
      }
      
      public function shake() : void
      {
         this.removeShake();
         this._shakeTween = new Tween(START_SHAKE_DURATION,this,{"x":this._x + SHAKE_MAX_SHIFT_X},{
            "ease":Cubic.easeOut,
            "onComplete":this.onStartShakeComplete
         });
      }
      
      public function show() : void
      {
         this.removeVisibilityTween();
         this.fillMaskMc.height = MIN_FILL_HEIGHT;
         this.alpha = Values.DEFAULT_ALPHA;
      }
      
      private function renewBlendMod() : void
      {
         this.bg.blendMode = BlendMode.SCREEN;
         this.label.blendMode = BlendMode.SCREEN;
         this.filledBg.blendMode = BlendMode.SCREEN;
         this.lid.blendMode = BlendMode.SCREEN;
      }
      
      private function removeVisibilityTween() : void
      {
         if(this._visibilityTween)
         {
            this._visibilityTween.paused = true;
            this._visibilityTween.onComplete = null;
            this._visibilityTween.dispose();
            this._visibilityTween = null;
         }
      }
      
      private function removeFillTween() : void
      {
         if(this._fillTween)
         {
            this._fillTween.paused = true;
            this._fillTween.onComplete = null;
            this._fillTween.dispose();
            this._fillTween = null;
         }
      }
      
      private function invalidateAll() : void
      {
         this.updateState();
         this.updateLabel();
         this.updateLayout();
      }
      
      private function updateState() : void
      {
         if(StringUtils.isEmpty(this._state))
         {
            return;
         }
         var _loc1_:String = !!this._isValid ? this._state : MECHANIC_WIDGET_HOTKEY_CONST.ALERT;
         this.lid.visible = this._isLongKey;
         this.bg.mask = null;
         gotoAndStop(_loc1_);
         this.lid.gotoAndStop(_loc1_);
         this.filledBg.setState(_loc1_);
         this.maskMc.visible = this._isLongKey;
         this.bg.mask = !!this._isLongKey ? this.maskMc : null;
         this.renewBlendMod();
      }
      
      private function updateLabel() : void
      {
         var _loc1_:String = !!this._isValid ? this._label : INVALID_KAY_NAME;
         this.label.text = _loc1_;
         this.filledLabel.text = _loc1_;
      }
      
      private function updateLayout() : void
      {
         var _loc1_:Number = this.label.textWidth + ADDITIONAL_TEXT_WIDTH >> 0;
         this.label.width = _loc1_;
         this.filledLabel.width = _loc1_;
         if(_loc1_ <= MIN_BG_W)
         {
            this.bg.width = MIN_BG_W;
            this.label.x = MIN_BG_W - _loc1_ >> 1;
         }
         else
         {
            this.bg.width = _loc1_ + WIDTH_ADD;
            this.label.x = LABEL_X;
         }
         this.filledBg.setWidth(this.bg.width);
         this.fillMaskMc.width = this.bg.width - this.fillMaskMc.x + FILLED_MASK_WIDTH_CORRECTION;
         this.filledLabel.x = this.label.x;
         if(this._isLongKey)
         {
            this.maskMc.setSize(this.bg.width);
            this.lid.x = this.bg.width >> 1;
         }
      }
      
      private function onHideComplete() : void
      {
         this.removeVisibilityTween();
      }
      
      private function onFillComplete() : void
      {
         this.removeFillTween();
      }
      
      private function onStartShakeComplete() : void
      {
         this.removeShake();
         this._shakeTween = new Tween(CONTINUE_SHAKE_DURATION,this,{"x":this._x},{
            "ease":Elastic.easeOut,
            "onComplete":this.onShakeComplete
         });
      }
      
      private function onShakeComplete() : void
      {
         this.removeShake();
      }
      
      private function removeShake() : void
      {
         if(this._shakeTween)
         {
            this._shakeTween.paused = true;
            this._shakeTween.onComplete = null;
            this._shakeTween.dispose();
            this._shakeTween = null;
         }
      }
      
      override public function get width() : Number
      {
         return this.bg.width;
      }
      
      override public function get height() : Number
      {
         return this.bg.height;
      }
      
      public function get command() : String
      {
         return this._command;
      }
      
      public function get isLongKey() : Boolean
      {
         return this._isLongKey;
      }
      
      public function get isInFillTween() : Boolean
      {
         return this._fillTween != null;
      }
   }
}
