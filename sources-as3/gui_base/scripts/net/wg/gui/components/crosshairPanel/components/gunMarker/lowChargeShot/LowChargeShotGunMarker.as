package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarker;
   
   public class LowChargeShotGunMarker extends GunMarker
   {
       
      
      public function LowChargeShotGunMarker()
      {
         super();
      }
      
      override public function setZoomFactor(param1:Number) : void
      {
         super.setZoomFactor(param1);
         if(this.gunRadiusMC)
         {
            this.gunRadiusMC.setZoomFactor(param1);
         }
      }
      
      public function setLowChargeInitialTime(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         if(this.gunRadiusMC)
         {
            this.gunRadiusMC.setLowChargeInitialTime(param1,param2,param3,param4);
         }
      }
      
      public function setLowChargeTimeLeft(param1:Number, param2:Number, param3:Boolean) : void
      {
         if(this.gunRadiusMC)
         {
            this.gunRadiusMC.setLowChargeTimeLeft(param1,param2,param3);
         }
      }
      
      private function get gunRadiusMC() : LowChargeShotGunMarkerDispersionCircle
      {
         return radiusMC as LowChargeShotGunMarkerDispersionCircle;
      }
   }
}
