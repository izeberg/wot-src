package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.CooldownTimeMarker;
   
   public class PerspectiveTpCooldownMarker extends CooldownTimeMarker
   {
       
      
      public function PerspectiveTpCooldownMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.PERSPECTIVE_TP_COOL_DOWN;
         super.initialize();
      }
   }
}
