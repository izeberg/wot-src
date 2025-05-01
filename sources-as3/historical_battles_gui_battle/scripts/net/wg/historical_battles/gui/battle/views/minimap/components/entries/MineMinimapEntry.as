package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.constants.ConsumablesMinimapEntryConst;
   
   public class MineMinimapEntry extends HbMinimapEntry
   {
       
      
      public function MineMinimapEntry()
      {
         super();
      }
      
      override protected function get atlasItemName() : String
      {
         return ConsumablesMinimapEntryConst.HB_MINE_ATLAS_ITEM_NAME;
      }
   }
}
