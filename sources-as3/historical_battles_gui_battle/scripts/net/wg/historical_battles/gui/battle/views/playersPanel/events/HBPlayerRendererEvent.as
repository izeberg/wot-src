package net.wg.historical_battles.gui.battle.views.playersPanel.events
{
   import flash.events.Event;
   import net.wg.historical_battles.gui.battle.views.playersPanel.VO.HBPlayerInfoVO;
   
   public class HBPlayerRendererEvent extends Event
   {
      
      public static const SWITCH_TO_PLAYER:String = "switchToPlayer";
      
      public static const SQUAD_ACCEPT_INVITE:String = "squadAcceptInvite";
      
      public static const SQUAD_SEND_INVITE:String = "squadSendInvite";
      
      public static const ITEM_LEFT_CLICK:String = "itemLeftClick";
      
      public static const ITEM_RIGHT_CLICK:String = "itemRightClick";
       
      
      public var data:HBPlayerInfoVO = null;
      
      public function HBPlayerRendererEvent(param1:String, param2:HBPlayerInfoVO, param3:Boolean = false, param4:Boolean = false)
      {
         this.data = param2;
         super(param1,param3,param4);
      }
   }
}
