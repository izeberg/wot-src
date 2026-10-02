package net.wg.portal.gui.battle.views.playersPanel.events
{
   import flash.events.Event;
   import net.wg.portal.gui.battle.views.playersPanel.VO.PlayerInfoVO;
   
   public class PlayerRendererEvent extends Event
   {
      
      public static const SWITCH_TO_PLAYER:String = "switchToPlayer";
      
      public static const SQUAD_ACCEPT_INVITE:String = "squadAcceptInvite";
      
      public static const SQUAD_SEND_INVITE:String = "squadSendInvite";
      
      public static const ITEM_LEFT_CLICK:String = "itemLeftClick";
      
      public static const ITEM_RIGHT_CLICK:String = "itemRightClick";
       
      
      public var data:PlayerInfoVO = null;
      
      public function PlayerRendererEvent(param1:String, param2:PlayerInfoVO, param3:Boolean = false, param4:Boolean = false)
      {
         this.data = param2;
         super(param1,param3,param4);
      }
   }
}
