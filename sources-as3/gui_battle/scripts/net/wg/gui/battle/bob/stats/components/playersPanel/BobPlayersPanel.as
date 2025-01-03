package net.wg.gui.battle.bob.stats.components.playersPanel
{
   import net.wg.gui.battle.bob.stats.components.data.VoiceChatActivationVO;
   import net.wg.gui.battle.bob.stats.components.events.VoiceChatActivationEvent;
   import net.wg.gui.battle.bob.stats.components.playersPanel.list.BobPlayersPanelList;
   import net.wg.gui.battle.bob.stats.components.playersPanel.list.BobPlayersPanelListLeft;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.interfaces.IPlayersPanelList;
   import net.wg.infrastructure.base.meta.IBobPlayersPanelMeta;
   import net.wg.infrastructure.base.meta.impl.BobPlayersPanelMeta;
   
   public class BobPlayersPanel extends BobPlayersPanelMeta implements IBobPlayersPanelMeta
   {
      
      private static const MIN_WIDTH:int = 1024;
      
      private static const MIN_HEIGHT:int = 768;
      
      private static const PREBATTLE_SKILL_BOTTOM_OFFSET:int = 80;
       
      
      public var prebattleTeamSkill:BobPlayersPrebattleTeamSkill = null;
      
      private var _stageWidth:int;
      
      private var _stageHeight:int;
      
      public function BobPlayersPanel()
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
         this.prebattleTeamSkill.dispose();
         this.prebattleTeamSkill = null;
      }
      
      public function as_setLeftTeamSkill(param1:String, param2:String, param3:String) : void
      {
         this.updateListTeamSkill(this.getTypedList(listLeft),param1,param2,param3);
         this.prebattleTeamSkill.initialize();
         this.prebattleTeamSkill.update(param1,param2,param3);
         this.updateLayout();
      }
      
      public function as_setRightTeamSkill(param1:String, param2:String, param3:String) : void
      {
         this.updateListTeamSkill(this.getTypedList(listRight),param1,param2,param3);
      }
      
      public function as_setBattleStarted(param1:Boolean) : void
      {
         if(param1)
         {
            this.getTypedList(listLeft).teamSkill.collapse();
            this.getTypedList(listRight).teamSkill.collapse();
            this.prebattleTeamSkill.hide();
         }
      }
      
      override public function updateStageSize(param1:Number, param2:Number) : void
      {
         super.updateStageSize(param1,param2);
         this._stageWidth = param1;
         this._stageHeight = param2;
         this.updateLayout();
         if(param1 <= MIN_WIDTH || param2 <= MIN_HEIGHT)
         {
            this.prebattleTeamSkill.hide();
         }
      }
      
      private function updateListTeamSkill(param1:BobPlayersPanelList, param2:String, param3:String, param4:String) : void
      {
         param1.teamSkill.initialize();
         param1.teamSkill.update(param2,param3,param4);
      }
      
      private function getTypedList(param1:IPlayersPanelList) : BobPlayersPanelList
      {
         return param1 as BobPlayersPanelList;
      }
      
      private function updateLayout() : void
      {
         this.prebattleTeamSkill.x = this._stageWidth >> 1;
         this.prebattleTeamSkill.y = this._stageHeight - this.prebattleTeamSkill.height - PREBATTLE_SKILL_BOTTOM_OFFSET >> 0;
      }
      
      override protected function setVoiceChatData(param1:VoiceChatActivationVO) : void
      {
         BobPlayersPanelListLeft(listLeft).setVoiceChatData(param1);
      }
      
      public function as_setVoiceChatControlSelected(param1:Boolean) : void
      {
         BobPlayersPanelListLeft(listLeft).setVoiceChatControlActive(param1);
      }
      
      public function as_setVoiceChatControlVisible(param1:Boolean) : void
      {
         BobPlayersPanelListLeft(listLeft).setVoiceChatVisibility(param1);
      }
      
      private function onVoiceChatControlClickedHandler(param1:VoiceChatActivationEvent) : void
      {
         onVoiceChatControlClickS();
      }
   }
}
