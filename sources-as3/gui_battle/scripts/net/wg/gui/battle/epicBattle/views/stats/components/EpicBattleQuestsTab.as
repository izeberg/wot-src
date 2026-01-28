package net.wg.gui.battle.epicBattle.views.stats.components
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class EpicBattleQuestsTab extends GFInjectComponent implements IDisplayableComponent
   {
       
      
      public function EpicBattleQuestsTab()
      {
         super();
         setManageSize(true);
      }
      
      public function isCompVisible() : Boolean
      {
         return true;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
      }
   }
}
