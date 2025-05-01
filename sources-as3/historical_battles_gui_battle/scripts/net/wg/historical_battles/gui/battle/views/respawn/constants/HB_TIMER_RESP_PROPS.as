package net.wg.historical_battles.gui.battle.views.respawn.constants
{
   import net.wg.data.constants.Errors;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   
   public class HB_TIMER_RESP_PROPS
   {
      
      private static const TIMER_SCALE:Object = {};
      
      private static const GLOW_SCALE:Object = {};
      
      private static const TITLE_FONT_SIZE:Object = {};
      
      private static const LABEL_FONT_SIZE:Object = {};
      
      private static const TITLE_Y:Object = {};
      
      private static const LABEL_Y:Object = {};
      
      private static const GLOW_Y:Object = {};
      
      {
         TITLE_FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 24;
         TITLE_FONT_SIZE[HB_STAGE_SIZE.SMALL] = 24;
         TITLE_FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 36;
         TITLE_FONT_SIZE[HB_STAGE_SIZE.LARGE] = 36;
         TITLE_FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 56;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 16;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.SMALL] = 16;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 24;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.LARGE] = 24;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 36;
         TIMER_SCALE[HB_STAGE_SIZE.EXTRA_SMALL] = 0.7;
         TIMER_SCALE[HB_STAGE_SIZE.SMALL] = 0.7;
         TIMER_SCALE[HB_STAGE_SIZE.MEDIUM] = 1;
         TIMER_SCALE[HB_STAGE_SIZE.LARGE] = 1;
         TIMER_SCALE[HB_STAGE_SIZE.EXTRA_LARGE] = 1.43;
         GLOW_SCALE[HB_STAGE_SIZE.EXTRA_SMALL] = 1;
         GLOW_SCALE[HB_STAGE_SIZE.SMALL] = 1;
         GLOW_SCALE[HB_STAGE_SIZE.MEDIUM] = 1.5;
         GLOW_SCALE[HB_STAGE_SIZE.LARGE] = 1.5;
         GLOW_SCALE[HB_STAGE_SIZE.EXTRA_LARGE] = 2.16;
         TITLE_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 114;
         TITLE_Y[HB_STAGE_SIZE.SMALL] = 114;
         TITLE_Y[HB_STAGE_SIZE.MEDIUM] = 170;
         TITLE_Y[HB_STAGE_SIZE.LARGE] = 170;
         TITLE_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 236;
         LABEL_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 146;
         LABEL_Y[HB_STAGE_SIZE.SMALL] = 146;
         LABEL_Y[HB_STAGE_SIZE.MEDIUM] = 220;
         LABEL_Y[HB_STAGE_SIZE.LARGE] = 220;
         LABEL_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 306;
         GLOW_Y[HB_STAGE_SIZE.EXTRA_SMALL] = -144;
         GLOW_Y[HB_STAGE_SIZE.SMALL] = -144;
         GLOW_Y[HB_STAGE_SIZE.MEDIUM] = -202;
         GLOW_Y[HB_STAGE_SIZE.LARGE] = -202;
         GLOW_Y[HB_STAGE_SIZE.EXTRA_LARGE] = -290;
      }
      
      public function HB_TIMER_RESP_PROPS()
      {
         super();
      }
      
      public static function getTimerScale(param1:uint) : Number
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return TIMER_SCALE[param1];
      }
      
      public static function getGlowScale(param1:uint) : Number
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return GLOW_SCALE[param1];
      }
      
      public static function getTitleFontSize(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return TITLE_FONT_SIZE[param1];
      }
      
      public static function getLabelFontSize(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LABEL_FONT_SIZE[param1];
      }
      
      public static function getTitleY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return TITLE_Y[param1];
      }
      
      public static function getLabelY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LABEL_Y[param1];
      }
      
      public static function getGlowY(param1:int) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return GLOW_Y[param1];
      }
   }
}
