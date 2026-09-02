package net.wg.gui.components.crosshairPanel.wt
{
   import fl.motion.easing.Cubic;
   import net.wg.infrastructure.base.meta.IWTCrosshairPanelContainerMeta;
   import net.wg.infrastructure.base.meta.impl.WTCrosshairPanelContainerMeta;
   import scaleform.clik.motion.Tween;
   
   public class WTCrosshairPanelContainer extends WTCrosshairPanelContainerMeta implements IWTCrosshairPanelContainerMeta
   {
      
      private static const FADE_DURATION:uint = 400;
       
      
      private var _fadeTween:Tween = null;
      
      public function WTCrosshairPanelContainer()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.clearFadeTween();
         super.onDispose();
      }
      
      public function as_hide(param1:Boolean) : void
      {
         if(!param1)
         {
            alpha = 0;
         }
         else
         {
            this.clearFadeTween();
            this._fadeTween = new Tween(FADE_DURATION,this,{"alpha":0},{"ease":Cubic.easeIn});
         }
      }
      
      public function as_hideIncreaseDamage(param1:Boolean) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.hideIncreaseDamage(param1);
         }
      }
      
      public function as_hideReloadBoost(param1:Boolean) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.hideReloadBoost();
         }
      }
      
      public function as_setPlasmaSaved(param1:Number) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.setPlasmaSaved(param1);
         }
      }
      
      public function as_show(param1:Boolean) : void
      {
         if(!param1)
         {
            alpha = 1;
         }
         else
         {
            this.clearFadeTween();
            this._fadeTween = new Tween(FADE_DURATION,this,{"alpha":1},{"ease":Cubic.easeIn});
         }
      }
      
      public function as_showBarrier(param1:Boolean, param2:String) : void
      {
         if(this.wtCrosshair is WTCrosshairArcade)
         {
            (this.wtCrosshair as WTCrosshairArcade).showBarrier(param1,param2);
         }
      }
      
      public function as_showExplosiveShotIndicator(param1:Boolean) : void
      {
         if(gunMarkersContainer != null)
         {
            gunMarkersContainer.setExplosiveShotMarker(param1);
         }
         if(this.wtCrosshair)
         {
            this.wtCrosshair.setExplosiveShotVisible(param1);
         }
      }
      
      public function as_showIncreaseDamage(param1:Boolean) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.showIncreaseDamage(param1);
         }
      }
      
      public function as_showPlasmaIndicator(param1:Number, param2:Number, param3:String) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.showPlasmaIndicator(param1,param2,param3);
         }
      }
      
      public function as_showReloadBoost(param1:Boolean) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.showReloadBoost(param1);
         }
      }
      
      public function as_updateIncreaseDamage(param1:uint, param2:Boolean, param3:Boolean) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.updateIncreaseDamage(param1,param2,param3);
         }
      }
      
      public function as_updateReloadBoost(param1:uint, param2:Boolean, param3:Boolean) : void
      {
         if(this.wtCrosshair)
         {
            this.wtCrosshair.updateReload(param1,param2,param3);
         }
      }
      
      private function clearFadeTween() : void
      {
         if(this._fadeTween)
         {
            this._fadeTween.dispose();
            this._fadeTween = null;
         }
      }
      
      private function get wtCrosshair() : WTCrosshairBase
      {
         if(currentCrosshair is WTCrosshairBase)
         {
            return currentCrosshair as WTCrosshairBase;
         }
         return null;
      }
   }
}
