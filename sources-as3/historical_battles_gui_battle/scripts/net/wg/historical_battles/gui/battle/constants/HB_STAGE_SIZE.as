package net.wg.historical_battles.gui.battle.constants
{
   import net.wg.utils.StageSizeBoundaries;
   
   public class HB_STAGE_SIZE
   {
      
      private static const STAGE_WIDTH:Object = {};
      
      private static const STAGE_HEIGHT:Object = {};
      
      public static const UNDEFINED:uint = 0;
      
      public static const EXTRA_SMALL:uint = 1;
      
      public static const SMALL:uint = 2;
      
      public static const MEDIUM:uint = 3;
      
      public static const LARGE:uint = 4;
      
      public static const EXTRA_LARGE:uint = 5;
      
      public static const VALID:Array = [EXTRA_SMALL,SMALL,MEDIUM,LARGE,EXTRA_LARGE];
      
      {
         STAGE_WIDTH[EXTRA_SMALL] = StageSizeBoundaries.WIDTH_1024;
         STAGE_WIDTH[SMALL] = StageSizeBoundaries.WIDTH_1366;
         STAGE_WIDTH[MEDIUM] = StageSizeBoundaries.WIDTH_1600;
         STAGE_WIDTH[LARGE] = StageSizeBoundaries.WIDTH_1920;
         STAGE_WIDTH[EXTRA_LARGE] = StageSizeBoundaries.WIDTH_2560;
         STAGE_HEIGHT[EXTRA_SMALL] = StageSizeBoundaries.HEIGHT_768;
         STAGE_HEIGHT[SMALL] = StageSizeBoundaries.HEIGHT_768;
         STAGE_HEIGHT[MEDIUM] = StageSizeBoundaries.HEIGHT_900;
         STAGE_HEIGHT[LARGE] = StageSizeBoundaries.HEIGHT_1080;
         STAGE_HEIGHT[EXTRA_LARGE] = StageSizeBoundaries.HEIGHT_1440;
      }
      
      public function HB_STAGE_SIZE()
      {
         super();
      }
      
      public static function getStageSize(param1:int, param2:int) : int
      {
         if(param1 >= STAGE_WIDTH[EXTRA_LARGE] && param2 >= STAGE_HEIGHT[EXTRA_LARGE])
         {
            return EXTRA_LARGE;
         }
         if(param1 >= STAGE_WIDTH[LARGE] && param2 >= STAGE_HEIGHT[LARGE])
         {
            return LARGE;
         }
         if(param1 >= STAGE_WIDTH[MEDIUM] && param2 >= STAGE_HEIGHT[MEDIUM])
         {
            return MEDIUM;
         }
         if(param1 >= STAGE_WIDTH[SMALL] && param2 >= STAGE_HEIGHT[SMALL])
         {
            return SMALL;
         }
         return EXTRA_SMALL;
      }
   }
}
