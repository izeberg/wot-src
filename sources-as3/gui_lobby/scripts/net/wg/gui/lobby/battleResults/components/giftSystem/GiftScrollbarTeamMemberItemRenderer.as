package net.wg.gui.lobby.battleResults.components.giftSystem
{
   import flash.events.MouseEvent;
   import net.wg.gui.lobby.battleResults.components.ScrollbarTeamMemberItemRenderer;
   import net.wg.gui.lobby.battleResults.data.GiftSystemVO;
   import net.wg.gui.lobby.battleResults.data.TeamMemberItemVO;
   
   public class GiftScrollbarTeamMemberItemRenderer extends ScrollbarTeamMemberItemRenderer implements IGiftTeamMemberItemRenderer
   {
      
      private static const PLAYER_NAME_WIDTH:int = 104;
       
      
      public var giftSendButtons:GiftSystemButtons = null;
      
      public function GiftScrollbarTeamMemberItemRenderer()
      {
         super();
         playerNameWidth = PLAYER_NAME_WIDTH;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         playerName.width = playerNameWidth;
         this.giftSendButtons.addEventListener(MouseEvent.CLICK,this.onGiftSendButtonsClickHandler);
      }
      
      override protected function onDispose() : void
      {
         this.giftSendButtons.removeEventListener(MouseEvent.CLICK,this.onGiftSendButtonsClickHandler);
         this.giftSendButtons.dispose();
         this.giftSendButtons = null;
         super.onDispose();
      }
      
      override protected function showData(param1:TeamMemberItemVO) : void
      {
         super.showData(param1);
         this.giftSendButtons.visible = !param1.isSelf;
         this.giftSendButtons.setTeamMemberData(param1);
      }
      
      private function onGiftSendButtonsClickHandler(param1:MouseEvent) : void
      {
         param1.stopPropagation();
      }
      
      public function setGiftSystemData(param1:GiftSystemVO) : void
      {
         this.giftSendButtons.setGiftSystemData(param1);
      }
   }
}
