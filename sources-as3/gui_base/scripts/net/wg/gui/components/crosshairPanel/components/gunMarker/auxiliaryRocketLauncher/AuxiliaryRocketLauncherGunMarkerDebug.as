package net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher
{
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerDebug;
   
   public class AuxiliaryRocketLauncherGunMarkerDebug extends GunMarkerDebug implements IAuxiliaryRocketLauncherGunMarker
   {
       
      
      public function AuxiliaryRocketLauncherGunMarkerDebug()
      {
         super();
      }
      
      public function setAuxiliaryRocketLauncherActive(param1:Boolean) : void
      {
         aimDamage.visible = !param1;
         gunTag.visible = !param1;
         radiusMC.visible = !param1;
      }
   }
}
