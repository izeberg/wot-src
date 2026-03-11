package net.wg.story_mode.battle.views.gameMessagesPanel
{
   import flash.utils.Dictionary;
   import net.wg.data.constants.generated.GAME_MESSAGES_CONSTS;
   import net.wg.gui.battle.views.gameMessagesPanel.GameMessagesPanel;
   import net.wg.gui.battle.views.gameMessagesPanel.components.EndGameMessage;
   
   public class StoryModeGameMessagesPanel extends GameMessagesPanel
   {
      
      public static const WIN_UI_LINKAGE:String = "msgStoryModeVictoryUI";
      
      public static const DRAW_UI_LINKAGE:String = "msgStoryModeDrawUI";
       
      
      public function StoryModeGameMessagesPanel()
      {
         super();
      }
      
      override protected function initMappingDict() : void
      {
         msgLinkageTypeDict = new Dictionary();
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.WIN] = WIN_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.DRAW] = DRAW_UI_LINKAGE;
         msgClassTypeDict = new Dictionary();
         msgClassTypeDict[GAME_MESSAGES_CONSTS.WIN] = EndGameMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.DRAW] = EndGameMessage;
      }
   }
}
