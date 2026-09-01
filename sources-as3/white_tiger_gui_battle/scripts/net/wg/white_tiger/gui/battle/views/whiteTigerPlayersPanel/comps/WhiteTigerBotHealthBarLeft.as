package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps
{
   public class WhiteTigerBotHealthBarLeft extends WhiteTigerBotHealthBar
   {
       
      
      public function WhiteTigerBotHealthBarLeft()
      {
         super();
      }
      
      override public function showHp(param1:Number) : void
      {
         super.showHp(param1);
         var _loc2_:Number = getHpMaskWidth();
         fxMask.x = Math.min(prevMaskWidth,_loc2_);
      }
   }
}
