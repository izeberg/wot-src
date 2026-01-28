package net.wg.gui.battle.views.epicMessagesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.gameMessagesPanel.components.MessageContainerBase;
   import net.wg.gui.battle.views.gameMessagesPanel.data.GameMessageVO;
   
   public class SupplyActiveMessage extends MessageContainerBase
   {
       
      
      public var mainTextMc:MovieClip = null;
      
      public function SupplyActiveMessage()
      {
         super();
      }
      
      override public function setData(param1:GameMessageVO) : void
      {
         super.setData(param1);
         this.mainTextMc.tf.text = param1.msgData.title;
      }
      
      override protected function onDispose() : void
      {
         this.mainTextMc = null;
         super.onDispose();
      }
   }
}
