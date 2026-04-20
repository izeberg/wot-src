package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   import flash.events.Event;
   import flash.events.EventDispatcher;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   
   public class ColorsProvider extends EventDispatcher implements IDisposable
   {
      
      private static const PURPLE_COLOR:uint = 8945407;
      
      private static const RED_TEXT_COLOR:uint = 15007744;
      
      private static const GREEN_TEXT_COLOR:uint = 9882665;
      
      private static const GLOW_COLOR:uint = 14155625;
      
      private static const GREEN_COLOR:uint = 9305906;
      
      private static const DARK_GREEN_COLOR:uint = 6272042;
      
      private static const WHITE_COLOR:uint = 16777215;
      
      private static const RED_COLOR:uint = 16711680;
      
      private static const BLOCK_COLOR:uint = 16721687;
      
      private static const GLOW_DURATION_1:Number = 0.7;
      
      private static const GLOW_CIRCLE_DURATION:Number = 0.5;
      
      private static const GLOW_ALPHA_START:Number = 0.8;
      
      private static const GLOW_ALPHA_END:Number = 0;
      
      private static const GLOW_CIRCLE_ALPHA_START:Number = 1;
      
      private static const GLOW_CIRCLE_ALPHA_END:Number = 0;
       
      
      private var _glowAlpha:Number = 0;
      
      private var _glowCircleAlpha:Number = 0;
      
      private var _isDisposed:Boolean = false;
      
      private var _isColorBlind:Boolean = false;
      
      private var _colorMgr:IColorSchemeManager = null;
      
      public function ColorsProvider()
      {
         super();
         if(App.instance)
         {
            this._colorMgr = App.colorSchemeMgr;
            this._isColorBlind = this._colorMgr.getIsColorBlindS();
            this._colorMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
         }
      }
      
      public final function dispose() : void
      {
         if(!this._isDisposed)
         {
            if(this._colorMgr)
            {
               this._colorMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
               this._colorMgr = null;
            }
            GTweener.removeTweens(this);
            this._isDisposed = true;
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function pulseGlow() : void
      {
         this.glowAlpha = GLOW_ALPHA_START;
         this.glowCircleAlpha = GLOW_CIRCLE_ALPHA_START;
         GTweener.removeTweens(this);
         GTweener.to(this,GLOW_DURATION_1,{"glowAlpha":GLOW_ALPHA_END},{
            "ease":Cubic.easeIn,
            "onChange":this.dispatchRedraw
         });
         GTweener.to(this,GLOW_CIRCLE_DURATION,{"glowCircleAlpha":GLOW_CIRCLE_ALPHA_END},{"ease":Cubic.easeIn});
      }
      
      private function dispatchRedraw() : void
      {
         dispatchEvent(new Event(Event.RENDER));
      }
      
      public function get textColorNotCompleted() : uint
      {
         return !!this._isColorBlind ? uint(PURPLE_COLOR) : uint(RED_TEXT_COLOR);
      }
      
      public function get colorLoaded() : uint
      {
         return GREEN_COLOR;
      }
      
      public function get colorLeft() : uint
      {
         return !!this._isColorBlind ? uint(PURPLE_COLOR) : uint(RED_COLOR);
      }
      
      public function get colorLeftLowCharge() : uint
      {
         return DARK_GREEN_COLOR;
      }
      
      public function get colorBlockEnabled() : uint
      {
         return !!this._isColorBlind ? uint(PURPLE_COLOR) : uint(BLOCK_COLOR);
      }
      
      public function get colorBlockDisabled() : uint
      {
         return WHITE_COLOR;
      }
      
      public function get colorPointer() : uint
      {
         return WHITE_COLOR;
      }
      
      public function get glowColor() : uint
      {
         return GLOW_COLOR;
      }
      
      public function get glowAlpha() : Number
      {
         return this._glowAlpha;
      }
      
      public function set glowAlpha(param1:Number) : void
      {
         this._glowAlpha = param1;
      }
      
      public function get glowCircleAlpha() : Number
      {
         return this._glowCircleAlpha;
      }
      
      public function set glowCircleAlpha(param1:Number) : void
      {
         this._glowCircleAlpha = param1;
      }
      
      public function get textColorCompleted() : uint
      {
         return GREEN_TEXT_COLOR;
      }
      
      public function get isColorBlind() : Boolean
      {
         return this._isColorBlind;
      }
      
      public function set isColorBlind(param1:Boolean) : void
      {
         this._isColorBlind = param1;
      }
      
      private function onColorSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this._isColorBlind = this._colorMgr.getIsColorBlindS();
         this.dispatchRedraw();
      }
   }
}
