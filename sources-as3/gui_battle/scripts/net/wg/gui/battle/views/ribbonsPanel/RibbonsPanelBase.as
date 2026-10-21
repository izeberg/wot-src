package net.wg.gui.battle.views.ribbonsPanel
{
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.BattleDisplayable;
   
   public class RibbonsPanelBase extends BattleDisplayable
   {
       
      
      public function RibbonsPanelBase()
      {
         super();
      }
      
      public function setFreeWorkingHeight(param1:int) : void
      {
      }
      
      public function setSettings(param1:Boolean, param2:Boolean, param3:Boolean, param4:Boolean) : void
      {
      }
      
      public function shiftItems() : void
      {
      }
      
      public function get freeHeightForRenderers() : int
      {
         return RibbonCtrl.ITEM_HEIGHT;
      }
      
      public function get offsetX() : int
      {
         return Values.ZERO;
      }
   }
}
