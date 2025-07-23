package net.wg.gui.battle.ranked.stats.components.playersPanel.interfaces
{
   import net.wg.gui.battle.components.stats.playersPanel.interfaces.IPlayersPanelListItem;
   
   public interface IRankedPlayersPanelListItem extends IPlayersPanelListItem
   {
       
      
      function setRankIcon(param1:int, param2:int, param3:Boolean) : void;
      
      function setSquad(param1:Boolean, param2:int) : void;
      
      function setVoiceChatConnected(param1:Boolean) : void;
   }
}
