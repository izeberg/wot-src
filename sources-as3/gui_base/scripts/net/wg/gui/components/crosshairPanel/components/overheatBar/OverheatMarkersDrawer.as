package net.wg.gui.components.crosshairPanel.components.overheatBar
{
   import flash.display.GradientType;
   import flash.display.Graphics;
   import flash.display.SpreadMethod;
   import flash.display.Sprite;
   import flash.filters.BitmapFilterQuality;
   import flash.filters.DropShadowFilter;
   import flash.geom.Matrix;
   
   public class OverheatMarkersDrawer
   {
       
      
      public function OverheatMarkersDrawer()
      {
         super();
      }
      
      public static function setShadowFilter(param1:Sprite) : void
      {
         var _loc2_:uint = 15619362;
         var _loc3_:Number = 0;
         var _loc4_:Number = 0;
         var _loc5_:Number = 1;
         var _loc6_:Number = 14;
         var _loc7_:Number = 14;
         var _loc8_:Number = 1;
         var _loc9_:int = BitmapFilterQuality.HIGH;
         param1.filters = [new DropShadowFilter(_loc3_,_loc4_,_loc2_,_loc5_,_loc6_,_loc7_,_loc8_,_loc9_)];
      }
      
      public static function drawProgressSegment(param1:uint, param2:Number, param3:Number, param4:uint, param5:Number = 1, param6:uint = 1, param7:uint = 0) : Sprite
      {
         var _loc12_:Sprite = null;
         var _loc15_:Number = NaN;
         var _loc16_:Number = NaN;
         var _loc19_:uint = 0;
         var _loc20_:uint = 0;
         var _loc21_:Number = NaN;
         var _loc22_:Sprite = null;
         var _loc8_:Number = 6.2831;
         var _loc9_:Number = 57.2958;
         var _loc10_:Number = 0.0174;
         var _loc11_:uint = 8;
         _loc12_ = new Sprite();
         var _loc13_:Graphics = _loc12_.graphics;
         _loc13_.clear();
         _loc13_.beginFill(param4,param5);
         var _loc14_:Number = param1 - param6;
         _loc15_ = param2 * _loc8_;
         _loc16_ = param3 * _loc8_ - _loc15_;
         var _loc17_:uint = Math.round(_loc16_ * _loc11_);
         var _loc18_:Number = 0;
         _loc13_.moveTo(Math.sin(_loc15_) * param1,-Math.cos(_loc15_) * param1);
         _loc19_ = 0;
         while(_loc19_ <= _loc17_)
         {
            _loc18_ = _loc19_ / _loc17_ * _loc16_ + _loc15_;
            _loc13_.lineTo(Math.sin(_loc18_) * param1,-Math.cos(_loc18_) * param1);
            _loc19_++;
         }
         _loc20_ = 0;
         while(_loc20_ <= _loc17_)
         {
            _loc18_ = (_loc17_ - _loc20_) / _loc17_ * _loc16_ + _loc15_;
            _loc13_.lineTo(Math.sin(_loc18_) * _loc14_,-Math.cos(_loc18_) * _loc14_);
            _loc20_++;
         }
         _loc13_.endFill();
         if(param7 > param6 && _loc17_ > 0)
         {
            _loc21_ = _loc10_ * 0.5;
            _loc22_ = drawGradientBox(param7,1,param4);
            _loc22_.x = Math.sin(_loc15_) * param1;
            _loc22_.y = -Math.cos(_loc15_) * param1;
            _loc22_.rotation = _loc15_ * _loc9_ - 90;
            _loc22_.alpha = param5;
            _loc12_.addChild(_loc22_);
            _loc22_ = drawGradientBox(param7,1,param4);
            _loc22_.x = Math.sin(_loc16_ + _loc15_ - _loc21_) * param1;
            _loc22_.y = -Math.cos(_loc16_ + _loc15_ - _loc21_) * param1;
            _loc22_.rotation = (_loc16_ + _loc15_) * _loc9_ - 90;
            _loc22_.alpha = param5;
            _loc12_.addChild(_loc22_);
         }
         return _loc12_;
      }
      
      public static function drawGradientBox(param1:uint, param2:uint, param3:uint) : Sprite
      {
         var _loc4_:String = GradientType.LINEAR;
         var _loc5_:String = SpreadMethod.PAD;
         var _loc6_:Array = [param3,param3];
         var _loc7_:Array = [1,0];
         var _loc8_:Array = [0,255];
         var _loc9_:Matrix = new Matrix();
         _loc9_.createGradientBox(param1,param2,0,0,0);
         var _loc10_:Sprite = new Sprite();
         var _loc11_:Graphics = _loc10_.graphics;
         _loc11_.beginGradientFill(_loc4_,_loc6_,_loc7_,_loc8_,_loc9_,_loc5_);
         _loc11_.drawRect(0,0,param1,param2);
         _loc11_.endFill();
         return _loc10_;
      }
      
      public static function getGradientColors(param1:uint, param2:uint, param3:uint) : Vector.<uint>
      {
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:int = 0;
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc14_:int = 0;
         var _loc15_:uint = 0;
         var _loc4_:Vector.<uint> = new <uint>[param1];
         var _loc5_:Vector.<int> = new Vector.<int>();
         var _loc6_:Vector.<int> = new Vector.<int>();
         var _loc7_:Vector.<uint> = new <uint>[16,8,0];
         var _loc8_:uint = _loc7_.length;
         _loc12_ = 0;
         while(_loc12_ < _loc8_)
         {
            _loc9_ = param1 >> _loc7_[_loc12_] & 255;
            _loc6_.push(_loc9_);
            _loc10_ = param2 >> _loc7_[_loc12_] & 255;
            _loc11_ = Math.round((_loc9_ - _loc10_) / (param3 + 1));
            _loc5_.push(_loc11_);
            _loc12_++;
         }
         _loc15_ = 1;
         while(_loc15_ <= param3)
         {
            _loc13_ = 0;
            _loc12_ = 0;
            while(_loc12_ < _loc8_)
            {
               _loc14_ = _loc6_[_loc12_] - _loc5_[_loc12_] * _loc15_;
               _loc13_ += (_loc14_ & 255) << _loc7_[_loc12_];
               _loc12_++;
            }
            _loc4_.push(_loc13_);
            _loc15_++;
         }
         _loc4_.push(param2);
         return _loc4_;
      }
   }
}
