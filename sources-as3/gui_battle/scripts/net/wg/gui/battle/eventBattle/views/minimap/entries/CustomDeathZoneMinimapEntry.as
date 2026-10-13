package net.wg.gui.battle.eventBattle.views.minimap.entries
{
   import flash.display.CapsStyle;
   import flash.display.GradientType;
   import flash.display.Graphics;
   import flash.display.JointStyle;
   import flash.display.LineScaleMode;
   import flash.display.SpreadMethod;
   import flash.display.Sprite;
   import flash.geom.Matrix;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class CustomDeathZoneMinimapEntry extends BattleUIComponent
   {
      
      private static const FILL_COLOR:int = 13369344;
      
      private static const FILL_ALPHA:Number = 0.8;
      
      private static const COORD_STEP:int = 2;
      
      private static const LINE_COLOR:int = 16766720;
      
      private static const ARGS:String = "Args";
      
      private static const MITER_LIMIT:int = 10;
      
      private static const MAX_GRADIENT:int = 255;
      
      private static const X_INDEX:int = 0;
      
      private static const Y_INDEX:int = 1;
      
      private static const RADIUS_INDEX:int = 2;
       
      
      public var placeholderShape:Sprite = null;
      
      public var placeholderBorder:Sprite = null;
      
      private var _fillColor:int = 13369344;
      
      private var _fillAlpha:Number = 0.8;
      
      private var _lineColor:int = 16766720;
      
      private var _lineAlpha:Number = 1.0;
      
      private var _lineThickness:Number = 1.0;
      
      private var _gradientColor:int = 0;
      
      private var _gradientAlpha:Number = 1.0;
      
      private var _gradientSize:Number = 0;
      
      private var _useGradient:Boolean = true;
      
      private var _zonesInternal:Array;
      
      private var _zonesExternal:Array;
      
      private var _zonesCircle:Array;
      
      public function CustomDeathZoneMinimapEntry()
      {
         this._zonesInternal = [];
         this._zonesExternal = [];
         this._zonesCircle = [];
         super();
      }
      
      override protected function onDispose() : void
      {
         this.placeholderShape = null;
         this.placeholderBorder = null;
         this._zonesInternal.splice(0,this._zonesInternal.length);
         this._zonesInternal = null;
         this._zonesExternal.splice(0,this._zonesExternal.length);
         this._zonesExternal = null;
         this._zonesCircle.splice(0,this._zonesCircle.length);
         this._zonesCircle = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Graphics = null;
         var _loc2_:Graphics = null;
         var _loc3_:int = 0;
         var _loc4_:Array = null;
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc7_:Matrix = null;
         var _loc8_:int = 0;
         var _loc9_:uint = 0;
         var _loc10_:Array = null;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            _loc1_ = this.placeholderShape.graphics;
            _loc2_ = this.placeholderBorder.graphics;
            _loc1_.clear();
            _loc2_.clear();
            _loc2_.lineStyle(this._lineThickness,this._lineColor,this._lineAlpha,false,LineScaleMode.VERTICAL,CapsStyle.NONE,JointStyle.MITER,MITER_LIMIT);
            if(this._useGradient)
            {
               _loc7_ = new Matrix();
               _loc8_ = this._gradientSize >> 1;
               _loc7_.createGradientBox(this._gradientSize,this._gradientSize,0,-_loc8_,-_loc8_);
               _loc1_.beginGradientFill(GradientType.RADIAL,[this._fillColor,this._gradientColor],[this._fillAlpha,this._gradientAlpha],[0,MAX_GRADIENT],_loc7_,SpreadMethod.PAD);
            }
            else
            {
               _loc1_.beginFill(this._fillColor,this._fillAlpha);
            }
            _loc3_ = this._zonesExternal.length;
            _loc4_ = null;
            _loc5_ = 0;
            _loc6_ = 0;
            _loc6_ = 0;
            while(_loc6_ < _loc3_)
            {
               _loc4_ = this._zonesExternal[_loc6_];
               _loc5_ = _loc4_.length;
               _loc1_.moveTo(_loc4_[X_INDEX],_loc4_[Y_INDEX]);
               _loc2_.moveTo(_loc4_[X_INDEX],_loc4_[Y_INDEX]);
               _loc9_ = COORD_STEP;
               while(_loc9_ < _loc5_)
               {
                  _loc1_.lineTo(_loc4_[_loc9_],_loc4_[_loc9_ + 1]);
                  _loc2_.lineTo(_loc4_[_loc9_],_loc4_[_loc9_ + 1]);
                  _loc9_ += COORD_STEP;
               }
               _loc2_.lineTo(_loc4_[X_INDEX],_loc4_[Y_INDEX]);
               _loc6_ += 1;
            }
            _loc3_ = this._zonesInternal.length;
            _loc6_ = 0;
            while(_loc6_ < _loc3_)
            {
               _loc4_ = this._zonesInternal[_loc6_];
               _loc5_ = _loc4_.length;
               _loc1_.moveTo(_loc4_[X_INDEX],_loc4_[Y_INDEX]);
               _loc2_.moveTo(_loc4_[X_INDEX],_loc4_[Y_INDEX]);
               _loc9_ = COORD_STEP;
               while(_loc9_ < _loc5_)
               {
                  _loc1_.lineTo(_loc4_[_loc9_],_loc4_[_loc9_ + 1]);
                  _loc2_.lineTo(_loc4_[_loc9_],_loc4_[_loc9_ + 1]);
                  _loc9_ += COORD_STEP;
               }
               _loc2_.lineTo(_loc4_[X_INDEX],_loc4_[Y_INDEX]);
               _loc6_ += 1;
            }
            _loc3_ = this._zonesCircle.length;
            _loc6_ = 0;
            while(_loc6_ < _loc3_)
            {
               _loc10_ = this._zonesCircle[_loc6_];
               _loc1_.drawCircle(_loc10_[X_INDEX],_loc10_[Y_INDEX],_loc10_[RADIUS_INDEX]);
               _loc2_.drawCircle(_loc10_[X_INDEX],_loc10_[Y_INDEX],_loc10_[RADIUS_INDEX]);
               _loc6_ += 1;
            }
            _loc1_.endFill();
         }
      }
      
      public function addCircleZone(param1:Number, param2:Number, param3:Number) : void
      {
         this._zonesCircle.push([param1,param2,param3]);
         invalidateData();
      }
      
      public function addExternalZoneData(... rest) : void
      {
         this._zonesExternal.push(rest);
         invalidateData();
      }
      
      public function addInternalZoneData(... rest) : void
      {
         this._zonesInternal.push(rest);
         invalidateData();
      }
      
      public function addZoneData(... rest) : void
      {
         this._zonesExternal.push(rest);
         invalidateData();
      }
      
      public function clearExternalZones() : void
      {
         this._zonesExternal.splice(0,this._zonesExternal.length);
         invalidateData();
      }
      
      public function clearInternalZones() : void
      {
         this._zonesInternal.splice(0,this._zonesInternal.length);
         this._zonesCircle.splice(0,this._zonesCircle.length);
         invalidateData();
      }
      
      public function clearZones() : void
      {
         this._zonesExternal.splice(0,this._zonesExternal.length);
         this._zonesInternal.splice(0,this._zonesInternal.length);
         this._zonesCircle.splice(0,this._zonesCircle.length);
         invalidateData();
      }
      
      public function setProperties(param1:int, param2:Number, param3:int, param4:Number, param5:Number = 1, param6:String = "normal", param7:String = "normal", param8:Boolean = false, param9:int = 0, param10:Number = 1.0, param11:int = 0) : void
      {
         this._fillColor = param1;
         this._fillAlpha = param2;
         this._lineColor = param3;
         this._lineAlpha = param4;
         this._lineThickness = param5;
         this.placeholderShape.blendMode = param6;
         this.placeholderBorder.blendMode = param7;
         this._useGradient = param8;
         this._gradientColor = param9;
         this._gradientAlpha = param10;
         this._gradientSize = param11;
         invalidateData();
      }
      
      public function setZoneData(... rest) : void
      {
         App.utils.asserter.assertNotNull(rest,ARGS + Errors.CANT_NULL);
         var _loc2_:Graphics = this.placeholderShape.graphics;
         var _loc3_:Graphics = this.placeholderBorder.graphics;
         _loc2_.clear();
         _loc3_.clear();
         _loc2_.beginFill(this._fillColor,this._fillAlpha);
         _loc3_.lineStyle(this._lineThickness,this._lineColor,this._lineAlpha,false,LineScaleMode.VERTICAL,CapsStyle.NONE,JointStyle.MITER,MITER_LIMIT);
         var _loc4_:int = rest.length;
         _loc2_.moveTo(rest[0],rest[1]);
         _loc3_.moveTo(rest[0],rest[1]);
         var _loc5_:uint = COORD_STEP;
         while(_loc5_ < _loc4_)
         {
            _loc2_.lineTo(rest[_loc5_],rest[_loc5_ + 1]);
            _loc3_.lineTo(rest[_loc5_],rest[_loc5_ + 1]);
            _loc5_ += COORD_STEP;
         }
         _loc3_.lineTo(rest[0],rest[1]);
         _loc2_.endFill();
      }
   }
}
