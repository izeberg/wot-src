package net.wg.gui.lobby.vehicleCustomization.controls
{
   import flash.display.FrameLabel;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.SoundTypes;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CUSTOMIZATION_ALIASES;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationInnerEntryPointVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationSoundEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.gfx.MouseEventEx;
   
   public class C11nInnerEntryPoint extends UIComponentEx
   {
      
      private static const STATE_UP:String = "up";
      
      private static const STATE_OVER:String = "over";
      
      private static const STATE_OUT:String = "out";
      
      private static const STATE_SELECTED:String = "selected";
      
      protected static const STATE_PREFIX_SMALL:String = "small_";
      
      private static const TF_WIDTH_SMALL:uint = 130;
      
      private static const TF_WIDTH_BIG:uint = 160;
      
      private static const TF_POS_X_SMALL:uint = 85;
      
      private static const TF_POS_X_BIG:uint = 0;
      
      private static const TF_POS_Y_CENTER_SMALL:uint = 42;
      
      private static const TF_POS_Y_CENTER_BIG:uint = 119;
      
      protected static const TF_SPACE_AROUND:uint = 4;
      
      private static const FONT_SIZE:uint = 15;
      
      private static const FONT_LEADING:int = -1;
       
      
      public var hitMc:Sprite = null;
      
      public var border:Sprite = null;
      
      public var borderHover:Sprite = null;
      
      public var textField:TextField = null;
      
      public var icon:C11nInnerEntryPointIcon = null;
      
      private var _data:CustomizationInnerEntryPointVO = null;
      
      private var _labelKay:String = "";
      
      private var _allowedFrames:Vector.<String> = null;
      
      private var _state:String = "up";
      
      private var _textFormat:TextFormat = null;
      
      public function C11nInnerEntryPoint()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         hitArea = this.hitMc;
         buttonMode = true;
         this.mouseChildren = false;
         this.border.mouseEnabled = false;
         this.border.mouseChildren = false;
         this.borderHover.mouseEnabled = false;
         this.borderHover.mouseChildren = false;
         this._textFormat = new TextFormat();
         this._textFormat.size = FONT_SIZE;
         this._textFormat.leading = FONT_LEADING;
         var _loc1_:Array = currentLabels;
         var _loc2_:int = _loc1_.length;
         this._allowedFrames = new Vector.<String>(0);
         var _loc3_:FrameLabel = null;
         var _loc4_:uint = 0;
         while(_loc4_ < _loc2_)
         {
            _loc3_ = _loc1_[_loc4_];
            this._allowedFrames.push(_loc3_.name);
            _loc4_++;
         }
         addEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         addEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
         addEventListener(MouseEvent.CLICK,this.onClickHandler);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         removeEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
         removeEventListener(MouseEvent.CLICK,this.onClickHandler);
         stop();
         if(this._allowedFrames != null)
         {
            this._allowedFrames.splice(0,this._allowedFrames.length);
            this._allowedFrames = null;
         }
         this._textFormat = null;
         this.icon.dispose();
         this.icon = null;
         this.textField = null;
         this.border = null;
         this.borderHover = null;
         this.hitMc = null;
         this._data = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA) && this._data)
         {
            this.updateData();
         }
         if(isInvalid(InvalidationType.STATE))
         {
            this.updateState();
            this.updateTexts();
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.updateLayout();
         }
      }
      
      public function initData(param1:CustomizationInnerEntryPointVO) : void
      {
         this.visible = false;
         this.setData(param1);
      }
      
      public function setData(param1:CustomizationInnerEntryPointVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      public function setScale(param1:Number) : void
      {
         if(scaleX == param1)
         {
            return;
         }
         scaleX = scaleY = param1;
         invalidateSize();
      }
      
      private function updateData() : void
      {
         this.icon.setData(this._data);
         invalidateState();
      }
      
      private function updateState() : void
      {
         var _loc1_:String = !!this._data.isSelected ? STATE_SELECTED : this._state;
         var _loc2_:String = !!this._data.isSmall ? STATE_PREFIX_SMALL + _loc1_ : _loc1_;
         var _loc3_:Boolean = this.visible != this._data.isVisible;
         this.visible = this._data.isVisible;
         if(this._allowedFrames.indexOf(_loc2_) >= 0 && (this._labelKay != _loc2_ || _loc3_))
         {
            if(this._data.isVisible)
            {
               gotoAndPlay(_loc2_);
            }
            this._labelKay = _loc2_;
         }
         this.enabled = !this._data.isSelected;
      }
      
      private function updateTexts() : void
      {
         this.textField.width = !!this._data.isSmall ? Number(TF_WIDTH_SMALL) : Number(TF_WIDTH_BIG);
         this.textField.htmlText = this._data.label;
         this.textField.height = this.textField.textHeight + TF_SPACE_AROUND;
         this.textField.setTextFormat(this._textFormat);
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      private function updateLayout() : void
      {
         this.textField.x = !!this._data.isSmall ? Number(TF_POS_X_SMALL) : Number(TF_POS_X_BIG);
         this.textField.y = (!!this._data.isSmall ? TF_POS_Y_CENTER_SMALL : TF_POS_Y_CENTER_BIG) - (this.textField.height >> 1);
      }
      
      private function setState(param1:String) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         invalidateState();
      }
      
      override public function get height() : Number
      {
         return this.hitMc.height;
      }
      
      private function onMouseOverHandler(param1:MouseEvent) : void
      {
         this.setState(STATE_OVER);
         dispatchEvent(new CustomizationSoundEvent(CustomizationSoundEvent.PLAY_SOUND,CUSTOMIZATION_ALIASES.SOUND_CUST_HIGHLIGHT));
      }
      
      private function onMouseOutHandler(param1:MouseEvent) : void
      {
         this.setState(STATE_OUT);
      }
      
      private function onClickHandler(param1:MouseEvent) : void
      {
         if(param1 is MouseEventEx)
         {
            if(MouseEventEx(param1).buttonIdx == MouseEventEx.LEFT_BUTTON)
            {
               dispatchEvent(new CustomizationSoundEvent(CustomizationSoundEvent.PLAY_SOUND,SoundTypes.CUSTOMIZATION_SELECT));
               dispatchEvent(new CustomizationEvent(CustomizationEvent.ENTRY_POINT_CLICKED,false,Values.DEFAULT_INT,this._data.itemId));
            }
         }
      }
   }
}
