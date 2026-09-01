package net.wg.gui.battle.views.widgetsPanel.bustleFeed
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.widgetsPanel.common.SmoothFrameProgress;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class BustleFeedProgress extends MovieClip implements IDisposable
   {
      
      private static const FIRST_FRAME:uint = 1;
      
      private static const LAST_FRAME:uint = 50;
       
      
      public var progressAnim:MovieClip = null;
      
      private var _progression:SmoothFrameProgress = null;
      
      private var _isDisposed:Boolean = false;
      
      public function BustleFeedProgress()
      {
         super();
         this.progressAnim.stop();
         this._progression = new SmoothFrameProgress(this.progressAnim,FIRST_FRAME,LAST_FRAME);
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this._progression.dispose();
         this._progression = null;
         this.progressAnim = null;
         this._isDisposed = true;
      }
      
      public function set isInProgress(param1:Boolean) : void
      {
         this._progression.isActive = param1;
      }
      
      public function setProgress(param1:Number) : void
      {
         this._progression.progress = param1;
      }
      
      public function setAlpha(param1:Number) : void
      {
         this.progressAnim.alpha = param1;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
   }
}
