package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Circular;
   import fl.motion.easing.Sine;
   import flash.display.CapsStyle;
   import flash.display.LineScaleMode;
   import flash.display.Sprite;
   import mx.charts.chartClasses.GraphicsUtilities;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   
   public class ChargeGunMarkerDispersionCircle extends GunMarkerDispersionCircle
   {
      
      private static const SWITCH_ANIMATION_DURATION:Number = 0.25;
      
      private static const SWITCH_ANIMATION_ROTATION:Number = -15;
      
      private static const FULL_CIRCLE:Number = Math.PI * 2;
      
      private static const HALF_PI:Number = Math.PI / 2;
      
      private static const SHOOT_BLOCK_RADIUS:uint = 240;
      
      private static const SHOOT_BLOCK_COLOR:uint = 16751872;
      
      private static const SHOOT_BLOCK_THICKNESS:uint = 3;
      
      private static const SHOOT_BLOCK_SPRITE_NAME:String = "shootBlockSprite";
       
      
      public var chargeGunMixing:GunMarkerMixingChargeGun;
      
      private var _shootBlockSprite:Sprite;
      
      private var _isChargeGunActive:Boolean = false;
      
      private var _isShootBlockActive:Boolean = false;
      
      private var _reloadingInPercent:Number = 0;
      
      private var _reloadingState:String = "";
      
      public function ChargeGunMarkerDispersionCircle()
      {
         super();
         this._shootBlockSprite = new Sprite();
         this._shootBlockSprite.name = SHOOT_BLOCK_SPRITE_NAME;
         addChild(this._shootBlockSprite);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(currMixingMC != null && isInvalid(GunMarkerConsts.GUN_MIXING_TYPE_VALIDATION))
         {
            currMixingMC.visible = !this._isChargeGunActive;
         }
         if(isInvalid(GunMarkerConsts.CHARGE_GUN_ACTIVE_VALIDATION))
         {
            GTweener.removeTweens(currMixingMC);
            GTweener.removeTweens(this.chargeGunMixing);
            if(this._isChargeGunActive)
            {
               if(currMixingMC != null)
               {
                  currMixingMC.alpha = mixingAlpha;
                  GTweener.to(currMixingMC,SWITCH_ANIMATION_DURATION,{"alpha":0},{"ease":Sine.easeOut});
               }
               this.chargeGunMixing.alpha = 0;
               this.chargeGunMixing.visible = true;
               this.chargeGunMixing.rotation = SWITCH_ANIMATION_ROTATION;
               GTweener.to(this.chargeGunMixing,SWITCH_ANIMATION_DURATION,{
                  "alpha":mixingAlpha,
                  "rotation":0
               },{
                  "onComplete":this.onFadeTweenComplete,
                  "ease":Circular.easeIn
               });
            }
            else
            {
               if(currMixingMC != null)
               {
                  currMixingMC.alpha = 0;
                  currMixingMC.visible = true;
                  GTweener.to(currMixingMC,SWITCH_ANIMATION_DURATION,{"alpha":mixingAlpha},{"ease":Circular.easeIn});
               }
               this.chargeGunMixing.alpha = mixingAlpha;
               this.chargeGunMixing.rotation = 0;
               GTweener.to(this.chargeGunMixing,SWITCH_ANIMATION_DURATION,{
                  "alpha":0,
                  "rotation":SWITCH_ANIMATION_ROTATION
               },{
                  "onComplete":this.onFadeTweenComplete,
                  "ease":Sine.easeOut
               });
            }
         }
      }
      
      override public function setReloadingParams(param1:Number, param2:String) : void
      {
         this._reloadingInPercent = param1;
         this._reloadingState = param2;
         var _loc3_:Number = !!this._isShootBlockActive ? Number(0) : Number(this._reloadingInPercent);
         super.setReloadingParams(_loc3_,this._reloadingState);
      }
      
      override protected function onDispose() : void
      {
         GTweener.removeTweens(currMixingMC);
         GTweener.removeTweens(this.chargeGunMixing);
         this.chargeGunMixing.dispose();
         this.chargeGunMixing = null;
         this._shootBlockSprite = null;
         super.onDispose();
      }
      
      public function setChargeGunState(param1:Number, param2:uint, param3:Boolean) : void
      {
         this.chargeGunMixing.setChargeGunState(param1,param2);
         if(this._isShootBlockActive != param3)
         {
            this._isShootBlockActive = param3;
            this.setReloadingParams(this._reloadingInPercent,this._reloadingState);
            this._shootBlockSprite.graphics.clear();
         }
         if(this._isShootBlockActive)
         {
            this._shootBlockSprite.graphics.clear();
            this._shootBlockSprite.graphics.lineStyle(SHOOT_BLOCK_THICKNESS,SHOOT_BLOCK_COLOR,1,false,LineScaleMode.NONE,CapsStyle.NONE);
            GraphicsUtilities.drawArc(this._shootBlockSprite.graphics,0,0,HALF_PI,-FULL_CIRCLE * param1,SHOOT_BLOCK_RADIUS);
         }
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         this.chargeGunMixing.zoomFactor = param1;
      }
      
      override public function setAlpha(param1:Number, param2:Boolean) : void
      {
         super.setAlpha(param1,param2);
         this.chargeGunMixing.alpha = mixingAlpha;
      }
      
      public function set isChargeActive(param1:Boolean) : void
      {
         if(param1 == this._isChargeGunActive)
         {
            return;
         }
         this._isChargeGunActive = param1;
         invalidate(GunMarkerConsts.CHARGE_GUN_ACTIVE_VALIDATION);
      }
      
      override public function setType(param1:Number) : void
      {
         invalidate(GunMarkerConsts.GUN_MIXING_TYPE_VALIDATION);
         super.setType(param1);
      }
      
      private function onFadeTweenComplete() : void
      {
         if(this._isChargeGunActive)
         {
            if(currMixingMC != null)
            {
               currMixingMC.visible = false;
            }
         }
         else
         {
            this.chargeGunMixing.visible = false;
         }
      }
   }
}
