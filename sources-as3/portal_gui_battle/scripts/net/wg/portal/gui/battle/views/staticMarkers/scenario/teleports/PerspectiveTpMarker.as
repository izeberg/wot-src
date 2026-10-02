package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarker;
   
   public class PerspectiveTpMarker extends ScenarioMarker
   {
       
      
      public function PerspectiveTpMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.PERSPECTIVE_TP_USED;
         marker.backIcon = VEHICLEMARKERATLAS.POI_BG_PROGRESS_BLUE;
         super.initialize();
      }
   }
}
