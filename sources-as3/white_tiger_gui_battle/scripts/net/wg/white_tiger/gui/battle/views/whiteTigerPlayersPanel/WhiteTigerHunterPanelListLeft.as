package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel
{
   public class WhiteTigerHunterPanelListLeft extends WhiteTigerHunterPanelList
   {
      
      private static const LINKAGE:String = "WhiteTigerHunterPanelListItemLeftUI";
       
      
      public function WhiteTigerHunterPanelListLeft()
      {
         super();
      }
      
      override protected function get itemLinkage() : String
      {
         return LINKAGE;
      }
      
      override protected function get isRightAligned() : Boolean
      {
         return false;
      }
      
      override public function toString() : String
      {
         return "[WG WhiteTigerHunterPanelListLeft]";
      }
   }
}
