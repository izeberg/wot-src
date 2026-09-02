package net.wg.white_tiger.gui.battle.views.wtFullStats
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.PlayerStatusView;
   import net.wg.gui.battle.random.views.stats.components.fullStats.FullStatsTable;
   import net.wg.gui.battle.views.stats.SpeakAnimation;
   import net.wg.gui.battle.views.stats.fullStats.SquadInviteStatusView;
   import net.wg.gui.components.controls.BadgeComponent;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.white_tiger.gui.battle.views.shared.HunterResurrectTimer;
   
   public class FullStatsTable extends net.wg.gui.battle.random.views.stats.components.fullStats.FullStatsTable
   {
      
      private static const NUM_ROWS:int = 6;
       
      
      public var resurrectTimer_c1r1:HunterResurrectTimer = null;
      
      public var resurrectTimer_c1r2:HunterResurrectTimer = null;
      
      public var resurrectTimer_c1r3:HunterResurrectTimer = null;
      
      public var resurrectTimer_c1r4:HunterResurrectTimer = null;
      
      public var resurrectTimer_c1r5:HunterResurrectTimer = null;
      
      public var resurrectTimer_c1r6:HunterResurrectTimer = null;
      
      public var resurrectTimer_c2r1:HunterResurrectTimer = null;
      
      public var resurrectTimer_c2r2:HunterResurrectTimer = null;
      
      public var resurrectTimer_c2r3:HunterResurrectTimer = null;
      
      public var resurrectTimer_c2r4:HunterResurrectTimer = null;
      
      public var resurrectTimer_c2r5:HunterResurrectTimer = null;
      
      public var resurrectTimer_c2r6:HunterResurrectTimer = null;
      
      public var resurrectTimerCollection:Vector.<HunterResurrectTimer> = null;
      
      public function FullStatsTable()
      {
         super();
         var _loc1_:BattleAtlasSprite = new BattleAtlasSprite();
         icoIGRCollection = new <BattleAtlasSprite>[_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_,_loc1_];
         var _loc2_:PlayerStatusView = new PlayerStatusView();
         playerStatusCollection = new <PlayerStatusView>[_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_,_loc2_];
         this.resurrectTimerCollection = new <HunterResurrectTimer>[this.resurrectTimer_c1r1,this.resurrectTimer_c1r2,this.resurrectTimer_c1r3,this.resurrectTimer_c1r4,this.resurrectTimer_c1r5,this.resurrectTimer_c1r6,this.resurrectTimer_c2r1,this.resurrectTimer_c2r2,this.resurrectTimer_c2r3,this.resurrectTimer_c2r4,this.resurrectTimer_c2r5,this.resurrectTimer_c2r6];
         deadBgCollection = new <BattleAtlasSprite>[deadBg_c1r1,deadBg_c1r2,deadBg_c1r3,deadBg_c1r4,deadBg_c1r5,deadBg_c1r6,deadBg_c2r1,deadBg_c2r2,deadBg_c2r3,deadBg_c2r4,deadBg_c2r5,deadBg_c2r6];
         fragsCollection = new <TextField>[frags_c1r1,frags_c1r2,frags_c1r3,frags_c1r4,frags_c1r5,frags_c1r6,frags_c2r1,frags_c2r2,frags_c2r3,frags_c2r4,frags_c2r5,frags_c2r6];
         hitCollection = new <MovieClip>[hit_c1r1,hit_c1r2,hit_c1r3,hit_c1r4,hit_c1r5,hit_c1r6,hit_c2r1,hit_c2r2,hit_c2r3,hit_c2r4,hit_c2r5,hit_c2r6];
         muteCollection = new <BattleAtlasSprite>[mute_c1r1,mute_c1r2,mute_c1r3,mute_c1r4,mute_c1r5,mute_c1r6,mute_c2r1,mute_c2r2,mute_c2r3,mute_c2r4,mute_c2r5,mute_c2r6];
         disableCommunicationCollection = new <BattleAtlasSprite>[disableCommunication_c1r1,disableCommunication_c1r2,disableCommunication_c1r3,disableCommunication_c1r4,disableCommunication_c1r5,disableCommunication_c1r6,disableCommunication_c2r1,disableCommunication_c2r2,disableCommunication_c2r3,disableCommunication_c2r4,disableCommunication_c2r5,disableCommunication_c2r6];
         noSoundCollection = new <BattleAtlasSprite>[noSound_c1r1,noSound_c1r2,noSound_c1r3,noSound_c1r4,noSound_c1r5,noSound_c1r6,noSound_c2r1,noSound_c2r2,noSound_c2r3,noSound_c2r4,noSound_c2r5,noSound_c2r6];
         playerNameCollection = new <TextField>[playerName_c1r1,playerName_c1r2,playerName_c1r3,playerName_c1r4,playerName_c1r5,playerName_c1r6,playerName_c2r1,playerName_c2r2,playerName_c2r3,playerName_c2r4,playerName_c2r5,playerName_c2r6];
         speakAnimationCollection = new <SpeakAnimation>[speakAnimation_c1r1,speakAnimation_c1r2,speakAnimation_c1r3,speakAnimation_c1r4,speakAnimation_c1r5,speakAnimation_c1r6,speakAnimation_c2r1,speakAnimation_c2r2,speakAnimation_c2r3,speakAnimation_c2r4,speakAnimation_c2r5,speakAnimation_c2r6];
         rankBadgesCollection = new <BadgeComponent>[rankBadge_c1r1,rankBadge_c1r2,rankBadge_c1r3,rankBadge_c1r4,rankBadge_c1r5,rankBadge_c1r6,rankBadge_c2r1,rankBadge_c2r2,rankBadge_c2r3,rankBadge_c2r4,rankBadge_c2r5,rankBadge_c2r6];
         squadCollection = new <BattleAtlasSprite>[squad_c1r1,squad_c1r2,squad_c1r3,squad_c1r4,squad_c1r5,squad_c1r6,squad_c2r1,squad_c2r2,squad_c2r3,squad_c2r4,squad_c2r5,squad_c2r6];
         squadStatusCollection = new <SquadInviteStatusView>[squadStatus_c1r1,squadStatus_c1r2,squadStatus_c1r3,squadStatus_c1r4,squadStatus_c1r5,squadStatus_c1r6,squadStatus_c2r1,squadStatus_c2r2,squadStatus_c2r3,squadStatus_c2r4,squadStatus_c2r5,squadStatus_c2r6];
         vehicleActionMarkerCollection = new <BattleAtlasSprite>[vehicleActionMarker_c1r1,vehicleActionMarker_c1r2,vehicleActionMarker_c1r3,vehicleActionMarker_c1r4,vehicleActionMarker_c1r5,vehicleActionMarker_c1r6,vehicleActionMarker_c2r1,vehicleActionMarker_c2r2,vehicleActionMarker_c2r3,vehicleActionMarker_c2r4,vehicleActionMarker_c2r5,vehicleActionMarker_c2r6];
         vehicleIconCollection = new <BattleAtlasSprite>[vehicleIcon_c1r1,vehicleIcon_c1r2,vehicleIcon_c1r3,vehicleIcon_c1r4,vehicleIcon_c1r5,vehicleIcon_c1r6,vehicleIcon_c2r1,vehicleIcon_c2r2,vehicleIcon_c2r3,vehicleIcon_c2r4,vehicleIcon_c2r5,vehicleIcon_c2r6];
         vehicleLevelCollection = new <BattleAtlasSprite>[vehicleLevel_c1r1,vehicleLevel_c1r2,vehicleLevel_c1r3,vehicleLevel_c1r4,vehicleLevel_c1r5,vehicleLevel_c1r6,vehicleLevel_c2r1,vehicleLevel_c2r2,vehicleLevel_c2r3,vehicleLevel_c2r4,vehicleLevel_c2r5,vehicleLevel_c2r6];
         vehicleNameCollection = new <TextField>[vehicleName_c1r1,vehicleName_c1r2,vehicleName_c1r3,vehicleName_c1r4,vehicleName_c1r5,vehicleName_c1r6,vehicleName_c2r1,vehicleName_c2r2,vehicleName_c2r3,vehicleName_c2r4,vehicleName_c2r5,vehicleName_c2r6];
         vehicleTypeCollection = new <BattleAtlasSprite>[vehicleType_c1r1,vehicleType_c1r2,vehicleType_c1r3,vehicleType_c1r4,vehicleType_c1r5,vehicleType_c1r6,vehicleType_c2r1,vehicleType_c2r2,vehicleType_c2r3,vehicleType_c2r4,vehicleType_c2r5,vehicleType_c2r6];
         testerBackCollection = new <BattleAtlasSprite>[testerBack_c1r1,testerBack_c1r2,testerBack_c1r3,testerBack_c1r4,testerBack_c1r5,testerBack_c1r6,testerBack_c2r1,testerBack_c2r2,testerBack_c2r3,testerBack_c2r4,testerBack_c2r5,testerBack_c2r6];
         icoTesterCollection = new <BattleAtlasSprite>[icoTester_c1r1,icoTester_c1r2,icoTester_c1r3,icoTester_c1r4,icoTester_c1r5,icoTester_c1r6,icoTester_c2r1,icoTester_c2r2,icoTester_c2r3,icoTester_c2r4,icoTester_c2r5,icoTester_c2r6];
         this.setTableImages();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IDisposable = null;
         for each(_loc1_ in this.resurrectTimerCollection)
         {
            _loc1_.dispose();
         }
         this.resurrectTimerCollection.length = 0;
         this.resurrectTimerCollection = null;
         this.resurrectTimer_c2r6 = null;
         this.resurrectTimer_c2r5 = null;
         this.resurrectTimer_c2r4 = null;
         this.resurrectTimer_c2r3 = null;
         this.resurrectTimer_c2r2 = null;
         this.resurrectTimer_c2r1 = null;
         this.resurrectTimer_c1r6 = null;
         this.resurrectTimer_c1r5 = null;
         this.resurrectTimer_c1r4 = null;
         this.resurrectTimer_c1r3 = null;
         this.resurrectTimer_c1r2 = null;
         this.resurrectTimer_c1r1 = null;
         super.onDispose();
      }
      
      override protected function setTableImages() : void
      {
         leftFrag.imageName = BATTLEATLAS.WT_STATS_TABLE_FRAGS;
         leftPlatoon.imageName = BATTLEATLAS.STATS_TABLE_PLATOON;
         App.utils.commons.flipHorizontal(leftFrag);
         rightFrag.imageName = BATTLEATLAS.WT_STATS_TABLE_FRAGS;
         rightPlatoon.imageName = BATTLEATLAS.STATS_TABLE_PLATOON;
      }
      
      override public function get numRows() : int
      {
         return NUM_ROWS;
      }
   }
}
