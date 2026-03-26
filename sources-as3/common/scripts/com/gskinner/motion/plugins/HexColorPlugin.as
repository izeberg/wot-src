package com.gskinner.motion.plugins
{
   import com.gskinner.motion.GTween;
   
   public class HexColorPlugin implements IGTweenPlugin
   {
      
      public static var enabled:Boolean = true;
      
      protected static var instance:HexColorPlugin;
      
      protected static var tweenProperties:Array = ["hexColor"];
       
      
      public function HexColorPlugin()
      {
         super();
      }
      
      public static function install(param1:Array = null) : void
      {
         if(instance)
         {
            return;
         }
         instance = new HexColorPlugin();
         GTween.installPlugin(instance,param1 || tweenProperties,true);
      }
      
      public function init(param1:GTween, param2:String, param3:Number) : Number
      {
         if(!(enabled && param1.pluginData.HexColorEnabled == null || param1.pluginData.HexColorEnabled))
         {
            return param3;
         }
         return param3;
      }
      
      public function tween(param1:GTween, param2:String, param3:Number, param4:Number, param5:Number, param6:Number, param7:Boolean) : Number
      {
         if(!(param1.pluginData.HexColorEnabled == null && enabled || param1.pluginData.HexColorEnabled))
         {
            return param3;
         }
         var _loc8_:uint = param4 >> 24 & 255;
         var _loc9_:uint = param4 >> 16 & 255;
         var _loc10_:uint = param4 >> 8 & 255;
         var _loc11_:uint = param4 & 255;
         var _loc12_:uint = param4 + param5 >> 0;
         var _loc13_:uint = _loc8_ + param6 * ((_loc12_ >> 24 & 255) - _loc8_);
         var _loc14_:uint = _loc9_ + param6 * ((_loc12_ >> 16 & 255) - _loc9_);
         var _loc15_:uint = _loc10_ + param6 * ((_loc12_ >> 8 & 255) - _loc10_);
         var _loc16_:uint = _loc11_ + param6 * ((_loc12_ & 255) - _loc11_);
         return uint(_loc13_ << 24 | _loc14_ << 16 | _loc15_ << 8 | _loc16_);
      }
   }
}
