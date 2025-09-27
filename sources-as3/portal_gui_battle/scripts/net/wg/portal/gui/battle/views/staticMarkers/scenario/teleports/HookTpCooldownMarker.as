package net.wg.portal.gui.battle.views.staticMarkers.scenario.teleports
{
   import net.wg.data.constants.generated.VEHICLEMARKERATLAS;
   import net.wg.portal.gui.battle.views.staticMarkers.scenario.core.CooldownTimeMarker;
   
   public class HookTpCooldownMarker extends CooldownTimeMarker
   {
       
      
      public function HookTpCooldownMarker()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = VEHICLEMARKERATLAS.HOOK_TP_COOL_DOWN;
         super.initialize();
      }
   }
}
