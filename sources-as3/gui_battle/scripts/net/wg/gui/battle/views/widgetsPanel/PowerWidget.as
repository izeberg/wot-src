package net.wg.gui.battle.views.widgetsPanel
{
   import com.gskinner.motion.easing.Quadratic;
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.power.TurbineAnimation;
   import net.wg.infrastructure.base.meta.IPowerWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.PowerWidgetMeta;
   
   public class PowerWidget extends PowerWidgetMeta implements IPowerWidgetMeta
   {
      
      private static const PROGRESSION_FRAMES_COUNT:uint = 107;
      
      private static const INSTANT_TRANSITION_STATES:Array = [];
      
      private static const TURBINE_SPEED_FACTOR_INCREMENT:Number = 2;
       
      
      public var turbineAnimation:TurbineAnimation;
      
      public var progressMC:MovieClip;
      
      public function PowerWidget()
      {
         super();
         this.blendMode = BlendMode.SCREEN;
      }
      
      override protected function onDispose() : void
      {
         this.turbineAnimation.dispose();
         this.turbineAnimation = null;
         this.progressMC = null;
         super.onDispose();
      }
      
      public function as_setProgress(param1:Number) : void
      {
         if(state == MECHANICS_WIDGET_CONST.PREPARING)
         {
            this.progressMC.gotoAndStop(1 + PROGRESSION_FRAMES_COUNT * param1 | 0);
            if(this.turbineAnimation.alpha == 0)
            {
               this.turbineAnimation.speedFactor = 0;
            }
         }
         else if(state == MECHANICS_WIDGET_CONST.ACTIVE)
         {
            this.turbineAnimation.speedFactor = 1 + Quadratic.easeInOut(param1,NaN,NaN,NaN) * TURBINE_SPEED_FACTOR_INCREMENT;
         }
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
   }
}
