package net.wg.gui.battle.views.stats.fullStats
{
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   import net.wg.data.constants.PlayerStatus;
   import net.wg.data.constants.UserTags;
   import net.wg.gui.battle.battleloading.BattleLoadingHelper;
   import net.wg.gui.battle.views.stats.StatsUserProps;
   import net.wg.gui.battle.views.stats.fullStats.interfaces.IStatsTableItemHolderBase;
   import net.wg.gui.components.dogtag.VO.DogTagVO;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class StatsTableItemHolderBase implements IStatsTableItemHolderBase, IDisposable
   {
       
      
      protected var statsItem:StatsTableItemBase = null;
      
      protected var data:DAAPIVehicleInfoVO = null;
      
      protected var activePlayerData:DAAPIVehicleInfoVO = null;
      
      protected var isCurrPlayer:Boolean = false;
      
      protected var userProps:StatsUserProps = null;
      
      protected var isRenderingRequired:Boolean;
      
      private var _isDisposed:Boolean = false;
      
      private var _isRenderingAvailable:Boolean;
      
      public function StatsTableItemHolderBase(param1:StatsTableItemBase)
      {
         super();
         this.statsItem = param1;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed && App.instance)
         {
            App.utils.asserter.assert(!this._isDisposed,"StatsItemHolder already disposed!");
         }
         this._isDisposed = true;
         this.onDispose();
      }
      
      public function getVehicleID() : Number
      {
         return this.data.vehicleID;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setActivePlayerData(param1:DAAPIVehicleInfoVO) : void
      {
         this.activePlayerData = param1;
         if(this._isRenderingAvailable)
         {
            this.vehicleDataSync();
         }
         else
         {
            this.isRenderingRequired = true;
         }
      }
      
      public function setDAAPIVehicleData(param1:DAAPIVehicleInfoVO) : void
      {
         this.data = param1;
         if(this._isRenderingAvailable)
         {
            this.vehicleDataSync();
         }
         else
         {
            this.isRenderingRequired = true;
         }
      }
      
      public function showDogTag(param1:DogTagVO) : void
      {
         this.statsItem.setShowDogTag(param1 != null);
      }
      
      public function updateColorBlind() : void
      {
         if(this.containsData)
         {
            this.statsItem.updateColorBlind();
            this.updateVehicleType();
         }
      }
      
      protected function vehicleDataSync() : void
      {
         if(this.data)
         {
            this.statsItem.setVehicleName(this.data.vehicleName);
            this.statsItem.setIsIGR(this.data.isIGR);
            this.statsItem.setBadge(this.data.badgeVO,this.data.hasSelectedBadge);
            this.statsItem.setFrags(this.data.frags);
            this.updateVehicleType();
            this.applyVehicleStatus();
            this.applyPlayerStatus();
            this.applyUserTags();
            this.updateUserProps();
            this.statsItem.setSuffixBadge(this.data.suffixBadgeType);
            this.statsItem.setSuffixBadgeStrip(this.data.suffixBadgeStripType);
         }
         else
         {
            this.statsItem.reset();
         }
      }
      
      protected function applyVehicleStatus() : void
      {
         this.statsItem.setIsDead(!this.data.isAlive());
         this.statsItem.setIsOffline(!this.data.isReady());
      }
      
      protected function applyPlayerStatus() : void
      {
         var _loc1_:uint = this.data.playerStatus;
         this.statsItem.setIsTeamKiller(this.data.isTeamKiller());
         this.statsItem.setIsSquadPersonal(this.data.isSquadPersonal());
         this.statsItem.setIsSelected(PlayerStatus.isSelected(_loc1_));
      }
      
      protected function applyUserTags() : void
      {
         this.isCurrPlayer = UserTags.isCurrentPlayer(this.data.userTags);
         this.statsItem.setIsCurrentPlayer(this.isCurrPlayer);
      }
      
      protected function updateUserProps() : void
      {
         if(!this.userProps)
         {
            this.userProps = new StatsUserProps(this.data.playerName,this.data.playerFakeName,this.data.clanAbbrev,this.data.region,0,this.data.userTags);
         }
         else
         {
            this.userProps.userName = this.data.playerName;
            this.userProps.fakeName = this.data.playerFakeName;
            this.userProps.clanAbbrev = this.data.clanAbbrev;
            this.userProps.region = this.data.region;
            this.userProps.tags = this.data.userTags;
         }
         this.statsItem.setPlayerName(this.userProps);
      }
      
      protected function updateVehicleType() : void
      {
         var _loc1_:String = BattleLoadingHelper.instance.getVehicleTypeIconId(this.data);
         if(_loc1_)
         {
            this.statsItem.setVehicleType(_loc1_);
         }
      }
      
      protected function onDispose() : void
      {
         this.statsItem.dispose();
         if(this.userProps)
         {
            this.userProps.dispose();
            this.userProps = null;
         }
         this.statsItem = null;
         this.activePlayerData = null;
         this.data = null;
      }
      
      public function get containsData() : Boolean
      {
         return this.data != null;
      }
      
      public function get isSelected() : Boolean
      {
         return Boolean(this.data) ? Boolean(PlayerStatus.isSelected(this.data.playerStatus)) : Boolean(false);
      }
      
      public function set isRenderingAvailable(param1:Boolean) : void
      {
         this._isRenderingAvailable = param1;
         if(param1 && this.isRenderingRequired)
         {
            this.isRenderingRequired = false;
            this.vehicleDataSync();
         }
      }
   }
}
