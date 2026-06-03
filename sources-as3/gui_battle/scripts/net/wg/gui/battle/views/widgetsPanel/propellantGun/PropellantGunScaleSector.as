package net.wg.gui.battle.views.widgetsPanel.propellantGun
{
   import flash.display.BitmapData;
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.geom.Matrix;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.utils.GraphicsUtilities;
   
   public class PropellantGunScaleSector extends BattleUIComponent
   {
      
      public static const BITMAP_ALIGN_DEFAULT:String = "none";
      
      public static const BITMAP_ALIGN_TO_MIN:String = "toMin";
      
      public static const BITMAP_ALIGN_TO_MAX:String = "toMax";
      
      private static const CONTENT_RADIUS:Number = 400;
      
      private static const SCALE_ARC_LENGTH:Number = Math.PI / 180 * 32;
      
      private static const SCALE_START_ANGLE:Number = -SCALE_ARC_LENGTH / 2;
      
      private static const BITMAP_OFFSET_X:Number = 360;
       
      
      public var content:Sprite;
      
      private var _bitmapData:BitmapData = null;
      
      private var _bitmapAlign:String = "none";
      
      private var _forceRedraw:Boolean = false;
      
      private var _minThreshold:Number = 0;
      
      private var _maxThreshold:Number = 1;
      
      private var _currProgress:Number = 1;
      
      private var _snapValues:Boolean = true;
      
      private var _lastAngle:Number = NaN;
      
      private var _lastArc:Number = NaN;
      
      public function PropellantGunScaleSector()
      {
         super();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.drawContent(this._forceRedraw);
            this._forceRedraw = false;
         }
      }
      
      override protected function onDispose() : void
      {
         this._bitmapData = null;
         this.content = null;
         super.onDispose();
      }
      
      private function normalize(param1:Number) : Number
      {
         if(!this._snapValues)
         {
            return param1;
         }
         return param1 >= 0 ? (param1 <= 1 ? Number(param1) : Number(1)) : Number(0);
      }
      
      private function drawContent(param1:Boolean = false) : void
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc2_:Graphics = this.content.graphics;
         _loc3_ = Math.min(this._currProgress,this._maxThreshold);
         _loc4_ = _loc3_ - this._minThreshold;
         _loc5_ = SCALE_START_ANGLE + this._minThreshold * SCALE_ARC_LENGTH;
         var _loc6_:Number = CONTENT_RADIUS * Math.cos(_loc5_);
         var _loc7_:Number = CONTENT_RADIUS * Math.sin(-_loc5_);
         var _loc8_:Number = _loc4_ * SCALE_ARC_LENGTH;
         if(!param1 && _loc5_ == this._lastAngle && _loc8_ == this._lastArc)
         {
            return;
         }
         this._lastAngle = _loc5_;
         this._lastArc = _loc8_;
         _loc2_.clear();
         if(!this._bitmapData || _loc4_ <= 0)
         {
            return;
         }
         var _loc9_:Matrix = new Matrix();
         _loc9_.translate(BITMAP_OFFSET_X - this._bitmapData.width,-this._bitmapData.height >> 1);
         switch(this._bitmapAlign)
         {
            case BITMAP_ALIGN_TO_MIN:
               _loc9_.rotate(this._minThreshold * -SCALE_ARC_LENGTH);
               break;
            case BITMAP_ALIGN_TO_MAX:
               _loc9_.rotate((1 - this._maxThreshold) * SCALE_ARC_LENGTH);
               break;
            case BITMAP_ALIGN_DEFAULT:
         }
         _loc2_.lineStyle();
         _loc2_.beginBitmapFill(this._bitmapData,_loc9_,false,true);
         _loc2_.lineTo(_loc6_,_loc7_);
         GraphicsUtilities.drawArc(_loc2_,0,0,_loc5_,_loc8_,CONTENT_RADIUS);
         _loc2_.lineTo(0,0);
         _loc2_.endFill();
      }
      
      public function set state(param1:String) : void
      {
         if(param1 == this.currentLabel)
         {
            return;
         }
         this.gotoAndPlay(param1);
      }
      
      public function set bitmapData(param1:BitmapData) : void
      {
         if(param1 == this._bitmapData)
         {
            return;
         }
         this._bitmapData = param1;
         this._forceRedraw = true;
         invalidateData();
      }
      
      public function set bitmapAlign(param1:String) : void
      {
         if(param1 == this._bitmapAlign)
         {
            return;
         }
         this._bitmapAlign = param1;
         this._forceRedraw = true;
         invalidateData();
      }
      
      public function get minThreshold() : Number
      {
         return this._minThreshold;
      }
      
      public function set minThreshold(param1:Number) : void
      {
         param1 = this.normalize(param1);
         if(param1 == this._minThreshold)
         {
            return;
         }
         this._minThreshold = param1;
         invalidateData();
      }
      
      public function get maxThreshold() : Number
      {
         return this._maxThreshold;
      }
      
      public function set maxThreshold(param1:Number) : void
      {
         param1 = this.normalize(param1);
         if(param1 == this._maxThreshold)
         {
            return;
         }
         this._maxThreshold = param1;
         invalidateData();
      }
      
      public function set currProgress(param1:Number) : void
      {
         param1 = this.normalize(param1);
         if(param1 == this._currProgress)
         {
            return;
         }
         this._currProgress = param1;
         invalidateData();
      }
      
      public function set snapValues(param1:Boolean) : void
      {
         if(param1 == this._snapValues)
         {
            return;
         }
         this._snapValues = param1;
         if(this._snapValues)
         {
            this._currProgress = this.normalize(this._currProgress);
            this._minThreshold = this.normalize(this._minThreshold);
            this._maxThreshold = this.normalize(this._maxThreshold);
            invalidateData();
         }
      }
   }
}
