package net.wg.gui.battle.ranked.stats.components.playersPanel.list
{
   import flash.geom.Rectangle;
   import net.wg.gui.battle.ranked.stats.components.RankedVoiceChatActivation;
   import net.wg.gui.battle.ranked.stats.components.data.VoiceChatActivationVO;
   import net.wg.gui.battle.ranked.stats.components.playersPanel.interfaces.IRankedPlayersPanelListLeft;
   
   public class RankedPlayersPanelListLeft extends RankedPlayersPanelList implements IRankedPlayersPanelListLeft
   {
      
      private static const LINKAGE:String = "RankedPlayersPanelListItemLeftUI";
      
      private static const WIDTH:uint = 485;
       
      
      public var rankedVoiceChatActivation:RankedVoiceChatActivation = null;
      
      public function RankedPlayersPanelListLeft()
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
      
      override public function toString() : String
      {
         return "[RankedPlayersPanelListLeft]";
      }
      
      override public function getRenderersVisibleWidth() : uint
      {
         var _loc1_:Rectangle = renderersContainer.getBounds(this);
         return _loc1_.x + WIDTH;
      }
      
      override protected function onDispose() : void
      {
         this.rankedVoiceChatActivation.dispose();
         this.rankedVoiceChatActivation = null;
         super.onDispose();
      }
      
      public function setVoiceChatControlActive(param1:Boolean) : void
      {
         this.rankedVoiceChatActivation.setIsActive(param1);
      }
      
      public function setVoiceChatData(param1:VoiceChatActivationVO) : void
      {
         this.rankedVoiceChatActivation.setData(param1);
      }
      
      public function setVoiceChatVisibility(param1:Boolean) : void
      {
         this.rankedVoiceChatActivation.visible = param1;
      }
   }
}
