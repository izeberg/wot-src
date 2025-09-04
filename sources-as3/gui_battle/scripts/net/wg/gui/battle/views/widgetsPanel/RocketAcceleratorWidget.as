package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.infrastructure.base.meta.IRocketAcceleratorIndicatorMeta;
   import net.wg.infrastructure.base.meta.impl.RocketAcceleratorIndicatorMeta;
   
   public class RocketAcceleratorWidget extends RocketAcceleratorIndicatorMeta implements IRocketAcceleratorIndicatorMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE,MECHANICS_WIDGET_CONST.IDLE];
      
      private static const BALLOON_Y:int = 7;
      
      private static const BALLOON_H_FULL:int = 27;
       
      
      public var countTF:TextField;
      
      public var balloonMask:MovieClip;
      
      public function RocketAcceleratorWidget()
      {
         super();
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         blendMode = BlendMode.SCREEN;
         this.balloonMask.y = BALLOON_Y;
      }
      
      override protected function onDispose() : void
      {
         this.countTF = null;
         this.balloonMask = null;
         super.onDispose();
      }
      
      public function as_setCount(param1:int) : void
      {
         this.countTF.text = param1.toString();
      }
      
      public function as_setProgress(param1:Number) : void
      {
         this.balloonMask.y = BALLOON_Y - BALLOON_H_FULL * param1 | 0;
      }
      
      public function as_updateLayout(param1:Number, param2:Number) : void
      {
      }
   }
}
