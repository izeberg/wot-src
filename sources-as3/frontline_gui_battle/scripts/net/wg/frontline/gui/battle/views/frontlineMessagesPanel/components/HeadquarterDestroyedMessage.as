package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.GAME_MESSAGES_CONSTS;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.HeadquarterDestroyedMessageVO;
   import net.wg.gui.battle.interfaces.IGameMessageVO;
   import net.wg.gui.battle.views.gameMessagesPanel.components.MessageContainerBase;
   import net.wg.gui.battle.views.gameMessagesPanel.events.GameMessagesPanelEvent;
   
   public class HeadquarterDestroyedMessage extends MessageContainerBase
   {
      
      private static const ERROR_CONVERTING_VO:String = "[HeadquarterDestroyedMessage] setData object was not in correct structure, could not convert to proper VO";
       
      
      public var mainTextMc:MovieClip = null;
      
      public var epicHQId:MovieClip = null;
      
      private var _msgDataVO:HeadquarterDestroyedMessageVO = null;
      
      public function HeadquarterDestroyedMessage()
      {
         super();
      }
      
      override public function getID() : int
      {
         return this._msgDataVO.hqID;
      }
      
      override public function setData(param1:IGameMessageVO) : void
      {
         messageData = param1;
         var _loc2_:HeadquarterDestroyedMessageVO = param1.msgData as HeadquarterDestroyedMessageVO;
         App.utils.asserter.assertNotNull(_loc2_,ERROR_CONVERTING_VO);
         this._msgDataVO = _loc2_;
         this.mainTextMc.titleTF.text = _loc2_.title;
         this.epicHQId.gotoAndStop(_loc2_.hqID);
      }
      
      override protected function getPostIntroGameMessagesPanelEvent() : GameMessagesPanelEvent
      {
         var _loc1_:GameMessagesPanelEvent = super.getPostIntroGameMessagesPanelEvent();
         _loc1_.messageModificator = GAME_MESSAGES_CONSTS.WITH_EVENT;
         return _loc1_;
      }
      
      override protected function onDispose() : void
      {
         this.mainTextMc = null;
         this.epicHQId = null;
         this._msgDataVO = null;
         super.onDispose();
      }
   }
}
