package net.wg.gui.battle.ranked.stats.components.playersPanel.list
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.data.constants.generated.PLAYERS_PANEL_STATE;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.stats.playersPanel.events.ChatCommandItemEvent;
   import net.wg.gui.battle.components.stats.playersPanel.list.BasePlayersPanelListItem;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.constants.PlayersPanelInvalidationType;
   import net.wg.gui.battle.ranked.stats.components.playersPanel.interfaces.IRankedPlayersPanelListItem;
   import net.wg.gui.battle.views.stats.constants.SquadInvalidationType;
   
   public class RankedPlayersPanelListItem extends BasePlayersPanelListItem implements IRankedPlayersPanelListItem
   {
      
      private static const RANK_ICON_AREA_WIDTH:int = 24;
      
      private static const RANK_ICON_WIDTH:int = 22;
      
      private static const RANK_ICON_OFFSET:int = 3;
      
      private static const DOG_TAG_WIDTH:int = 22;
      
      private static const DOG_TAG_OFFSET:int = -3;
      
      private static const SQUAD_ICON_WIDTH:int = 22;
      
      private static const SQUAD_ICON_OFFSET:int = 5;
      
      private static const NOSOUND_ICON_SQUAD_Y_OFFSET:int = 4;
       
      
      public var rankIcon:BattleAtlasSprite = null;
      
      public var squadIcon:BattleAtlasSprite = null;
      
      public var noSoundIcon:BattleAtlasSprite = null;
      
      private var _level:int;
      
      private var _division:int;
      
      private var _isGroup:Boolean;
      
      private var _isLeftAligned:Boolean = true;
      
      private var _isSquadPersonal:Boolean = false;
      
      private var _squadIndex:int = 0;
      
      private var _hasActiveCommand:Boolean = false;
      
      private var _voiceChatConnected:Boolean = true;
      
      private var _noSoundIconOriginalY:int = -1;
      
      private var _noSoundIconSquadY:int = -1;
      
      public function RankedPlayersPanelListItem()
      {
         super();
         maxPlayerNameWidth = WIDTH - ICONS_AREA_WIDTH - vehicleTF.width - fragsTF.width - RANK_ICON_AREA_WIDTH - SQUAD_ICON_WIDTH;
         this.rankIcon.mouseEnabled = this.rankIcon.mouseChildren = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.noSoundIcon.visible = false;
         this._noSoundIconOriginalY = this.noSoundIcon.y;
         this._noSoundIconSquadY = this._noSoundIconOriginalY + NOSOUND_ICON_SQUAD_Y_OFFSET;
         this.rankIcon.mouseEnabled = this.rankIcon.mouseChildren = false;
         chatCommandState.addEventListener(ChatCommandItemEvent.ACTIVE_COMMAND_CHANGED,this.onActiveCommandChangedHandler);
      }
      
      override protected function draw() : void
      {
         var _loc1_:Function = null;
         var _loc2_:Boolean = false;
         var _loc3_:Function = null;
         var _loc4_:Boolean = false;
         super.draw();
         if(isInvalid(PlayersPanelInvalidationType.RANK_CHANGED))
         {
            this.rankIcon.visible = this._level > -1 || this._division > -1;
            if(this.rankIcon.visible)
            {
               _loc1_ = !!this._isGroup ? BATTLEATLAS.getRBRanksGroupIcon : BATTLEATLAS.getRBRankIcon;
               this.rankIcon.imageName = _loc1_(this._division.toString(),this._level.toString());
            }
         }
         if(isInvalid(SquadInvalidationType.SQUAD_INDEX))
         {
            _loc2_ = this._squadIndex > 0 && !dogTag.visible;
            this.updateSquadIconVisibility(_loc2_);
            if(_loc2_)
            {
               _loc3_ = !!this._isSquadPersonal ? BATTLEATLAS.squad_gold : BATTLEATLAS.squad_silver;
               this.squadIcon.imageName = _loc3_(this._squadIndex.toString());
            }
         }
         if(isInvalid(PlayersPanelInvalidationType.VOICE_CHAT_STATUS_CHANGED))
         {
            _loc4_ = state > PLAYERS_PANEL_STATE.HIDDEN && !this._voiceChatConnected;
            if(_loc4_)
            {
               this.noSoundIcon.imageName = BATTLEATLAS.ICON_NO_SOUND;
               this.updateNoSoundIconY();
            }
            this.noSoundIcon.visible = _loc4_;
         }
      }
      
      override protected function onDispose() : void
      {
         chatCommandState.removeEventListener(ChatCommandItemEvent.ACTIVE_COMMAND_CHANGED,this.onActiveCommandChangedHandler);
         this.rankIcon = null;
         this.squadIcon = null;
         this.noSoundIcon = null;
         super.onDispose();
      }
      
      override protected function updateDogTag() : void
      {
         dogTag.visible = true;
         this.updateSquadIconVisibility(false);
      }
      
      override protected function updatePositionsRight() : void
      {
         x = -(fragsTF.x + fragsTF.width + RANK_ICON_WIDTH + DOG_TAG_WIDTH ^ 0);
         this.rankIcon.x = fragsTF.x + fragsTF.width - RANK_ICON_OFFSET ^ 0;
         dogTag.x = this.rankIcon.x + RANK_ICON_WIDTH + DOG_TAG_OFFSET;
         this.noSoundIcon.x = this.squadIcon.x = this.rankIcon.x + SQUAD_ICON_WIDTH + SQUAD_ICON_OFFSET;
      }
      
      override protected function updatePositionsLeft() : void
      {
         x = -(fragsTF.x - RANK_ICON_WIDTH - DOG_TAG_WIDTH ^ 0);
         this.rankIcon.x = fragsTF.x - RANK_ICON_WIDTH + RANK_ICON_OFFSET ^ 0;
         this.noSoundIcon.x = this.squadIcon.x = this.rankIcon.x - SQUAD_ICON_WIDTH;
      }
      
      override public function isSquadPersonal() : Boolean
      {
         return this._isSquadPersonal;
      }
      
      public function setRankIcon(param1:int, param2:int, param3:Boolean) : void
      {
         if(this._level == param2 && this._division == param1)
         {
            return;
         }
         this._level = param2;
         this._division = param1;
         this._isGroup = param3;
         invalidate(PlayersPanelInvalidationType.RANK_CHANGED);
      }
      
      override public function setChatCommandVisibility(param1:Boolean) : void
      {
         super.setChatCommandVisibility(param1);
      }
      
      override protected function initializeRightAligned(param1:Boolean) : void
      {
         this._isLeftAligned = !param1;
         invalidateState();
      }
      
      public function setSquad(param1:Boolean, param2:int) : void
      {
         if(this._isSquadPersonal == param1 && this._squadIndex == param2)
         {
            return;
         }
         this._isSquadPersonal = param1;
         this._squadIndex = param2;
         invalidate(SquadInvalidationType.SQUAD_INDEX);
         invalidate(PlayersPanelInvalidationType.PLAYER_SCHEME);
         invalidate(PlayersPanelInvalidationType.VOICE_CHAT_STATUS_CHANGED);
      }
      
      public function setVoiceChatConnected(param1:Boolean) : void
      {
         if(this._voiceChatConnected == param1)
         {
            return;
         }
         this._voiceChatConnected = param1;
         invalidate(PlayersPanelInvalidationType.VOICE_CHAT_STATUS_CHANGED);
      }
      
      private function updateNoSoundIconY() : void
      {
         this.noSoundIcon.y = !!this.squadIcon.visible ? Number(this._noSoundIconSquadY) : Number(this._noSoundIconOriginalY);
      }
      
      private function updateSquadIconVisibility(param1:Boolean) : void
      {
         this.squadIcon.visible = param1;
         this.updateNoSoundIconY();
      }
      
      private function onActiveCommandChangedHandler(param1:ChatCommandItemEvent) : void
      {
         this._hasActiveCommand = param1.isActiveCommandVisible;
      }
   }
}
