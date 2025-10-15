package net.wg.portal.gui.battle.components
{
   import flash.display.MovieClip;
   import net.wg.data.constants.Time;
   import net.wg.infrastructure.base.SimpleDisposable;
   import scaleform.clik.motion.Tween;
   
   public class AbilityProgressFill extends SimpleDisposable
   {
      
      private static const GLOW_MC_TARGET_X:int = 44;
      
      private static const BAR_MC_TARGET_WIDTH:int = 1;
       
      
      public var glowMc:MovieClip = null;
      
      public var barMc:MovieClip = null;
      
      private var _glowMcOriginX:int = 0;
      
      private var _barMcOriginWidth:int = 0;
      
      private var _glowMcTween:Tween = null;
      
      private var _barMcTween:Tween = null;
      
      public function AbilityProgressFill()
      {
         super();
         this._glowMcOriginX = this.glowMc.x;
         this._barMcOriginWidth = this.barMc.width;
      }
      
      override protected function onDispose() : void
      {
         this.clearProgressTween();
         this.glowMc = null;
         this.barMc = null;
         super.onDispose();
      }
      
      public function clearProgressTween() : void
      {
         if(this._glowMcTween)
         {
            this._glowMcTween.dispose();
            this._glowMcTween = null;
         }
         if(this._barMcTween)
         {
            this._barMcTween.dispose();
            this._barMcTween = null;
         }
      }
      
      public function startCountdown(param1:int) : void
      {
         this.clearProgressTween();
         this.glowMc.x = this._glowMcOriginX;
         this.glowMc.visible = true;
         this.barMc.width = this._barMcOriginWidth;
         this._glowMcTween = new Tween(param1 * Time.MILLISECOND_IN_SECOND,this.glowMc,{"x":GLOW_MC_TARGET_X},{"onComplete":this.onGlowMcTweenComplete});
         this._barMcTween = new Tween(param1 * Time.MILLISECOND_IN_SECOND,this.barMc,{"width":BAR_MC_TARGET_WIDTH});
      }
      
      private function onGlowMcTweenComplete() : void
      {
         this.glowMc.visible = false;
      }
   }
}
