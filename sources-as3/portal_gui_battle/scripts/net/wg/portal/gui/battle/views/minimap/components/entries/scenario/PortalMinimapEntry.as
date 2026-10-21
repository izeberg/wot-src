package net.wg.portal.gui.battle.views.minimap.components.entries.scenario
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.SimpleMinimapEntry;
   
   public class PortalMinimapEntry extends SimpleMinimapEntry
   {
      
      private static const MARKER_OFFSET_X:uint = 6;
      
      private static const MARKER_OFFSET_Y:uint = 5;
       
      
      public function PortalMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.PORTAL;
         marker.scaleX = marker.scaleY = 0.5;
         marker.x = MARKER_OFFSET_X;
         marker.y = MARKER_OFFSET_Y;
      }
   }
}
