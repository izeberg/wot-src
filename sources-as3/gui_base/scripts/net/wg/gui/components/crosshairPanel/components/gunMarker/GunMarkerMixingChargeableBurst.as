package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   public class GunMarkerMixingChargeableBurst extends GunMarkerMixingSolid
   {
      
      private static const RELOAD_COLOR:uint = 16773822;
      
      private static const RELOAD_THICKNESS:uint = 1;
      
      private static const BACK_RELOAD_THICKNESS:uint = 1;
       
      
      public function GunMarkerMixingChargeableBurst()
      {
         super();
      }
      
      override protected function getInitReloadThickness() : uint
      {
         return RELOAD_THICKNESS;
      }
      
      override protected function getInitBackReloadThickness() : uint
      {
         return BACK_RELOAD_THICKNESS;
      }
      
      override protected function get reloadColor() : uint
      {
         return RELOAD_COLOR;
      }
   }
}
