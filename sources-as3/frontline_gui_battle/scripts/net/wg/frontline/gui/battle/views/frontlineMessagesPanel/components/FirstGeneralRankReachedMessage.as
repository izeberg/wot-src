package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.FirstGeneralRankReachedMessageVO;
   import net.wg.gui.battle.interfaces.IGameMessageVO;
   import net.wg.gui.battle.views.gameMessagesPanel.components.MessageContainerBase;
   
   public class FirstGeneralRankReachedMessage extends MessageContainerBase
   {
      
      private static const ERROR_CONVERTING_VO:String = "[FirstGeneralRankReachedMessage] setData object was not in correct structure, could not convert to proper VO";
       
      
      public var mainTextMc:MovieClip = null;
      
      private var _msgDataVO:FirstGeneralRankReachedMessageVO = null;
      
      public function FirstGeneralRankReachedMessage()
      {
         super();
      }
      
      override public function setData(param1:IGameMessageVO) : void
      {
         messageData = param1;
         var _loc2_:FirstGeneralRankReachedMessageVO = param1.msgData as FirstGeneralRankReachedMessageVO;
         App.utils.asserter.assertNotNull(_loc2_,ERROR_CONVERTING_VO);
         this._msgDataVO = _loc2_;
         this.mainTextMc.titleTF.text = _loc2_.title;
         this.mainTextMc.subtitleTF.text = _loc2_.subTitle;
      }
      
      override protected function onDispose() : void
      {
         this.mainTextMc = null;
         this._msgDataVO = null;
         super.onDispose();
      }
   }
}
