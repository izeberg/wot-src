package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.RankUpMessageVO;
   import net.wg.gui.battle.interfaces.IGameMessageVO;
   import net.wg.gui.battle.views.gameMessagesPanel.components.MessageContainerBase;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class RankUpMessage extends MessageContainerBase
   {
      
      private static const ERROR_CONVERTING_VO:String = "[RankUpMessage] setData object was not in correct structure, could not convert to proper VO";
       
      
      public var mainTextMc:MovieClip = null;
      
      public var icon:MovieClip = null;
      
      public var rankUpSubMc:RankUpSubElement = null;
      
      private var _msgDataVO:RankUpMessageVO = null;
      
      public function RankUpMessage()
      {
         super();
      }
      
      override public function setData(param1:IGameMessageVO) : void
      {
         messageData = param1;
         var _loc2_:RankUpMessageVO = param1.msgData as RankUpMessageVO;
         App.utils.asserter.assertNotNull(_loc2_,ERROR_CONVERTING_VO);
         this._msgDataVO = _loc2_;
         this.mainTextMc.titleTF.text = _loc2_.title;
         this.icon.gotoAndStop(_loc2_.rank);
         if(StringUtils.isNotEmpty(_loc2_.subTitle))
         {
            this.rankUpSubMc.setText(_loc2_.subTitle);
         }
         else
         {
            this.rankUpSubMc.visible = false;
         }
      }
      
      override protected function onDispose() : void
      {
         this.icon = null;
         this.mainTextMc = null;
         this._msgDataVO = null;
         this.rankUpSubMc.dispose();
         this.rankUpSubMc = null;
         super.onDispose();
      }
   }
}
