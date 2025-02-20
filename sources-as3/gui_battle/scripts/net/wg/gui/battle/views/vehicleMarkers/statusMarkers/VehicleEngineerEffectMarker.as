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
         this.iconMc.stop();
      }
      
      override public function setVisibility(param1:Boolean) : void
      {
         super.setVisibility(param1);
         if(param1)
         {
            this.iconMc.play();
         }
         else
         {
            this.iconMc.stop();
         }
      }
      
      override public function showEffectTimer(param1:Number, param2:Boolean, param3:Boolean, param4:Boolean = true, param5:Boolean = true) : void
      {
         var _loc6_:String = (!!param2 ? ATTACKER_PREFIX : DEFENDER_PREFIX) + color;
         if(_loc6_ != this._iconFrame)
         {
            this._iconFrame = _loc6_;
            this.iconMc.gotoAndStop(_loc6_);
         }
         super.showEffectTimer(param1,param2,param3,param4,param5);
      }
      
      override protected function onHiddenStateShowed() : void
      {
         this.iconMc.stop();
         super.onHiddenStateShowed();
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.iconMc = null;
         super.onDispose();
      }
   }
}
