package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   import flash.display.MovieClip;
   
   public class VehicleEngineerEffectMarker extends VehicleAnimatedGlowMarker
   {
      
      protected static const DEFENDER_PREFIX:String = "defender_";
      
      protected static const ATTACKER_PREFIX:String = "attacker_";
       
      
      public var iconMc:MovieClip = null;
      
      private var _iconFrame:String = "";
      
      public function VehicleEngineerEffectMarker()
      {
         super();
      }
      
      override public function showEffectTimer(param1:Number, param2:Boolean, param3:Boolean, param4:Boolean = true, param5:Boolean = true) : void
      {
         this.updateIconColor();
         super.showEffectTimer(param1,param2,param3,param4,param5);
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         super.updateColorSettings(param1);
         this.updateIconColor();
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.iconMc = null;
         super.onDispose();
      }
      
      private function updateIconColor() : void
      {
         var _loc1_:String = (!!isSourceVehicle ? ATTACKER_PREFIX : DEFENDER_PREFIX) + color;
         if(_loc1_ != this._iconFrame)
         {
            this._iconFrame = _loc1_;
            this.iconMc.gotoAndStop(_loc1_);
         }
      }
   }
}
