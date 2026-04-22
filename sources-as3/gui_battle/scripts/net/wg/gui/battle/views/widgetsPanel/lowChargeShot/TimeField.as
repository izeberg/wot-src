package net.wg.gui.battle.views.widgetsPanel.lowChargeShot
{
   import com.gskinner.motion.plugins.HexColorPlugin;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.external.ExternalInterface;
   import flash.filters.DropShadowFilter;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.LOW_CHARGE_SHOT_CONSTS;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.ColorsProvider;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class TimeField extends Sprite implements IDisposable
   {
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
      
      protected static const ALPHA_NORMAL:Number = 1;
      
      protected static const ALPHA_FADED:Number = 0.5;
      
      protected static const ALPHA_HIDDEN:Number = 0;
      
      protected static const DURATION_QUICK:Number = 0.1;
      
      protected static const DURATION_LONG:Number = 0.5;
       
      
      public var textField:TextField = null;
      
      protected var _colorsProvider:ColorsProvider = null;
      
      private var _shadowFilterNormal:DropShadowFilter;
      
      private var _shadowFilterFaded:DropShadowFilter;
      
      private var _textColor:uint = 0;
      
      private var _opacity:Number = 1;
      
      private var _isDisposed:Boolean = false;
      
      private var _reloadingState:Number = -1;
      
      public function TimeField()
      {
         this._shadowFilterNormal = new DropShadowFilter(0,0,729344,1,2,2,6,3);
         this._shadowFilterFaded = new DropShadowFilter(0,0,729344,0.3,2,2,6,3);
         super();
         HexColorPlugin.install(["textColor"]);
      }
      
      public function dispose() : void
      {
         if(!this.isDisposed())
         {
            this._colorsProvider.removeEventListener(Event.RENDER,this.onColorsRenderHandler);
            this._colorsProvider = null;
            this._shadowFilterNormal = null;
            this._shadowFilterFaded = null;
            this.textField = null;
            this.onDispose();
         }
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setReloadingState(param1:Number) : void
      {
         if(this._reloadingState != param1)
         {
            this._reloadingState = param1;
            switch(this._reloadingState)
            {
               case LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE:
                  this.playLowCharge();
                  break;
               case LOW_CHARGE_SHOT_CONSTS.ALMOST_FINISHED:
                  this.playAlmostFinished();
                  break;
               case LOW_CHARGE_SHOT_CONSTS.FULL_CHARGE:
                  this.playFullCharge();
                  break;
               case LOW_CHARGE_SHOT_CONSTS.QUICK_RELOAD:
                  this.playQuickReload();
                  break;
               default:
                  this.playInitial();
            }
         }
      }
      
      public function setValue(param1:Number, param2:Boolean = true) : void
      {
         var _loc3_:TextFormat = this.textField.getTextFormat();
         this.textField.text = this.formatTime(param1,param2);
         this.textField.setTextFormat(_loc3_);
      }
      
      protected function playAlmostFinished() : void
      {
      }
      
      protected function playFullCharge() : void
      {
      }
      
      protected function playInitial() : void
      {
      }
      
      protected function playLowCharge() : void
      {
      }
      
      protected function playQuickReload() : void
      {
      }
      
      protected function updateShadow(param1:Boolean) : void
      {
         var _loc2_:DropShadowFilter = alpha == param1 ? this._shadowFilterFaded : this._shadowFilterNormal;
         this.textField.filters = [_loc2_];
      }
      
      protected function onDispose() : void
      {
      }
      
      private function formatTime(param1:Number, param2:Boolean) : String
      {
         var _loc3_:String = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,param1]);
         return !!param2 ? _loc3_.slice(0,_loc3_.length - 1) : _loc3_;
      }
      
      public function set colorsProvider(param1:ColorsProvider) : void
      {
         if(this._colorsProvider != param1)
         {
            if(this._colorsProvider)
            {
               this._colorsProvider.removeEventListener(Event.RENDER,this.onColorsRenderHandler);
            }
            this._colorsProvider = param1;
            this._colorsProvider.addEventListener(Event.RENDER,this.onColorsRenderHandler);
         }
      }
      
      public function get opacity() : Number
      {
         return this._opacity;
      }
      
      public function set opacity(param1:Number) : void
      {
         this._opacity = param1;
         this.textField.alpha = this._opacity;
      }
      
      public function get textColor() : Number
      {
         return this._textColor;
      }
      
      public function set textColor(param1:Number) : void
      {
         this._textColor = param1;
         var _loc2_:TextFormat = this.textField.getTextFormat();
         _loc2_.color = this._textColor;
         this.textField.setTextFormat(_loc2_);
      }
      
      private function onColorsRenderHandler(param1:Event) : void
      {
         var _loc2_:Number = this._reloadingState;
         this._reloadingState = Values.DEFAULT_INT;
         this.setReloadingState(_loc2_);
      }
   }
}
