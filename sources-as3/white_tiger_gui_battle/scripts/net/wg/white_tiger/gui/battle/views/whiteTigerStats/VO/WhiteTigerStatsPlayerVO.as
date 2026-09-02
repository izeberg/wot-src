package net.wg.white_tiger.gui.battle.views.whiteTigerStats.VO
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.components.controls.VO.BadgeVisualVO;
   
   public class WhiteTigerStatsPlayerVO extends DAAPIDataClass
   {
      
      private static const BADGE_FIELD:String = "badgeVO";
       
      
      public var badgeVO:BadgeVisualVO = null;
      
      public function WhiteTigerStatsPlayerVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == BADGE_FIELD)
         {
            this.badgeVO = new BadgeVisualVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         if(this.badgeVO)
         {
            this.badgeVO.dispose();
            this.badgeVO = null;
         }
         super.onDispose();
      }
   }
}
