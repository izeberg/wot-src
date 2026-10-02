package net.wg.portal.gui.battle.views.campCapturePanel
{
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamCaptureProgressReset;
   
   public class CampCaptureProgressReset extends TeamCaptureProgressReset
   {
      
      private static const RESET_BITMAP_SRC:String = "ResetBaseLine_";
       
      
      public function CampCaptureProgressReset()
      {
         super();
      }
      
      override protected function getBitmapSrcPrefix() : String
      {
         return RESET_BITMAP_SRC;
      }
   }
}
