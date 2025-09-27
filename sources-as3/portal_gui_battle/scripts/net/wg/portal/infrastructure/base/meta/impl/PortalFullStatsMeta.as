package net.wg.portal.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.portal.data.VO.fullStats.PortalFullStatsVO;
   
   public class PortalFullStatsMeta extends BattleDisplayable
   {
       
      
      private var _portalFullStatsVO:PortalFullStatsVO;
      
      public function PortalFullStatsMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._portalFullStatsVO)
         {
            this._portalFullStatsVO.dispose();
            this._portalFullStatsVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:PortalFullStatsVO = this._portalFullStatsVO;
         this._portalFullStatsVO = new PortalFullStatsVO(param1);
         this.setData(this._portalFullStatsVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:PortalFullStatsVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
