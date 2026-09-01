package net.wg.gui.battle.views.widgetsPanel.autoreloaderSurge
{
   import flash.display.MovieClip;
   import flash.events.TimerEvent;
   import flash.utils.Timer;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class AutoreloaderSurgeActionLine extends MovieClip implements IDisposable
   {
      
      public static const GLOW_ANIMATION_FRAME:int = 32;
      
      private static const CIRCLE_FRAMES:int = 18;
      
      private static const PLAY_DELAY_MS:int = 500;
       
      
      public var pointer:MovieClip = null;
      
      private var _sectorCount:int = 0;
      
      private var _disposed:Boolean = false;
      
      private var _delayTimer:Timer = null;
      
      private var _pendingFrame:int = 1;
      
      public function AutoreloaderSurgeActionLine()
      {
         super();
         stop();
         this.pointer.visible = false;
      }
      
      public function set sectorCount(param1:int) : void
      {
         this._sectorCount = param1;
      }
      
      public function playFromSector(param1:int) : void
      {
         this.hide();
         this._pendingFrame = this._sectorCount > 1 ? int(Math.round(param1 * CIRCLE_FRAMES / (this._sectorCount - 1)) + 1) : int(1);
         this.stopDelay();
         this._delayTimer = new Timer(PLAY_DELAY_MS,1);
         this._delayTimer.addEventListener(TimerEvent.TIMER_COMPLETE,this.onDelayComplete);
         this._delayTimer.start();
      }
      
      public function dispose() : void
      {
         this.stopDelay();
         addFrameScript(GLOW_ANIMATION_FRAME,null);
         this.pointer = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function show() : void
      {
         this.pointer.visible = true;
      }
      
      public function hide() : void
      {
         this.pointer.visible = false;
      }
      
      private function onDelayComplete(param1:TimerEvent) : void
      {
         this.stopDelay();
         this.show();
         gotoAndPlay(this._pendingFrame);
      }
      
      private function stopDelay() : void
      {
         if(this._delayTimer)
         {
            this._delayTimer.removeEventListener(TimerEvent.TIMER_COMPLETE,this.onDelayComplete);
            this._delayTimer.stop();
            this._delayTimer = null;
         }
      }
   }
}
