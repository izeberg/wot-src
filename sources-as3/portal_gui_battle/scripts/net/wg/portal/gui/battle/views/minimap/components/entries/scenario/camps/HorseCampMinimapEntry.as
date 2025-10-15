package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.camps
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class HorseCampMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function HorseCampMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.HORSE_CAMP;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_RED;
      }
   }
}
