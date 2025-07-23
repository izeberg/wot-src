package net.wg.gui.battle.ranked.stats.components.playersPanel.list
{
   public class RankedPlayersPanelListRight extends RankedPlayersPanelList
   {
      
      private static const LINKAGE:String = "RankedPlayersPanelListItemRightUI";
       
      
      public function RankedPlayersPanelListRight()
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
         return "[PlayersPanelListRight]";
      }
   }
}
