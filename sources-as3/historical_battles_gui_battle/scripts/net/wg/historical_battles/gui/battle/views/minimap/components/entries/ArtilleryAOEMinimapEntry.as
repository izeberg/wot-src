package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.constants.ConsumablesMinimapEntryConst;
   
   public class ArtilleryAOEMinimapEntry extends HbMinimapEntry
   {
       
      
      public function ArtilleryAOEMinimapEntry()
      {
         super();
      }
      
      override protected function get atlasItemName() : String
      {
         return ConsumablesMinimapEntryConst.HB_AOE_ARTILLERY_ENTRY_ENEMY;
      }
   }
}
