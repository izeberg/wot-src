package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class AccuracyGunMarkerDispersionCircle extends SimpleContainer implements IGunMarkerDispersion
   {
      
      public static const STACKS_VALIDATION:String = "accuracyStackInvalid";
       
      
      public var invalidateCrosshair:Function = null;
      
      public var currMixingMC:IGunMarkerMixing = null;
      
      public var accuracyGunMixing:GunMarkerMixingAccuracyGun;
      
      private var _reloadingInPercent:Number = -1;
      
      private var _reloadingState:String = "";
      
      private var _accuracyStacks:int = 0;
      
      public function AccuracyGunMarkerDispersionCircle()
      {
         super();
         this.currMixingMC = this.accuracyGunMixing;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._reloadingInPercent != -1 && isInvalid(GunMarkerConsts.GUN_RELOAD_VALIDATION))
         {
            this.accuracyGunMixing.setReloadingAsPercent(this._reloadingInPercent);
            this.accuracyGunMixing.setReloadingState(this._reloadingState);
         }
         if(isInvalid(STACKS_VALIDATION))
         {
            this.accuracyGunMixing.setStacks(this._accuracyStacks);
         }
      }
      
      override protected function onDispose() : void
      {
         this.accuracyGunMixing.dispose();
         this.accuracyGunMixing = null;
         this.currMixingMC = null;
         super.onDispose();
      }
      
      public function setAccuracyStacks(param1:int) : void
      {
         this._accuracyStacks = param1;
         invalidate(STACKS_VALIDATION);
      }
      
      public function setAlpha(param1:Number, param2:Boolean) : void
      {
         this.accuracyGunMixing.alpha = param1;
      }
      
      public function setChargeableBurstMode(param1:Boolean) : void
      {
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
      }
      
      public function setReloadingParams(param1:Number, param2:String) : void
      {
         if(this._reloadingState != param2 || this._reloadingInPercent != param1)
         {
            this._reloadingState = param2;
            this._reloadingInPercent = param1;
            invalidate(GunMarkerConsts.GUN_RELOAD_VALIDATION);
         }
      }
      
      public function setThickness(param1:String) : void
      {
         this.accuracyGunMixing.setThickness(param1);
      }
      
      public function setType(param1:Number) : void
      {
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         this.accuracyGunMixing.setZoomFactor(param1);
      }
   }
}
