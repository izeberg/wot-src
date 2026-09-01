package net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher
{
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   
   public class AuxiliaryRocketLauncherGunMarker extends GunMarker implements IAuxiliaryRocketLauncherGunMarker
   {
       
      
      public var gunTagRocket:AuxiliaryRocketLauncherGunMarkerTag = null;
      
      private var _auxRocketRadiusMC:AuxiliaryRocketLauncherGunMarkerDispersionCircle = null;
      
      public function AuxiliaryRocketLauncherGunMarker()
      {
         super();
         this._auxRocketRadiusMC = radiusMC as AuxiliaryRocketLauncherGunMarkerDispersionCircle;
      }
      
      override public function setZoomFactor(param1:Number) : void
      {
         super.setZoomFactor(param1);
         if(this.gunTagRocket)
         {
            this.gunTagRocket.setZoomFactor(param1);
         }
      }
      
      override protected function onDispose() : void
      {
         this.gunTagRocket.dispose();
         this.gunTagRocket = null;
         this._auxRocketRadiusMC = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.setAuxiliaryRocketLauncherActive(false);
      }
      
      override protected function draw() : void
      {
         var _loc1_:Number = NaN;
         super.draw();
         if(isInvalid(GunMarkerConsts.GUN_SCALE_VALIDATION))
         {
            _loc1_ = gunTag.scaleX;
            this.gunTagRocket.scaleX = this.gunTagRocket.scaleY = _loc1_;
         }
      }
      
      public function setAuxiliaryRocketLauncherActive(param1:Boolean) : void
      {
         if(this._auxRocketRadiusMC)
         {
            this._auxRocketRadiusMC.setAuxiliaryRocketLauncherActive(param1);
         }
         gunTag.visible = !param1;
         if(this.gunTagRocket)
         {
            this.gunTagRocket.setVisible(param1);
         }
      }
   }
}
