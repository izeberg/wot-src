package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.CooldownTimeMarker;
   
   public class HorseTpCooldownMarker extends CooldownTimeMarker
   {
       
      
      public function HorseTpCooldownMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.HORSE_TP_COOL_DOWN;
         super.initialize();
      }
   }
}
