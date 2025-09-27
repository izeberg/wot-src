package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.SimpleMarker;
   
   public class HookTpReadyMarker extends SimpleMarker
   {
       
      
      public function HookTpReadyMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.HOOK_TP_READY;
         super.initialize();
      }
   }
}
