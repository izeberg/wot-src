package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   public class VehicleInspireTargetMarker extends VehicleAnimatedGlowMarker
   {
       
      
      public var arrowContainer:MarkerAssetContainer = null;
      
      private var _isPlaying:Boolean = false;
      
      public function VehicleInspireTargetMarker()
      {
         super();
         this.arrowContainer.stop();
      }
      
      override public function showEffectTimer(param1:Number, param2:Boolean, param3:Boolean, param4:Boolean = true, param5:Boolean = true) : void
      {
         super.showEffectTimer(param1,param2,param3,param4,param5);
         if(!this._isPlaying)
         {
            this._isPlaying = true;
            this.arrowContainer.play();
         }
      }
      
      override protected function onHiddenStateShowed() : void
      {
         super.onHiddenStateShowed();
         this.arrowContainer.stop();
         this._isPlaying = false;
      }
      
      override protected function onDispose() : void
      {
         this.arrowContainer.dispose();
         this.arrowContainer = null;
         super.onDispose();
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         this.arrowContainer.updateColorSettings(arrowColorFrame);
      }
      
      override protected function updateSourceVehicle() : void
      {
         this.arrowContainer.updateColorSettings(arrowColorFrame);
      }
   }
}
