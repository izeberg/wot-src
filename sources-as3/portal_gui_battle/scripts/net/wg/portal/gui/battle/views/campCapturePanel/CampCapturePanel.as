package net.wg.portal.gui.battle.views.campCapturePanel
{
   import net.wg.portal.data.constants.PortalLinkages;
   
   public class CampCapturePanel extends CaptureBarsPanel
   {
       
      
      public function CampCapturePanel()
      {
         super();
      }
      
      override protected function getBarLinkage() : String
      {
         return PortalLinkages.PORTAL_CAMP_CAPTURE_BAR;
      }
   }
}
