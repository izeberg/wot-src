package net.wg.portal.gui.battle.views.interceptionWidget
{
   import net.wg.portal.gui.battle.components.AbilityInfoWidget;
   import net.wg.portal.gui.battle.components.KeyShortcut;
   import net.wg.portal.infrastructure.base.meta.IPortalInterceptionWidgetMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalInterceptionWidgetMeta;
   import net.wg.utils.StageBreakPointList;
   
   public class InterceptionWidget extends PortalInterceptionWidgetMeta implements IPortalInterceptionWidgetMeta
   {
      
      private static const ABILITY_INFO_WIDGET_PADDING_BOTTOM:int = 30;
       
      
      public var infoWidget:AbilityInfoWidget = null;
      
      public function InterceptionWidget()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.infoWidget.addPrimaryActionShortcutKey(KeyShortcut.SPACE_KEY,PORTAL_EVENT.INTERCEPTION_DESCRIPTION);
      }
      
      override protected function onDispose() : void
      {
         this.infoWidget.dispose();
         this.infoWidget = null;
         super.onDispose();
      }
      
      public function as_updateTime(param1:int) : void
      {
         this.infoWidget.startCountdown(param1);
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = param2 >> 1;
         this.infoWidget.y = _loc3_ - this.infoWidget.height - ABILITY_INFO_WIDGET_PADDING_BOTTOM;
         if(App.stageSizeMgr.currentBreakPoint == StageBreakPointList.EXTRA_SMALL)
         {
            this.infoWidget.useExtraSmallLayout();
         }
         else
         {
            this.infoWidget.useMediumLayout();
         }
      }
   }
}
