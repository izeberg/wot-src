package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.frontlineOverviewMapScreen.data.FrontlineOverviewMapScreenVO;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class FrontlineOverviewMapScreenMeta extends BattleDisplayable
   {
       
      
      private var _frontlineOverviewMapScreenVO:FrontlineOverviewMapScreenVO;
      
      public function FrontlineOverviewMapScreenMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._frontlineOverviewMapScreenVO)
         {
            this._frontlineOverviewMapScreenVO.dispose();
            this._frontlineOverviewMapScreenVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setKeyBindings(param1:Object) : void
      {
         var _loc2_:FrontlineOverviewMapScreenVO = this._frontlineOverviewMapScreenVO;
         this._frontlineOverviewMapScreenVO = new FrontlineOverviewMapScreenVO(param1);
         this.setKeyBindings(this._frontlineOverviewMapScreenVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setKeyBindings(param1:FrontlineOverviewMapScreenVO) : void
      {
         var _loc2_:String = "as_setKeyBindings" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
