package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   public class VehicleBerserkerMarker extends VehicleAnimatedGlowMarker
   {
       
      
      public var iconContainer:MarkerAssetContainer = null;
      
      public function VehicleBerserkerMarker()
      {
         super();
         this.iconContainer.setAnimated(false);
      }
      
      override protected function onDispose() : void
      {
         this.iconContainer.dispose();
         this.iconContainer = null;
         super.onDispose();
      }
      
      override protected function onHiddenStateShowed() : void
      {
         super.onHiddenStateShowed();
         this.iconContainer.setAnimated(false);
      }
      
      override public function setVisibility(param1:Boolean) : void
      {
         super.setVisibility(param1);
         this.iconContainer.setAnimated(param1);
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         this.iconContainer.updateColorSettings(color);
      }
   }
}
