package net.wg.portal.gui.battle.views.staticMarkers.scenario
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.SimpleMarker;
   
   public class PortalMarker extends SimpleMarker
   {
       
      
      public function PortalMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.PORTAL;
         super.initialize();
      }
   }
}
