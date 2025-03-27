package net.wg.gui.battle.pveBase.views.minimap.entries
{
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class PveBitmapEntry extends BattleUIComponent
   {
       
      
      public function PveBitmapEntry()
      {
         super();
      }
      
      public function setIcon(param1:String) : void
      {
         App.atlasMgr.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,param1,graphics,Values.EMPTY_STR,true,false,true);
      }
   }
}
