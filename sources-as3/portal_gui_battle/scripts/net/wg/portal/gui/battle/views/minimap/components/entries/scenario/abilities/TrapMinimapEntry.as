package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.abilities
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core.SimpleMinimapEntry;
   
   public class TrapMinimapEntry extends SimpleMinimapEntry
   {
       
      
      public function TrapMinimapEntry()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         marker.iconType = BATTLEATLAS.TRAP;
      }
   }
}
