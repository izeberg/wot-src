package net.wg.white_tiger.gui.components.crosshairPanel
{
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingWithoutProgress;
   
   public class WhiteTigerGunMarkerDispersionCircle extends GunMarkerDispersionCircle
   {
       
      
      public var mixingTypeWt:GunMarkerMixingWithoutProgress = null;
      
      public function WhiteTigerGunMarkerDispersionCircle()
      {
         super();
         this.mixingTypeWt.dotsMc.visible = false;
         mixings.type6 = this.mixingTypeWt;
         this.mixingTypeWt.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.mixingTypeWt.dispose();
         this.mixingTypeWt = null;
         super.onDispose();
      }
   }
}
