package net.wg.portal.gui.battle.components
{
   import flash.display.MovieClip;
   import net.wg.data.constants.Time;
   import net.wg.infrastructure.base.SimpleDisposable;
   import scaleform.clik.motion.Tween;
   
   public class AbilityProgressFill extends SimpleDisposable
   {
      
      private static const GLOW_MC_TARGET_X:int = -14;
      
      private static const BAR_MC_TARGET_WIDTH:int = 1;
      
      private static const GLOW_MC_OFFSET_X:uint = 16;
      
      private static const WIDTH_EXTRA_SMALL:uint = 46;
      
      private static const WIDTH_MEDIUM:uint = 88;
      
      private static const TIME_MIN:uint = 400;
      
      private static const RERUN_TWEEN_DELAY:uint = 100;
       
      
      public var glowMc:MovieClip = null;
      
      public var barMc:MovieClip = null;
      
      public var bg:MovieClip = null;
      
      private var _glowMcTween:Tween = null;
      
      private var _barMcTween:Tween = null;
      
      private var _isExtraSmallLayout:Boolean = false;
      
      public function AbilityProgressFill()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.clearProgressTween();
         this.glowMc = null;
         this.barMc = null;
         this.bg = null;
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
         this.updateLayout();
         this.barMc.visible = true;
         this.runTween(param1 * Time.MILLISECOND_IN_SECOND);
      }
      
      public function useExtraSmallLayout() : void
      {
         if(!this._isExtraSmallLayout)
         {
            this._isExtraSmallLayout = true;
            this.updateLayout();
         }
      }
      
      public function useMediumLayout() : void
      {
         if(this._isExtraSmallLayout)
         {
            this._isExtraSmallLayout = false;
            this.updateLayout();
         }
      }
      
      private function runTween(param1:int) : void
      {
         this._glowMcTween = new Tween(param1,this.glowMc,{"x":GLOW_MC_TARGET_X},{"onComplete":this.onGlowMcTweenComplete});
         this._barMcTween = new Tween(param1,this.barMc,{"width":BAR_MC_TARGET_WIDTH});
      }
      
      private function updateLayout() : void
      {
         var _loc2_:int = 0;
         if(this._glowMcTween)
         {
            _loc2_ = this._glowMcTween.duration - this._glowMcTween.position;
            this.clearProgressTween();
            if(_loc2_ > TIME_MIN)
            {
               App.utils.scheduler.scheduleTask(this.runTween,RERUN_TWEEN_DELAY,_loc2_);
            }
         }
         var _loc1_:uint = !!this._isExtraSmallLayout ? uint(WIDTH_EXTRA_SMALL) : uint(WIDTH_MEDIUM);
         this.glowMc.x = _loc1_ - GLOW_MC_OFFSET_X;
         this.barMc.width = _loc1_;
         this.bg.width = _loc1_;
      }
      
      private function onGlowMcTweenComplete() : void
      {
         this.barMc.visible = false;
         this.clearProgressTween();
      }
   }
}
