package net.wg.portal.gui.battle.views.minimap.components.entries.scenario
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.SimpleMinimapEntry;
   
   public class PortalMinimapEntry extends SimpleMinimapEntry
   {
       
      
      public function PortalMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.PORTAL;
      }
   }
}
