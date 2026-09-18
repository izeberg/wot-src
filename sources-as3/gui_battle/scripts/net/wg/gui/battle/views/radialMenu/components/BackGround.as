package net.wg.gui.battle.views.radialMenu.components
{
   import flash.display.BitmapData;
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.geom.Matrix;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class BackGround extends Sprite implements IDisposable
   {
      
      private static const HOLE_LINKAGE:String = "radialMenuHoleUI";
      
      private static const HOLE_HALF_SIZE:int = 166;
      
      private static const ASSET_ALPHA:Number = 0.6;
       
      
      private var _disposed:Boolean = false;
      
      private var _darkening:Sprite = null;
      
      private var _holeBitmap:BitmapData = null;
      
      private var _backgroundAlpha:Number = 0.6;
      
      private var _stageWidth:int = 0;
      
      private var _stageHeight:int = 0;
      
      public function BackGround()
      {
         super();
         this._darkening = new Sprite();
         this._darkening.mouseEnabled = false;
         addChildAt(this._darkening,0);
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         if(this._darkening != null)
         {
            this._darkening.graphics.clear();
            if(contains(this._darkening))
            {
               removeChild(this._darkening);
            }
            this._darkening = null;
         }
         if(this._holeBitmap != null)
         {
            this._holeBitmap.dispose();
            this._holeBitmap = null;
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function redraw() : void
      {
         this.drawDarkening();
      }
      
      public function setBackgroundAlpha(param1:Number) : void
      {
         this._backgroundAlpha = param1;
         this.applyDarkeningAlpha();
      }
      
      public function setSize(param1:int, param2:int) : void
      {
         if(this._stageWidth == param1 && this._stageHeight == param2)
         {
            return;
         }
         this._stageWidth = param1;
         this._stageHeight = param2;
         this.drawDarkening();
      }
      
      private function drawDarkening() : void
      {
         var _loc1_:Graphics = this._darkening.graphics;
         _loc1_.clear();
         if(this._stageWidth <= 0 || this._stageHeight <= 0)
         {
            return;
         }
         var _loc2_:int = this.holeHalfSize;
         if(this._holeBitmap == null)
         {
            this._holeBitmap = this.createHoleBitmap();
         }
         var _loc3_:int = _loc2_ << 1;
         if(this._holeBitmap == null || this._holeBitmap.width < _loc3_ || this._holeBitmap.height < _loc3_)
         {
            DebugUtils.LOG_ERROR("BackGround: no vignette of " + _loc3_ + " for " + HOLE_LINKAGE);
            return;
         }
         var _loc4_:int = Math.floor(-x - (parent != null ? parent.x : 0)) - 1;
         var _loc5_:int = Math.floor(-y - (parent != null ? parent.y : 0)) - 1;
         var _loc6_:Matrix = new Matrix();
         _loc6_.translate(-_loc2_,-_loc2_);
         _loc1_.beginBitmapFill(this._holeBitmap,_loc6_,false,false);
         _loc1_.drawRect(_loc4_,_loc5_,this._stageWidth + 2,this._stageHeight + 2);
         _loc1_.endFill();
         this.applyDarkeningAlpha();
      }
      
      private function createHoleBitmap() : BitmapData
      {
         if(App.utils.classFactory == null)
         {
            return null;
         }
         return App.utils.classFactory.getObject(HOLE_LINKAGE) as BitmapData;
      }
      
      private function applyDarkeningAlpha() : void
      {
         this._darkening.alpha = this._backgroundAlpha / ASSET_ALPHA;
      }
      
      protected function get holeHalfSize() : int
      {
         return HOLE_HALF_SIZE;
      }
   }
}
