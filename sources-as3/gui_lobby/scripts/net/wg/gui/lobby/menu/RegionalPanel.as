package net.wg.gui.lobby.menu
{
   import flash.utils.Dictionary;
   import scaleform.clik.core.UIComponent;
   
   public class RegionalPanel extends UIComponent
   {
      
      private static const LANGUAGE_KO:String = "ko";
      
      private static const REGION_DEFAULT:String = "default";
       
      
      private const regionCheckers:Dictionary = new Dictionary();
      
      public function RegionalPanel()
      {
         super();
         this.regionCheckers[LANGUAGE_KO] = checkIsKorean;
      }
      
      private static function checkIsKorean() : Boolean
      {
         var _loc1_:String = App.utils.locale.makeString(SETTINGS.LANGUAGE_CODE);
         return (App.globalVarsMgr.isDevelopmentS() || App.globalVarsMgr.isAsiaS()) && _loc1_ === LANGUAGE_KO;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         gotoAndStop(this.getCurrentRegion());
      }
      
      private function getCurrentRegion() : String
      {
         var _loc2_:* = null;
         var _loc1_:String = REGION_DEFAULT;
         for(_loc2_ in this.regionCheckers)
         {
            if(this.regionCheckers[_loc2_]())
            {
               _loc1_ = _loc2_;
               break;
            }
         }
         return _loc1_;
      }
   }
}
