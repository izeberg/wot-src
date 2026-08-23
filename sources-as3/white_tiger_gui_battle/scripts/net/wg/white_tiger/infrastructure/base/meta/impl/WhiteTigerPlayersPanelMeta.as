package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.PlayersPanelBase;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.white_tiger.gui.battle.VO.DAAPIWhiteTigerBossBotInfoVO;
   
   public class WhiteTigerPlayersPanelMeta extends PlayersPanelBase
   {
       
      
      private var _dAAPIWhiteTigerBossBotInfoVO:DAAPIWhiteTigerBossBotInfoVO;
      
      public function WhiteTigerPlayersPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._dAAPIWhiteTigerBossBotInfoVO)
         {
            this._dAAPIWhiteTigerBossBotInfoVO.dispose();
            this._dAAPIWhiteTigerBossBotInfoVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setBossBotInfo(param1:Object) : void
      {
         var _loc2_:DAAPIWhiteTigerBossBotInfoVO = this._dAAPIWhiteTigerBossBotInfoVO;
         this._dAAPIWhiteTigerBossBotInfoVO = new DAAPIWhiteTigerBossBotInfoVO(param1);
         this.setBossBotInfo(this._dAAPIWhiteTigerBossBotInfoVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setBossBotInfo(param1:DAAPIWhiteTigerBossBotInfoVO) : void
      {
         var _loc2_:String = "as_setBossBotInfo" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
