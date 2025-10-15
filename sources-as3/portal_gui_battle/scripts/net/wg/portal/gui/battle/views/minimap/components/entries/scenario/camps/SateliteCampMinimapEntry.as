package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.camps
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class SateliteCampMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function SateliteCampMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.SATELITE_CAMP;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_RED;
      }
   }
}
