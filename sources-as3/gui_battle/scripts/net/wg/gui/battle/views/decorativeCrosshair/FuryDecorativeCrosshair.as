package net.wg.gui.battle.views.decorativeCrosshair
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.utils.getTimer;
   import net.wg.infrastructure.base.meta.IFuryDecorativeCrosshairMeta;
   import net.wg.infrastructure.base.meta.impl.FuryDecorativeCrosshairMeta;
   
   public class FuryDecorativeCrosshair extends FuryDecorativeCrosshairMeta implements IFuryDecorativeCrosshairMeta
   {
      
      private static const FRAME_PER_STEP:int = 100;
      
      private static const MIN_DIFF_TO_ANIMATE:int = 5;
      
      private static const TWEEN_DURATION:int = 150;
      
      private static var _currentAnimStackIncrease:Boolean = false;
      
      private static var _currentAnimStacksLeft:int = 0;
      
      private static const SHOW_ANIM:String = "show";
      
      private static const HIDE_ANIM:String = "hide";
       
      
      public var stack1:MovieClip = null;
      
      public var stack2:MovieClip = null;
      
      public var stack3:MovieClip = null;
      
      public var stack4:MovieClip = null;
      
      public var stack5:MovieClip = null;
      
      private var _stacks:Array;
      
      private var _currentFrame:int = 0;
      
      private var _startFrame:int = 0;
      
      private var _targetFrame:int = 0;
      
      private var _tweenStartTime:int = 0;
      
      private var _isTweening:Boolean = false;
      
      private var _prevActiveStacks:int = 0;
      
      public function FuryDecorativeCrosshair()
      {
         this._stacks = [this.stack1,this.stack2,this.stack3,this.stack4,this.stack5];
         super();
         this._stacks = [this.stack1,this.stack2,this.stack3,this.stack4,this.stack5];
      }
      
      override protected function onDispose() : void
      {
         App.utils.scheduler.cancelTask(this.updateAnimation);
         this.cleanTween();
         this._stacks = null;
         this.stack1 = null;
         this.stack2 = null;
         this.stack3 = null;
         this.stack4 = null;
         this.stack5 = null;
         super.onDispose();
      }
      
      private function cleanTween() : void
      {
         this._isTweening = false;
         removeEventListener(Event.ENTER_FRAME,this.updateTween);
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(visible != param1)
         {
            this.cleanTween();
         }
         super.visible = param1;
      }
      
      private function updateAnimation() : void
      {
         var _loc1_:String = !!_currentAnimStackIncrease ? SHOW_ANIM : HIDE_ANIM;
         var _loc2_:uint = this._prevActiveStacks;
         _loc2_ += !!_currentAnimStackIncrease ? -_currentAnimStacksLeft : _currentAnimStacksLeft - 1;
         this._stacks[_loc2_].gotoAndPlay(_loc1_);
         _currentAnimStacksLeft -= 1;
      }
      
      public function as_setGunStackProgress(param1:int, param2:Number) : void
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc3_:Number = FRAME_PER_STEP * (Math.max(param1 - 1,0) + param2);
         var _loc4_:Number = Math.abs(_loc3_ - this._currentFrame);
         if(this._prevActiveStacks != param1)
         {
            _currentAnimStackIncrease = param1 > this._prevActiveStacks;
            _loc5_ = !!_currentAnimStackIncrease ? int(this._prevActiveStacks) : int(param1);
            _loc6_ = !!_currentAnimStackIncrease ? int(param1) : int(this._prevActiveStacks);
            _currentAnimStacksLeft = _loc6_ - _loc5_;
            this._prevActiveStacks = param1;
            App.utils.scheduler.cancelTask(this.updateAnimation);
            App.utils.scheduler.scheduleRepeatableTask(this.updateAnimation,!!_currentAnimStackIncrease ? Number(200) : Number(50),_loc6_ - _loc5_);
         }
         if(_loc4_ < MIN_DIFF_TO_ANIMATE)
         {
            if(this._isTweening)
            {
               this.cleanTween();
            }
            this._currentFrame = _loc3_;
            gotoAndStop(Math.round(this._currentFrame));
         }
         else
         {
            this._startFrame = this._currentFrame;
            this._targetFrame = _loc3_;
            this._tweenStartTime = getTimer();
            if(!this._isTweening)
            {
               this._isTweening = true;
               addEventListener(Event.ENTER_FRAME,this.updateTween);
            }
         }
      }
      
      private function updateTween(param1:Event) : void
      {
         var _loc2_:int = getTimer() - this._tweenStartTime;
         var _loc3_:Number = _loc2_ / TWEEN_DURATION;
         if(_loc3_ > 1)
         {
            _loc3_ = 1;
         }
         var _loc4_:Number = 1 - Math.pow(1 - _loc3_,2);
         this._currentFrame = this._startFrame + _loc4_ * (this._targetFrame - this._startFrame);
         gotoAndStop(Math.round(this._currentFrame));
         if(_loc2_ >= TWEEN_DURATION)
         {
            this._currentFrame = this._targetFrame;
            gotoAndStop(this._currentFrame);
            this.cleanTween();
         }
      }
   }
}
