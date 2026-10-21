package net.wg.portal.gui.battle.views.playersPanel
{
   import net.wg.data.ListDAAPIDataProvider;
   import net.wg.data.constants.generated.BATTLE_CONTEXT_MENU_HANDLER_TYPE;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.VO.PlayersPanelContextMenuSentData;
   import net.wg.infrastructure.events.VoiceChatEvent;
   import net.wg.infrastructure.managers.IContextMenuManager;
   import net.wg.portal.gui.battle.views.playersPanel.VO.PlayerInfoVO;
   import net.wg.portal.gui.battle.views.playersPanel.events.PlayerRendererEvent;
   import net.wg.portal.infrastructure.base.meta.IPortalPlayersPanelMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalPlayersPanelMeta;
   
   public class PlayersPanel extends PortalPlayersPanelMeta implements IPortalPlayersPanelMeta
   {
       
      
      public var playersList:PlayersList = null;
      
      private var _dataProvider:ListDAAPIDataProvider = null;
      
      private var _contextMenuMgr:IContextMenuManager;
      
      public function PlayersPanel()
      {
         this._contextMenuMgr = App.contextMenuMgr;
         super();
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(PlayerRendererEvent.ITEM_LEFT_CLICK,this.onItemLeftClickHandler);
         removeEventListener(PlayerRendererEvent.ITEM_RIGHT_CLICK,this.onItemRightClickHandler);
         App.voiceChatMgr.removeEventListener(VoiceChatEvent.START_SPEAKING,this.onVoiceChatStartSpeakingHandler);
         App.voiceChatMgr.removeEventListener(VoiceChatEvent.STOP_SPEAKING,this.onVoiceChatStopSpeakingHandler);
         this._contextMenuMgr = null;
         this.playersList.dispose();
         this.playersList = null;
         this._dataProvider.cleanUp();
         this._dataProvider = null;
         super.onDispose();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this._dataProvider = new ListDAAPIDataProvider(PlayerInfoVO);
         this.playersList.dataProvider = this._dataProvider;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(PlayerRendererEvent.ITEM_LEFT_CLICK,this.onItemLeftClickHandler);
         addEventListener(PlayerRendererEvent.ITEM_RIGHT_CLICK,this.onItemRightClickHandler);
         App.voiceChatMgr.addEventListener(VoiceChatEvent.START_SPEAKING,this.onVoiceChatStartSpeakingHandler);
         App.voiceChatMgr.addEventListener(VoiceChatEvent.STOP_SPEAKING,this.onVoiceChatStopSpeakingHandler);
      }
      
      public function as_getDP() : Object
      {
         return this._dataProvider;
      }
      
      public function as_setChatCommand(param1:int, param2:String, param3:uint) : void
      {
         var _loc4_:PlayerRenderer = this.playersList.getPlayerRender(param1);
         if(_loc4_)
         {
            _loc4_.setChatCommand(param2,param3);
         }
      }
      
      public function as_setChatCommandsVisibility(param1:Boolean) : void
      {
         this.playersList.isChatCommVisible = param1;
      }
      
      public function as_setPlayerHp(param1:int, param2:int, param3:int, param4:Boolean) : void
      {
         var _loc5_:PlayerRenderer = this.playersList.getPlayerRender(param1);
         if(_loc5_)
         {
            _loc5_.updateHp(param2,param3,param4);
         }
      }
      
      public function as_setPlayerState(param1:int, param2:String) : void
      {
         var _loc3_:PlayerRenderer = this.playersList.getPlayerRender(param1);
         if(_loc3_)
         {
            _loc3_.updatePlayerState(param2);
         }
      }
      
      public function as_setPlayersSwitchingAllowed(param1:Boolean) : void
      {
         this.playersList.isPlayerSwitchingAllowed = param1;
      }
      
      private function setSpeaking(param1:Number, param2:Boolean) : void
      {
         var _loc3_:PlayerRenderer = this.playersList.getPlayerByAccountID(param1);
         if(_loc3_)
         {
            _loc3_.isSpeaking = param2;
         }
      }
      
      override public function get height() : Number
      {
         return this.playersList.height;
      }
      
      private function onItemRightClickHandler(param1:PlayerRendererEvent) : void
      {
         App.toolTipMgr.hide();
         this._contextMenuMgr.show(BATTLE_CONTEXT_MENU_HANDLER_TYPE.PLAYERS_PANEL,this,new PlayersPanelContextMenuSentData(param1.data.vehicleID));
      }
      
      private function onItemLeftClickHandler(param1:PlayerRendererEvent) : void
      {
         switchToOtherPlayerS(param1.data.vehicleID);
      }
      
      private function onVoiceChatStartSpeakingHandler(param1:VoiceChatEvent) : void
      {
         var _loc2_:Number = param1.getAccountDBID();
         if(!_loc2_)
         {
            return;
         }
         this.setSpeaking(_loc2_,true);
      }
      
      private function onVoiceChatStopSpeakingHandler(param1:VoiceChatEvent) : void
      {
         var _loc2_:Number = param1.getAccountDBID();
         if(!_loc2_)
         {
            return;
         }
         this.setSpeaking(_loc2_,false);
      }
   }
}
