package net.wg.gui.battle.views.decorativeCrosshair.accuracy
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class AccuracyProgressbar extends MovieClip implements IDisposable
   {
      
      private static const MARK_ANIM_CYCLE:String = "cycle";
      
      private static const MARK_ANIM_BLINK:String = "blink";
      
      private static const MARK_ANIM_HIDE:String = "hide";
      
      private static const FULL_ANIM_SHOW:String = "show";
      
      private static const FULL_ANIM_HIDE:String = "hide";
      
      private static const SMOOTHING_FACTOR:Number = 0.2;
      
      private static const FRAME_TOLERANCE:int = 1;
       
      
      public var full:MovieClip = null;
      
      public var mark:MovieClip = null;
      
      private var _framePerStack:uint;
      
      private var _gainingActive:Boolean = false;
      
      private var _isMaxStackGained:Boolean = false;
      
      private var _currentFrame:uint = 0;
      
      private var _targetFrame:uint = 0;
      
      private var _maxStackCount:uint = 1;
      
      private var _isDisposed:Boolean = false;
      
      public function AccuracyProgressbar()
      {
         super();
         this.mark.gotoAndStop(MARK_ANIM_CYCLE);
         App.stage.addEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
      }
      
      public function setMaxStackCount(param1:uint) : void
      {
         this._maxStackCount = param1;
         this._framePerStack = totalFrames / this._maxStackCount;
      }
      
      public function updateStacksAndProgress(param1:int, param2:Number, param3:Boolean) : void
      {
         this._targetFrame = this._framePerStack * (param1 + param2);
         if(this._isMaxStackGained != param3)
         {
            this.full.gotoAndPlay(!!param3 ? FULL_ANIM_SHOW : FULL_ANIM_HIDE);
            this.mark.visible = !param3;
            this._isMaxStackGained = param3;
         }
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
         gotoAndStop(this._currentFrame);
      }
      
      public function gainingActive(param1:Boolean) : void
      {
         if(this._gainingActive && !param1)
         {
            this.mark.gotoAndPlay(MARK_ANIM_HIDE);
         }
         else if(!this._gainingActive && param1)
         {
            this.mark.gotoAndPlay(MARK_ANIM_BLINK);
         }
         else if(!param1)
         {
            this.mark.gotoAndStop(MARK_ANIM_CYCLE);
         }
         this._gainingActive = param1;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         App.stage.removeEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
         this.mark = null;
         this.full = null;
         this._isDisposed = true;
      }
   }
}
