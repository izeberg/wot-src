package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import com.gskinner.motion.GTweener;
   import mx.effects.easing.Cubic;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.IGunMarkerDispersion;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.IGunMarkerMixing;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class LowChargeShotGunMarkerDispersionCircle extends SimpleContainer implements IGunMarkerDispersion
   {
      
      private static const SECONDARY_ALPHA_MULTIPLAYER:Number = 0.2;
      
      private static const TWEEN_DURATION:Number = 1;
       
      
      public var currMixingMC:IGunMarkerMixing = null;
      
      public var lowChargeShotMixingMC:LowChargeShotGunMarkerMixing = null;
      
      public var invalidateCrosshair:Function = null;
      
      private var _type:Number = -1;
      
      private var _alpha:Number = 1;
      
      private var _isSecondary:Boolean = false;
      
      private var _reloadController:LowChargeShotReloadController;
      
      public function LowChargeShotGunMarkerDispersionCircle()
      {
         this._reloadController = new LowChargeShotReloadController();
         super();
         this.currMixingMC = this.lowChargeShotMixingMC;
         this._reloadController.addEventListener(LowChargeShotReloadEvent.TICK,this.onReloadControllerTickHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(GunMarkerConsts.GUN_MIXING_TYPE_VALIDATION))
         {
            if(this.currMixingMC)
            {
               if(this.invalidateCrosshair != null)
               {
                  this.invalidateCrosshair();
               }
               this.currMixingMC.visible = true;
            }
         }
         if(isInvalid(GunMarkerConsts.GUN_ALPHA_VALIDATION))
         {
            if(this._isSecondary)
            {
               GTweener.removeTweens(this.currMixingMC);
               GTweener.to(this.currMixingMC,TWEEN_DURATION,{"alpha":this.mixingAlpha * SECONDARY_ALPHA_MULTIPLAYER},{
                  "onComplete":this.onFadeComplete,
                  "ease":Cubic.easeOut
               });
            }
            else
            {
               this.updateAlpha();
            }
         }
      }
      
      override protected function onDispose() : void
      {
         GTweener.removeTweens(this.currMixingMC);
         this.currMixingMC = null;
         this.invalidateCrosshair = null;
         this._reloadController.removeEventListener(LowChargeShotReloadEvent.TICK,this.onReloadControllerTickHandler);
         this._reloadController.dispose();
         this._reloadController = null;
         this.lowChargeShotMixingMC.dispose();
         this.lowChargeShotMixingMC = null;
         super.onDispose();
      }
      
      public function setAlpha(param1:Number, param2:Boolean) : void
      {
         this._isSecondary = param2;
         this._alpha = param1;
         if(this.currMixingMC)
         {
            this.currMixingMC.alpha = this.mixingAlpha;
         }
         invalidate(GunMarkerConsts.GUN_ALPHA_VALIDATION);
      }
      
      public function setChargeableBurstMode(param1:Boolean) : void
      {
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         this.lowChargeShotMixingMC.setIsColorBlind(param1);
      }
      
      public function setLowChargeInitialTime(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         this._reloadController.trySetInitialTime(param1,param2,param3,param4);
         this.lowChargeShotMixingMC.setLowChargeShotGunStageCaps(this._reloadController.lowChargeCap,this._reloadController.blockStageCap);
      }
      
      public function setLowChargeTimeLeft(param1:Number, param2:Number, param3:Boolean) : void
      {
         this._reloadController.setTimeLeft(param1,param2,param3);
      }
      
      public function setReloadingParams(param1:Number, param2:String) : void
      {
      }
      
      public function setThickness(param1:String) : void
      {
         this.lowChargeShotMixingMC.setThickness(param1);
      }
      
      public function setType(param1:Number) : void
      {
         if(this._type != param1)
         {
            this._type = param1;
            invalidate(GunMarkerConsts.GUN_MIXING_TYPE_VALIDATION);
         }
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         this.lowChargeShotMixingMC.zoomFactor = param1;
      }
      
      private function updateAlpha() : void
      {
         var _loc1_:Number = !!this._isSecondary ? Number(this.mixingAlpha * SECONDARY_ALPHA_MULTIPLAYER) : Number(this.mixingAlpha);
         this.lowChargeShotMixingMC.alpha = _loc1_;
      }
      
      private function onFadeComplete() : void
      {
         this.updateAlpha();
      }
      
      protected function get mixingAlpha() : Number
      {
         return this._alpha;
      }
      
      private function onReloadControllerTickHandler(param1:LowChargeShotReloadEvent) : void
      {
         this.lowChargeShotMixingMC.setReloadingProgress(param1.progress,param1.state);
      }
   }
}
