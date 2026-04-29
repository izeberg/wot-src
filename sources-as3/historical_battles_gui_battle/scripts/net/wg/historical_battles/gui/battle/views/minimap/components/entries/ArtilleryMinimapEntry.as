package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.constants.ConsumablesMinimapEntryConst;
   
   public class ArtilleryMinimapEntry extends HbMinimapEntry
   {
       
      
      public function ArtilleryMinimapEntry()
      {
         super();
      }
      
      override protected function get atlasItemName() : String
      {
         return ConsumablesMinimapEntryConst.HB_ARTILLERY_ATLAS_ITEM_NAME;
      }
   }
}
