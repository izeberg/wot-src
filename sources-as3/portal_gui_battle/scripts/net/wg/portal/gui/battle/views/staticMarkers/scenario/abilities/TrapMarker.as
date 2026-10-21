package net.wg.portal.gui.battle.views.staticMarkers.scenario.abilities
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.SimpleMarker;
   
   public class TrapMarker extends SimpleMarker
   {
       
      
      public function TrapMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.TRAP;
         super.initialize();
      }
   }
}
