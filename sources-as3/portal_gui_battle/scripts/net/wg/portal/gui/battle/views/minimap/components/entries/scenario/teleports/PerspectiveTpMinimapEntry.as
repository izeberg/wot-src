package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class PerspectiveTpMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function PerspectiveTpMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.PERSPECTIVE_TP_READY;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_BLUE;
      }
   }
}
