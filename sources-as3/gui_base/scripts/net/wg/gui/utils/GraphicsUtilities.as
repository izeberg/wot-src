package net.wg.gui.utils
{
   import flash.display.Graphics;
   
   public class GraphicsUtilities
   {
       
      
      public function GraphicsUtilities()
      {
         super();
      }
      
      public static function drawArc(param1:Graphics, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number) : void
      {
         var _loc7_:Number = NaN;
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
         var _loc18_:uint = 0;
         if(Math.abs(param5) >= 2 * Math.PI)
         {
            param1.drawCircle(param2,param3,param6);
            return;
         }
         _loc11_ = Math.ceil(Math.abs(param5) / (Math.PI / 4));
         _loc7_ = param5 / _loc11_;
         _loc8_ = -_loc7_;
         _loc9_ = -param4;
         if(_loc11_ > 0)
         {
            _loc12_ = param2 + Math.cos(param4) * param6;
            _loc13_ = param3 + Math.sin(-param4) * param6;
            param1.moveTo(_loc12_,_loc13_);
            _loc18_ = 0;
            while(_loc18_ < _loc11_)
            {
               _loc9_ += _loc8_;
               _loc10_ = _loc9_ - _loc8_ / 2;
               _loc14_ = param2 + Math.cos(_loc9_) * param6;
               _loc15_ = param3 + Math.sin(_loc9_) * param6;
               _loc16_ = param2 + Math.cos(_loc10_) * (param6 / Math.cos(_loc8_ / 2));
               _loc17_ = param3 + Math.sin(_loc10_) * (param6 / Math.cos(_loc8_ / 2));
               param1.curveTo(_loc16_,_loc17_,_loc14_,_loc15_);
               _loc18_++;
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
      
      public static function drawSector(param1:Graphics, param2:Number, param3:Number) : void
      {
         var _loc5_:int = 0;
         var _loc6_:Number = NaN;
         var _loc9_:int = 0;
         var _loc10_:int = 0;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:int = 0;
         param1.moveTo(0,0);
         if(Math.abs(param3) > 360)
         {
            param3 = 360;
         }
         var _loc4_:int = 180 - param3 >> 1;
         _loc5_ = Math.ceil(Math.abs(param3) / 45);
         _loc6_ = param3 / _loc5_;
         var _loc7_:Number = -_loc6_ / 180 * Math.PI;
         var _loc8_:Number = -_loc4_ / 180 * Math.PI;
         if(_loc5_ > 0)
         {
            _loc9_ = Math.cos(-_loc8_) * param2;
            _loc10_ = Math.sin(_loc8_) * param2;
            param1.lineTo(_loc9_,_loc10_);
            _loc16_ = 0;
            while(_loc16_ < _loc5_)
            {
               _loc8_ += _loc7_;
               _loc11_ = _loc8_ - _loc7_ / 2;
               _loc12_ = Math.cos(_loc8_) * param2;
               _loc13_ = Math.sin(_loc8_) * param2;
               _loc14_ = Math.cos(_loc11_) * (param2 / Math.cos(_loc7_ / 2));
               _loc15_ = Math.sin(_loc11_) * (param2 / Math.cos(_loc7_ / 2));
               param1.curveTo(_loc14_,_loc15_,_loc12_,_loc13_);
               _loc16_++;
            }
            param1.lineTo(0,0);
         }
      }
   }
}
