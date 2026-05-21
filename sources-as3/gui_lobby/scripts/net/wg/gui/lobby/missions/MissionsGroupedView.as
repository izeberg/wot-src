package net.wg.gui.lobby.missions
{
   import net.wg.gui.lobby.eventBoards.events.MissionPremiumEvent;
   import net.wg.gui.lobby.missions.event.MissionHeaderEvent;
   import net.wg.infrastructure.base.meta.IMissionsGroupedViewMeta;
   import net.wg.infrastructure.base.meta.impl.MissionsGroupedViewMeta;
   
   public class MissionsGroupedView extends MissionsGroupedViewMeta implements IMissionsGroupedViewMeta
   {
       
      
      public function MissionsGroupedView()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(MissionHeaderEvent.COLLAPSE,this.onCollapseHandler);
         addEventListener(MissionHeaderEvent.MOVE_TO_ACTION,this.onMoveToActionHandler);
         addEventListener(MissionPremiumEvent.BUTTON_DETAILS_CLICK,this.onButtonDetailsClickHandler);
         addEventListener(MissionHeaderEvent.OPEN_INFO_PAGE,this.onOpenInfoPageEventHandler);
         addEventListener(MissionHeaderEvent.OPEN_SHOP_PAGE,this.onOpenShopPageEventHandler);
         addEventListener(MissionHeaderEvent.OPEN_EVENT_PAGE,this.onOpenEventPageEventHandler);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MissionHeaderEvent.MOVE_TO_ACTION,this.onMoveToActionHandler);
         removeEventListener(MissionHeaderEvent.COLLAPSE,this.onCollapseHandler);
         removeEventListener(MissionPremiumEvent.BUTTON_DETAILS_CLICK,this.onButtonDetailsClickHandler);
         removeEventListener(MissionHeaderEvent.OPEN_INFO_PAGE,this.onOpenInfoPageEventHandler);
         removeEventListener(MissionHeaderEvent.OPEN_SHOP_PAGE,this.onOpenShopPageEventHandler);
         removeEventListener(MissionHeaderEvent.OPEN_EVENT_PAGE,this.onOpenEventPageEventHandler);
         super.onDispose();
      }
      
      private function onMoveToActionHandler(param1:MissionHeaderEvent) : void
      {
         clickActionBtnS(param1.actionId);
      }
      
      private function onCollapseHandler(param1:MissionHeaderEvent) : void
      {
         expandS(param1.missionId,!param1.isCollapsed);
      }
      
      private function onButtonDetailsClickHandler(param1:MissionPremiumEvent) : void
      {
         onClickButtonDetailsS();
      }
      
      private function onOpenInfoPageEventHandler(param1:MissionHeaderEvent) : void
      {
         onClickInfoBtnS(param1.actionId);
      }
      
      private function onOpenShopPageEventHandler(param1:MissionHeaderEvent) : void
      {
         onClickOpenShopBtnS(param1.actionId);
      }
      
      private function onOpenEventPageEventHandler(param1:MissionHeaderEvent) : void
      {
         onClickOpenEventBtnS(param1.actionId);
      }
   }
}
