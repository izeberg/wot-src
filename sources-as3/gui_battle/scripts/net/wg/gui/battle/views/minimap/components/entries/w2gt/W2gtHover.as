package net.wg.gui.battle.views.minimap.components.entries.w2gt
{
   import fl.motion.easing.Cubic;
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.filters.BitmapFilterQuality;
   import flash.filters.DropShadowFilter;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class W2gtHover extends Sprite implements IDisposable
   {
      
      private static const OUTLINE_BLUR:int = 2;
      
      private static const OUTLINE_STRENGTH:Number = 16;
      
      private static const FILL_ALPHA:Number = 0.5;
      
      private static const COORDINATES_STEP:int = 2;
      
      private static const GLOW_BLUR:int = 50;
      
      private static const GLOW_STRENGTH:Number = 1.4;
      
      private static const TWEEN_DURATION:Number = 400;
       
      
      public var fillMc:Sprite = null;
      
      public var strokeMc:Sprite = null;
      
      public var glowMc:Sprite = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _fillColor:Number = NaN;
      
      private var _borderShadowFilter:DropShadowFilter = null;
      
      private var _glowShadowFilter:DropShadowFilter = null;
      
      private var _zones:Array;
      
      private var _tween:Tween;
      
      public function W2gtHover()
      {
         this._zones = [];
         super();
         this._borderShadowFilter = new DropShadowFilter(0,0,0,Values.DEFAULT_ALPHA,OUTLINE_BLUR,OUTLINE_BLUR,OUTLINE_STRENGTH,BitmapFilterQuality.MEDIUM,false,true);
         this._glowShadowFilter = new DropShadowFilter(0,0,0,Values.DEFAULT_ALPHA,GLOW_BLUR,GLOW_BLUR,GLOW_STRENGTH,BitmapFilterQuality.MEDIUM,false,true);
         this.strokeMc.alpha = FILL_ALPHA;
         this.alpha = Values.ZERO;
      }
      
      public final function dispose() : void
      {
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         this.clearTween();
         this._zones.splice(0,this._zones.length);
         this._zones = null;
         this.fillMc = null;
         this.strokeMc = null;
         this.strokeMc.filters = null;
         this.glowMc = null;
         this.glowMc.filters = null;
         this._borderShadowFilter = null;
         this._glowShadowFilter = null;
         return this._isDisposed;
      }
      
      public function setFill(param1:int) : void
      {
         if(this._fillColor != param1)
         {
            this._fillColor = param1;
            this.doFill();
         }
      }
      
      private function doFill() : void
      {
         if(!this._zones || this._zones.length == 0 || isNaN(this._fillColor))
         {
            return;
         }
         this._borderShadowFilter.color = this._fillColor;
         this._glowShadowFilter.color = this._fillColor;
         this.strokeMc.filters = [this._borderShadowFilter];
         this.glowMc.filters = [this._glowShadowFilter];
         var _loc1_:Graphics = this.fillMc.graphics;
         var _loc2_:Graphics = this.strokeMc.graphics;
         var _loc3_:Graphics = this.glowMc.graphics;
         _loc2_.clear();
         _loc2_.beginFill(Values.ZERO);
         _loc3_.clear();
         _loc3_.beginFill(Values.ZERO);
         _loc1_.clear();
         _loc1_.beginFill(this._fillColor);
         var _loc4_:int = this._zones.length;
         _loc2_.moveTo(this._zones[0],this._zones[1]);
         _loc3_.moveTo(this._zones[0],this._zones[1]);
         _loc1_.moveTo(this._zones[0],this._zones[1]);
         var _loc5_:uint = COORDINATES_STEP;
         while(_loc5_ < _loc4_)
         {
            _loc1_.lineTo(this._zones[_loc5_],this._zones[_loc5_ + 1]);
            _loc2_.lineTo(this._zones[_loc5_],this._zones[_loc5_ + 1]);
            _loc3_.lineTo(this._zones[_loc5_],this._zones[_loc5_ + 1]);
            _loc5_ += COORDINATES_STEP;
         }
         _loc1_.endFill();
         _loc2_.endFill();
         _loc3_.endFill();
      }
      
      public function setZones(param1:Array) : void
      {
         this._zones = param1;
         this.doFill();
      }
      
      public function setAlpha(param1:Number) : void
      {
         this.clearTween();
         if(param1 > this.alpha)
         {
            this.alpha = param1;
         }
         else
         {
            this._tween = new Tween(TWEEN_DURATION,this,{"alpha":param1},{
               "ease":Cubic.easeInOut,
               "paused":false
            });
         }
      }
      
      private function clearTween() : void
      {
         if(this._tween)
         {
            this._tween.paused = true;
            this._tween.dispose();
            this._tween = null;
         }
      }
   }
}
