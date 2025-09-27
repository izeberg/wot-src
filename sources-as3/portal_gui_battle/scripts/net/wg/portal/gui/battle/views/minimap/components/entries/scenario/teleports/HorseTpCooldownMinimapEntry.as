package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.teleports
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class HorseTpCooldownMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function HorseTpCooldownMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.HORSE_TP_COOL_DOWN;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_GREY;
      }
   }
}
