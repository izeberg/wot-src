package net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher
{
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   
   public class AuxiliaryRocketLauncherGunMarkerDispersionCircle extends GunMarkerDispersionCircle
   {
       
      
      private var _isActive:Boolean = false;
      
      public function AuxiliaryRocketLauncherGunMarkerDispersionCircle()
      {
         super();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(currMixingMC != null && isInvalid(GunMarkerConsts.GUN_MIXING_TYPE_VALIDATION))
         {
            currMixingMC.visible = !this._isActive;
         }
      }
      
      public function setAuxiliaryRocketLauncherActive(param1:Boolean) : void
      {
         this._isActive = param1;
         if(currMixingMC != null)
         {
            currMixingMC.visible = !param1;
         }
      }
   }
}
