package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps
{
   public class WhiteTigerBotHealthBarRight extends WhiteTigerBotHealthBar
   {
       
      
      public function WhiteTigerBotHealthBarRight()
      {
         super();
      }
      
      override public function showHp(param1:Number) : void
      {
         super.showHp(param1);
         var _loc2_:Number = getHpMaskX();
         fxMask.x = Math.min(prevMaskX,_loc2_);
      }
   }
}
