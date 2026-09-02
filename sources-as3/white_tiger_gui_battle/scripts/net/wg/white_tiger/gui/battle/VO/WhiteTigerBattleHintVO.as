package net.wg.white_tiger.gui.battle.VO
{
   import net.wg.gui.battle.views.battleHint.vo.BattleHintVO;
   
   public class WhiteTigerBattleHintVO extends BattleHintVO
   {
       
      
      public var timer:int = 0;
      
      public function WhiteTigerBattleHintVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDispose() : void
      {
         super.onDispose();
      }
   }
}
