package net.wg.gui.battle.views.epicMessagesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.epicMessagesPanel.data.CommonSubElementMessageVO;
   import net.wg.gui.battle.views.gameMessagesPanel.components.MessageContainerBase;
   import net.wg.gui.battle.views.gameMessagesPanel.data.GameMessageVO;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class CommonSubElementMessage extends MessageContainerBase
   {
      
      private static const ERROR_CONVERTING_VO:String = "[CommonSubElementMessage] setData object was not in correct structure, could not convert to proper VO";
       
      
      public var icon:MovieClip = null;
      
      public var mainTextMc:MovieClip = null;
      
      public var subTextMc:CommonSubElement = null;
      
      public function CommonSubElementMessage()
      {
         super();
      }
      
      override public function setData(param1:GameMessageVO) : void
      {
         messageData = param1;
         var _loc2_:CommonSubElementMessageVO = param1.msgData as CommonSubElementMessageVO;
         App.utils.asserter.assertNotNull(_loc2_,ERROR_CONVERTING_VO);
         this.mainTextMc.titleTF.text = _loc2_.title;
         this.icon.gotoAndStop(_loc2_.iconFrame);
         if(StringUtils.isNotEmpty(_loc2_.subTitle))
         {
            this.subTextMc.setText(_loc2_.subTitle);
         }
         else
         {
            this.subTextMc.visible = false;
         }
      }
      
      override protected function onDispose() : void
      {
         this.icon = null;
         this.mainTextMc = null;
         this.subTextMc.dispose();
         this.subTextMc = null;
         super.onDispose();
      }
   }
}
