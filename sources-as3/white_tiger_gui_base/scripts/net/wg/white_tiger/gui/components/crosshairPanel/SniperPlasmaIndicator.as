package net.wg.white_tiger.gui.components.crosshairPanel
{
   public class SniperPlasmaIndicator extends BasePlasmaIndicator
   {
      
      private static const PLASMA_INDICATOR_Y_HORIZONTAL:Number = 544;
      
      private static const PLASMA_INDICATOR_Y_DIAGONAL:Number = 980;
      
      private static const PLASMA_INDICATOR_Y_RADIAL:Number = 980;
      
      private static const PLASMA_INDICATOR_Y_DASHED:Number = 980;
      
      private static const PLASMA_INDICATOR_Y_SIEGE:Number = 980;
       
      
      public function SniperPlasmaIndicator()
      {
         super();
      }
      
      override protected function getPlasmaDamageIndicatorYPos() : Array
      {
         return [PLASMA_INDICATOR_Y_DIAGONAL,PLASMA_INDICATOR_Y_HORIZONTAL,PLASMA_INDICATOR_Y_RADIAL,PLASMA_INDICATOR_Y_DASHED,PLASMA_INDICATOR_Y_SIEGE];
      }
   }
}
