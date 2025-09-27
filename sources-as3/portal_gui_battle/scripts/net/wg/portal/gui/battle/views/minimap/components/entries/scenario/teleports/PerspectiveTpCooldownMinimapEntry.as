package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class PerspectiveTpCooldownMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function PerspectiveTpCooldownMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.PERSPECTIVE_TP_COOL_DOWN;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_GREY;
      }
   }
}
