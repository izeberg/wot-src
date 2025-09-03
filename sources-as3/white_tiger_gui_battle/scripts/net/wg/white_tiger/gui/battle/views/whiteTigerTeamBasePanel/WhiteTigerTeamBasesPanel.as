package net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel
{
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamCaptureBar;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerTeamBasesPanelMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WhiteTigerTeamBasesPanelMeta;
   
   public class WhiteTigerTeamBasesPanel extends WhiteTigerTeamBasesPanelMeta implements IWhiteTigerTeamBasesPanelMeta
   {
      
      private static const LINKAGE_NAME:String = "WhiteTigerTeamCaptureBarUI";
       
      
      public function WhiteTigerTeamBasesPanel()
      {
         super();
      }
      
      override protected function getBarLinkage() : String
      {
         return LINKAGE_NAME;
      }
      
      public function as_updateCapture(param1:Number, param2:Number, param3:Number, param4:String, param5:String, param6:String, param7:String, param8:Boolean) : void
      {
         var _loc10_:WhiteTigerTeamCaptureBar = null;
         as_updateCaptureData(param1,param2,param3,param4,param5,param6,param7);
         var _loc9_:TeamCaptureBar = getCaptureBarById(param1);
         if(_loc9_ is WhiteTigerTeamCaptureBar)
         {
            _loc10_ = _loc9_ as WhiteTigerTeamCaptureBar;
            _loc10_.lockGenerator(param8);
         }
      }
   }
}
