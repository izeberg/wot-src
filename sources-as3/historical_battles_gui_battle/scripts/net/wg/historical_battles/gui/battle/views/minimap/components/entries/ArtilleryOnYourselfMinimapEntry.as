package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.constants.ConsumablesMinimapEntryConst;
   
   public class ArtilleryOnYourselfMinimapEntry extends HbMinimapEntry
   {
       
      
      public function ArtilleryOnYourselfMinimapEntry()
      {
         super();
      }
      
      override protected function get atlasItemName() : String
      {
         return ConsumablesMinimapEntryConst.HB_ARTILLERY_ON_YOURSELF_ATLAS_ITEM_NAME;
      }
   }
}
