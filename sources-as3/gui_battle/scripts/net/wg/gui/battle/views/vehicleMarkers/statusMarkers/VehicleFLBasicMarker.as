package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   import flash.display.MovieClip;
   
   public class VehicleFLBasicMarker extends VehicleAnimatedGlowMarker
   {
       
      
      public var iconMc:MovieClip = null;
      
      private var _iconColor:String = "";
      
      public function VehicleFLBasicMarker()
      {
         super();
      }
      
      override public function showEffectTimer(param1:Number, param2:Boolean, param3:Boolean, param4:Boolean = true, param5:Boolean = true) : void
      {
         if(this._iconColor != color)
         {
            this._iconColor = color;
            this.iconMc.gotoAndStop(color);
         }
         super.showEffectTimer(param1,param2,param3,param4,param5);
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.iconMc = null;
         super.onDispose();
      }
      
      override protected function updateColorSettings(param1:uint) : void
      {
         this.iconMc.gotoAndStop(color);
      }
   }
}
