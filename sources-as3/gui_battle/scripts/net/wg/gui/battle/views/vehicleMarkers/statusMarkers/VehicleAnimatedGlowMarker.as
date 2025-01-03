package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   public class VehicleAnimatedGlowMarker extends VehicleAnimatedStatusBaseMarker
   {
       
      
      public var glowContainer:MarkerAssetContainer = null;
      
      public function VehicleAnimatedGlowMarker()
      {
         super();
         this.glowContainer.setAnimated(false);
      }
      
      override public function set visible(param1:Boolean) : void
      {
         super.visible = param1;
         this.glowContainer.setAnimated(param1);
      }
      
      override protected function onDispose() : void
      {
         this.glowContainer.dispose();
         this.glowContainer = null;
         super.onDispose();
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         super.updateColorSettings(param1);
         this.glowContainer.updateColorSettings(color);
      }
      
      override protected function onHiddenStateShowed() : void
      {
         super.onHiddenStateShowed();
         this.glowContainer.setAnimated(false);
      }
   }
}
