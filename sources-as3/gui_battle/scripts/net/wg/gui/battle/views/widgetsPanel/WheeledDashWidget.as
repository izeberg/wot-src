package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.wheeledDash.HighlightTimer;
   import net.wg.infrastructure.base.meta.IWheeledDashWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.WheeledDashWidgetMeta;
   
   public class WheeledDashWidget extends WheeledDashWidgetMeta implements IWheeledDashWidgetMeta
   {
      
      private static const INVALID_COOLDOWN:int = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const PROGRESS_ALPHA:Number = 0.5;
      
      private static const PROGRESS_ALPHA_REDUCE_ALPHA:Number = 0.8;
      
      private static const PREPARING_ICON_ALPHA:Number = 0.5;
      
      private static const PREPARING_ICON_REDUCE_ALPHA:Number = 0.8;
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE,MECHANICS_WIDGET_CONST.IDLE];
      
      private static const TIMER_ARROW_X_SHIFT:int = 6;
      
      private static const TIMER_ARROW_Y_SHIFT:int = 4;
       
      
      public var forwardProgress:MovieClip;
      
      public var reverseProgress:MovieClip;
      
      public var arrows:Sprite;
      
      public var preparingIcon:Sprite;
      
      private var _isHighlighted:Boolean = false;
      
      public function WheeledDashWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
         this.forwardProgress.alpha = PROGRESS_ALPHA;
         this.forwardProgress.visible = false;
         this.preparingIcon.alpha = PREPARING_ICON_ALPHA;
         this.arrows.visible = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INVALID_COOLDOWN))
         {
            this.updateArrowPosition();
         }
      }
      
      override protected function onDispose() : void
      {
         this.forwardProgress = null;
         this.reverseProgress = null;
         this.arrows = null;
         this.preparingIcon = null;
         super.onDispose();
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         super.applyState(param1,param2);
         var _loc3_:Boolean = [MECHANICS_WIDGET_CONST.DEPLOYING,MECHANICS_WIDGET_CONST.PREPARING].indexOf(param1) != -1;
         this.forwardProgress.visible = _loc3_;
         this.preparingIcon.visible = _loc3_ || param1 == MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      override protected function getHotKeyVisibility() : Boolean
      {
         var _loc1_:Boolean = super.getHotKeyVisibility();
         return _loc1_ && this.state == MECHANICS_WIDGET_CONST.READY;
      }
      
      public function as_isReducedCooldown(param1:Boolean) : void
      {
         if(param1)
         {
            this.forwardProgress.alpha = PROGRESS_ALPHA_REDUCE_ALPHA;
            this.preparingIcon.alpha = PREPARING_ICON_REDUCE_ALPHA;
         }
         else
         {
            this.forwardProgress.alpha = PROGRESS_ALPHA;
            this.preparingIcon.alpha = PREPARING_ICON_ALPHA;
         }
         this.arrows.visible = param1;
         this._isHighlighted = param1;
         invalidate(INVALID_COOLDOWN);
      }
      
      public function as_setActiveProgress(param1:Number) : void
      {
         this.reverseProgress.gotoAndStop(WidgetsPanel.REVERES_PROGRESSION_MAX_FRAME * param1);
      }
      
      public function as_setPreparingProgress(param1:Number) : void
      {
         this.forwardProgress.gotoAndStop(WidgetsPanel.FORWARD_PROGRESSION_MAX_FRAME * param1);
      }
      
      private function updateArrowPosition() : void
      {
         this.arrows.x = timer.x + timer.timeWidth + TIMER_ARROW_X_SHIFT;
         this.arrows.y = timer.y + TIMER_ARROW_Y_SHIFT;
         var _loc1_:HighlightTimer = timer as HighlightTimer;
         if(_loc1_)
         {
            _loc1_.highlight = this._isHighlighted;
         }
      }
   }
}
