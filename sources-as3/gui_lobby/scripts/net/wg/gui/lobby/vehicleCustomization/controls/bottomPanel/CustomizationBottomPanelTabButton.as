package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Point;
   import net.wg.data.constants.ComponentState;
   import net.wg.data.constants.ImageCacheTypes;
   import net.wg.data.constants.generated.CUSTOMIZATION_ALIASES;
   import net.wg.gui.components.advanced.collapsingBar.ResizableButton;
   import net.wg.gui.components.controls.BitmapFill;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationSoundEvent;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.core.UIComponent;
   import scaleform.clik.utils.Padding;
   
   public class CustomizationBottomPanelTabButton extends ResizableButton
   {
      
      private static const DISABLE_ALPHA:Number = 0.2;
      
      private static const DISABLE_ALPHA_TEXT:Number = 0.5;
      
      private static const ALPHA_TEXT:Number = 1;
      
      private static const INACTIVE_ALPHA:Number = 0.5;
      
      private static const ACTIVE_ALPHA:Number = 0.8;
      
      private static const SELECTED_ALPHA:Number = 1;
      
      private static const PLUS_OFFSET_X:int = 9;
      
      private static const COUNTER_OFFSET_X:int = 10;
      
      private static const PLUS_OFFSET_Y:int = 10;
      
      private static const COUNTER_PADDING:int = 7;
      
      private static const COUNTER_PADDING_SMALL:int = 2;
      
      private static const TEXT_FIELD_OFFSET_X:int = -5;
      
      private static const ICON_SOURCE_INVALID:String = "imageSrcInv";
      
      private static const HOVER_POSTFIX:String = "_hover";
      
      private static const ACTIVE_POSTFIX:String = "_active";
      
      private static const LAST_PREFIX:String = "last_";
      
      private static const OUT:String = "out";
      
      private static const DISABLE_PATTERN:String = "uniDisablePattern";
      
      private static const INACTIVE_COLOR:uint = 9211006;
      
      private static const ACTIVE_COLOR:uint = 12495231;
      
      private static const SELECTED_COLOR:uint = 16768409;
      
      private static const HOVER_COLOR:uint = 16777189;
       
      
      public var states:MovieClip = null;
      
      public var icon:Image = null;
      
      public var plus:Sprite = null;
      
      public var iconActive:Image = null;
      
      public var counterEx:CustomizationTabCounter = null;
      
      private var _iconSource:String = "";
      
      private var _offsetFromIcon:int = 0;
      
      private var _iconSize:Point;
      
      private var _last:Boolean = false;
      
      private var _active:Boolean = false;
      
      public function CustomizationBottomPanelTabButton()
      {
         this._iconSize = new Point();
         super();
      }
      
      override public function getOriginSize() : Point
      {
         return new Point(this.calculateOriginWidth(),calculateOriginHeight());
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         if(this.states != null)
         {
            _labelHash = UIComponent.generateLabelHash(this.states);
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.icon.alpha = !!enabled ? Number(INACTIVE_ALPHA) : Number(DISABLE_ALPHA);
         this.icon.addEventListener(Event.CHANGE,this.onIconChangeHandler);
         soundEnabled = false;
         this.icon.cacheType = ImageCacheTypes.NOT_USE_CACHE;
         focusable = false;
         mouseEnabledOnDisabled = true;
         disableMc.repeat = BitmapFill.REPEAT_ALL;
         disableMc.source = DISABLE_PATTERN;
         disabledFillPadding = new Padding(0,2,0,2);
      }
      
      override protected function calculateOriginWidth() : int
      {
         var _loc1_:int = !!this.hasText ? int(this._offsetFromIcon) : int(0);
         return tabBar.getTextWidth(this) + _loc1_ + this._iconSize.x + (padding << 1);
      }
      
      override protected function draw() : void
      {
         if(isInvalid(InvalidationType.STATE))
         {
            if(StringUtils.isNotEmpty(_newFrame))
            {
               App.utils.asserter.assert(_labelHash.hasOwnProperty(_newFrame),"Not found state " + _newFrame);
               this.states.gotoAndPlay(_newFrame);
               if(_baseDisposed)
               {
                  return;
               }
            }
         }
         super.draw();
         if(isInvalid(ICON_SOURCE_INVALID))
         {
            if(StringUtils.isNotEmpty(this._iconSource))
            {
               this.icon.source = this._iconSource;
               this.iconActive.source = this._iconSource.replace(HOVER_POSTFIX,ACTIVE_POSTFIX);
            }
            invalidateSize();
         }
      }
      
      override protected function onDispose() : void
      {
         this.icon.removeEventListener(Event.CHANGE,this.onIconChangeHandler);
         this.icon.dispose();
         this.iconActive.dispose();
         this.counterEx.dispose();
         this.states = null;
         this.icon = null;
         this.iconActive = null;
         this._iconSource = null;
         this._iconSize = null;
         this.counterEx = null;
         super.onDispose();
      }
      
      override protected function checkChild(param1:DisplayObject) : Boolean
      {
         return super.checkChild(param1) || param1 != this.icon || param1 != this.iconActive || param1 != this.counterEx;
      }
      
      override protected function updateScale(param1:Number, param2:Number) : void
      {
         this.icon.scaleX = this.iconActive.scaleX = this.plus.scaleX = this.counterEx.scaleX = param1;
         this.icon.scaleY = this.iconActive.scaleY = this.plus.scaleY = this.counterEx.scaleY = param2;
         super.updateScale(param1,param2);
      }
      
      override protected function setState(param1:String) : void
      {
         super.setState(param1);
         if(param1 == ComponentState.DOWN)
         {
            return;
         }
         textField.textColor = INACTIVE_COLOR;
         textField.alpha = !!enabled ? Number(ALPHA_TEXT) : Number(DISABLE_ALPHA_TEXT);
         this.iconActive.alpha = this.icon.alpha = this.plus.alpha = !!enabled ? Number(INACTIVE_ALPHA) : Number(DISABLE_ALPHA);
         if(!enabled)
         {
            return;
         }
         if(this._active)
         {
            textField.textColor = ACTIVE_COLOR;
            this.iconActive.alpha = this.icon.alpha = this.plus.alpha = ACTIVE_ALPHA;
            if(selected || param1 == ComponentState.OVER)
            {
               textField.textColor = SELECTED_COLOR;
               this.iconActive.alpha = this.icon.alpha = this.plus.alpha = SELECTED_ALPHA;
            }
         }
         else if(param1 == ComponentState.OVER)
         {
            textField.textColor = HOVER_COLOR;
            this.iconActive.alpha = this.icon.alpha = this.plus.alpha = ACTIVE_ALPHA;
         }
      }
      
      override protected function getStatePrefixes() : Vector.<String>
      {
         if(this._last && !selected)
         {
            return Vector.<String>([LAST_PREFIX]);
         }
         return super.getStatePrefixes();
      }
      
      override protected function updateChildPositions() : void
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc1_:Boolean = StringUtils.isNotEmpty(this._iconSource);
         var _loc2_:int = this.icon.width != 0 ? int(this.icon.width) : int(this._iconSize.x);
         var _loc3_:int = this.icon.height != 0 ? int(this.icon.height) : int(this._iconSize.y);
         var _loc4_:int = 9;
         if(collapsed)
         {
            _loc5_ = hitMc.width >> 1;
            _loc6_ = 0;
            if(this.hasText)
            {
               _loc6_ = _loc5_ - (textField.width >> 1);
               if(_loc1_)
               {
                  _loc6_ -= this.icon.width + this._offsetFromIcon >> 1;
               }
            }
            else if(_loc1_)
            {
               _loc6_ = _loc5_ - (this.icon.width >> 1);
            }
            if(_loc1_)
            {
               this.icon.x = this.iconActive.x = _loc6_;
               this.icon.y = this.iconActive.y = hitMc.height - this.icon.height >> 1;
               this.plus.x = this.icon.x + PLUS_OFFSET_X;
               this.plus.y = this.icon.y + PLUS_OFFSET_Y;
               if(this.hasText)
               {
                  textField.x = this.icon.x + this.icon.width + this._offsetFromIcon + TEXT_FIELD_OFFSET_X;
                  textField.y = hitMc.height - textField.height >> 1;
                  this.counterEx.x = textField.x + textField.width - COUNTER_PADDING | 0;
               }
               else
               {
                  this.counterEx.x = this.icon.x + this.icon.width - COUNTER_PADDING_SMALL;
               }
            }
            else if(this.hasText)
            {
               textField.x = _loc6_;
               textField.y = hitMc.height - textField.height >> 1;
               this.counterEx.x = textField.x + textField.width - COUNTER_PADDING | 0;
            }
         }
         else
         {
            if(_loc1_)
            {
               this.icon.x = this.iconActive.x = _loc4_;
               this.icon.y = this.iconActive.y = hitMc.height - _loc3_ >> 1;
               this.plus.x = this.icon.x + PLUS_OFFSET_X;
               this.plus.y = this.icon.y + PLUS_OFFSET_Y;
               this.counterEx.x = _loc4_;
               _loc4_ += _loc2_ + this._offsetFromIcon;
            }
            if(this.hasText)
            {
               _loc4_ += TEXT_FIELD_OFFSET_X;
               textField.x = _loc4_;
               textField.y = hitMc.height - textField.height >> 1;
               this.counterEx.x = textField.x + textField.width - COUNTER_PADDING | 0;
            }
         }
         this.counterEx.x += COUNTER_OFFSET_X;
         updateDisable();
      }
      
      public function setNotification(param1:int, param2:Boolean) : void
      {
         var _loc3_:String = null;
         this.counterEx.visible = enabled && (param1 > 0 || param2);
         if(this.counterEx.visible)
         {
            _loc3_ = !!param2 ? VEHICLE_CUSTOMIZATION.CUSTOMIZATION_NOTIFICATION_NEW : param1.toString();
            this.counterEx.text = _loc3_;
         }
      }
      
      public function setIconSize(param1:int, param2:int) : void
      {
         if(this._iconSize.x == param1 || this._iconSize.y == param2)
         {
            return;
         }
         this._iconSize.x = param1;
         this._iconSize.y = param2;
      }
      
      public function showPlus(param1:Boolean) : void
      {
         this.plus.visible = param1;
      }
      
      public function setActive(param1:Boolean) : void
      {
         this._active = param1;
         this.icon.visible = !this._active;
         this.iconActive.visible = this._active;
         this.setState(state);
      }
      
      public function getActive() : Boolean
      {
         return this._active;
      }
      
      override public function set label(param1:String) : void
      {
         super.label = App.utils.toUpperOrLowerCase(param1,true);
      }
      
      override public function set selected(param1:Boolean) : void
      {
         if(selected != param1)
         {
            this.icon.visible = !param1;
            this.iconActive.visible = param1;
            super.selected = param1;
         }
         this.setState(state);
      }
      
      public function set iconSource(param1:String) : void
      {
         if(this._iconSource != param1)
         {
            this._iconSource = param1;
            invalidate(ICON_SOURCE_INVALID);
         }
      }
      
      public function get hasText() : Boolean
      {
         return StringUtils.isNotEmpty(this.label);
      }
      
      public function set offsetFromIcon(param1:int) : void
      {
         if(this._offsetFromIcon == param1)
         {
            return;
         }
         this._offsetFromIcon = param1;
         invalidate(LAYOUT_INVALID);
      }
      
      public function get last() : Boolean
      {
         return this._last;
      }
      
      public function set last(param1:Boolean) : void
      {
         this._last = param1;
         this.setState(OUT);
      }
      
      public function set first(param1:Boolean) : void
      {
         bgMc.visible = !param1;
         this.states.visible = !param1;
      }
      
      override protected function onMouseRollOverHandler(param1:MouseEvent) : void
      {
         super.onMouseRollOverHandler(param1);
         dispatchEvent(new CustomizationSoundEvent(CustomizationSoundEvent.PLAY_SOUND,CUSTOMIZATION_ALIASES.SOUND_CUST_HIGHLIGHT));
      }
      
      private function onIconChangeHandler(param1:Event) : void
      {
         invalidate(LAYOUT_INVALID);
      }
   }
}
