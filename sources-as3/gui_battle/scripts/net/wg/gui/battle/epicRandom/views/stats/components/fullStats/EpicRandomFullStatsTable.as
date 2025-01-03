package net.wg.gui.battle.epicRandom.views.stats.components.fullStats
{
   import net.wg.data.constants.ImageCacheTypes;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.buttons.BattleButton;
   import net.wg.gui.battle.epicRandom.battleloading.components.EpicRandomStatsTable;
   import net.wg.gui.components.controls.Image;
   
   public class EpicRandomFullStatsTable extends EpicRandomStatsTable
   {
       
      
      public var squadAcceptBt:BattleButton = null;
      
      public var squadAddBt:BattleButton = null;
      
      public var background:Image = null;
      
      public var leftTank:BattleAtlasSprite = null;
      
      public var leftFrag:BattleAtlasSprite = null;
      
      public var leftPlatoon:BattleAtlasSprite = null;
      
      public var rightFrag:BattleAtlasSprite = null;
      
      public var rightTank:BattleAtlasSprite = null;
      
      public var rightPlatoon:BattleAtlasSprite = null;
      
      public function EpicRandomFullStatsTable()
      {
         super();
         this.background.cacheType = ImageCacheTypes.NOT_USE_CACHE;
         this.background.source = RES_ICONS.MAPS_ICONS_BATTLE_STATS_TAB_BG;
         this.leftTank.imageName = BATTLEATLAS.STATS_TABLE_TANK;
         this.leftFrag.imageName = BATTLEATLAS.STATS_TABLE_FRAGS;
         this.leftPlatoon.imageName = BATTLEATLAS.STATS_TABLE_PLATOON;
         App.utils.commons.flipHorizontal(this.leftFrag);
         this.rightTank.imageName = BATTLEATLAS.STATS_TABLE_TANK;
         this.rightFrag.imageName = BATTLEATLAS.STATS_TABLE_FRAGS;
         this.rightPlatoon.imageName = BATTLEATLAS.STATS_TABLE_PLATOON;
         App.utils.commons.flipHorizontal(this.rightTank);
      }
      
      override protected function onDispose() : void
      {
         this.squadAcceptBt.dispose();
         this.squadAddBt.dispose();
         this.squadAcceptBt = null;
         this.squadAddBt = null;
         this.background.dispose();
         this.background = null;
         this.leftTank = null;
         this.leftFrag = null;
         this.leftPlatoon = null;
         this.rightFrag = null;
         this.rightTank = null;
         this.rightPlatoon = null;
         super.onDispose();
      }
   }
}
