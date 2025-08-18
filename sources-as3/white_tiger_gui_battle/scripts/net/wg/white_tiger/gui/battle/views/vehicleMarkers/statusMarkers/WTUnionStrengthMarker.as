package net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers
{
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.MarkerAssetContainer;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleAnimatedStatusBaseMarker;
   
   public class WTUnionStrengthMarker extends VehicleAnimatedStatusBaseMarker
   {
       
      
      public var iconContainer:MarkerAssetContainer = null;
      
      public var counter:WTUnionStrengthCounter = null;
      
      public function WTUnionStrengthMarker()
      {
         super();
         this.iconContainer.setAnimated(false);
      }
      
      override public function showEffectTimer(param1:Number, param2:Boolean, param3:Boolean, param4:Boolean = true, param5:Boolean = true) : void
      {
         this.counter.count = param1 < Values.ZERO ? uint(Values.ZERO) : uint(param1);
         super.showEffectTimer(param1,param2,param3,param4,param5);
      }
      
      override public function setVisibility(param1:Boolean) : void
      {
         super.setVisibility(param1);
         this.iconContainer.setAnimated(param1);
      }
      
      override protected function onDispose() : void
      {
         this.iconContainer.dispose();
         this.iconContainer = null;
         this.counter.dispose();
         this.counter = null;
         super.onDispose();
      }
      
      override protected function onHiddenStateShowed() : void
      {
         this.iconContainer.setAnimated(false);
         super.onHiddenStateShowed();
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         this.iconContainer.updateColorSettings(color);
      }
   }
}
