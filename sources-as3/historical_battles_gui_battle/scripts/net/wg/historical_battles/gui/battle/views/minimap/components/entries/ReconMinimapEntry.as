package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.constants.ConsumablesMinimapEntryConst;
   
   public class ReconMinimapEntry extends HbMinimapEntry
   {
       
      
      public function ReconMinimapEntry()
      {
         super();
      }
      
      override protected function get atlasItemName() : String
      {
         return ConsumablesMinimapEntryConst.HB_RECON_ATLAS_ITEM_NAME;
      }
   }
}
