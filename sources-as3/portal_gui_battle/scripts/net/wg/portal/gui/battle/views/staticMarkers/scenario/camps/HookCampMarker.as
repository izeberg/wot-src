package net.wg.portal.gui.battle.views.staticMarkers.scenario.camps
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.ScenarioMarker;
   
   public class HookCampMarker extends ScenarioMarker
   {
       
      
      public function HookCampMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.HOOK_CAMP;
         marker.backIcon = VEHICLEMARKERATLAS.POI_BG_PROGRESS_RED;
         super.initialize();
      }
   }
}
