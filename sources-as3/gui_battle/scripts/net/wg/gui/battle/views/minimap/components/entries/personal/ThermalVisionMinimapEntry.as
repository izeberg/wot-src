package net.wg.gui.battle.views.minimap.components.entries.personal
{
   import flash.display.GradientType;
   import flash.display.Graphics;
   import flash.display.SpreadMethod;
   import flash.display.Sprite;
   import flash.geom.Matrix;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class ThermalVisionMinimapEntry extends BattleUIComponent
   {
      
      private static const LINE_STYLE_THICKNESS:Number = 0.5;
      
      private static const SECTOR_COLOR:uint = 8378677;
      
      private static const SECTOR_COLOR_DISABLED:uint = 9013641;
      
      private static const SECTOR_FILL_ALPHA:Number = 0.25;
      
      private static const SECTOR_FILL_ALPHA_DISABLED:Number = 0.4;
      
      private static const SECTOR_FILL_ALPHA_GRADIENT:Number = 0.1;
      
      private static const SECTOR_EDGE_ALPHA:Number = 0.2;
      
      private static const SECTOR_EDGE_ALPHA_DISABLED:Number = 0.3;
      
      private static const DEGREE_360:int = 360;
      
      private static const ROTATION_90:int = 90;
      
      private static const PI2:Number = 6.2831;
      
      private static const DIVISIONS_PER_RADIAN:uint = 8;
      
      private static const DEFAULT_MAP_SIZE:int = 210;
       
      
      private var _isEnabled:Boolean = false;
      
      private var _distance:Number = 0;
      
      private var _fov:Number = 0;
      
      private var _fill:Sprite = null;
      
      private var _leftEdge:Sprite = null;
      
      private var _rightEdge:Sprite = null;
      
      private var _mapSizeKoef:Number = 1;
      
      public function ThermalVisionMinimapEntry()
      {
         super();
      }
      
      private static function drawSectorFill(param1:Graphics, param2:int, param3:Number, param4:uint, param5:Number) : void
      {
         var _loc16_:uint = 0;
         var _loc6_:String = GradientType.RADIAL;
         var _loc7_:String = SpreadMethod.PAD;
         var _loc8_:Array = [param4,param4,param4];
         var _loc9_:Array = [param5,param5,Math.max(param5 - SECTOR_FILL_ALPHA_GRADIENT,0)];
         var _loc10_:Array = [0,220,255];
         var _loc11_:Matrix = new Matrix();
         var _loc12_:int = param2 * 2;
         _loc11_.createGradientBox(_loc12_,_loc12_,0,-param2,-param2);
         param1.clear();
         param1.beginGradientFill(_loc6_,_loc8_,_loc9_,_loc10_,_loc11_,_loc7_);
         param1.moveTo(0,0);
         var _loc13_:Number = param3 / DEGREE_360 * PI2;
         var _loc14_:uint = Math.round(_loc13_ * DIVISIONS_PER_RADIAN);
         var _loc15_:Number = 0;
         _loc16_ = 0;
         while(_loc16_ <= _loc14_)
         {
            _loc15_ = _loc16_ / _loc14_ * _loc13_;
            param1.lineTo(Math.sin(_loc15_) * param2,-Math.cos(_loc15_) * param2);
            _loc16_++;
         }
         param1.lineTo(0,0);
         param1.endFill();
      }
      
      private static function drawSectorEdge(param1:Graphics, param2:Number, param3:Number, param4:uint, param5:Number) : void
      {
         var _loc6_:String = GradientType.LINEAR;
         var _loc7_:String = SpreadMethod.PAD;
         var _loc8_:Array = [param4,param4,param4];
         var _loc9_:Array = [1,1,param5];
         var _loc10_:Array = [0,140,255];
         var _loc11_:Matrix = new Matrix();
         _loc11_.createGradientBox(param2,param3,0,0,0);
         param1.clear();
         param1.beginGradientFill(_loc6_,_loc8_,_loc9_,_loc10_,_loc11_,_loc7_);
         param1.drawRect(0,0,param2,param3);
         param1.endFill();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._fill = new Sprite();
         addChild(this._fill);
         this._leftEdge = new Sprite();
         addChild(this._leftEdge);
         this._rightEdge = new Sprite();
         addChild(this._rightEdge);
      }
      
      override protected function onDispose() : void
      {
         this._fill = null;
         this._leftEdge = null;
         this._rightEdge = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         var _loc2_:Number = NaN;
         var _loc3_:uint = 0;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         super.draw();
         if(isInvalid(InvalidationType.DATA) || isInvalid(InvalidationType.STATE))
         {
            _loc1_ = this._distance * this._mapSizeKoef | 0;
            _loc2_ = this._fov * 0.5;
            _loc3_ = !!this._isEnabled ? uint(SECTOR_COLOR) : uint(SECTOR_COLOR_DISABLED);
            _loc4_ = !!this._isEnabled ? Number(SECTOR_FILL_ALPHA) : Number(SECTOR_FILL_ALPHA_DISABLED);
            drawSectorFill(this._fill.graphics,_loc1_,this._fov,_loc3_,_loc4_);
            this._fill.rotation = -_loc2_;
            this._leftEdge.graphics.clear();
            this._rightEdge.graphics.clear();
            if(Math.abs(this._fov) < DEGREE_360)
            {
               _loc5_ = !!this._isEnabled ? Number(SECTOR_EDGE_ALPHA) : Number(SECTOR_EDGE_ALPHA_DISABLED);
               drawSectorEdge(this._leftEdge.graphics,_loc1_,LINE_STYLE_THICKNESS,_loc3_,_loc5_);
               this._leftEdge.rotation = -_loc2_ - ROTATION_90;
               drawSectorEdge(this._rightEdge.graphics,_loc1_,LINE_STYLE_THICKNESS,_loc3_,_loc5_);
               this._rightEdge.rotation = _loc2_ - ROTATION_90;
            }
         }
      }
      
      private function updateEntryScaleFactor(param1:int) : void
      {
         this._mapSizeKoef = DEFAULT_MAP_SIZE / param1;
         invalidateData();
      }
      
      public function as_initMapSize(param1:int) : void
      {
         this.updateEntryScaleFactor(param1);
      }
      
      public function as_setSectorSettings(param1:Number, param2:Number) : void
      {
         this._fov = param1;
         this._distance = param2;
         invalidateData();
      }
      
      public function as_updateSectorState(param1:Boolean) : void
      {
         if(this._isEnabled != param1)
         {
            this._isEnabled = param1;
            invalidateState();
         }
      }
      
      public function as_updateSectorVisibility(param1:Boolean) : void
      {
         this._fill.visible = this._leftEdge.visible = this._rightEdge.visible = param1;
      }
   }
}
