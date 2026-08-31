package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import flash.display.GradientType;
   import flash.display.Shape;
   import flash.display.SpreadMethod;
   import flash.events.Event;
   import flash.events.EventDispatcher;
   import flash.geom.Matrix;
   import net.wg.data.constants.generated.LOW_CHARGE_SHOT_CONSTS;
   import net.wg.gui.utils.GraphicsUtilities;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class MarkerDrawer extends EventDispatcher implements IDisposable
   {
      
      private static const LINE_NO_SCALE:String = "none";
      
      private static const LINE_SCALE_NORMAL:String = "normal";
      
      private static const LINE_NO_CAPS:String = "none";
      
      private static const PI_X2:Number = Math.PI * 2;
      
      private static const RADIUS:int = 256;
      
      private static const CIRCLE_ALPHA:int = 1;
      
      private static const SHOT_GAP_X4:Number = 4;
      
      private static const SHOT_GAP_X8:Number = 6;
      
      private static const SHOT_GAP_X16:Number = 9;
      
      private static const GRADIENT_SIZE_RATIO_SMALL:Number = 1.2;
      
      private static const GRADIENT_SIZE_RATIO_BIG:Number = 0.7;
      
      private static const GRADIENT_ALPHAS:Array = [1,0.35,0.18,0];
      
      private static const GRADIENT_RATIOS:Array = [169,199,214,235];
      
      private static const BLOCK_ALPHA:Number = 0.4;
      
      private static const BLOCK_THICKNESS_SMALL:Number = 1.5;
      
      private static const BLOCK_THICKNESS_BIG:int = 2;
      
      private static const THIN_THICKNESS:int = 1;
      
      private static const ZOOM_X4:int = 4;
      
      private static const ZOOM_X8:int = 8;
      
      private static const SMALL_SHOT_GAP_PROP:Number = 0.8;
      
      private static const TICK_SIZE_RATIO_X4_SMALL:Number = 0.01;
      
      private static const TICK_SIZE_RATIO_X4_BIG:Number = 0.02;
      
      private static const TICK_SIZE_RATIO_X8:Number = 0.028;
      
      private static const TICK_SIZE_RATIO_X16:Number = 0.035;
      
      private static const POINTER_SIZE:Number = 3.5;
      
      private static const TICK_SCALE_MAX:Number = 0.1;
      
      private static const TICK_SCALE_MIN:Number = 0.0625;
      
      private static const MIN_POINTER_LENGTH:Number = 1.3;
       
      
      private var _commonLayer:Shape = null;
      
      private var _blendedLayer:Shape = null;
      
      private var _colors:ColorsProvider;
      
      private var _isDisposed:Boolean = false;
      
      private var _gradientMatrix:Matrix;
      
      private var _gradientAlphas:Array;
      
      private var _gradientColors:Array = null;
      
      private var _zoomFactor:Number = 1.0;
      
      private var _lowChargeCap:Number = 0;
      
      private var _blockStageCap:Number = 0;
      
      private var _counterScale:Number = 0;
      
      private var _curPercents:Number = 0;
      
      private var _gunState:Number = 0;
      
      private var _isInvalid:Boolean = false;
      
      public function MarkerDrawer(param1:Shape, param2:Shape)
      {
         this._colors = new ColorsProvider();
         this._gradientMatrix = new Matrix();
         this._gradientAlphas = [0,0,0,0];
         super();
         this._commonLayer = param1;
         this._blendedLayer = param2;
         var _loc3_:uint = this._colors.glowColor;
         this._gradientColors = [_loc3_,_loc3_,_loc3_,_loc3_];
         this._colors.addEventListener(Event.RENDER,this.onColorsRenderHandler);
      }
      
      private static function clamp(param1:Number, param2:Number, param3:Number) : Number
      {
         return param1 < param2 ? Number(param2) : (param1 > param3 ? Number(param3) : Number(param1));
      }
      
      public final function dispose() : void
      {
         if(!this._isDisposed)
         {
            this._commonLayer = null;
            this._blendedLayer = null;
            this._colors.removeEventListener(Event.RENDER,this.onColorsRenderHandler);
            this._colors = null;
            this._isDisposed = true;
         }
      }
      
      public function draw() : void
      {
         if(!this._isInvalid)
         {
            return;
         }
         switch(this._gunState)
         {
            case LOW_CHARGE_SHOT_CONSTS.STATE_NONE:
            case LOW_CHARGE_SHOT_CONSTS.INITIAL_RELOAD:
               this.drawInitialReload();
               break;
            case LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE:
               this.drawLowCharge();
               break;
            case LOW_CHARGE_SHOT_CONSTS.ALMOST_FINISHED:
               this.drawAlmostFinished();
               break;
            case LOW_CHARGE_SHOT_CONSTS.FULL_CHARGE:
               this.drawFullCharge();
               break;
            case LOW_CHARGE_SHOT_CONSTS.QUICK_RELOAD:
               this.drawQuickReload();
               break;
            case LOW_CHARGE_SHOT_CONSTS.EMPTY:
               this.drawEmpty();
         }
         this._isInvalid = false;
      }
      
      public function drawAlmostFinished() : void
      {
         this.clear();
         this.drawArc(this._commonLayer,this._colors.colorLoaded,this.boldThickness,CIRCLE_ALPHA,this.shotGap,Math.max(this._curPercents,1 - this._blockStageCap));
         this.drawArc(this._commonLayer,this._colors.colorBlockEnabled,this.boldThickness,CIRCLE_ALPHA,this.blockStageStartPosition,1);
         this.drawPointer(this._curPercents);
      }
      
      public function drawEmpty() : void
      {
         this.clear();
         this.drawArc(this._commonLayer,this._colors.colorLeft,THIN_THICKNESS,CIRCLE_ALPHA,this.shotGap,this._lowChargeCap);
         this.drawArc(this._commonLayer,this._colors.colorLeft,THIN_THICKNESS,CIRCLE_ALPHA,this._lowChargeCap + this.shotGap,1);
         this.drawTick(this._lowChargeCap,this.boldThickness,this.tickSizeRatio,this._colors.colorLeft,1);
      }
      
      public function drawFullCharge() : void
      {
         this.clear();
         this.drawArc(this._commonLayer,this._colors.colorLoaded,this.boldThickness,CIRCLE_ALPHA,0,1);
      }
      
      public function drawInitialReload() : void
      {
         this.clear();
         this.drawArc(this._commonLayer,this._colors.colorLoaded,THIN_THICKNESS,CIRCLE_ALPHA,this.shotGap,this._curPercents);
         this.drawArc(this._commonLayer,this._colors.colorLeft,THIN_THICKNESS,CIRCLE_ALPHA,this._curPercents,this._lowChargeCap);
         this.drawArc(this._commonLayer,this._colors.colorLeft,THIN_THICKNESS,CIRCLE_ALPHA,this._lowChargeCap + this.shotGap,1);
         this.drawTick(this._lowChargeCap,this.boldThickness,this.tickSizeRatio,this._colors.colorLeft,1);
      }
      
      public function drawLowCharge() : void
      {
         this.clear();
         var _loc1_:Number = 1 - this._colors.glowCircleAlpha;
         if(this._colors.glowAlpha > 0)
         {
            this.drawArcGradient(this._blendedLayer,this.gradientSizeRatio,this.shotGap,this._lowChargeCap,this._colors.glowAlpha,RADIUS);
         }
         this.drawArc(this._commonLayer,this._colors.colorLoaded,THIN_THICKNESS,_loc1_,this.shotGap,this._lowChargeCap);
         this.drawArc(this._commonLayer,this._colors.colorLoaded,this.boldThickness,_loc1_,this._lowChargeCap + this.shotGap,Math.max(this._curPercents,this._lowChargeCap + this.shotGap));
         this.drawTick(this._lowChargeCap,this.boldThickness,this.tickSizeRatio,this._colors.colorLoaded,_loc1_);
         this.drawArc(this._commonLayer,this._colors.colorLeftLowCharge,THIN_THICKNESS,_loc1_,clamp(this._curPercents + this.smallShotGap,this._lowChargeCap + this.smallShotGap,1 - this._blockStageCap - this.smallShotGap),1 - this._blockStageCap);
         this.drawArc(this._commonLayer,this._colors.colorBlockDisabled,this.boldThickness,BLOCK_ALPHA * _loc1_,1 - this._blockStageCap + this.shotGap,1);
         if(this._colors.glowCircleAlpha > 0)
         {
            this.drawArc(this._commonLayer,this._colors.glowColor,this.boldThickness,this._colors.glowCircleAlpha,this.shotGap,this._lowChargeCap);
            this.drawArc(this._commonLayer,this._colors.glowColor,this.boldThickness,this._colors.glowCircleAlpha,this._lowChargeCap + this.shotGap,1);
            this.drawTick(this._lowChargeCap,this.boldThickness,this.tickSizeRatio,this._colors.glowColor,this._colors.glowCircleAlpha);
         }
         if(this._curPercents >= this._lowChargeCap + this.shotGap)
         {
            this.drawPointer(this._curPercents);
         }
      }
      
      public function drawQuickReload() : void
      {
         this.clear();
         this.drawArc(this._commonLayer,this._colors.colorLoaded,this.boldThickness,CIRCLE_ALPHA,0,Math.min(this._curPercents,1));
         this.drawArc(this._commonLayer,this._colors.colorLeft,THIN_THICKNESS,CIRCLE_ALPHA,this._curPercents,1);
      }
      
      public function invalidate() : void
      {
         this._isInvalid = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         if(this._colors.isColorBlind != param1)
         {
            this._colors.isColorBlind = param1;
            this.invalidate();
         }
      }
      
      public function setLowChargeShotGunStageCaps(param1:Number, param2:Number) : void
      {
         if(this._lowChargeCap != param1 && this._blockStageCap != param2)
         {
            this._lowChargeCap = param1;
            this._blockStageCap = param2;
            this.invalidate();
         }
      }
      
      private function clear() : void
      {
         this._commonLayer.graphics.clear();
         this._blendedLayer.graphics.clear();
      }
      
      private function drawTick(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number) : void
      {
         var _loc6_:Number = param1 * PI_X2;
         var _loc7_:Number = RADIUS * param3 / this._counterScale;
         this._commonLayer.graphics.lineStyle(param2,param4,param5,false,LINE_NO_SCALE,LINE_NO_CAPS);
         this._commonLayer.graphics.moveTo(Math.cos(_loc6_) * RADIUS,Math.sin(_loc6_) * RADIUS);
         this._commonLayer.graphics.lineTo(Math.cos(_loc6_) * (RADIUS + _loc7_),Math.sin(_loc6_) * (RADIUS + _loc7_));
      }
      
      private function drawPointer(param1:Number) : void
      {
         var _loc3_:Number = NaN;
         var _loc2_:Number = param1 * PI_X2;
         _loc3_ = Math.max(MIN_POINTER_LENGTH,this.pointerSize / this._counterScale);
         this._commonLayer.graphics.lineStyle(this.boldThickness,this._colors.colorPointer,1,false,"normal",LINE_NO_CAPS);
         var _loc4_:Number = RADIUS - (_loc3_ - this.boldThickness >> 1);
         var _loc5_:Number = RADIUS + (_loc3_ + this.boldThickness >> 1);
         this._commonLayer.graphics.moveTo(Math.cos(_loc2_) * _loc4_,Math.sin(_loc2_) * _loc4_);
         this._commonLayer.graphics.lineTo(Math.cos(_loc2_) * _loc5_,Math.sin(_loc2_) * _loc5_);
      }
      
      private function drawArc(param1:Shape, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number = 256) : void
      {
         var _loc8_:Number = param5 * PI_X2;
         var _loc9_:Number = param6 * PI_X2;
         var _loc10_:Number = -(_loc9_ - _loc8_);
         param1.graphics.lineStyle(param3,param2,param4,false,LINE_NO_SCALE,LINE_NO_CAPS);
         GraphicsUtilities.drawArc(param1.graphics,0,0,-_loc8_ - PI_X2,_loc10_,param7 + param3 * 0.5);
      }
      
      private function drawArcGradient(param1:Shape, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number) : void
      {
         var _loc7_:Number = param6 * param2;
         param6 += _loc7_ >> 1;
         var _loc8_:Number = param3 * PI_X2;
         var _loc9_:Number = param4 * PI_X2;
         var _loc10_:Number = -(_loc9_ - _loc8_);
         var _loc11_:Number = param6 << 1;
         this._gradientMatrix.createGradientBox(_loc11_,_loc11_,0,-param6,-param6);
         var _loc12_:int = GRADIENT_ALPHAS.length;
         var _loc13_:int = 0;
         while(_loc13_ < _loc12_)
         {
            this._gradientAlphas[_loc13_] = GRADIENT_ALPHAS[_loc13_] * param5;
            _loc13_++;
         }
         param1.graphics.lineStyle(_loc7_,0,1,false,LINE_SCALE_NORMAL,LINE_NO_CAPS);
         param1.graphics.lineGradientStyle(GradientType.RADIAL,this._gradientColors,this._gradientAlphas,GRADIENT_RATIOS,this._gradientMatrix,SpreadMethod.PAD);
         GraphicsUtilities.drawArc(param1.graphics,0,0,-_loc8_ - PI_X2,_loc10_,param6);
      }
      
      public function get zoomFactor() : Number
      {
         return this._zoomFactor;
      }
      
      public function set zoomFactor(param1:Number) : void
      {
         if(this._zoomFactor != param1)
         {
            this._zoomFactor = param1;
            this.invalidate();
         }
      }
      
      public function get counterScale() : Number
      {
         return this._counterScale;
      }
      
      public function set counterScale(param1:Number) : void
      {
         if(this._counterScale != param1)
         {
            this._counterScale = param1;
            this.invalidate();
         }
      }
      
      public function set curPercents(param1:Number) : void
      {
         if(this._curPercents != param1)
         {
            this._curPercents = param1;
            this.invalidate();
         }
      }
      
      public function set gunState(param1:Number) : void
      {
         if(this._gunState != param1)
         {
            this._gunState = param1;
            if(this._gunState == LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE)
            {
               this._colors.pulseGlow();
            }
            this.invalidate();
         }
      }
      
      private function get blockStageStartPosition() : Number
      {
         return Math.min(1 - this._blockStageCap * this.blockProgress + this.smallShotGap,1);
      }
      
      private function get smallShotGap() : Number
      {
         return this.shotGap * SMALL_SHOT_GAP_PROP;
      }
      
      private function get shotGap() : Number
      {
         var _loc1_:Number = NaN;
         if(this._zoomFactor <= ZOOM_X4)
         {
            _loc1_ = SHOT_GAP_X4;
         }
         else if(this._zoomFactor <= ZOOM_X8)
         {
            _loc1_ = SHOT_GAP_X8;
         }
         else
         {
            _loc1_ = SHOT_GAP_X16;
         }
         var _loc2_:Number = RADIUS + (THIN_THICKNESS >> 1);
         var _loc3_:Number = _loc1_ / this._counterScale;
         return _loc3_ / _loc2_ / PI_X2;
      }
      
      private function get pointerSize() : Number
      {
         return POINTER_SIZE;
      }
      
      private function get gradientSizeRatio() : Number
      {
         return this._zoomFactor <= ZOOM_X8 ? Number(GRADIENT_SIZE_RATIO_SMALL) : Number(GRADIENT_SIZE_RATIO_BIG);
      }
      
      private function get tickSizeRatio() : Number
      {
         var _loc1_:Number = NaN;
         if(this._zoomFactor <= ZOOM_X4)
         {
            if(this._counterScale >= TICK_SCALE_MAX)
            {
               return TICK_SIZE_RATIO_X4_BIG;
            }
            if(this._counterScale <= TICK_SCALE_MIN)
            {
               return TICK_SIZE_RATIO_X4_SMALL;
            }
            _loc1_ = (TICK_SCALE_MAX - this._counterScale) / (TICK_SCALE_MAX - TICK_SCALE_MIN);
            return TICK_SIZE_RATIO_X4_BIG + (TICK_SIZE_RATIO_X4_SMALL - TICK_SIZE_RATIO_X4_BIG) * _loc1_;
         }
         if(this._zoomFactor <= ZOOM_X8)
         {
            return TICK_SIZE_RATIO_X8;
         }
         return TICK_SIZE_RATIO_X16;
      }
      
      private function get boldThickness() : Number
      {
         return this._zoomFactor <= ZOOM_X4 ? Number(BLOCK_THICKNESS_SMALL) : Number(BLOCK_THICKNESS_BIG);
      }
      
      private function get blockProgress() : Number
      {
         var _loc1_:Number = clamp((1 - this._curPercents) / this._blockStageCap,0,1);
         return this._gunState == LOW_CHARGE_SHOT_CONSTS.ALMOST_FINISHED ? Number(_loc1_) : Number(1);
      }
      
      private function onColorsRenderHandler(param1:Event) : void
      {
         dispatchEvent(new Event(Event.RENDER));
      }
   }
}
