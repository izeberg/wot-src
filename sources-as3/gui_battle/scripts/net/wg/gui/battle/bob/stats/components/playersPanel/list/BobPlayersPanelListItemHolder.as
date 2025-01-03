package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   import net.wg.gui.battle.bob.data.BobDAAPIVehicleInfoVO;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.list.PlayersPanelListItem;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.list.PlayersPanelListItemHolder;
   
   public class BobPlayersPanelListItemHolder extends PlayersPanelListItemHolder
   {
       
      
      private var bobListItem:BobPlayersPanelListItem = null;
      
      public function BobPlayersPanelListItemHolder(param1:PlayersPanelListItem)
      {
         this.bobListItem = BobPlayersPanelListItem(param1);
         super(param1);
      }
      
      override protected function onDispose() : void
      {
         this.bobListItem = null;
         super.onDispose();
      }
      
      override protected function updateListItemVehicleDataValues() : void
      {
         var _loc1_:BobDAAPIVehicleInfoVO = BobDAAPIVehicleInfoVO(vehicleData);
         this.bobListItem.setBloggerInfo(_loc1_.bloggerID,_loc1_.isBlogger);
         super.updateListItemVehicleDataValues();
      }
   }
}
