package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.abilities
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.SimpleMinimapEntry;
   
   public class MinefieldMinimapEntry extends SimpleMinimapEntry
   {
       
      
      public function MinefieldMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.MINEFIELD;
      }
   }
}
