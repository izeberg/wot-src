package net.wg.portal.gui.battle.views.interceptionWidget
{
   import flash.display.Sprite;
   import net.wg.portal.gui.battle.components.AbilityDurationWidget;
   import net.wg.portal.infrastructure.base.meta.IPortalInterceptionWidgetMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalInterceptionWidgetMeta;
   
   public class InterceptionWidget extends PortalInterceptionWidgetMeta implements IPortalInterceptionWidgetMeta
   {
      
      private static const ABILITY_DURATION_WIDGET_PADDING_BOTTOM:int = 276;
      
      private static const ICON_PADDING_BOTTOM:int = 8;
       
      
      public var icon:Sprite = null;
      
      public var durationWidget:AbilityDurationWidget = null;
      
      public function InterceptionWidget()
      {
         super();
         this.durationWidget.timerPrefix = PORTAL_EVENT.TIMER_LABEL_INTERCEPTIONWIDGET;
      }
      
      override protected function onDispose() : void
      {
         this.icon = null;
         this.durationWidget.dispose();
         this.durationWidget = null;
         super.onDispose();
      }
      
      public function as_updateTime(param1:int) : void
      {
         this.durationWidget.startCountdown(param1);
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         var _loc3_:int = param2 >> 1;
         this.durationWidget.y = _loc3_ - ABILITY_DURATION_WIDGET_PADDING_BOTTOM;
         this.icon.y = this.durationWidget.y + (this.durationWidget.height - this.icon.height >> 1) + ICON_PADDING_BOTTOM | 0;
      }
   }
}
