package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.infrastructure.base.meta.IConcentrationWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.ConcentrationWidgetMeta;
   
   public class ConcentrationWidget extends ConcentrationWidgetMeta implements IConcentrationWidgetMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE,MECHANICS_WIDGET_CONST.IDLE];
       
      
      public var forwardProgress:MovieClip;
      
      public var reverseProgress:MovieClip;
      
      public function ConcentrationWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function onDispose() : void
      {
         this.forwardProgress = null;
         this.reverseProgress = null;
         super.onDispose();
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
      
      public function as_setActiveProgress(param1:Number) : void
      {
         this.reverseProgress.gotoAndStop(WidgetsPanel.REVERES_PROGRESSION_MAX_FRAME * param1);
      }
      
      public function as_setPreparingProgress(param1:Number) : void
      {
         this.forwardProgress.gotoAndStop(WidgetsPanel.FORWARD_PROGRESSION_MAX_FRAME * param1);
      }
   }
}
