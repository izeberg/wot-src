package net.wg.gui.battle.views.widgetsPanel.stanceDance
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class StanceDanceProgress extends MovieClip implements IDisposable
   {
      
      private static const MAX_FRAME_COUNT:uint = 100;
      
      private static const SMOOTHING_FACTOR:Number = 0.1;
      
      private static const FRAME_TOLERANCE:int = 1;
       
      
      public var progressOn:MovieClip = null;
      
      public var progressOff:MovieClip = null;
      
      public var progressActive:MovieClip = null;
      
      private var _targetFrame:Number = 0;
      
      private var _currentFrame:Number = 0;
      
      private var _isDisposed:Boolean = false;
      
      public function StanceDanceProgress()
      {
         super();
         App.stage.addEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         App.stage.removeEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
         this.progressActive = null;
         this.progressOff = null;
         this.progressOn = null;
         this._isDisposed = true;
      }
      
      public function setProgress(param1:Number) : void
      {
         this._targetFrame = param1 * MAX_FRAME_COUNT;
      }
      
      private function onEnterFrameHandler(param1:Event) : void
      {
         var _loc2_:int = this._targetFrame - this._currentFrame;
         if(Math.abs(_loc2_) <= FRAME_TOLERANCE)
         {
            this._currentFrame = this._targetFrame;
         }
         else
         {
            this._currentFrame += _loc2_ * SMOOTHING_FACTOR;
         }
         this.progressActive.gotoAndStop(this._currentFrame);
         this.progressOff.gotoAndStop(this._currentFrame);
         this.progressOn.gotoAndStop(this._currentFrame);
      }
   }
}
