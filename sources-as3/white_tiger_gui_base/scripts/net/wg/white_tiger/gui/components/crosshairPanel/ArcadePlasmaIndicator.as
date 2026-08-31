package net.wg.white_tiger.gui.components.crosshairPanel
{
   public class ArcadePlasmaIndicator extends BasePlasmaIndicator
   {
      
      private static const PLASMA_INDICATOR_Y_HORIZONTAL:Number = 550;
      
      private static const PLASMA_INDICATOR_Y_DIAGONAL:Number = 1050;
      
      private static const PLASMA_INDICATOR_Y_RADIAL:Number = 1050;
      
      private static const PLASMA_INDICATOR_Y_DASHED:Number = 1050;
      
      private static const PLASMA_INDICATOR_Y_SIEGE:Number = 1050;
      
      private static const PLASMA_INDICATOR_SCALE_DIAGONAL:Number = 1.25;
      
      private static const PLASMA_INDICATOR_SCALE_HORIZONTAL:Number = 0.75;
      
      private static const PLASMA_INDICATOR_SCALE_RADIAL:Number = 1.25;
      
      private static const PLASMA_INDICATOR_SCALE_DASHED:Number = 1.25;
      
      private static const PLASMA_INDICATOR_SCALE_SIEGE:Number = 1.25;
       
      
      public function ArcadePlasmaIndicator()
      {
         super();
      }
      
      override protected function getPlasmaDamageIndicatorYPos() : Array
      {
         return [PLASMA_INDICATOR_Y_DIAGONAL,PLASMA_INDICATOR_Y_HORIZONTAL,PLASMA_INDICATOR_Y_RADIAL,PLASMA_INDICATOR_Y_DASHED,PLASMA_INDICATOR_Y_SIEGE];
      }
      
      override protected function getPlasmaDamageIndicatorScale() : Array
      {
         return [PLASMA_INDICATOR_SCALE_DIAGONAL,PLASMA_INDICATOR_SCALE_HORIZONTAL,PLASMA_INDICATOR_SCALE_RADIAL,PLASMA_INDICATOR_SCALE_DASHED,PLASMA_INDICATOR_SCALE_SIEGE];
      }
   }
}
