package net.wg.gui.battle.views.widgetsPanel.temperatureGun
{
   import flash.display.BitmapData;
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.geom.Matrix;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.utils.GraphicsUtilities;
   
   public class TemperatureGunScaleSector extends BattleUIComponent
   {
      
      public static const PROGRESS_ROTATION_ANGLE:Number = 73.5;
      
      private static const SCALE_START_ANGLE:Number = -Math.PI / 2;
      
      private static const SCALE_ARC_LENGTH:Number = -Math.PI / 180 * PROGRESS_ROTATION_ANGLE;
      
      private static const CONTENT_RADIUS:Number = 280;
       
      
      public var content:Sprite;
      
      public var marker:Sprite;
      
      private var _bitmapData:BitmapData = null;
      
      private var _forceRedraw:Boolean = false;
      
      private var _minThreshold:Number = 0;
      
      private var _maxThreshold:Number = 1;
      
      private var _currProgress:Number = 1;
      
      private var _lastAngle:Number = NaN;
      
      private var _lastArc:Number = NaN;
      
      public function TemperatureGunScaleSector()
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
         this.marker = null;
         super.onDispose();
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
      
      private function normalize(param1:Number) : Number
      {
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
         if(this.marker)
         {
            this.marker.visible = _loc4_ > 0;
            if(this.marker.visible)
            {
               this.marker.rotation = _loc3_ * PROGRESS_ROTATION_ANGLE;
            }
         }
         _loc2_.clear();
         if(!this._bitmapData || _loc4_ <= 0)
         {
            return;
         }
         var _loc9_:Matrix = new Matrix();
         _loc9_.translate(-this._bitmapData.width,0);
         _loc2_.lineStyle();
         _loc2_.beginBitmapFill(this._bitmapData,_loc9_,false,true);
         _loc2_.lineTo(_loc6_,_loc7_);
         GraphicsUtilities.drawArc(_loc2_,0,0,_loc5_,_loc8_,CONTENT_RADIUS);
         _loc2_.lineTo(0,0);
         _loc2_.endFill();
      }
   }
}
