package net.wg.historical_battles.gui.battle.views.gameMessagesPanel
{
   import net.wg.data.constants.generated.GAME_MESSAGES_CONSTS;
   import net.wg.data.constants.generated.HB_GAME_MESSAGES_CONSTS;
   import net.wg.gui.battle.views.gameMessagesPanel.GameMessagesPanel;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.HBEndGameMessage;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.HBEndGameMessageVictory;
   import net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components.ObjectiveGameMessage;
   
   public class HBGameMessagesPanel extends GameMessagesPanel
   {
       
      
      public function HBGameMessagesPanel()
      {
         super();
      }
      
      override protected function initMappingDict() : void
      {
         super.initMappingDict();
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED] = HB_GAME_MESSAGES_CONSTS.BASE_CAPTURED_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE] = HB_GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE_LINKAGE;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED] = ObjectiveGameMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE] = ObjectiveGameMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.WIN] = HBEndGameMessageVictory;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.DEFEAT] = HBEndGameMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.DRAW] = HBEndGameMessage;
      }
   }
}
