package net.wg.historical_battles.gui.battle.constants
{
   public class HB_ENEMY_TYPE
   {
      
      private static const AIMER:String = "aimer";
      
      private static const RUNNER:String = "runner";
       
      
      public function HB_ENEMY_TYPE()
      {
         super();
      }
      
      public static function needAttention(param1:String) : Boolean
      {
         return param1 == AIMER || param1 == RUNNER;
      }
   }
}
