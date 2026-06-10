package net.wg.gui.lobby.messengerBar.carousel
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.geom.ColorTransform;
   import net.wg.data.constants.generated.TEXT_ALIGN;
   import net.wg.gui.components.advanced.BlinkingButton;
   import net.wg.gui.lobby.messengerBar.carousel.data.IToolTipData;
   import net.wg.infrastructure.interfaces.IDynamicContent;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.utils.ConstrainedElement;
   import scaleform.clik.utils.Padding;
   
   public class ChannelButton extends BlinkingButton implements IDynamicContent
   {
      
      private static const TF_PADDING_INVALID:String = "tfpInv";
      
      private static const COLOR_BG_VISIBLE_INVALID:String = "cBgVisibleInv";
      
      private static const TF_COLOR_TRANSFORM_INVALID:String = "tfCtInv";
      
      private static const LABEL_INVALID:String = "lblInv";
      
      private static const TOOLTIP_INVALID:String = "tooltipInv";
      
      private static const FOCUSED_STATE_PREFIX:String = "focused_";
      
      private static const BLINKING_STATE_PREFIX:String = "blinking_";
      
      private static const SELECTED_STATE_PREFIX:String = "selected_";
      
      private static const OUT:String = "out";
      
      private static const UP:String = "up";
      
      private static const DISABLE_FILL_ALPHA:Number = 0.7;
       
      
      protected var _iconAlign:String = "left";
      
      protected var _iconOffsetRight:Number = 0;
      
      public var mcColorBg:MovieClip;
      
      private var _tfPadding:Padding;
      
      private var _selectedFocused:Boolean;
      
      private var _colorBgVisible:Boolean = false;
      
      private var _textFieldColorTransform:ColorTransform;
      
      private var _tooltipData:IToolTipData;
      
      private var _toolTipMgr:ITooltipMgr;
      
      public function ChannelButton()
      {
         this._toolTipMgr = App.toolTipMgr;
         super();
         _iconOffsetLeft = 1;
         _iconOffsetTop = 1;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.mcColorBg.visible = false;
         mouseEnabledOnDisabled = true;
         disableMc.alpha = DISABLE_FILL_ALPHA;
      }
      
      override protected function draw() : void
      {
         var _loc1_:ConstrainedElement = null;
         if(this._tfPadding && isInvalid(TF_PADDING_INVALID))
         {
            _loc1_ = constraints.getElement(textField.name);
            _loc1_.left = this._tfPadding.left;
            _loc1_.right = this._tfPadding.right;
         }
         super.draw();
         if(isInvalid(InvalidationType.STATE) || isInvalid(TF_COLOR_TRANSFORM_INVALID) && this._textFieldColorTransform)
         {
            textField.transform.colorTransform = this._textFieldColorTransform;
         }
         if(isInvalid(InvalidationType.STATE) || isInvalid(COLOR_BG_VISIBLE_INVALID))
         {
            this.mcColorBg.visible = this._colorBgVisible;
         }
         if(isInvalid(LABEL_INVALID) || isInvalid(InvalidationType.STATE))
         {
            textField.htmlText = _label;
            App.utils.commons.truncateTextFieldText(textField,textField.text);
         }
         if(isInvalid(TOOLTIP_INVALID) && this.canShowTooltipByHover() && this.hitTestPoint(stage.mouseX,stage.mouseY,true))
         {
            this.showTooltip();
         }
      }
      
      override protected function getStatePrefixes() : Vector.<String>
      {
         var _loc1_:String = "";
         if(blinking)
         {
            if(this._selectedFocused)
            {
               return Vector.<String>([BLINKING_STATE_PREFIX,FOCUSED_STATE_PREFIX]);
            }
            return Vector.<String>(!!_selected ? [BLINKING_STATE_PREFIX,SELECTED_STATE_PREFIX] : [BLINKING_STATE_PREFIX]);
         }
         if(this._selectedFocused)
         {
            return Vector.<String>([FOCUSED_STATE_PREFIX,_loc1_]);
         }
         return Vector.<String>(!!_selected ? [SELECTED_STATE_PREFIX,_loc1_] : [_loc1_]);
      }
      
      override protected function showTooltip() : void
      {
         if(_tooltip)
         {
            this._toolTipMgr.show(_tooltip);
         }
         else if(this._tooltipData)
         {
            if(this._tooltipData.tooltipId)
            {
               if(this._tooltipData.isWulfTooltip)
               {
                  this._toolTipMgr.showWulfTooltip.apply(this._toolTipMgr,[this._tooltipData.tooltipId].concat(this._tooltipData.tooltipArgs));
               }
               else
               {
                  this._toolTipMgr.showComplex(this._tooltipData.tooltipId);
               }
            }
            else
            {
               this._toolTipMgr.show(this._tooltipData.label);
            }
         }
      }
      
      override protected function canShowTooltipByHover() : Boolean
      {
         return true;
      }
      
      override protected function updateText() : void
      {
         if(_label != null && textField != null)
         {
            textField.htmlText = _label;
         }
      }
      
      override protected function onDispose() : void
      {
         this._tooltipData = null;
         this._tfPadding = null;
         this._textFieldColorTransform = null;
         this.mcColorBg = null;
         this._toolTipMgr = null;
         super.onDispose();
      }
      
      override protected function updateDisable() : void
      {
         if(disableMc != null)
         {
            disableMc.x = disabledFillPadding.left;
            disableMc.y = disabledFillPadding.top;
            disableMc.scaleX = 1 / this.scaleX;
            disableMc.scaleY = 1 / this.scaleY;
            disableMc.widthFill = Math.round(this.mcColorBg.width * this.scaleX) - disabledFillPadding.horizontal;
            disableMc.heightFill = Math.round(this.mcColorBg.height * this.scaleY) - disabledFillPadding.vertical;
            disableMc.visible = !enabled;
         }
      }
      
      override protected function configIcon() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         if(loader && loader.content)
         {
            _loc1_ = 1 / this.scaleX;
            _loc2_ = 1 / this.scaleY;
            loader.y = _iconOffsetTop * _loc2_;
            if(this._iconAlign == TEXT_ALIGN.LEFT)
            {
               loader.x = _iconOffsetLeft * _loc1_;
            }
            else
            {
               if(this._iconAlign != TEXT_ALIGN.RIGHT)
               {
                  throw new Error("invalid icon align value: ",this._iconAlign);
               }
               loader.x = width * _loc1_ - loader.content.width - this.scaleX * this._iconOffsetRight;
            }
            loader.tabEnabled = loader.mouseEnabled = false;
            loader.visible = true;
         }
      }
      
      override protected function handleMouseRollOut(param1:MouseEvent) : void
      {
         super.handleMouseRollOut(param1);
         this._toolTipMgr.hide();
      }
      
      public function setTextFieldColorTransform(param1:ColorTransform) : void
      {
         this._textFieldColorTransform = param1;
         invalidate(TF_COLOR_TRANSFORM_INVALID);
      }
      
      public function setTooltipData(param1:IToolTipData) : void
      {
         this._tooltipData = param1;
         invalidate(TOOLTIP_INVALID);
      }
      
      public function showColorBg(param1:Boolean) : void
      {
         this._colorBgVisible = param1;
         invalidate(COLOR_BG_VISIBLE_INVALID);
      }
      
      override public function set label(param1:String) : void
      {
         var _loc2_:String = (this._iconAlign == TEXT_ALIGN.LEFT && _iconSource && _iconSource != "" ? "     " : "") + param1;
         if(_loc2_ != label)
         {
            super.label = _loc2_;
            invalidate(LABEL_INVALID);
         }
      }
      
      override public function set tooltip(param1:String) : void
      {
         if(_tooltip != param1)
         {
            _tooltip = param1;
            this._toolTipMgr.hide();
         }
      }
      
      override public function set width(param1:Number) : void
      {
         if(width != param1)
         {
            super.width = param1;
            invalidate(LABEL_INVALID);
         }
      }
      
      public function set selectedFocused(param1:Boolean) : void
      {
         if(this._selectedFocused != param1)
         {
            this._selectedFocused = param1;
            if(_state == OUT)
            {
               setState(UP);
            }
            else
            {
               setState(state);
            }
         }
      }
      
      public function set textFieldPadding(param1:Padding) : void
      {
         this._tfPadding = param1;
         invalidate(TF_PADDING_INVALID);
         invalidateState();
      }
      
      [Inspectable(defaultValue="0",name="iconOffsetRight",type="Number")]
      public function get iconOffsetRight() : Number
      {
         return this._iconOffsetRight;
      }
      
      public function set iconOffsetRight(param1:Number) : void
      {
         if(this._iconOffsetRight != param1)
         {
            this._iconOffsetRight = param1;
            invalidateSize();
         }
      }
      
      public function get iconAlign() : String
      {
         return this._iconAlign;
      }
      
      public function set iconAlign(param1:String) : void
      {
         if(this._iconAlign != param1)
         {
            this._iconAlign = param1;
            invalidateSize();
         }
      }
   }
}
