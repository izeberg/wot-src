package net.wg.gui.battle.comp7.stats.components.playersPanel.interfaces
{
   import net.wg.gui.battle.components.stats.playersPanel.interfaces.IPlayersPanelListItem;
   
   public interface IComp7PlayersPanelListItem extends IPlayersPanelListItem
   {
       
      
      function removePointOfInterest(param1:uint) : void;
      
      function updatePointOfInterest(param1:uint, param2:Number) : void;
      
      function setRank(param1:String, param2:String, param3:Boolean) : void;
      
      function setSquad(param1:Boolean, param2:int) : void;
      
      function setVoiceChatConnected(param1:Boolean) : void;
      
      function set isSuperSquad(param1:Boolean) : void;
   }
}
