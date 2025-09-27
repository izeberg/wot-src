package net.wg.portal.gui.battle.views.guidedMissileWidget
{
   import flash.display.Sprite;
   import net.wg.portal.gui.battle.components.AbilityDurationWidget;
   import net.wg.portal.gui.battle.components.PortalShortcutBtn;
   import net.wg.portal.infrastructure.base.meta.IPortalGuidedMissileWidgetMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalGuidedMissileWidgetMeta;
   
   public class GuidedMissileWidget extends PortalGuidedMissileWidgetMeta implements IPortalGuidedMissileWidgetMeta
   {
      
      private static const ABILITY_DURATION_WIDGET_PADDING_BOTTOM:int = 276;
      
      private static const ICON_PADDING_BOTTOM:int = 10;
       
      
      public var shortcutActivate:PortalShortcutBtn = null;
      
      public var shortcutAccelerate:PortalShortcutBtn = null;
      
      public var icon:Sprite = null;
      
      public var durationWidget:AbilityDurationWidget = null;
      
      public function GuidedMissileWidget()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.shortcutActivate.setNameAndDesc(PORTAL_EVENT.ACTIVATE_SHORTCUT,PORTAL_EVENT.ACTIVATE_DESCRIPTION);
         this.shortcutAccelerate.setNameAndDesc(PORTAL_EVENT.ACCELERATE_SHORTCUT,PORTAL_EVENT.ACCELERATE_DESCRIPTION);
         this.durationWidget.timerPrefix = PORTAL_EVENT.TIMER_LABEL_GUIDEDMISSILEWIDGET;
      }
      
      override protected function onDispose() : void
      {
         this.shortcutActivate.dispose();
         this.shortcutActivate = null;
         this.shortcutAccelerate.dispose();
         this.shortcutAccelerate = null;
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
         var _loc3_:Number = param2 >> 1;
         this.durationWidget.y = _loc3_ - ABILITY_DURATION_WIDGET_PADDING_BOTTOM;
         this.icon.y = this.durationWidget.y + (this.durationWidget.height - this.icon.height >> 1) + ICON_PADDING_BOTTOM | 0;
      }
   }
}
