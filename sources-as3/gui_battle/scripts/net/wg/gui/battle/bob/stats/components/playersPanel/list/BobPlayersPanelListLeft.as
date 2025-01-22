package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   import net.wg.gui.battle.bob.stats.components.VoiceChatActivation;
   import net.wg.gui.battle.bob.stats.components.data.VoiceChatActivationVO;
   
   public class BobPlayersPanelListLeft extends BobPlayersPanelList
   {
      
      private static const LINKAGE:String = "BobPlayersPanelListItemLeftUI";
       
      
      public var voiceChatActivation:VoiceChatActivation = null;
      
      public function BobPlayersPanelListLeft()
      {
         super();
      }
      
      override protected function get itemLinkage() : String
      {
         return LINKAGE;
      }
      
      override protected function get isRightAligned() : Boolean
      {
         return false;
      }
      
      override protected function onDispose() : void
      {
         this.voiceChatActivation.dispose();
         this.voiceChatActivation = null;
         super.onDispose();
      }
      
      override public function toString() : String
      {
         return "[WG BobPlayersPanelListLeft]";
      }
      
      public function setVoiceChatControlActive(param1:Boolean) : void
      {
         this.voiceChatActivation.setIsActive(param1);
      }
      
      public function setVoiceChatData(param1:VoiceChatActivationVO) : void
      {
         this.voiceChatActivation.setData(param1);
      }
      
      public function setVoiceChatVisibility(param1:Boolean) : void
      {
         this.voiceChatActivation.visible = param1;
      }
   }
}
