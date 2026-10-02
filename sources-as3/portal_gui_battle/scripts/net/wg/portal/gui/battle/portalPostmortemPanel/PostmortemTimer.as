package net.wg.portal.gui.battle.portalPostmortemPanel
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.battle.components.FrameAnimationTimer;
   
   public class PostmortemTimer extends FrameAnimationTimer
   {
      
      private static const START_FRAME:int = 1;
      
      private static const END_FRAME:int = 145;
       
      
      public var graphicsSpr:PostmortemTimerContainer = null;
      
      public function PostmortemTimer()
      {
         super();
         init(true,true);
      }
      
      override protected function invokeAdditionalActionOnIntervalUpdate() : void
      {
      }
      
      override protected function getProgressBarMc() : MovieClip
      {
         return this.graphicsSpr.progressBar;
      }
      
      override protected function getTimerTF() : TextField
      {
         return this.graphicsSpr.textField;
      }
      
      override protected function onIntervalHideUpdateHandler() : void
      {
         this.stopTimer();
      }
      
      override protected function getStartFrame() : int
      {
         return START_FRAME;
      }
      
      override protected function getEndFrame() : int
      {
         return END_FRAME;
      }
      
      override protected function resetAnimState() : void
      {
      }
      
      override protected function onDispose() : void
      {
         this.graphicsSpr.dispose();
         this.graphicsSpr = null;
         super.onDispose();
      }
      
      public function stopTimer() : void
      {
         pauseRadialTimer();
         pauseHideTimer();
      }
   }
}
