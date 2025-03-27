package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.frontlineInGameRank.data.FrontlineInGameRankVO;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class FrontlineInGameRankMeta extends BattleDisplayable
   {
       
      
      public var levelUpAnimationComplete:Function;
      
      private var _frontlineInGameRankVO:FrontlineInGameRankVO;
      
      public function FrontlineInGameRankMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._frontlineInGameRankVO)
         {
            this._frontlineInGameRankVO.dispose();
            this._frontlineInGameRankVO = null;
         }
         super.onDispose();
      }
      
      public function levelUpAnimationCompleteS() : void
      {
         App.utils.asserter.assertNotNull(this.levelUpAnimationComplete,"levelUpAnimationComplete" + Errors.CANT_NULL);
         this.levelUpAnimationComplete();
      }
      
      public final function as_setRank(param1:Object) : void
      {
         var _loc2_:FrontlineInGameRankVO = this._frontlineInGameRankVO;
         this._frontlineInGameRankVO = new FrontlineInGameRankVO(param1);
         this.setRank(this._frontlineInGameRankVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setRank(param1:FrontlineInGameRankVO) : void
      {
         var _loc2_:String = "as_setRank" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
