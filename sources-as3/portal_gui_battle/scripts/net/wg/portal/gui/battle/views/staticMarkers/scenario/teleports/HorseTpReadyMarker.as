package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.SimpleMarker;
   
   public class HorseTpReadyMarker extends SimpleMarker
   {
       
      
      public function HorseTpReadyMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.HORSE_TP_READY;
         super.initialize();
      }
   }
}
