package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.VO.daapi.DAAPITriggeredCommandsVO;
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.gui.battle.eventBattle.views.eventPlayersPanel.VO.DAAPIPlayerPanelInfoVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class EventPlayersPanelMeta extends BattleDisplayable
   {
       
      
      private var _dAAPIPlayerPanelInfoVO:DAAPIPlayerPanelInfoVO;
      
      public function EventPlayersPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._dAAPIPlayerPanelInfoVO)
         {
            this._dAAPIPlayerPanelInfoVO.dispose();
            this._dAAPIPlayerPanelInfoVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setPlayerPanelInfo(param1:Object) : void
      {
         var _loc2_:DAAPIPlayerPanelInfoVO = this._dAAPIPlayerPanelInfoVO;
         this._dAAPIPlayerPanelInfoVO = new DAAPIPlayerPanelInfoVO(param1);
         this.setPlayerPanelInfo(this._dAAPIPlayerPanelInfoVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_updateTriggeredChatCommands(param1:Object) : void
      {
         var _loc2_:DAAPITriggeredCommandsVO = new DAAPITriggeredCommandsVO(param1);
         this.updateTriggeredChatCommands(_loc2_);
      }
      
      protected function setPlayerPanelInfo(param1:DAAPIPlayerPanelInfoVO) : void
      {
         var _loc2_:String = "as_setPlayerPanelInfo" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function updateTriggeredChatCommands(param1:DAAPITriggeredCommandsVO) : void
      {
         var _loc2_:String = "as_updateTriggeredChatCommands" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
