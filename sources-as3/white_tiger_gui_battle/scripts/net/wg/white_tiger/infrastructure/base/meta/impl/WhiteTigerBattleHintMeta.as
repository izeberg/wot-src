package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.white_tiger.gui.battle.VO.WhiteTigerBattleHintVO;
   
   public class WhiteTigerBattleHintMeta extends BattleDisplayable
   {
       
      
      public var onFadeOutFinished:Function;
      
      private var _whiteTigerBattleHintVO:WhiteTigerBattleHintVO;
      
      public function WhiteTigerBattleHintMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._whiteTigerBattleHintVO)
         {
            this._whiteTigerBattleHintVO.dispose();
            this._whiteTigerBattleHintVO = null;
         }
         super.onDispose();
      }
      
      public function onFadeOutFinishedS() : void
      {
         App.utils.asserter.assertNotNull(this.onFadeOutFinished,"onFadeOutFinished" + Errors.CANT_NULL);
         this.onFadeOutFinished();
      }
      
      public final function as_showHint(param1:Object) : void
      {
         var _loc2_:WhiteTigerBattleHintVO = this._whiteTigerBattleHintVO;
         this._whiteTigerBattleHintVO = new WhiteTigerBattleHintVO(param1);
         this.showHint(this._whiteTigerBattleHintVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function showHint(param1:WhiteTigerBattleHintVO) : void
      {
         var _loc2_:String = "as_showHint" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
