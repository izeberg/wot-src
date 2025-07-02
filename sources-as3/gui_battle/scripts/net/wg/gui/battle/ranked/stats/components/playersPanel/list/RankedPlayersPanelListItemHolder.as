package net.wg.gui.battle.ranked.stats.components.playersPanel.list
{
   import net.wg.gui.battle.components.stats.playersPanel.list.BasePlayersListItemHolder;
   import net.wg.gui.battle.ranked.VO.daapi.RankedDAAPIVehicleInfoVO;
   import net.wg.gui.battle.ranked.stats.components.playersPanel.interfaces.IRankedPlayersPanelListItem;
   
   public class RankedPlayersPanelListItemHolder extends BasePlayersListItemHolder
   {
       
      
      private var _rankedListItem:IRankedPlayersPanelListItem = null;
      
      public function RankedPlayersPanelListItemHolder(param1:RankedPlayersPanelListItem)
      {
         this._rankedListItem = IRankedPlayersPanelListItem(param1);
         super(param1);
      }
      
      override protected function onDispose() : void
      {
         this._rankedListItem = null;
         super.onDispose();
      }
      
      override protected function updateListItemVehicleDataValues() : void
      {
         var _loc1_:RankedDAAPIVehicleInfoVO = RankedDAAPIVehicleInfoVO(vehicleData);
         this._rankedListItem.setRankIcon(_loc1_.division,_loc1_.level,_loc1_.isGroup);
         this._rankedListItem.setVoiceChatConnected(_loc1_.voiceChatConnected);
      }
      
      override protected function applyPlayerStatusValues() : void
      {
         this._rankedListItem.setSquad(vehicleData.isSquadPersonal(),vehicleData.squadIndex);
      }
   }
}
