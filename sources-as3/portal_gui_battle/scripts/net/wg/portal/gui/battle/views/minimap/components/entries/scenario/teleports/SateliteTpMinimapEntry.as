package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class SateliteTpMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function SateliteTpMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.SATELITE_TP_READY;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_BLUE;
      }
   }
}
