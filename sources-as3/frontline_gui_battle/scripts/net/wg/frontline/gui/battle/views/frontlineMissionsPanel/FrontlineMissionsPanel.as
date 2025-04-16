package net.wg.frontline.gui.battle.views.frontlineMissionsPanel
{
   import flash.display.MovieClip;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.EPIC_CONSTS;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlinePlayerStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehiclesStatsVO;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.components.FrontlineMissionsAnimatedMarker;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.data.FrontlineMissionVO;
   import net.wg.frontline.infrastructure.base.meta.IFrontlineMissionsPanelMeta;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineMissionsPanelMeta;
   import net.wg.frontline.infrastructure.helpers.statisticsDataController.interfaces.IFrontlineBattleStatisticDataController;
   
   public class FrontlineMissionsPanel extends FrontlineMissionsPanelMeta implements IFrontlineBattleStatisticDataController, IFrontlineMissionsPanelMeta
   {
      
      private static const STOP_FRAME:int = 2;
      
      private static const INTRO_FRAME:String = "intro";
      
      private static const EMPTY_PRIMARY_MISSION_ERROR:String = "[FrontlineMissionsPanel] Empty primary objective received.";
      
      private static const UNKNOWN_PRIMARY_MISSION_ERROR:String = "[FrontlineMissionsPanel] Unknown primary objective received: ";
       
      
      public var primaryMission:MovieClip = null;
      
      public var missionSubtext:MovieClip = null;
      
      public var animatedMarker:FrontlineMissionsAnimatedMarker = null;
      
      private var _missionData:FrontlineMissionVO = null;
      
      private var _isAttacker:Boolean = false;
      
      private var _hqIndex:int = -1;
      
      private var _missionDescValue:String = "";
      
      public function FrontlineMissionsPanel()
      {
         super();
         stop();
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         super.draw();
         if(isInvalid(InvalidationType.DATA) && this._missionData != null)
         {
            this.primaryMission.primaryMissionTF.text = this._missionData.missionText.toUpperCase();
            this.missionSubtext.visible = this._missionData.subText != Values.EMPTY_STR;
            this.missionSubtext.missionDescriptionTF.text = this._missionData.subText;
            _loc1_ = this._missionData.objectiveType;
            if(_loc1_ != EPIC_CONSTS.PRIMARY_BASE_MISSION && _loc1_ != EPIC_CONSTS.PRIMARY_HQ_MISSION && _loc1_ != EPIC_CONSTS.PRIMARY_WAYPOINT_MISSION)
            {
               gotoAndStop(STOP_FRAME);
               if(_loc1_ == EPIC_CONSTS.PRIMARY_EMPTY_MISSION)
               {
                  DebugUtils.LOG_DEBUG(EMPTY_PRIMARY_MISSION_ERROR);
               }
               else
               {
                  DebugUtils.LOG_DEBUG(UNKNOWN_PRIMARY_MISSION_ERROR,_loc1_);
               }
            }
            else
            {
               this.animatedMarker.setState(_loc1_,this._isAttacker,this._missionData.objectiveID);
               gotoAndPlay(INTRO_FRAME);
            }
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            if(this._hqIndex >= 0)
            {
               this.animatedMarker.setHeadquarterID(this._hqIndex);
            }
         }
         if(isInvalid(InvalidationType.STATE))
         {
            this.missionSubtext.missionValueTF.htmlText = this._missionDescValue;
            if(this._missionData)
            {
               this.missionSubtext.visible = this._missionDescValue != Values.EMPTY_STR && this._missionData.subText != Values.EMPTY_STR;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.animatedMarker.dispose();
         this.animatedMarker = null;
         this.primaryMission = null;
         this.missionSubtext = null;
         if(this._missionData)
         {
            this._missionData.dispose();
            this._missionData = null;
         }
         super.onDispose();
      }
      
      override protected function setPrimaryMission(param1:FrontlineMissionVO) : void
      {
         this._missionData = param1;
         invalidateData();
      }
      
      public function as_setMissionDescriptionValue(param1:String) : void
      {
         this._missionDescValue = param1;
         invalidateState();
      }
      
      public function as_setNearestHQ(param1:int) : void
      {
         if(this._hqIndex == param1)
         {
            return;
         }
         this._hqIndex = param1;
         invalidateSize();
      }
      
      public function setEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
      }
      
      public function updateEpicPlayerStats(param1:FrontlinePlayerStatsVO) : void
      {
         if(this._isAttacker == param1.isAttacker)
         {
            return;
         }
         this._isAttacker = param1.isAttacker;
         invalidateData();
      }
      
      public function updateEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
      }
   }
}
