package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.MovieClip;
   import flash.geom.ColorTransform;
   import flash.utils.clearTimeout;
   import flash.utils.setTimeout;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.data.constants.generated.STATIONARY_RELOAD_WIDGET_CONSTS;
   import net.wg.infrastructure.base.meta.IStationaryReloadWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.StationaryReloadWidgetMeta;
   
   public class StationaryReloadWidget extends StationaryReloadWidgetMeta implements IStationaryReloadWidgetMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE,MECHANICS_WIDGET_CONST.IDLE,MECHANICS_WIDGET_CONST.PREPARING,MECHANICS_WIDGET_CONST.ACTIVE];
      
      private static const CRITICAL_COLOR_TRANSFORM:ColorTransform = new ColorTransform(0,0,0,1,255,127,0,0);
      
      private static const DESTROYED_COLOR_TRANSFORM:ColorTransform = new ColorTransform(0,0,0,1,255,0,0,0);
      
      private static const DESTROYED_ANIMATION_DURATION:int = 5000;
      
      private static const INVALID_CONDITION:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
       
      
      public var statusIndicator:MovieClip;
      
      private var _damageAnimTimeoutId:int = -1;
      
      private var _condition:String = "normal";
      
      public function StationaryReloadWidget()
      {
         super();
      }
      
      override protected function draw() : void
      {
         var _loc1_:ColorTransform = null;
         super.draw();
         if(this.statusIndicator && isInvalid(InvalidationType.STATE | INVALID_CONDITION))
         {
            _loc1_ = null;
            if(this._condition == STATIONARY_RELOAD_WIDGET_CONSTS.CRITICAL)
            {
               _loc1_ = CRITICAL_COLOR_TRANSFORM;
            }
            else if(this._condition == STATIONARY_RELOAD_WIDGET_CONSTS.DESTROYED)
            {
               _loc1_ = DESTROYED_COLOR_TRANSFORM;
            }
            this.statusIndicator.transform.colorTransform = _loc1_;
            if(timer)
            {
               timer.transform.colorTransform = _loc1_;
            }
            this.clearAnimationTimeout();
            this.statusIndicator.gotoAndPlay(this._condition);
            if(this._condition == STATIONARY_RELOAD_WIDGET_CONSTS.DESTROYED)
            {
               this._damageAnimTimeoutId = setTimeout(this.onAnimationComplete,DESTROYED_ANIMATION_DURATION);
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearAnimationTimeout();
         this.statusIndicator = null;
         super.onDispose();
      }
      
      public function as_setCondition(param1:String) : void
      {
         if(this._condition == param1)
         {
            return;
         }
         this._condition = param1;
         invalidate(INVALID_CONDITION);
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.DISABLE;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      private function onAnimationComplete() : void
      {
         if(this.statusIndicator)
         {
            this.statusIndicator.gotoAndStop(this._condition);
         }
         this._damageAnimTimeoutId = -1;
      }
      
      private function clearAnimationTimeout() : void
      {
         if(this._damageAnimTimeoutId == -1)
         {
            return;
         }
         clearTimeout(this._damageAnimTimeoutId);
         this._damageAnimTimeoutId = -1;
      }
   }
}
