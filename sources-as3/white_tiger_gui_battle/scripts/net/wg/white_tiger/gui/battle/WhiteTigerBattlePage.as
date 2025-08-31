package net.wg.white_tiger.gui.battle
{
   import flash.events.Event;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.gui.battle.random.views.BattlePage;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_VIEW_ALIASES;
   import net.wg.white_tiger.gui.battle.views.battleHints.WhiteTigerBattleHint;
   import net.wg.white_tiger.gui.battle.views.bossTeleportation.WhiteTigerTeleportView;
   import net.wg.white_tiger.gui.battle.views.hunterRespawn.WhiteTigerHunterRespawnView;
   import net.wg.white_tiger.gui.battle.views.minimap.WhiteTigerMinimap;
   import net.wg.white_tiger.gui.battle.views.shared.WhiteTigerDeploymentMapView;
   import net.wg.white_tiger.gui.battle.views.whiteTigerHud.WhiteTigerHud;
   import net.wg.white_tiger.gui.battle.views.whiteTigerOvertime.WhiteTigerOvertime;
   import net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.WhiteTigerPlayersPanel;
   import net.wg.white_tiger.gui.battle.views.whiteTigerStatusNotificationPanel.WhiteTigerStatusNotificationsPanel;
   
   public class WhiteTigerBattlePage extends BattlePage
   {
      
      private static const SCREEN_MEDIUM_WIDTH:Number = 1920;
      
      private static const SCREEN_MEDIUM_HEIGHT:Number = 1080;
      
      private static const MINIMAP_SIZE_INDEX_SMALL:int = 3;
      
      private static const MINIMAP_SIZE_INDEX_BIG:int = 5;
      
      private static const MINIMAP_OFFSET:int = 18;
      
      private static const BATTLE_MSGS_SWAP_AREA_OFFSET:int = 15;
      
      private static const UNEXPECTED_ALIAS:String = "Unexpected deploy selection alias: ";
       
      
      public var whiteTigerHud:WhiteTigerHud = null;
      
      public var whiteTigerPlayersPanel:WhiteTigerPlayersPanel = null;
      
      public var hunterRespawn:WhiteTigerHunterRespawnView = null;
      
      public var bossTeleport:WhiteTigerTeleportView = null;
      
      public var overtime:WhiteTigerOvertime = null;
      
      public var wtBattleHint:WhiteTigerBattleHint = null;
      
      public var statusNotificationsPanel:WhiteTigerStatusNotificationsPanel = null;
      
      private var _whiteTigerMinimap:WhiteTigerMinimap = null;
      
      private var _minimapIndex:int = 0;
      
      public function WhiteTigerBattlePage()
      {
         super();
         this._whiteTigerMinimap = WhiteTigerMinimap(minimap);
         if(this._whiteTigerMinimap)
         {
            this._minimapIndex = getChildIndex(this._whiteTigerMinimap);
         }
      }
      
      override protected function configUI() : void
      {
         this.addEventListener(Event.RESIZE,this.onResize);
         this.addEventListener(Event.CHANGE,this.onChange);
         postmortemPanelUI.isEnabledPostmortemPanel = false;
         super.configUI();
      }
      
      override protected function onPopulate() : void
      {
         if(this.whiteTigerHud)
         {
            this.registerComponent(this.whiteTigerHud,WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_HUD);
         }
         if(this.whiteTigerPlayersPanel)
         {
            this.registerComponent(this.whiteTigerPlayersPanel,WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_PLAYERS_PANEL);
         }
         if(this.hunterRespawn)
         {
            this.registerComponent(this.hunterRespawn,WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_HUNTER_RESPAWN);
         }
         if(this.bossTeleport)
         {
            this.registerComponent(this.bossTeleport,WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_BOSS_TELEPORT);
         }
         if(this.overtime)
         {
            this.registerComponent(this.overtime,WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_OVERTIME);
         }
         if(this.wtBattleHint)
         {
            this.registerComponent(this.wtBattleHint,WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_BATTLE_HINT);
         }
         if(this.statusNotificationsPanel)
         {
            this.registerComponent(this.statusNotificationsPanel,BATTLE_VIEW_ALIASES.STATUS_NOTIFICATIONS_PANEL);
         }
         this.updateOvertimePosition();
         super.onPopulate();
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         this.whiteTigerHud.updateStage(param1,param2);
         this.whiteTigerPlayersPanel.updateStageSize(param1,param2);
         this.hunterRespawn.updateStage(param1,param2);
         this.bossTeleport.updateStage(param1,param2);
         this.wtBattleHint.updateStage(param1,param2);
         this.statusNotificationsPanel.updateStage(param1,param2);
         this.updateBattleMsgSwapArea();
         this.updateOvertimePosition();
      }
      
      private function onChange(param1:Event = null) : void
      {
         this.onEvPlayersPanelChangeHandler(param1);
         this.updateOvertimePosition(param1);
      }
      
      private function onResize(param1:Event = null) : void
      {
         this.updateOvertimePosition(param1);
      }
      
      override protected function createStatisticsController() : BattleStatisticDataController
      {
         return new WhiteTigerBattleStatisticDataController(this);
      }
      
      override protected function initializeStatisticsController(param1:BattleStatisticDataController) : void
      {
         param1.registerComponentController(this.whiteTigerPlayersPanel);
         super.initializeStatisticsController(param1);
      }
      
      override protected function updateTeamBasesPanelPosition(param1:Boolean = false) : void
      {
         this.alignBattleHintsWithTeamsPanelPosition(teamBasesPanelUI.numChildren);
      }
      
      override protected function setComponentsVisibility(param1:Vector.<String>, param2:Vector.<String>) : void
      {
         var _loc3_:String = null;
         super.setComponentsVisibility(param1,param2);
         for each(_loc3_ in param1)
         {
            if(_loc3_ == WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_HUNTER_RESPAWN || _loc3_ == WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_BOSS_TELEPORT)
            {
               this.setMinimapDeploymentMode(_loc3_,true);
               return;
            }
         }
         for each(_loc3_ in param2)
         {
            if(_loc3_ == WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_HUNTER_RESPAWN || _loc3_ == WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_BOSS_TELEPORT)
            {
               this.setMinimapDeploymentMode(_loc3_,false);
               return;
            }
         }
      }
      
      private function alignBattleHintsWithTeamsPanelPosition(param1:Number) : void
      {
         switch(param1)
         {
            case 1:
               this.wtBattleHint.updatePositionY(this.wtBattleHint.HINT_DEFAULT_Y_POSITION);
               break;
            case 2:
               this.wtBattleHint.updatePositionY(this.wtBattleHint.HINT_DEFAULT_Y_POSITION + this.wtBattleHint.HINT_CONTAINER_Y_OFFSET);
               break;
            case 3:
               this.wtBattleHint.updatePositionY(this.wtBattleHint.HINT_DEFAULT_Y_POSITION + 4 * this.wtBattleHint.HINT_CONTAINER_Y_OFFSET);
               break;
            default:
               this.wtBattleHint.updatePositionY(this.wtBattleHint.HINT_DEFAULT_Y_POSITION);
         }
      }
      
      private function updateOvertimePosition(param1:Event = null) : void
      {
         this.overtime.x = _width >> 1;
         this.overtime.y = _height >> 2;
      }
      
      private function setMinimapDeploymentMode(param1:String, param2:Boolean) : void
      {
         if(this._whiteTigerMinimap.isDeploymentMode == param2)
         {
            return;
         }
         var _loc3_:WhiteTigerDeploymentMapView = null;
         switch(param1)
         {
            case WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_HUNTER_RESPAWN:
               _loc3_ = this.hunterRespawn;
               break;
            case WHITE_TIGER_BATTLE_VIEW_ALIASES.WHITE_TIGER_BOSS_TELEPORT:
               _loc3_ = this.bossTeleport;
               break;
            default:
               throw new Error(UNEXPECTED_ALIAS + Values.SPACE_STR + param1);
         }
         if(param2)
         {
            _loc3_.attachMinimap(minimap);
         }
         else
         {
            _loc3_.detachMinimap();
            addChildAt(minimap,this._minimapIndex);
         }
         this._whiteTigerMinimap.isDeploymentMode = param2;
         this.updateMinimapPosition();
      }
      
      private function onEvPlayersPanelChangeHandler(param1:Event) : void
      {
         this.updateBattleMsgSwapArea();
      }
      
      private function updateBattleMsgSwapArea() : void
      {
         var _loc1_:int = this.whiteTigerPlayersPanel.y + this.whiteTigerPlayersPanel.listLeft.y + this.whiteTigerPlayersPanel.listLeft.height + BATTLE_MSGS_SWAP_AREA_OFFSET;
         battleMessenger.updateSwapAreaHeight(damagePanel.y - _loc1_);
      }
      
      override protected function registerComponent(param1:IDAAPIModule, param2:String) : void
      {
         if(param1)
         {
            super.registerComponent(param1,param2);
         }
      }
      
      override protected function getAllowedMinimapSizeIndex(param1:Number) : Number
      {
         var _loc5_:Boolean = false;
         var _loc6_:int = 0;
         if(this._whiteTigerMinimap.isDeploymentMode)
         {
            _loc5_ = _height < SCREEN_MEDIUM_HEIGHT || _width < SCREEN_MEDIUM_WIDTH;
            return int(!!_loc5_ ? int(MINIMAP_SIZE_INDEX_SMALL) : int(MINIMAP_SIZE_INDEX_BIG));
         }
         var _loc2_:Number = App.appHeight >> 1;
         var _loc3_:Number = App.appWidth - consumablesPanel.panelWidth - MINIMAP_OFFSET | 0;
         var _loc4_:Rectangle = null;
         while(param1 > MinimapSizeConst.MIN_SIZE_INDEX)
         {
            _loc4_ = minimap.getMinimapRectBySizeIndex(param1);
            if(_loc2_ - _loc4_.height >= 0 && _loc3_ - _loc4_.width >= 0)
            {
               break;
            }
            param1--;
         }
         return param1;
      }
      
      override protected function updateMinimapPosition() : void
      {
         if(!this._whiteTigerMinimap.isDeploymentMode)
         {
            super.updateMinimapPosition();
         }
      }
      
      override protected function get isQuestProgress() : Boolean
      {
         return false;
      }
      
      override protected function onDispose() : void
      {
         this.removeEventListener(Event.RESIZE,this.onResize);
         this.removeEventListener(Event.CHANGE,this.onChange);
         this.whiteTigerHud = null;
         this.whiteTigerPlayersPanel = null;
         this.hunterRespawn = null;
         this.bossTeleport = null;
         this.overtime = null;
         this.wtBattleHint = null;
         this.statusNotificationsPanel = null;
         this._whiteTigerMinimap = null;
         super.onDispose();
      }
   }
}
