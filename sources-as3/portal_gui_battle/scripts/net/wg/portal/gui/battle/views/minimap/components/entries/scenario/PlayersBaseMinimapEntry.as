package net.wg.portal.gui.battle.views.minimap.components.entries.scenario
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.ScenarioMinimapEntry;
   
   public class PlayersBaseMinimapEntry extends ScenarioMinimapEntry
   {
       
      
      public function PlayersBaseMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.PLAYER_BASE;
         marker.iconTypeColorblind = BATTLEATLAS.PLAYER_BASE_COLORBLIND;
         marker.backIcon = BATTLEATLAS.POI_CAMP_BG_BLUE;
      }
   }
}
