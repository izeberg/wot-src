package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.infrastructure.base.meta.ITargetDesignatorWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.TargetDesignatorWidgetMeta;
   
   public class TargetDesignatorWidget extends TargetDesignatorWidgetMeta implements ITargetDesignatorWidgetMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE,MECHANICS_WIDGET_CONST.IDLE];
      
      private static const HOT_KEY_START_POS_X:int = 0;
      
      private static const HOT_KEY_START_POS_Y:int = 0;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
       
      
      public var forwardProgress:MovieClip;
      
      public var hotkeyTarget:MovieClip = null;
      
      public function TargetDesignatorWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function getHotKeysTarget() : DisplayObjectContainer
      {
         return this.hotkeyTarget;
      }
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),true,HotkeySettings.DIRECTION_DOWN,Values.ZERO,HOT_KEY_GAP_Y);
      }
      
      override protected function onDispose() : void
      {
         this.forwardProgress = null;
         this.hotkeyTarget = null;
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
      
      public function as_setPreparingProgress(param1:Number) : void
      {
         this.forwardProgress.gotoAndStop(WidgetsPanel.FORWARD_PROGRESSION_MAX_FRAME * param1);
      }
   }
}
