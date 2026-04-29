package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import net.wg.historical_battles.gui.battle.views.minimap.components.entries.constants.ConsumablesMinimapEntryConst;
   
   public class HBKeyTargetMinimapEntry extends HbMinimapEntry
   {
       
      
      public function HBKeyTargetMinimapEntry()
      {
         super();
      }
      
      override protected function get atlasItemName() : String
      {
         return ConsumablesMinimapEntryConst.HB_CONTROL_POINT_BOSS_ITEM_NAME;
      }
   }
}
