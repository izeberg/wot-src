package net.wg.portal.gui.battle.views.staticMarkers.scenario
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarker;
   
   public class PlayersBaseMarker extends ScenarioMarker
   {
       
      
      public function PlayersBaseMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.PLAYER_BASE;
         marker.iconTypeColorblind = VEHICLEMARKERATLAS.PLAYER_BASE_COLORBLIND;
         marker.backIcon = VEHICLEMARKERATLAS.POI_BG_PROGRESS_BLUE;
         super.initialize();
      }
   }
}
