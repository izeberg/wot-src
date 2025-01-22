package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.events.Event;
   import net.wg.infrastructure.base.SimpleDisposable;
   import scaleform.clik.motion.Tween;
   
   public class ActionAnim extends SimpleDisposable
   {
      
      private static const HIDE_DURATION:int = 1000;
       
      
      private var _hideTween:Tween = null;
      
      public function ActionAnim()
      {
         super();
         addFrameScript(totalFrames - 2,this.onAnimationComplete);
      }
      
      override protected function onDispose() : void
      {
         stop();
         if(this._hideTween)
         {
            this._hideTween.dispose();
            this._hideTween = null;
         }
         super.onDispose();
      }
      
      public function hideAnim() : void
      {
         stop();
         if(!this._hideTween)
         {
            this._hideTween = new Tween(HIDE_DURATION,this,{"alpha":0},{"onComplete":this.onHideTweenComplete});
         }
         this._hideTween.paused = false;
      }
      
      public function hideImmediately() : void
      {
         if(this._hideTween && !this._hideTween.paused)
         {
            this._hideTween.paused = true;
         }
         this.animComplete();
      }
      
      public function show() : void
      {
         alpha = 1;
         visible = true;
         gotoAndPlay(1);
      }
      
      protected function animComplete() : void
      {
         gotoAndStop(1);
         visible = false;
         dispatchEvent(new Event(Event.COMPLETE));
      }
      
      private function onAnimationComplete() : void
      {
         this.animComplete();
      }
      
      private function onHideTweenComplete(param1:Tween) : void
      {
         this.animComplete();
      }
   }
}
