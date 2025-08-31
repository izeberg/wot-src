package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   public class AccuracyGunMarker extends GunMarker
   {
       
      
      public function AccuracyGunMarker()
      {
         super();
      }
      
      public function setStacks(param1:uint) : void
      {
         var _loc2_:AccuracyGunMarkerDispersionCircle = radiusMC as AccuracyGunMarkerDispersionCircle;
         if(_loc2_ != null)
         {
            _loc2_.setAccuracyStacks(param1);
         }
      }
      
      override public function setZoomFactor(param1:Number) : void
      {
         var _loc2_:AccuracyGunMarkerDispersionCircle = radiusMC as AccuracyGunMarkerDispersionCircle;
         if(_loc2_ != null)
         {
            _loc2_.setZoomFactor(param1);
         }
         super.setZoomFactor(param1);
      }
   }
}
