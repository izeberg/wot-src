package net.wg.gui.lobby.historicalBattles.constants
{
   import net.wg.utils.StageBreakPointList;
   
   public class HB_HANGAR_COMPONENTS
   {
      
      public static const DIVISION_PANEL_SIZE:Object = {};
      
      public static const PROGRESSION_WIDGET_SIZE:Object = {};
      
      public static const ORDER_WIDGET_SIZE:Object = {};
      
      public static const SHOP_WIDGET_SIZE:Object = {};
      
      public static const MAIN_REWARD_WIDGET_SIZE:Object = {};
      
      public static const FRONT_PANEL_HEIGHT:Object = {};
      
      private static const STAGE_EXTRA_SMALL:String = StageBreakPointList.EXTRA_SMALL.name;
      
      private static const STAGE_SMALL:String = StageBreakPointList.SMALL.name;
      
      private static const STAGE_MEDIUM:String = StageBreakPointList.MEDIUM.name;
      
      private static const STAGE_LARGE:String = StageBreakPointList.LARGE.name;
      
      private static const STAGE_EXTRA_LARGE:String = StageBreakPointList.EXTRA_LARGE.name;
      
      {
         PROGRESSION_WIDGET_SIZE[STAGE_EXTRA_SMALL] = {
            "width":116,
            "height":185
         };
         PROGRESSION_WIDGET_SIZE[STAGE_SMALL] = {
            "width":116,
            "height":185
         };
         PROGRESSION_WIDGET_SIZE[STAGE_MEDIUM] = {
            "width":144,
            "height":231
         };
         PROGRESSION_WIDGET_SIZE[STAGE_LARGE] = {
            "width":144,
            "height":231
         };
         PROGRESSION_WIDGET_SIZE[STAGE_EXTRA_LARGE] = {
            "width":216,
            "height":346
         };
         ORDER_WIDGET_SIZE[STAGE_EXTRA_SMALL] = {
            "width":180,
            "height":180
         };
         ORDER_WIDGET_SIZE[STAGE_SMALL] = {
            "width":320,
            "height":191
         };
         ORDER_WIDGET_SIZE[STAGE_MEDIUM] = {
            "width":462,
            "height":300
         };
         ORDER_WIDGET_SIZE[STAGE_LARGE] = {
            "width":462,
            "height":300
         };
         ORDER_WIDGET_SIZE[STAGE_EXTRA_LARGE] = {
            "width":592,
            "height":346
         };
         SHOP_WIDGET_SIZE[STAGE_EXTRA_SMALL] = 180;
         SHOP_WIDGET_SIZE[STAGE_SMALL] = 180;
         SHOP_WIDGET_SIZE[STAGE_MEDIUM] = 260;
         SHOP_WIDGET_SIZE[STAGE_LARGE] = 260;
         SHOP_WIDGET_SIZE[STAGE_EXTRA_LARGE] = 346;
         MAIN_REWARD_WIDGET_SIZE[STAGE_EXTRA_SMALL] = {
            "width":212,
            "height":401,
            "top":66
         };
         MAIN_REWARD_WIDGET_SIZE[STAGE_SMALL] = {
            "width":212,
            "height":401,
            "top":68
         };
         MAIN_REWARD_WIDGET_SIZE[STAGE_MEDIUM] = {
            "width":212,
            "height":401,
            "top":96
         };
         MAIN_REWARD_WIDGET_SIZE[STAGE_LARGE] = {
            "width":300,
            "height":590,
            "top":107
         };
         MAIN_REWARD_WIDGET_SIZE[STAGE_EXTRA_LARGE] = {
            "width":360,
            "height":697,
            "top":150
         };
         DIVISION_PANEL_SIZE[STAGE_EXTRA_SMALL] = {
            "width":560,
            "height":310
         };
         DIVISION_PANEL_SIZE[STAGE_SMALL] = {
            "width":560,
            "height":300
         };
         DIVISION_PANEL_SIZE[STAGE_MEDIUM] = {
            "width":632,
            "height":350
         };
         DIVISION_PANEL_SIZE[STAGE_LARGE] = {
            "width":632,
            "height":352
         };
         DIVISION_PANEL_SIZE[STAGE_EXTRA_LARGE] = {
            "width":844,
            "height":454
         };
         FRONT_PANEL_HEIGHT[STAGE_EXTRA_SMALL] = 178;
         FRONT_PANEL_HEIGHT[STAGE_SMALL] = 178;
         FRONT_PANEL_HEIGHT[STAGE_MEDIUM] = 226;
         FRONT_PANEL_HEIGHT[STAGE_LARGE] = 226;
         FRONT_PANEL_HEIGHT[STAGE_EXTRA_LARGE] = 300;
      }
      
      public function HB_HANGAR_COMPONENTS()
      {
         super();
      }
   }
}
