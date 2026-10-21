package net.wg.gui.components.tooltips.inblocks.blocks
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import net.wg.data.constants.Errors;
   import net.wg.gui.components.tooltips.inblocks.data.ImageBlockVO;
   import net.wg.gui.components.tooltips.inblocks.events.ToolTipBlockEvent;
   import net.wg.gui.events.AnimationEvent;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.controls.UILoader;
   
   public class AdvancedClipBlock extends BaseTooltipBlock
   {
      
      private static const MOVIE_PATH:String = "moviePath ";
      
      private static const MIN_ANIMATION_FRAMES:int = 20;
       
      
      private var _loader:UILoader;
      
      private var _data:ImageBlockVO;
      
      private var _isDataApplied:Boolean = false;
      
      private var _mainAnimationClip:MovieClip;
      
      public function AdvancedClipBlock()
      {
         this._loader = new UILoader();
         super();
         this._loader.addEventListener(Event.COMPLETE,this.onLoaderCompleteHandler);
      }
      
      override public function cleanUp() : void
      {
         this.clearData();
         this._loader.unload();
         super.cleanUp();
      }
      
      override public function setBlockData(param1:Object) : void
      {
         this.clearData();
         this._data = new ImageBlockVO(param1);
         this._isDataApplied = false;
         invalidateBlock();
      }
      
      override public function setBlockWidth(param1:int) : void
      {
      }
      
      override protected function onDispose() : void
      {
         this.cleanUp();
         this._loader.removeEventListener(Event.COMPLETE,this.onLoaderCompleteHandler);
         if(this._loader.loader && this._loader.content)
         {
            this._loader.content.removeEventListener(Event.ENTER_FRAME,this.onChangeFrameHandler);
         }
         this._loader.dispose();
         this._loader = null;
         if(this._mainAnimationClip)
         {
            this._mainAnimationClip.removeEventListener(Event.ENTER_FRAME,this.onAnimEnterFameHandler);
         }
         this._mainAnimationClip = null;
         super.onDispose();
      }
      
      override protected function onValidateBlock() : Boolean
      {
         if(!this._isDataApplied)
         {
            this.applyData();
            return true;
         }
         return false;
      }
      
      private function applyData() : void
      {
         App.utils.asserter.assert(StringUtils.isNotEmpty(this._data.imagePath),MOVIE_PATH + Errors.CANT_EMPTY);
         this._loader.source = this._data.imagePath;
         this._isDataApplied = true;
      }
      
      private function clearData() : void
      {
         if(this._data != null)
         {
            this._data.dispose();
            this._data = null;
         }
      }
      
      private function setMainAnim(param1:MovieClip) : void
      {
         if(this._mainAnimationClip != param1)
         {
            this._mainAnimationClip = param1;
            this._mainAnimationClip.addEventListener(Event.ENTER_FRAME,this.onAnimEnterFameHandler);
         }
      }
      
      private function searchAnimMovieClip(param1:MovieClip) : void
      {
         var _loc3_:MovieClip = null;
         var _loc2_:int = param1.numChildren;
         var _loc4_:int = 0;
         while(_loc4_ < _loc2_)
         {
            _loc3_ = param1.getChildAt(_loc4_) as MovieClip;
            if(_loc3_ && _loc3_.totalFrames > MIN_ANIMATION_FRAMES)
            {
               this.setMainAnim(_loc3_);
               break;
            }
            _loc4_++;
         }
      }
      
      public function get mainAnimationClip() : MovieClip
      {
         return this._mainAnimationClip;
      }
      
      private function onLoaderCompleteHandler(param1:Event) : void
      {
         var _loc2_:MovieClip = this._loader.content as MovieClip;
         addChild(_loc2_);
         if(_loc2_.totalFrames > MIN_ANIMATION_FRAMES)
         {
            this.setMainAnim(_loc2_);
         }
         else
         {
            _loc2_.addEventListener(Event.ENTER_FRAME,this.onChangeFrameHandler);
         }
         dispatchEvent(new ToolTipBlockEvent(ToolTipBlockEvent.SIZE_CHANGE,this));
      }
      
      private function onChangeFrameHandler(param1:Event) : void
      {
         var _loc2_:MovieClip = this._loader.content as MovieClip;
         if(_loc2_ && _loc2_.currentFrame == _loc2_.totalFrames)
         {
            this.searchAnimMovieClip(_loc2_);
            _loc2_.removeEventListener(Event.ENTER_FRAME,this.onChangeFrameHandler);
         }
      }
      
      private function onAnimEnterFameHandler(param1:Event) : void
      {
         if(this._mainAnimationClip && this._mainAnimationClip.currentFrame == this._mainAnimationClip.totalFrames)
         {
            dispatchEvent(new AnimationEvent(AnimationEvent.ANIM_COMPLETE,true,true));
            this._mainAnimationClip.removeEventListener(Event.ENTER_FRAME,this.onAnimEnterFameHandler);
         }
      }
   }
}
