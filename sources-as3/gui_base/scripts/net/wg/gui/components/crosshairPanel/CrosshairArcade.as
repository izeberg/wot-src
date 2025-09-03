package net.wg.gui.components.crosshairPanel
{
   import net.wg.utils.StageSizeBoundaries;
   
   public class CrosshairArcade extends CrosshairWithCassette
   {
      
      private static const CASSETE_POSITION_DIAGONAL:int = -2;
      
      private static const CASSETE_POSITION_HORIZONTAL:int = 8;
      
      private static const CASSETE_POSITION_RADIAL:int = -2;
      
      private static const CASSETE_POSITION_DASHED:int = -2;
      
      private static const RELOAD_TIME_BLINK_Y_DIAGONAL:int = 9;
      
      private static const RELOAD_TIME_BLINK_Y_HORIZONTAL:int = 39;
      
      private static const RELOAD_TIME_BLINK_Y_RADIAL:int = 10;
      
      private static const RELOAD_TIME_BLINK_Y_DASHED:int = 39;
      
      private static const RELOAD_TIME_BLINK_Y_SIEGE:int = 22;
      
      private static const RELOAD_TIME_BLINK_Y_PILLBOX:int = 22;
      
      private static const SIEGE_NET_SCALE_SMALL:Number = 0.65;
      
      private static const SIEGE_NET_SCALE_NORMAL:Number = 0.8;
       
      
      public function CrosshairArcade()
      {
         super();
      }
      
      override protected function getCassettePositions() : Array
      {
         return [CASSETE_POSITION_DIAGONAL,CASSETE_POSITION_HORIZONTAL,CASSETE_POSITION_RADIAL,CASSETE_POSITION_DASHED];
      }
      
      override protected function getReloadTimeBlinkYPos() : Array
      {
         return [RELOAD_TIME_BLINK_Y_DIAGONAL,RELOAD_TIME_BLINK_Y_HORIZONTAL,RELOAD_TIME_BLINK_Y_RADIAL,RELOAD_TIME_BLINK_Y_DASHED,RELOAD_TIME_BLINK_Y_SIEGE,RELOAD_TIME_BLINK_Y_PILLBOX];
      }
      
      override protected function getSiegeNetScale(param1:Number, param2:Number) : Number
      {
         if(param1 < StageSizeBoundaries.WIDTH_1920)
         {
            return SIEGE_NET_SCALE_SMALL;
         }
         return SIEGE_NET_SCALE_NORMAL;
      }
   }
}
