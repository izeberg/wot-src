package net.wg.historical_battles.gui.battle.views.respawn.constants
{
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.historical_battles.data.constants.generated.HB_VEHICLE_CARD_STATE;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   
   public class HB_VEHICLE_CARD_PROPS
   {
      
      private static const PICK_BTN_SLIM_STYLES:Array = [HB_STAGE_SIZE.EXTRA_SMALL,HB_STAGE_SIZE.SMALL];
      
      private static const SCALE:Object = {};
      
      private static const GAP:Object = {};
      
      private static const WIDTH_WIDE:Object = {};
      
      private static const WIDTH:Object = {};
      
      private static const HEIGHT:Object = {};
      
      private static const EMBLEM_SCALE:Object = {};
      
      private static const EMBLEM_Y:Object = {};
      
      private static const VEH_NAME_Y:Object = {};
      
      private static const VEH_NAME_EXTRA_Y:Object = {};
      
      private static const VEH_IMG_Y:Object = {};
      
      private static const VEH_STATE_Y:Object = {};
      
      private static const PICK_BTN_PADDING_HOR:Object = {};
      
      private static const PICK_BTN_BOTTOM_OFFSET:Object = {};
      
      private static const VEH_IMG_ALPHA:Object = {};
      
      private static const SMOKE_ALPHA:Object = {};
      
      private static const GLOW_ALPHA:Object = {};
      
      private static const PICKED_ALPHA:Object = {};
      
      public static const VEH_NAME_DEAD_ALPHA:Number = 0.7;
      
      {
         SCALE[HB_STAGE_SIZE.EXTRA_SMALL] = 0.6;
         SCALE[HB_STAGE_SIZE.SMALL] = 0.7;
         SCALE[HB_STAGE_SIZE.MEDIUM] = 0.8;
         SCALE[HB_STAGE_SIZE.LARGE] = 1;
         SCALE[HB_STAGE_SIZE.EXTRA_LARGE] = 1.3;
         GAP[HB_STAGE_SIZE.EXTRA_SMALL] = 6;
         GAP[HB_STAGE_SIZE.SMALL] = 4;
         GAP[HB_STAGE_SIZE.MEDIUM] = 14;
         GAP[HB_STAGE_SIZE.LARGE] = 18;
         GAP[HB_STAGE_SIZE.EXTRA_LARGE] = 24;
         WIDTH_WIDE[HB_STAGE_SIZE.EXTRA_SMALL] = 180;
         WIDTH_WIDE[HB_STAGE_SIZE.SMALL] = 210;
         WIDTH_WIDE[HB_STAGE_SIZE.MEDIUM] = 240;
         WIDTH_WIDE[HB_STAGE_SIZE.LARGE] = 300;
         WIDTH_WIDE[HB_STAGE_SIZE.EXTRA_LARGE] = 390;
         WIDTH[HB_STAGE_SIZE.EXTRA_SMALL] = 150;
         WIDTH[HB_STAGE_SIZE.SMALL] = 176;
         WIDTH[HB_STAGE_SIZE.MEDIUM] = 200;
         WIDTH[HB_STAGE_SIZE.LARGE] = 250;
         WIDTH[HB_STAGE_SIZE.EXTRA_LARGE] = 326;
         HEIGHT[HB_STAGE_SIZE.EXTRA_SMALL] = 234;
         HEIGHT[HB_STAGE_SIZE.SMALL] = 274;
         HEIGHT[HB_STAGE_SIZE.MEDIUM] = 312;
         HEIGHT[HB_STAGE_SIZE.LARGE] = 390;
         HEIGHT[HB_STAGE_SIZE.EXTRA_LARGE] = 508;
         EMBLEM_SCALE[HB_STAGE_SIZE.EXTRA_SMALL] = 1.6;
         EMBLEM_SCALE[HB_STAGE_SIZE.SMALL] = 1.8;
         EMBLEM_SCALE[HB_STAGE_SIZE.MEDIUM] = 1.84;
         EMBLEM_SCALE[HB_STAGE_SIZE.LARGE] = 2.3;
         EMBLEM_SCALE[HB_STAGE_SIZE.EXTRA_LARGE] = 3;
         EMBLEM_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 0;
         EMBLEM_Y[HB_STAGE_SIZE.SMALL] = 0;
         EMBLEM_Y[HB_STAGE_SIZE.MEDIUM] = 2;
         EMBLEM_Y[HB_STAGE_SIZE.LARGE] = 4;
         EMBLEM_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 9;
         VEH_NAME_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 178;
         VEH_NAME_Y[HB_STAGE_SIZE.SMALL] = 214;
         VEH_NAME_Y[HB_STAGE_SIZE.MEDIUM] = 234;
         VEH_NAME_Y[HB_STAGE_SIZE.LARGE] = 310;
         VEH_NAME_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 404;
         VEH_NAME_EXTRA_Y[HB_STAGE_SIZE.EXTRA_SMALL] = -12;
         VEH_NAME_EXTRA_Y[HB_STAGE_SIZE.SMALL] = -12;
         VEH_NAME_EXTRA_Y[HB_STAGE_SIZE.MEDIUM] = -14;
         VEH_NAME_EXTRA_Y[HB_STAGE_SIZE.LARGE] = -16;
         VEH_NAME_EXTRA_Y[HB_STAGE_SIZE.EXTRA_LARGE] = -18;
         VEH_IMG_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 24;
         VEH_IMG_Y[HB_STAGE_SIZE.SMALL] = 16;
         VEH_IMG_Y[HB_STAGE_SIZE.MEDIUM] = 24;
         VEH_IMG_Y[HB_STAGE_SIZE.LARGE] = 10;
         VEH_IMG_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 28;
         VEH_STATE_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 204;
         VEH_STATE_Y[HB_STAGE_SIZE.SMALL] = 242;
         VEH_STATE_Y[HB_STAGE_SIZE.MEDIUM] = 278;
         VEH_STATE_Y[HB_STAGE_SIZE.LARGE] = 342;
         VEH_STATE_Y[HB_STAGE_SIZE.EXTRA_LARGE] = 446;
         PICK_BTN_PADDING_HOR[HB_STAGE_SIZE.EXTRA_SMALL] = 0;
         PICK_BTN_PADDING_HOR[HB_STAGE_SIZE.SMALL] = 8;
         PICK_BTN_PADDING_HOR[HB_STAGE_SIZE.MEDIUM] = 4;
         PICK_BTN_PADDING_HOR[HB_STAGE_SIZE.LARGE] = 10;
         PICK_BTN_PADDING_HOR[HB_STAGE_SIZE.EXTRA_LARGE] = 30;
         PICK_BTN_BOTTOM_OFFSET[HB_STAGE_SIZE.EXTRA_SMALL] = 18;
         PICK_BTN_BOTTOM_OFFSET[HB_STAGE_SIZE.SMALL] = 20;
         PICK_BTN_BOTTOM_OFFSET[HB_STAGE_SIZE.MEDIUM] = 22;
         PICK_BTN_BOTTOM_OFFSET[HB_STAGE_SIZE.LARGE] = 24;
         PICK_BTN_BOTTOM_OFFSET[HB_STAGE_SIZE.EXTRA_LARGE] = 30;
         SMOKE_ALPHA[HB_VEHICLE_CARD_STATE.DEFAULT] = 0.7;
         SMOKE_ALPHA[HB_VEHICLE_CARD_STATE.HOVER] = 1;
         SMOKE_ALPHA[HB_VEHICLE_CARD_STATE.PICKED] = 1;
         SMOKE_ALPHA[HB_VEHICLE_CARD_STATE.DEAD] = 0.7;
         VEH_IMG_ALPHA[HB_VEHICLE_CARD_STATE.DEFAULT] = 0.7;
         VEH_IMG_ALPHA[HB_VEHICLE_CARD_STATE.HOVER] = 1;
         VEH_IMG_ALPHA[HB_VEHICLE_CARD_STATE.PICKED] = 1;
         VEH_IMG_ALPHA[HB_VEHICLE_CARD_STATE.DEAD] = 0.7;
         GLOW_ALPHA[HB_VEHICLE_CARD_STATE.DEFAULT] = 0.5;
         GLOW_ALPHA[HB_VEHICLE_CARD_STATE.HOVER] = 1;
         GLOW_ALPHA[HB_VEHICLE_CARD_STATE.PICKED] = 1;
         GLOW_ALPHA[HB_VEHICLE_CARD_STATE.DEAD] = 0.3;
         PICKED_ALPHA[HB_VEHICLE_CARD_STATE.DEFAULT] = 0;
         PICKED_ALPHA[HB_VEHICLE_CARD_STATE.HOVER] = 0;
         PICKED_ALPHA[HB_VEHICLE_CARD_STATE.PICKED] = 1;
         PICKED_ALPHA[HB_VEHICLE_CARD_STATE.DEAD] = 0;
      }
      
      public function HB_VEHICLE_CARD_PROPS()
      {
         super();
      }
      
      public static function getPickBtnStyle(param1:uint) : String
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return PICK_BTN_SLIM_STYLES.indexOf(param1) != -1 ? UniversalBtnStylesConst.STYLE_SLIM_ORANGE : UniversalBtnStylesConst.STYLE_HEAVY_ORANGE;
      }
      
      public static function getScale(param1:uint) : Number
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return SCALE[param1];
      }
      
      public static function getGap(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return GAP[param1];
      }
      
      public static function getWidth(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return WIDTH[param1];
      }
      
      public static function getWidthWide(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return WIDTH_WIDE[param1];
      }
      
      public static function getAnimStartWidth(param1:uint, param2:Boolean) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return !!param2 ? uint(WIDTH[param1]) : uint(WIDTH_WIDE[param1]);
      }
      
      public static function getAnimEndWidth(param1:uint, param2:Boolean) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return !!param2 ? uint(WIDTH_WIDE[param1]) : uint(WIDTH[param1]);
      }
      
      public static function getHeight(param1:uint) : uint
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return HEIGHT[param1];
      }
      
      public static function getEmblemScale(param1:uint) : Number
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return EMBLEM_SCALE[param1];
      }
      
      public static function getEmblemY(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return EMBLEM_Y[param1];
      }
      
      public static function getVehNameY(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return VEH_NAME_Y[param1];
      }
      
      public static function getVehNameExtraY(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return VEH_NAME_EXTRA_Y[param1];
      }
      
      public static function getVehImgY(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return VEH_IMG_Y[param1];
      }
      
      public static function getVehStateY(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return VEH_STATE_Y[param1];
      }
      
      public static function getPickBtnPaddingHor(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return PICK_BTN_PADDING_HOR[param1];
      }
      
      public static function getPickBtnBottomOffset(param1:uint) : int
      {
         App.utils.asserter.assert(HB_STAGE_SIZE.VALID.indexOf(param1) != -1,Errors.WRONG_VALUE);
         return PICK_BTN_BOTTOM_OFFSET[param1];
      }
      
      public static function getVehImgAlpha(param1:int) : Number
      {
         return VEH_IMG_ALPHA[param1];
      }
      
      public static function getSmokeAlpha(param1:int) : Number
      {
         return SMOKE_ALPHA[param1];
      }
      
      public static function getGlowAlpha(param1:int) : Number
      {
         return GLOW_ALPHA[param1];
      }
      
      public static function getPickedAlpha(param1:int) : Number
      {
         return PICKED_ALPHA[param1];
      }
   }
}
