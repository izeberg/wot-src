package net.wg.historical_battles.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.historical_battles.gui.battle.views.phaseIndicator.data.HBPhaseIndicatorVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class HBPhaseIndicatorMeta extends BattleDisplayable
   {
       
      
      private var _hBPhaseIndicatorVO:HBPhaseIndicatorVO;
      
      public function HBPhaseIndicatorMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._hBPhaseIndicatorVO)
         {
            this._hBPhaseIndicatorVO.dispose();
            this._hBPhaseIndicatorVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:HBPhaseIndicatorVO = this._hBPhaseIndicatorVO;
         this._hBPhaseIndicatorVO = new HBPhaseIndicatorVO(param1);
         this.setData(this._hBPhaseIndicatorVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:HBPhaseIndicatorVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
