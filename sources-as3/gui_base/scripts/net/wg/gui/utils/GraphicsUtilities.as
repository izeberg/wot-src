package net.wg.gui.utils
{
   import flash.display.Graphics;
   import flash.geom.Point;
   
   public class GraphicsUtilities
   {
       
      
      public function GraphicsUtilities()
      {
         super();
      }
      
      public static function drawArc(param1:Graphics, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Boolean = false) : void
      {
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:uint = 0;
         if(Math.abs(param5) >= 2 * Math.PI)
         {
            param1.drawCircle(param2,param3,param6);
            return;
         }
         _loc12_ = Math.ceil(Math.abs(param5) / (Math.PI / 6));
         _loc8_ = param5 / _loc12_;
         _loc9_ = -_loc8_;
         _loc10_ = -param4;
         if(_loc12_ > 0)
         {
            _loc13_ = param2 + Math.cos(param4) * param6;
            _loc14_ = param3 + Math.sin(-param4) * param6;
            if(param7)
            {
               param1.lineTo(_loc13_,_loc14_);
            }
            else
            {
               param1.moveTo(_loc13_,_loc14_);
            }
            _loc19_ = 0;
            while(_loc19_ < _loc12_)
            {
               _loc10_ += _loc9_;
               _loc11_ = _loc10_ - _loc9_ / 2;
               _loc15_ = param2 + Math.cos(_loc10_) * param6;
               _loc16_ = param3 + Math.sin(_loc10_) * param6;
               _loc17_ = param2 + Math.cos(_loc11_) * (param6 / Math.cos(_loc9_ / 2));
               _loc18_ = param3 + Math.sin(_loc11_) * (param6 / Math.cos(_loc9_ / 2));
               param1.curveTo(_loc17_,_loc18_,_loc15_,_loc16_);
               _loc19_++;
            }
         }
      }
      
      public static function drawDashedArc(param1:Graphics, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number, param8:Number) : void
      {
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc15_:uint = 0;
         var _loc16_:Number = NaN;
         _loc9_ = Math.abs(param5);
         _loc10_ = param7 + param8;
         var _loc11_:Number = Math.ceil(_loc9_ / _loc10_);
         var _loc12_:Number = Math.min(param7,_loc9_ % _loc10_);
         var _loc13_:int = _loc9_ / param5;
         var _loc14_:Number = param4;
         if(_loc11_ > 0)
         {
            _loc15_ = 0;
            while(_loc15_ < _loc11_)
            {
               _loc16_ = _loc15_ == _loc11_ - 1 ? Number(_loc12_) : Number(param7);
               drawArc(param1,param2,param3,_loc14_,_loc13_ * _loc16_,param6);
               _loc14_ += _loc13_ * _loc10_;
               _loc15_++;
            }
         }
      }
      
      public static function drawDashLine(param1:Graphics, param2:Number, param3:Number = 1, param4:Number = 1, param5:Number = 0, param6:Number = 0, param7:Number = 0) : void
      {
         if(param3 <= 0 || param4 <= 0 || param2 <= 0)
         {
            return;
         }
         var _loc8_:Number = 0;
         var _loc9_:Boolean = true;
         var _loc10_:Number = param6;
         var _loc11_:Number = param7;
         var _loc12_:Number = Math.cos(param5);
         var _loc13_:Number = Math.sin(param5);
         param1.moveTo(_loc10_,_loc11_);
         while(_loc8_ < param2)
         {
            _loc8_ += !!_loc9_ ? param3 : param4;
            if(_loc8_ > param2)
            {
               _loc8_ = param2;
            }
            _loc10_ = param6 + _loc12_ * _loc8_;
            _loc11_ = param7 + _loc13_ * _loc8_;
            if(_loc9_)
            {
               param1.lineTo(_loc10_,_loc11_);
            }
            else
            {
               param1.moveTo(_loc10_,_loc11_);
            }
            _loc9_ = !_loc9_;
         }
      }
      
      public static function pointFromLengthAndAngle(param1:Number, param2:Number, param3:Number = 0, param4:Number = 0) : Point
      {
         return new Point(param3 + Math.cos(-param2) * param1,param4 + Math.sin(param2) * param1);
      }
   }
}
