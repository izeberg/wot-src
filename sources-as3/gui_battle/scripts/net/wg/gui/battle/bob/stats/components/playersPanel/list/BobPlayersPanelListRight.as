package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   public class BobPlayersPanelListRight extends BobPlayersPanelList
   {
      
      private static const LINKAGE:String = "BobPlayersPanelListItemRightUI";
       
      
      public function BobPlayersPanelListRight()
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
         return "[WG BobPlayersPanelListRight]";
      }
   }
}
