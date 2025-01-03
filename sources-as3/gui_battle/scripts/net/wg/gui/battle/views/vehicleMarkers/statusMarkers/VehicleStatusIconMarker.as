package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   import flash.display.MovieClip;
   
   public class VehicleStatusIconMarker extends VehicleAnimatedGlowMarker
   {
       
      
      public var iconMC:MovieClip = null;
      
      public function VehicleStatusIconMarker()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.iconMC = null;
         super.onDispose();
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         this.iconMC.gotoAndStop(color);
      }
   }
}
