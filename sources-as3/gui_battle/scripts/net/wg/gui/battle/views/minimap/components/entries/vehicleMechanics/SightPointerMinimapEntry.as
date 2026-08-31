package net.wg.gui.battle.views.minimap.components.entries.vehicleMechanics
{
   import flash.display.CapsStyle;
   import flash.display.GradientType;
   import flash.display.Graphics;
   import flash.display.LineScaleMode;
   import flash.display.MovieClip;
   import flash.geom.Matrix;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.utils.GraphicsUtilities;
   
   public class SightPointerMinimapEntry extends BattleUIComponent
   {
      
      private static const AREA_MAX_SIZE_REAL:uint = 210;
      
      private static const DEG_TO_RAD:Number = 1 / 180 * Math.PI;
      
      private static const SECTOR_ROTATION:Number = 90;
      
      private static const STROKE_THICKNESS:int = 1;
      
      private static const DASH_LINE_LENGTH:int = 2;
      
      private static const DASH_LINE_GAP:int = 2;
      
      private static const DASH_LINE_COLOR:int = 16515071;
      
      private static const DASH_LINE_ALPHA:Number = 0.8;
      
      private static const SECTOR_TIP_COLOR:int = 16777215;
      
      private static const SECTOR_TIP_ALPHA:Number = 0.4;
      
      private static const HIGHLIGHT_LENGTH:int = 108;
       
      
      private var _arenaWidth:int = 0;
      
      private var _viewRange:int = 0;
      
      private var _viewAngle:Number = 0;
      
      private var _minViewAngle:Number = 0;
      
      private const GRADIENT_COLORS:Array = [13565943,15918847];
      
      private const GRADIENT_ALPHAS:Array = [0.3,0.12];
      
      private const GRADIENT_RATIOS:Array = [75,255];
      
      private const EDGES_COLORS:Array = [16777215,16777215,16777215];
      
      private const EDGES_ALPHAS:Array = [0,0.9,0.3];
      
      private const EDGES_RATIOS:Array = [0,15,255];
      
      private var gradientMatrix:Matrix;
      
      public var highlightLeft:MovieClip;
      
      public var highlightRight:MovieClip;
      
      public function SightPointerMinimapEntry()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.gradientMatrix = new Matrix();
         this.drawEdges();
      }
      
      override protected function onDispose() : void
      {
         super.onDispose();
         this.gradientMatrix = null;
         this.highlightLeft = null;
         this.highlightRight = null;
      }
      
      public function as_initArenaSize(param1:int, param2:int) : void
      {
         this._arenaWidth = param1;
         invalidateData();
      }
      
      public function as_setViewRange(param1:int) : void
      {
         this._viewRange = param1;
         invalidateData();
      }
      
      public function as_setViewAngle(param1:Number) : void
      {
         this._viewAngle = param1;
         invalidateData();
      }
      
      public function as_setMinViewAngle(param1:Number) : void
      {
         this._minViewAngle = param1;
         invalidateData();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Number = NaN;
         if(!isInvalid(InvalidationType.DATA))
         {
            return;
         }
         _loc1_ = AREA_MAX_SIZE_REAL / this._arenaWidth;
         var _loc2_:Number = this._viewRange * _loc1_;
         var _loc3_:Number = (-this._viewAngle / 2 + SECTOR_ROTATION) * DEG_TO_RAD;
         var _loc4_:Number = this._viewAngle * DEG_TO_RAD;
         graphics.clear();
         this.drawSector(_loc2_,_loc3_,_loc4_);
         this.drawTip(_loc2_,_loc3_,_loc4_);
         this.drawHighlights(_loc2_);
         if(this._viewAngle != this._minViewAngle)
         {
            this.drawDashLines(_loc2_);
         }
      }
      
      private function drawEdges() : void
      {
         this.gradientMatrix.createGradientBox(HIGHLIGHT_LENGTH * 2,HIGHLIGHT_LENGTH * 2,0,-HIGHLIGHT_LENGTH,-HIGHLIGHT_LENGTH);
         this.drawEdge(this.highlightLeft.graphics);
         this.drawEdge(this.highlightRight.graphics);
      }
      
      private function drawEdge(param1:Graphics) : void
      {
         param1.clear();
         param1.lineStyle(STROKE_THICKNESS,0,1,false,LineScaleMode.NONE);
         param1.lineGradientStyle(GradientType.RADIAL,this.EDGES_COLORS,this.EDGES_ALPHAS,this.EDGES_RATIOS,this.gradientMatrix);
         param1.lineTo(0,-HIGHLIGHT_LENGTH);
      }
      
      private function drawSector(param1:Number, param2:Number, param3:Number) : void
      {
         this.gradientMatrix.createGradientBox(param1 * 2,param1 * 2,0,-param1,-param1);
         graphics.lineStyle();
         graphics.beginGradientFill(GradientType.RADIAL,this.GRADIENT_COLORS,this.GRADIENT_ALPHAS,this.GRADIENT_RATIOS,this.gradientMatrix);
         graphics.moveTo(0,0);
         GraphicsUtilities.drawArc(graphics,0,0,param2,param3,param1,true);
         graphics.lineTo(0,0);
         graphics.endFill();
      }
      
      private function drawTip(param1:Number, param2:Number, param3:Number) : void
      {
         graphics.lineStyle(STROKE_THICKNESS,SECTOR_TIP_COLOR,SECTOR_TIP_ALPHA,false,LineScaleMode.NONE,CapsStyle.NONE);
         GraphicsUtilities.drawArc(graphics,0,0,param2,param3,param1);
      }
      
      private function drawHighlights(param1:Number) : void
      {
         this.highlightLeft.scaleY = this.highlightRight.scaleY = Math.min(1,param1 / HIGHLIGHT_LENGTH);
         this.highlightLeft.rotation = -this._viewAngle / 2;
         this.highlightRight.rotation = this._viewAngle / 2;
      }
      
      private function drawDashLines(param1:Number) : void
      {
         var _loc2_:Number = (-this._minViewAngle / 2 - SECTOR_ROTATION) * DEG_TO_RAD;
         var _loc3_:Number = (this._minViewAngle / 2 - SECTOR_ROTATION) * DEG_TO_RAD;
         graphics.lineStyle(STROKE_THICKNESS,DASH_LINE_COLOR,DASH_LINE_ALPHA,false,LineScaleMode.NONE,CapsStyle.NONE);
         GraphicsUtilities.drawDashLine(graphics,param1,DASH_LINE_LENGTH,DASH_LINE_GAP,_loc2_);
         GraphicsUtilities.drawDashLine(graphics,param1,DASH_LINE_LENGTH,DASH_LINE_GAP,_loc3_);
      }
   }
}
