package net.wg.gui.battle.ranked.stats.components.playersPanel.interfaces
{
   import net.wg.gui.battle.random.views.stats.components.playersPanel.interfaces.IPlayersPanelList;
   import net.wg.gui.battle.ranked.stats.components.data.VoiceChatActivationVO;
   
   public interface IRankedPlayersPanelListLeft extends IPlayersPanelList
   {
       
      
      function setVoiceChatVisibility(param1:Boolean) : void;
      
      function setVoiceChatData(param1:VoiceChatActivationVO) : void;
      
      function setVoiceChatControlActive(param1:Boolean) : void;
   }
}
