package net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel
{
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamCaptureProgressReset;
   
   public class WhiteTigerTeamCaptureProgressReset extends TeamCaptureProgressReset
   {
      
      private static const RESET_BITMAP_SRC:String = "ResetBaseLine_";
       
      
      public function WhiteTigerTeamCaptureProgressReset()
      {
         super();
      }
      
      override protected function getBitmapSrcPrefix() : String
      {
         return RESET_BITMAP_SRC;
      }
   }
}
