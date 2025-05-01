package net.wg.historical_battles.gui.battle.views.respawn.constants
{
   import flash.geom.Point;
   import net.wg.data.constants.Errors;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   
   public class HB_DIVISION_PROPS
   {
      
      private static const ICONS_SCALE:Object = {};
      
      private static const LABEL_FONT_SIZE:Object = {};
      
      private static const NAME_FONT_SIZE:Object = {};
      
      private static const LABEL_POS:Object = {};
      
      private static const NAME_POS:Object = {};
      
      private static const EMBLEM_X:Object = {};
      
      private static const LINES_Y:Object = {};
      
      private static const LINE_RIGHT_GAP:Object = {};
      
      {
         LABEL_FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 15;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.SMALL] = 15;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 22;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.LARGE] = 22;
         LABEL_FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 36;
         NAME_FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 24;
         NAME_FONT_SIZE[HB_STAGE_SIZE.SMALL] = 24;
         NAME_FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 36;
         NAME_FONT_SIZE[HB_STAGE_SIZE.LARGE] = 36;
         NAME_FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 56;
         ICONS_SCALE[HB_STAGE_SIZE.EXTRA_SMALL] = 0.7;
         ICONS_SCALE[HB_STAGE_SIZE.SMALL] = 0.7;
         ICONS_SCALE[HB_STAGE_SIZE.MEDIUM] = 1;
         ICONS_SCALE[HB_STAGE_SIZE.LARGE] = 1;
         ICONS_SCALE[HB_STAGE_SIZE.EXTRA_LARGE] = 1.25;
         LABEL_POS[HB_STAGE_SIZE.EXTRA_SMALL] = new Point(284,10);
         LABEL_POS[HB_STAGE_SIZE.SMALL] = new Point(284,10);
         LABEL_POS[HB_STAGE_SIZE.MEDIUM] = new Point(391,16);
         LABEL_POS[HB_STAGE_SIZE.LARGE] = new Point(391,16);
         LABEL_POS[HB_STAGE_SIZE.EXTRA_LARGE] = new Point(506,8);
         NAME_POS[HB_STAGE_SIZE.EXTRA_SMALL] = new Point(284,30);
         NAME_POS[HB_STAGE_SIZE.SMALL] = new Point(284,30);
         NAME_POS[HB_STAGE_SIZE.MEDIUM] = new Point(391,44);
         NAME_POS[HB_STAGE_SIZE.LARGE] = new Point(391,44);
         NAME_POS[HB_STAGE_SIZE.EXTRA_LARGE] = new Point(506,52);
         EMBLEM_X[HB_STAGE_SIZE.EXTRA_SMALL] = 196;
         EMBLEM_X[HB_STAGE_SIZE.SMALL] = 196;
         EMBLEM_X[HB_STAGE_SIZE.MEDIUM] = 267;
         EMBLEM_X[HB_STAGE_SIZE.LARGE] = 267;
         EMBLEM_X[HB_STAGE_SIZE.EXTRA_LARGE] = 346;
         LINES_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 37;
         LINES_Y[HB_STAGE_SIZE.SMALL] = 37;
         LINES_Y[HB_STAGE_SIZE.MEDIUM] = 52;
         LINES_Y[HB_STAGE_SIZE.LARGE] = 52;
         LINES_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 65;
         LINE_RIGHT_GAP[HB_STAGE_SIZE.EXTRA_SMALL] = 23;
         LINE_RIGHT_GAP[HB_STAGE_SIZE.SMALL] = 23;
         LINE_RIGHT_GAP[HB_STAGE_SIZE.MEDIUM] = 30;
         LINE_RIGHT_GAP[HB_STAGE_SIZE.LARGE] = 30;
         LINE_RIGHT_GAP[HB_STAGE_SIZE.EXTRA_LARGE] = 48;
      }
      
      public function HB_DIVISION_PROPS()
      {
         super();
      }
      
      public static function getIconsScale(param1:uint) : Number
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return ICONS_SCALE[param1];
      }
      
      public static function getLabelFontSize(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LABEL_FONT_SIZE[param1];
      }
      
      public static function getNameFontSize(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return NAME_FONT_SIZE[param1];
      }
      
      public static function getLabelPos(param1:uint) : Point
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LABEL_POS[param1];
      }
      
      public static function getNamePos(param1:uint) : Point
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return NAME_POS[param1];
      }
      
      public static function getEmblemX(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return EMBLEM_X[param1];
      }
      
      public static function getLinesY(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LINES_Y[param1];
      }
      
      public static function getLineRightGap(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return LINE_RIGHT_GAP[param1];
      }
   }
}
