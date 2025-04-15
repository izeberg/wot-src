package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data
{
   import net.wg.data.constants.generated.GAME_MESSAGES_CONSTS;
   import net.wg.gui.battle.views.gameMessagesPanel.data.GameMessageVO;
   
   public class FrontlineGameMessageVO extends GameMessageVO
   {
       
      
      public function FrontlineGameMessageVO(param1:Object)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "FrontlineGameMessageVO " + messageType + " " + priority + " " + length;
      }
      
      override protected function convertMsgData() : void
      {
         switch(messageType)
         {
            case GAME_MESSAGES_CONSTS.OVERTIME:
               msgData = new OverTimeMessageVO(_cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.BASE_CAPTURED:
            case GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE:
               msgData = new SectorBaseMessageVO(_cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.BASE_CONTESTED:
            case GAME_MESSAGES_CONSTS.BASE_CONTESTED_POSITIVE:
               msgData = new SectorBaseContestedMessageVO(_cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.RANK_UP:
               msgData = new RankUpMessageVO(_cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED_POSITIVE:
            case GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED:
               msgData = new HeadquarterDestroyedMessageVO(_cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK_POSITIVE:
            case GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK:
               msgData = new HeadquarterAttackedMessageVO(_cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.GENERAL_RANK_REACHED:
               msgData = new FirstGeneralRankReachedMessageVO(_cachedMsgData);
         }
         if(msgData)
         {
            _cachedMsgData = null;
            return;
         }
         super.convertMsgData();
      }
   }
}
