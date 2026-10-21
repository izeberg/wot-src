package net.wg.portal.gui.battle.views.staticMarkers.scenario.camps
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarker;
   
   public class PerspectiveCampMarker extends ScenarioMarker
   {
       
      
      public function PerspectiveCampMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.PERSPECTIVE_CAMP;
         marker.backIcon = VEHICLEMARKERATLAS.POI_BG_PROGRESS_RED;
         super.initialize();
      }
   }
}
