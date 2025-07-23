package net.wg.gui.battle.ranked.stats.components.playersPanel
{
   import net.wg.gui.battle.ranked.stats.components.data.VoiceChatActivationVO;
   import net.wg.gui.battle.ranked.stats.components.events.VoiceChatActivationEvent;
   import net.wg.gui.battle.ranked.stats.components.playersPanel.interfaces.IRankedPlayersPanelListLeft;
   import net.wg.infrastructure.base.meta.IRankedPlayersPanelMeta;
   import net.wg.infrastructure.base.meta.impl.RankedPlayersPanelMeta;
   
   public class RankedPlayersPanel extends RankedPlayersPanelMeta implements IRankedPlayersPanelMeta
   {
       
      
      public function RankedPlayersPanel()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(VoiceChatActivationEvent.CONTROL_CLICKED,this.onVoiceChatControlClickedHandler);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(VoiceChatActivationEvent.CONTROL_CLICKED,this.onVoiceChatControlClickedHandler);
         super.onDispose();
      }
      
      override protected function setVoiceChatData(param1:VoiceChatActivationVO) : void
      {
         IRankedPlayersPanelListLeft(listLeft).setVoiceChatData(param1);
      }
      
      public function as_setVoiceChatControlSelected(param1:Boolean) : void
      {
         IRankedPlayersPanelListLeft(listLeft).setVoiceChatControlActive(param1);
      }
      
      public function as_setVoiceChatControlVisible(param1:Boolean) : void
      {
         IRankedPlayersPanelListLeft(listLeft).setVoiceChatVisibility(param1);
      }
      
      private function onVoiceChatControlClickedHandler(param1:VoiceChatActivationEvent) : void
      {
         onVoiceChatControlClickS();
      }
   }
}
