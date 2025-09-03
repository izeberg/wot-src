package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   public class ChargeGunMarker extends GunMarker
   {
       
      
      public function ChargeGunMarker()
      {
         super();
      }
      
      public function set chargeGunActive(param1:Boolean) : void
      {
         var _loc2_:ChargeGunMarkerDispersionCircle = radiusMC as ChargeGunMarkerDispersionCircle;
         if(_loc2_ != null)
         {
            _loc2_.isChargeActive = param1;
         }
      }
      
      override public function setZoomFactor(param1:Number) : void
      {
         var _loc2_:ChargeGunMarkerDispersionCircle = radiusMC as ChargeGunMarkerDispersionCircle;
         if(_loc2_ != null)
         {
            _loc2_.setZoomFactor(param1);
         }
         super.setZoomFactor(param1);
      }
      
      public function setChargeGunState(param1:Number, param2:uint, param3:Boolean) : void
      {
         var _loc4_:ChargeGunMarkerDispersionCircle = radiusMC as ChargeGunMarkerDispersionCircle;
         if(_loc4_ != null)
         {
            _loc4_.setChargeGunState(param1,param2,param3);
         }
      }
   }
}
