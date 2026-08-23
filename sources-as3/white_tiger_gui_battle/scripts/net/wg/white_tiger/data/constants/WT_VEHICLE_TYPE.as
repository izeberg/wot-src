package net.wg.white_tiger.data.constants
{
   public class WT_VEHICLE_TYPE
   {
      
      public static const UNDEFINED:String = "undefined";
      
      public static const BOSS:String = "boss";
      
      public static const BOSS_2025:String = "boss_2025";
      
      public static const BOSS_SPECIAL:String = "boss_special";
      
      public static const HUNTER:String = "hunter";
      
      private static const BOSS_TYPES:Array = [BOSS,BOSS_2025,BOSS_SPECIAL];
       
      
      public function WT_VEHICLE_TYPE()
      {
         super();
      }
      
      public static function isBossType(param1:String) : Boolean
      {
         return BOSS_TYPES.indexOf(param1) != -1;
      }
   }
}
