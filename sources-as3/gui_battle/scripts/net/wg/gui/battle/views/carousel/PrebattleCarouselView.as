package net.wg.gui.battle.views.carousel
{
   import fl.motion.easing.Circular;
   import net.wg.infrastructure.base.meta.impl.PrebattleCarouselViewMeta;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class PrebattleCarouselView extends PrebattleCarouselViewMeta implements IDisplayableComponent
   {
      
      private static const WIDTH:int = 1024;
      
      private static const HEIGHT:int = 140;
      
      private static const HIDE_TWEEN_DURATION:int = 300;
      
      private static const HIDE_OFFSET:int = 15;
       
      
      private var _tween:Tween = null;
      
      private var _visible:Boolean = true;
      
      private var _isHidden:Boolean = true;
      
      private var _showShadows:Boolean = true;
      
      private var _useAnim:Boolean = false;
      
      private var _originalY:int;
      
      public function PrebattleCarouselView()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
      }
      
      override protected function onDispose() : void
      {
         this.clearTween();
         super.onDispose();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this.updateVisibility();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseEnabled = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.STATE))
         {
            dispatchEvent(new PrebattleCarouselEvent(PrebattleCarouselEvent.STATE_CHANGED));
         }
      }
      
      public function as_hide(param1:Boolean) : void
      {
         this._useAnim = param1;
         if(param1)
         {
            this._tween = new Tween(HIDE_TWEEN_DURATION,this,{
               "alpha":0,
               "y":y + HIDE_OFFSET
            },{
               "ease":Circular.easeOut,
               "onComplete":this.onHideCompleted
            });
         }
         else
         {
            this.onHideCompleted();
         }
      }
      
      public function as_show() : void
      {
         alpha = 1;
         y = this._originalY;
         this._isHidden = false;
         this.clearTween();
         this.updateVisibility();
         dispatchEvent(new PrebattleCarouselEvent(PrebattleCarouselEvent.VIEW_SHOWN));
      }
      
      public function as_showShadows(param1:Boolean) : void
      {
         this._showShadows = param1;
         invalidateState();
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         this._visible = param1;
         this.updateVisibility();
      }
      
      public function setYPos(param1:int) : void
      {
         this._originalY = param1;
         this.y = param1;
      }
      
      private function updateVisibility() : void
      {
         visible = this._visible && !this._isHidden;
      }
      
      private function clearTween() : void
      {
         if(this._tween)
         {
            this._tween.paused = true;
            this._tween.dispose();
            this._tween = null;
         }
      }
      
      private function onHideCompleted(param1:Tween = null) : void
      {
         this._isHidden = true;
         dispatchEvent(new PrebattleCarouselEvent(PrebattleCarouselEvent.VIEW_HIDDEN,this._useAnim));
         this.clearTween();
         visible = false;
         onViewIsHiddenS();
      }
      
      public function get isHidden() : Boolean
      {
         return this._isHidden;
      }
      
      public function setInteractive(param1:Boolean) : void
      {
         mouseChildren = tabEnabled = tabChildren = param1;
      }
   }
}
