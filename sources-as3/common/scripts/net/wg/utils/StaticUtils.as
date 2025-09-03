package net.wg.utils
{
   import flash.display.DisplayObject;
   import flash.utils.getQualifiedClassName;
   
   public class StaticUtils
   {
       
      
      public function StaticUtils()
      {
         super();
      }
      
      public static function getObjectHierarchy(param1:DisplayObject, param2:DisplayObject = null, param3:Boolean = true, param4:Boolean = true) : String
      {
         var _loc7_:String = null;
         if(param1 == null || param1 == param2 || param1 == App.stage)
         {
            return null;
         }
         var _loc5_:String = param1.name;
         if(param3)
         {
            _loc7_ = getQualifiedClassName(param1);
            _loc5_ += "[" + (!!param4 ? _loc7_.split("::",2).pop() : _loc7_) + "]";
         }
         var _loc6_:String = getObjectHierarchy(param1.parent,param2,param3,param4);
         return (Boolean(_loc6_) ? _loc6_ + "." : "") + _loc5_;
      }
      
      public static function hsl2Rgb(param1:Number, param2:Number, param3:Number) : uint
      {
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         param1 %= 360;
         param2 = Math.min(Math.max(param2,0),1);
         param3 = Math.min(Math.max(param3,0),1);
         var _loc4_:Number = (1 - Math.abs(2 * param3 - 1)) * param2;
         var _loc5_:Number = param1 / 60;
         var _loc6_:Number = _loc4_ * (1 - Math.abs(_loc5_ % 2 - 1));
         if(0 <= _loc5_ && _loc5_ < 1)
         {
            _loc7_ = _loc4_;
            _loc8_ = _loc6_;
            _loc9_ = 0;
         }
         else if(1 <= _loc5_ && _loc5_ < 2)
         {
            _loc7_ = _loc6_;
            _loc8_ = _loc4_;
            _loc9_ = 0;
         }
         else if(2 <= _loc5_ && _loc5_ < 3)
         {
            _loc7_ = 0;
            _loc8_ = _loc4_;
            _loc9_ = _loc6_;
         }
         else if(3 <= _loc5_ && _loc5_ < 4)
         {
            _loc7_ = 0;
            _loc8_ = _loc6_;
            _loc9_ = _loc4_;
         }
         else if(4 <= _loc5_ && _loc5_ < 5)
         {
            _loc7_ = _loc6_;
            _loc8_ = 0;
            _loc9_ = _loc4_;
         }
         else
         {
            _loc7_ = _loc4_;
            _loc8_ = 0;
            _loc9_ = _loc6_;
         }
         var _loc10_:Number = param3 - _loc4_ / 2;
         var _loc11_:uint = Math.round((_loc7_ + _loc10_) * 255);
         var _loc12_:uint = Math.round((_loc8_ + _loc10_) * 255);
         var _loc13_:uint = Math.round((_loc9_ + _loc10_) * 255);
         return _loc11_ << 16 | _loc12_ << 8 | _loc13_;
      }
      
      public static function number2Color(param1:int) : uint
      {
         var _loc2_:Number = param1 * 137 % 360;
         var _loc3_:Number = 0.7;
         var _loc4_:Number = 0.5;
         return hsl2Rgb(_loc2_,_loc3_,_loc4_);
      }
      
      public static function string2Hash(param1:String) : int
      {
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         while(_loc3_ < param1.length)
         {
            _loc2_ = (_loc2_ << 5) - _loc2_ + param1.charCodeAt(_loc3_);
            _loc2_ |= 0;
            _loc3_++;
         }
         return _loc2_;
      }
   }
}
