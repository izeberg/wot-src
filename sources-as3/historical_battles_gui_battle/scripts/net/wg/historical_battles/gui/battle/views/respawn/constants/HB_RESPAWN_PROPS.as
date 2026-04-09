package net.wg.historical_battles.gui.battle.views.respawn.constants
{
   import net.wg.data.constants.Errors;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   
   public class HB_RESPAWN_PROPS
   {
      
      private static const GOAL_TIME_FONT_SIZE:Object = {};
      
      private static const GOAL_TIME_Y:Object = {};
      
      private static const TIMER_Y:Object = {};
      
      private static const DIVISION_Y:Object = {};
      
      private static const VEHICLES_Y:Object = {};
      
      private static const LINE_Y:Object = {};
      
      {
         GOAL_TIME_FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 14;
         GOAL_TIME_FONT_SIZE[HB_STAGE_SIZE.SMALL] = 14;
         GOAL_TIME_FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 14;
         GOAL_TIME_FONT_SIZE[HB_STAGE_SIZE.LARGE] = 20;
         GOAL_TIME_FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 24;
         GOAL_TIME_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 6;
         GOAL_TIME_Y[HB_STAGE_SIZE.SMALL] = 6;
         GOAL_TIME_Y[HB_STAGE_SIZE.MEDIUM] = 6;
         GOAL_TIME_Y[HB_STAGE_SIZE.LARGE] = 4;
         GOAL_TIME_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 2;
         TIMER_Y[HB_STAGE_SIZE.EXTRA_SMALL] = -20;
         TIMER_Y[HB_STAGE_SIZE.SMALL] = -20;
         TIMER_Y[HB_STAGE_SIZE.MEDIUM] = -26;
         TIMER_Y[HB_STAGE_SIZE.LARGE] = -26;
         TIMER_Y[HB_STAGE_SIZE.EXTRA_LARGE] = -32;
         DIVISION_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 258;
         DIVISION_Y[HB_STAGE_SIZE.SMALL] = 206;
         DIVISION_Y[HB_STAGE_SIZE.MEDIUM] = 262;
         DIVISION_Y[HB_STAGE_SIZE.LARGE] = 302;
         DIVISION_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 424;
         VEHICLES_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 352;
         VEHICLES_Y[HB_STAGE_SIZE.SMALL] = 312;
         VEHICLES_Y[HB_STAGE_SIZE.MEDIUM] = 390;
         VEHICLES_Y[HB_STAGE_SIZE.LARGE] = 446;
         VEHICLES_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 610;
         LINE_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 616;
         LINE_Y[HB_STAGE_SIZE.SMALL] = 636;
         LINE_Y[HB_STAGE_SIZE.MEDIUM] = 756;
         LINE_Y[HB_STAGE_SIZE.LARGE] = 910;
         LINE_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 1214;
      }
      
      public function HB_RESPAWN_PROPS()
      {
         super();
      }
      
      public static function getGoalTimeFontSize(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return GOAL_TIME_FONT_SIZE[param1];
      }
      
      public static function getGoalTimeY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return GOAL_TIME_Y[param1];
      }
      
      public static function getTimerY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return TIMER_Y[param1];
      }
      
      public static function getDivisionY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return DIVISION_Y[param1];
      }
      
      public static function getVehiclesY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return VEHICLES_Y[param1];
      }
      
      public static function getLineY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LINE_Y[param1];
      }
   }
}
