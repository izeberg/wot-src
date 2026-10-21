package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarker;
   
   public class HookTpCooldownMarker extends ScenarioMarker
   {
       
      
      public function HookTpCooldownMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.HOOK_TP_COOL_DOWN;
         marker.backIcon = VEHICLEMARKERATLAS.POI_BG_GREY;
         super.initialize();
      }
   }
}
