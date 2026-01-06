package net.wg.gui.battle.epicBattle.views.components
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class EpicBattleQuests extends GFInjectComponent implements IDisplayableComponent
   {
       
      
      public function EpicBattleQuests()
      {
         super();
         setManageSize(true);
         setSize(250,177);
         name = "EpicBattleQuests";
      }
      
      public function isCompVisible() : Boolean
      {
         return false;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         visible = param1;
      }
   }
}
