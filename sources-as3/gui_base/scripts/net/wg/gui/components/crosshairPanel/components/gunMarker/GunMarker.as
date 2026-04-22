package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.generated.GUN_MARKER_VIEW_CONSTANTS;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class GunMarker extends SimpleContainer implements IGunMarker
   {
       
      
      public var gunTag:GunMarkerTag = null;
      
      public var radiusMC:IGunMarkerDispersion = null;
      
      public var aimDamage:GunMarkerAimDamage = null;
      
      private var _gunTagAlpha:Number = -1;
      
      private var _mixingAlpha:Number = -1;
      
      private var _scale:Number = 1;
      
      private var _isSecondary:Boolean = false;
      
      private var _penetrationFx:PenetrationFX = null;
      
      public function GunMarker()
      {
         super();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(GunMarkerConsts.GUN_TAG_ALPHA_VALIDATION))
         {
            this.gunTag.alpha = this._gunTagAlpha;
         }
         if(isInvalid(GunMarkerConsts.GUN_MIXING_ALPHA_VALIDATION))
         {
            this.radiusMC.setAlpha(this._mixingAlpha,this._isSecondary);
         }
         if(isInvalid(GunMarkerConsts.GUN_SCALE_VALIDATION))
         {
            this.gunTag.scaleX = this.gunTag.scaleY = this._scale;
            this.aimDamage.scaleX = this.aimDamage.scaleY = this._scale;
         }
      }
      
      override protected function onDispose() : void
      {
         this.radiusMC.dispose();
         this.radiusMC = null;
         this.gunTag.dispose();
         this.gunTag = null;
         this.aimDamage.dispose();
         this.aimDamage = null;
         if(this._penetrationFx)
         {
            removeChild(this._penetrationFx);
            this._penetrationFx.dispose();
            this._penetrationFx = null;
         }
         super.onDispose();
      }
      
      public function setAimDamageStage(param1:String) : void
      {
         this.aimDamage.setStage(param1);
      }
      
      public function setChargeableBurstMode(param1:Boolean) : void
      {
         this.radiusMC.setChargeableBurstMode(param1);
      }
      
      public function setColor(param1:String) : void
      {
         this.gunTag.setColor(param1);
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         this.radiusMC.setIsColorBlind(param1);
      }
      
      public function setIsSecondary(param1:Boolean) : void
      {
         this._isSecondary = param1;
         this.gunTag.visible = this.aimDamage.visible = !param1;
         if(this._isSecondary)
         {
            this.radiusMC.setThickness(GunMarkerDispersionCircle.THIN);
         }
         invalidate(GunMarkerConsts.GUN_MIXING_ALPHA_VALIDATION);
      }
      
      public function setSecondaryActive(param1:Boolean) : void
      {
         if(this._isSecondary)
         {
            this.radiusMC.setAlpha(this._mixingAlpha,this._isSecondary);
            this.radiusMC.visible = param1;
         }
      }
      
      public function setDispersionCircleThickness(param1:Boolean) : void
      {
         if(!this._isSecondary)
         {
            this.radiusMC.setThickness(!!param1 ? GunMarkerDispersionCircle.BOLD : GunMarkerDispersionCircle.THIN);
         }
      }
      
      public function setMixingScale(param1:Number) : void
      {
         this.radiusMC.scaleX = this.radiusMC.scaleY = param1;
      }
      
      public function setReloadingParams(param1:Number, param2:String) : void
      {
         this.radiusMC.setReloadingParams(param1,param2);
         this.gunTag.setReloadingState(param2);
      }
      
      public function setScale(param1:Number) : void
      {
         if(this._scale != param1)
         {
            this._scale = param1;
            invalidate(GunMarkerConsts.GUN_SCALE_VALIDATION);
         }
      }
      
      public function setSettings(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         this.gunTag.setType(param1);
         this.radiusMC.setType(param2);
         if(this._gunTagAlpha != param3)
         {
            this._gunTagAlpha = param3;
            invalidate(GunMarkerConsts.GUN_TAG_ALPHA_VALIDATION);
         }
         if(this._mixingAlpha != param4)
         {
            this._mixingAlpha = param4;
            invalidate(GunMarkerConsts.GUN_MIXING_ALPHA_VALIDATION);
         }
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         this.aimDamage.zoomFactor = param1;
      }
      
      public function showPenetrationFx() : void
      {
         var _loc1_:Class = null;
         if(this._penetrationFx == null)
         {
            _loc1_ = getDefinitionByName(GUN_MARKER_VIEW_CONSTANTS.PENETRATION_FX_LINKAGE) as Class;
            this._penetrationFx = new _loc1_();
            addChild(this._penetrationFx);
         }
         this._penetrationFx.showPenetrationFX();
      }
   }
}
