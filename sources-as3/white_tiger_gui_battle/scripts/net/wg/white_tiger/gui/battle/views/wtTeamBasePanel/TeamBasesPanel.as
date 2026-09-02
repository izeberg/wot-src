package net.wg.white_tiger.gui.battle.views.wtTeamBasePanel
{
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamBasesPanel;
   import net.wg.white_tiger.data.constants.WT_LINKAGES;
   
   public class TeamBasesPanel extends net.wg.gui.battle.random.views.teamBasesPanel.TeamBasesPanel
   {
       
      
      public function TeamBasesPanel()
      {
         super();
      }
      
      override protected function getBarLinkage() : String
      {
         return WT_LINKAGES.WT_CAPTURE_BAR_LINKAGE;
      }
   }
}
