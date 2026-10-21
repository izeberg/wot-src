package net.wg.portal.gui.battle.components.battleDamagePanel
{
   import net.wg.gui.components.battleDamagePanel.BattleDamageLogPanel;
   
   public class BattleDamageLogPanel extends net.wg.gui.components.battleDamagePanel.BattleDamageLogPanel
   {
       
      
      public function BattleDamageLogPanel()
      {
         super();
      }
      
      override public function as_addDetailMessageTop(param1:String, param2:String, param3:String, param4:String, param5:String, param6:String) : void
      {
         damageLogDetailsBottomController.addDetailsMessage(param1,param2,param3,param4,param5,param6);
      }
   }
}
