package net.wg.gui.components.tooltips.inblocks
{
   import fl.transitions.easing.Strong;
   import flash.display.DisplayObject;
   import net.wg.gui.events.AnimationEvent;
   import scaleform.clik.motion.Tween;
   
   public class AdvancedShuffleTooltip extends TooltipInBlocks
   {
      
      private static const MAIN_ANIMATION_NAME:String = "mainAnimationClip";
      
      private static const TWEEN_DURATION:int = 150;
      
      private static const TWEEN_BG_DURATION:int = 350;
       
      
      private var _rawData:Array = null;
      
      private var _dataIdx:int = 0;
      
      private var _isUpdateData:Boolean = false;
      
      private var _fadeInTween:Tween = null;
      
      private var _fadeOutTween:Tween = null;
      
      private var _bgTween:Tween = null;
      
      public function AdvancedShuffleTooltip()
      {
         super();
         this._fadeInTween = new Tween(TWEEN_DURATION,this,{"alpha":1},{"paused":true});
      }
      
      override protected function initData(param1:Object) : void
      {
         var _loc2_:Array = param1["data"] as Array;
         if(_loc2_)
         {
            this._rawData = _loc2_;
            param1["data"] = App.utils.data.cloneObject(this._rawData[0]);
            if(this._rawData.length > 1)
            {
               this._fadeOutTween = new Tween(TWEEN_DURATION,content,{"alpha":0},{
                  "paused":true,
                  "onComplete":this.onFadeOutComplete
               });
               addEventListener(AnimationEvent.ANIM_COMPLETE,this.onAnimCompleteHandler);
            }
         }
         this._dataIdx = 0;
         super.initData(param1);
      }
      
      override protected function setBackgroundSize(param1:int, param2:int) : void
      {
         if(!this._isUpdateData)
         {
            super.setBackgroundSize(param1,param2);
         }
         else
         {
            if(this._bgTween)
            {
               this._bgTween.paused = true;
            }
            this._bgTween = new Tween(TWEEN_BG_DURATION,background,{
               "width":param1,
               "height":param2
            },{
               "paused":false,
               "ease":Strong.easeOut
            });
         }
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(AnimationEvent.ANIM_COMPLETE,this.onAnimCompleteHandler);
         this._fadeOutTween = this.removeTween(this._fadeOutTween);
         this._bgTween = this.removeTween(this._bgTween);
         this._fadeInTween = this.removeTween(this._fadeInTween);
         this._rawData = null;
         super.onDispose();
      }
      
      private function removeTween(param1:Tween) : Tween
      {
         if(param1)
         {
            param1.dispose();
         }
         return null;
      }
      
      override protected function fadeIn() : void
      {
         this.visible = true;
         this._fadeInTween.target.alpha = 0;
         this._fadeInTween.paused = false;
      }
      
      private function onFadeOutComplete(param1:Tween) : void
      {
         this._fadeInTween.dispose();
         this._fadeInTween = new Tween(TWEEN_DURATION,content,{"alpha":1},{"paused":true});
         redraw();
      }
      
      override public function set x(param1:Number) : void
      {
         if(this._isUpdateData)
         {
            return;
         }
         super.x = param1;
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(this._isUpdateData)
         {
            return;
         }
         super.visible = param1;
      }
      
      override public function set y(param1:Number) : void
      {
         if(this._isUpdateData)
         {
            return;
         }
         super.y = param1;
      }
      
      private function onAnimCompleteHandler(param1:AnimationEvent) : void
      {
         param1.stopImmediatePropagation();
         var _loc2_:DisplayObject = param1.target as DisplayObject;
         if(_loc2_ && _loc2_.hasOwnProperty(MAIN_ANIMATION_NAME))
         {
            _loc2_[MAIN_ANIMATION_NAME].stop();
            _loc2_.visible = false;
         }
         this._isUpdateData = true;
         ++this._dataIdx;
         if(this._dataIdx >= this._rawData.length)
         {
            this._dataIdx = 0;
         }
         _data = App.utils.data.cloneObject(this._rawData[this._dataIdx]);
         this._fadeOutTween.paused = false;
      }
   }
}
