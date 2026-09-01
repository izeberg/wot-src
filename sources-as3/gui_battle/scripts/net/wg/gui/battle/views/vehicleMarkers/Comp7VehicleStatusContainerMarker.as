package net.wg.gui.battle.views.vehicleMarkers
{
   import net.wg.data.constants.generated.BATTLE_MARKER_STATES;
   import net.wg.gui.battle.views.vehicleMarkers.events.StatusAnimationEvent;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleStunMarker;
   
   public class Comp7VehicleStatusContainerMarker extends VehicleStatusContainerMarker
   {
       
      
      public var illuminationFlareMarker:VehicleStunMarker = null;
      
      public function Comp7VehicleStatusContainerMarker()
      {
         super();
         setupMarker(BATTLE_MARKER_STATES.COMP7_ILLUMINATION_FLARE_MARKER,this.illuminationFlareMarker);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.illuminationFlareMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,onStatusAnimationEventHiddenHandler);
         this.illuminationFlareMarker.setupFrameEvents();
      }
      
      override protected function onBeforeDispose() : void
      {
         this.illuminationFlareMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,onStatusAnimationEventHiddenHandler);
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.illuminationFlareMarker.dispose();
         this.illuminationFlareMarker = null;
         super.onDispose();
      }
      
      override public function setDebuffEffectColor(param1:String, param2:uint) : void
      {
         this.illuminationFlareMarker.setEffectColor(param1,param2);
         super.setDebuffEffectColor(param1,param2);
      }
      
      override public function setSecondString(param1:String) : void
      {
         this.illuminationFlareMarker.setSecondString(param1);
         super.setSecondString(param1);
      }
   }
}
