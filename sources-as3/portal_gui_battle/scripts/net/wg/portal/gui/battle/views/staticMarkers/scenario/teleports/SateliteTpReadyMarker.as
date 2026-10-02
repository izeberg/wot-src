package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.SimpleMarker;
   
   public class SateliteTpReadyMarker extends SimpleMarker
   {
       
      
      public function SateliteTpReadyMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.SATELITE_TP_READY;
         marker.backIcon = VEHICLEMARKERATLAS.POI_BG_PROGRESS_BLUE;
         super.initialize();
      }
   }
}
