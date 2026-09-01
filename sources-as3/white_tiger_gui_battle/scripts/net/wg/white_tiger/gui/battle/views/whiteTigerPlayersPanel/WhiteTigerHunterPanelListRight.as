package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel
{
   public class WhiteTigerHunterPanelListRight extends WhiteTigerHunterPanelList
   {
      
      private static const LINKAGE:String = "WhiteTigerHunterPanelListItemRightUI";
       
      
      public function WhiteTigerHunterPanelListRight()
      {
         super();
      }
      
      override protected function get itemLinkage() : String
      {
         return LINKAGE;
      }
      
      override protected function get isRightAligned() : Boolean
      {
         return true;
      }
      
      override public function toString() : String
      {
         return "[WG WhiteTigerHunterPanelListRight]";
      }
   }
}
