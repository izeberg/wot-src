package net.wg.frontline.gui.battle.views.frontlineMessagesPanel
{
   import net.wg.data.constants.generated.GAME_MESSAGES_CONSTS;
   import net.wg.frontline.data.constants.FrontlineLinkages;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.BaseCaptureMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.BaseContestedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.FirstGeneralRankReachedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.HeadquarterAttackedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.HeadquarterDestroyedMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.OverTimeMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.RankUpMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.RetreatMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.TimeRemainingMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components.UnlockTankLevelMessage;
   import net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data.FrontlineGameMessageVO;
   import net.wg.gui.battle.interfaces.IGameMessageVO;
   import net.wg.gui.battle.views.gameMessagesPanel.GameMessagesPanel;
   import net.wg.infrastructure.base.meta.IGameMessagesPanelMeta;
   
   public class FrontlineMessagesPanel extends GameMessagesPanel implements IGameMessagesPanelMeta
   {
       
      
      public function FrontlineMessagesPanel()
      {
         super();
         mouseEnabled = false;
         mouseChildren = false;
      }
      
      override protected function getIGameMessageVOForMessageVO(param1:Object) : IGameMessageVO
      {
         return new FrontlineGameMessageVO(param1);
      }
      
      override protected function initMappingDict() : void
      {
         super.initMappingDict();
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.TIME_REMAINING] = FrontlineLinkages.TIME_REMAINING_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.TIME_REMAINING_POSITIVE] = FrontlineLinkages.TIME_REMAINING_POSITIVE_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.OVERTIME] = FrontlineLinkages.OVER_TIME_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE] = FrontlineLinkages.BASE_CAPTURED_POSITIVE_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED] = FrontlineLinkages.BASE_CAPTURED_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.BASE_CONTESTED_POSITIVE] = FrontlineLinkages.BASE_CONTESTED_POSITIVE_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.BASE_CONTESTED] = FrontlineLinkages.BASE_CONTESTED_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.RANK_UP] = FrontlineLinkages.RANK_UP_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED_POSITIVE] = FrontlineLinkages.OBJECTIVE_DESTROYED_POSITIVE_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED] = FrontlineLinkages.OBJECTIVE_DESTROYED_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.RETREAT] = FrontlineLinkages.RETREAT_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK_POSITIVE] = FrontlineLinkages.OBJECTIVE_UNDER_ATTACK_POSITIVE_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK] = FrontlineLinkages.OBJECTIVE_UNDER_ATTACK_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.GENERAL_RANK_REACHED] = FrontlineLinkages.FIRST_GENERAL_RANK_REACHED_UI_LINKAGE;
         msgLinkageTypeDict[GAME_MESSAGES_CONSTS.UNLOCK_TANK_LEVEL] = FrontlineLinkages.UNLOCK_TANK_LEVEL_UI_LINKAGE;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.TIME_REMAINING] = TimeRemainingMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.TIME_REMAINING_POSITIVE] = TimeRemainingMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.OVERTIME] = OverTimeMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE] = BaseCaptureMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.BASE_CAPTURED] = BaseCaptureMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.BASE_CONTESTED_POSITIVE] = BaseContestedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.BASE_CONTESTED] = BaseContestedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.RANK_UP] = RankUpMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED_POSITIVE] = HeadquarterDestroyedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED] = HeadquarterDestroyedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.RETREAT] = RetreatMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK_POSITIVE] = HeadquarterAttackedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK] = HeadquarterAttackedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.GENERAL_RANK_REACHED] = FirstGeneralRankReachedMessage;
         msgClassTypeDict[GAME_MESSAGES_CONSTS.UNLOCK_TANK_LEVEL] = UnlockTankLevelMessage;
      }
   }
}
