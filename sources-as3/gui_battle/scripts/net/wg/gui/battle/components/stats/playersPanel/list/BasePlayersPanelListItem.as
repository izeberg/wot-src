package net.wg.gui.battle.components.stats.playersPanel.list
{
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.data.constants.generated.PLAYERS_PANEL_STATE;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.components.PrestigeLevel;
   import net.wg.gui.battle.components.stats.playersPanel.ChatCommandItemComponent;
   import net.wg.gui.battle.components.stats.playersPanel.SpottedIndicator;
   import net.wg.gui.battle.components.stats.playersPanel.events.PlayersPanelItemEvent;
   import net.wg.gui.battle.components.stats.playersPanel.interfaces.IPlayersPanelListItem;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.constants.PlayersPanelInvalidationType;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.list.PlayersPanelDynamicSquad;
   import net.wg.gui.battle.random.views.stats.constants.VehicleActions;
   import net.wg.gui.battle.views.stats.SpeakAnimation;
   import net.wg.gui.battle.views.stats.constants.PlayerStatusSchemeName;
   import net.wg.gui.components.controls.BadgeComponent;
   import net.wg.gui.components.controls.DogTagIcon;
   import net.wg.gui.components.controls.VO.BadgeVisualVO;
   import net.wg.infrastructure.interfaces.IColorScheme;
   import net.wg.infrastructure.interfaces.IUserProps;
   import net.wg.utils.ICommons;
   import scaleform.gfx.TextFieldEx;
   
   public class BasePlayersPanelListItem extends BattleUIComponent implements IPlayersPanelListItem
   {
      
      protected static const ICONS_AREA_WIDTH:int = 63;
      
      protected static const WIDTH:int = 339;
      
      protected static const BADGE_OFFSET:int = 5;
      
      private static const DOG_TAG_OFFSET:int = -5;
      
      private static const ALT_TEXT_COLOR:uint = 16777215;
      
      private static const DEAD_ALT_TEXT_ALPHA:Number = 0.73;
      
      private static const PLAYER_NAME_MARGIN:int = 8;
      
      private static const VEHICLE_TF_RIGHT_X:int = -WIDTH + ICONS_AREA_WIDTH;
      
      private static const VEHICLE_TF_LEFT_X:int = WIDTH - ICONS_AREA_WIDTH;
      
      private static const UNKNOWN_VEHICLE_LEVEL:int = -1;
      
      private static const BADGE_ICON_AREA_WIDTH:int = 24;
      
      private static const BADGE_ALPHA:int = 1;
      
      private static const BADGE_ALPHA_NOT_ACTIVE:Number = 0.7;
      
      private static const CHAT_COMMAND_RIGHT_ICON_OFFSET:int = -79;
      
      private static const CHAT_COMMAND_LEFT_ICON_OFFSET:int = 79;
      
      private static const CHAT_COMMAND_LEFT_OFFSET:int = 36;
      
      private static const VEHICLE_ICON_LEFT_OFFSET:int = -8;
      
      private static const VEHICLE_ICON_RIGHT_OFFSET:int = 8;
      
      private static const VEHICLE_LEVEL_LEFT_OFFSET:int = 19;
      
      private static const VEHICLE_LEVEL_RIGHT_OFFSET:int = -32;
      
      private static const SPEAK_ANIMATION_LEFT_OFFSET:int = -41;
      
      private static const SPEAK_ANIMATION_RIGHT_OFFSET:int = -83;
      
      private static const SPOTTED_INDICATOR_LEFT_OFFSET:int = 0;
      
      private static const SPOTTED_INDICATOR_RIGHT_OFFSET:int = 4;
      
      private static const HP_BAR_PRESTIGE_LEFT_OFFSET:int = -30;
      
      private static const HP_BAR_PRESTIGE_RIGHT_OFFSET:int = 36;
      
      private static const ACTION_MARKER_LEFT_OFFSET:int = 30;
      
      private static const ACTION_MARKER_RIGHT_OFFSET:int = -25;
      
      private static const PRESTIGE_LEVEL_DEFAULT_ALPHA:Number = 1;
      
      private static const PRESTIGE_LEVEL_DEAD_ALPHA:Number = 0.5;
       
      
      public var dynamicSquad:PlayersPanelDynamicSquad;
      
      public var fragsTF:TextField = null;
      
      public var playerNameFullTF:TextField = null;
      
      public var playerNameCutTF:TextField = null;
      
      public var vehicleTF:TextField = null;
      
      public var badge:BadgeComponent = null;
      
      public var dogTag:DogTagIcon = null;
      
      public var hpBarPlayersPanelListItem:HPBarPlayersPanelListItem = null;
      
      public var icoIGR:BattleAtlasSprite = null;
      
      public var vehicleLevel:BattleAtlasSprite = null;
      
      public var vehicleIcon:BattleAtlasSprite = null;
      
      public var mute:BattleAtlasSprite = null;
      
      public var speakAnimation:SpeakAnimation = null;
      
      public var selfBg:BattleAtlasSprite = null;
      
      public var normAltBg:BattleAtlasSprite = null;
      
      public var bg:BattleAtlasSprite = null;
      
      public var deadAltBg:BattleAtlasSprite = null;
      
      public var deadBg:BattleAtlasSprite = null;
      
      public var actionMarker:BattleAtlasSprite = null;
      
      public var hit:Sprite = null;
      
      public var disableCommunication:BattleAtlasSprite = null;
      
      public var chatCommandState:ChatCommandItemComponent = null;
      
      public var spottedIndicator:SpottedIndicator = null;
      
      public var prestigeLevel:PrestigeLevel = null;
      
      protected var maxPlayerNameWidth:uint = 0;
      
      protected var isAlive:Boolean = true;
      
      protected var isMute:Boolean = false;
      
      protected var isSelected:Boolean = false;
      
      protected var hasBadge:Boolean = false;
      
      protected var userProps:IUserProps = null;
      
      private var _holderItemID:int = -1;
      
      private var _state:int = -1;
      
      private var _vehicleName:String = null;
      
      private var _frags:int = 0;
      
      private var _isSpeaking:Boolean = false;
      
      private var _isOffline:Boolean = false;
      
      private var _isTeamKiller:Boolean = false;
      
      private var _isIGR:Boolean = false;
      
      private var _vehicleImage:String = null;
      
      private var _vehicleLevel:int = 0;
      
      private var _isCurrentPlayer:Boolean = false;
      
      private var _isRightAligned:Boolean = false;
      
      private var _isIgnoredTmp:Boolean = false;
      
      private var _badgeVO:BadgeVisualVO = null;
      
      private var _showDogTag:Boolean = false;
      
      private var _commons:ICommons = null;
      
      private var _isHpBarsVisible:Boolean = false;
      
      private var _hpSettingValue:uint = 0;
      
      private var _originalTFAlpha:Number = 0;
      
      private var _vehicleIconDefaultX:int = 0;
      
      public function BasePlayersPanelListItem()
      {
         super();
         this._commons = App.utils.commons;
         this._vehicleIconDefaultX = this.vehicleIcon.x;
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         removeEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         removeEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
         this.speakAnimation.dispose();
         this.disableCommunication = null;
         if(this.dynamicSquad)
         {
            this.dynamicSquad.dispose();
            this.dynamicSquad = null;
         }
         this.userProps = null;
         this.fragsTF = null;
         this.chatCommandState.dispose();
         this.chatCommandState = null;
         this.spottedIndicator.dispose();
         this.spottedIndicator = null;
         this.playerNameFullTF = null;
         this.playerNameCutTF = null;
         this.vehicleTF = null;
         this.icoIGR = null;
         this.vehicleLevel = null;
         this.vehicleIcon = null;
         this.mute = null;
         this.speakAnimation = null;
         this.selfBg = null;
         this.normAltBg = null;
         this.bg = null;
         this.deadAltBg = null;
         this.deadBg = null;
         this.actionMarker = null;
         hitArea = null;
         this.hit = null;
         this.hpBarPlayersPanelListItem.dispose();
         this.hpBarPlayersPanelListItem = null;
         this.badge.dispose();
         this.badge = null;
         this.prestigeLevel.dispose();
         this.prestigeLevel = null;
         if(this.dogTag)
         {
            this.dogTag.dispose();
            this.dogTag = null;
         }
         this._badgeVO = null;
         this._commons = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.fragsTF.mouseEnabled = false;
         this.playerNameFullTF.mouseEnabled = false;
         this.playerNameCutTF.mouseEnabled = false;
         this.vehicleTF.mouseEnabled = false;
         this.icoIGR.mouseEnabled = false;
         this.vehicleLevel.mouseEnabled = false;
         this.vehicleLevel.isCentralizeByX = true;
         this.vehicleIcon.mouseEnabled = false;
         this.mute.mouseEnabled = false;
         this.speakAnimation.mouseEnabled = false;
         this.speakAnimation.mouseChildren = false;
         this.actionMarker.mouseEnabled = false;
         this.badge.mouseEnabled = this.badge.mouseChildren = false;
         if(this.dogTag)
         {
            this.dogTag.visible = false;
         }
         this.chatCommandState.mouseEnabled = false;
         this.spottedIndicator.mouseEnabled = false;
         TextFieldEx.setNoTranslate(this.fragsTF,true);
         TextFieldEx.setNoTranslate(this.playerNameFullTF,true);
         TextFieldEx.setNoTranslate(this.playerNameCutTF,true);
         TextFieldEx.setNoTranslate(this.vehicleTF,true);
         hitArea = this.hit;
         addEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         addEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         addEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
         this.icoIGR.visible = false;
         this.icoIGR.imageName = BATTLEATLAS.ICO_IGR;
         this.mute.visible = false;
         this.mute.imageName = BATTLEATLAS.STATS_MUTE;
         if(this.disableCommunication)
         {
            this.disableCommunication.visible = false;
            this.disableCommunication.imageName = BATTLEATLAS.ICON_TOXIC_CHAT_OFF;
         }
         this.bg.imageName = BATTLEATLAS.PLAYERS_PANEL_BG;
         this.normAltBg.visible = false;
         this.normAltBg.imageName = BATTLEATLAS.PLAYERS_PANEL_NORM_ALT_BG;
         this.deadAltBg.visible = false;
         this.deadAltBg.imageName = BATTLEATLAS.PLAYERS_PANEL_DEAD_ALT_BG;
         this.selfBg.visible = false;
         this.selfBg.imageName = BATTLEATLAS.PLAYERS_PANEL_SELF_BG;
         this.deadBg.visible = false;
         this.deadBg.imageName = BATTLEATLAS.PLAYERS_PANEL_DEAD_BG;
         this.selfBg.mouseEnabled = this.selfBg.mouseChildren = false;
         this.deadBg.mouseEnabled = this.deadBg.mouseChildren = false;
         this.bg.mouseEnabled = this.bg.mouseChildren = false;
         this._originalTFAlpha = this.vehicleTF.alpha;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._showDogTag && isInvalid(PlayersPanelInvalidationType.DOG_TAG_CHANGED))
         {
            this.updateDogTag();
         }
         if(isInvalid(PlayersPanelInvalidationType.BADGE_CHANGED))
         {
            if(this.hasBadge)
            {
               this.badge.setData(this._badgeVO);
            }
            this.badge.visible = this.hasBadge;
         }
         if(isInvalid(PlayersPanelInvalidationType.VEHILCE_NAME))
         {
            this._commons.truncateTextFieldText(this.vehicleTF,this._vehicleName);
         }
         if(isInvalid(PlayersPanelInvalidationType.FRAGS))
         {
            this.fragsTF.text = Boolean(this._frags) ? this._frags.toString() : Values.EMPTY_STR;
         }
         if(isInvalid(PlayersPanelInvalidationType.MUTE))
         {
            this.mute.visible = this.isMute;
            this.speakAnimation.mute = this.isMute;
            if(!this.isMute && this._isSpeaking)
            {
               this.speakAnimation.speaking = true;
            }
            if(this.disableCommunication)
            {
               this.disableCommunication.visible = this._isIgnoredTmp;
            }
         }
         if(!this.isMute && isInvalid(PlayersPanelInvalidationType.IS_SPEAKING))
         {
            this.speakAnimation.speaking = this._isSpeaking;
         }
         if(isInvalid(PlayersPanelInvalidationType.SELECTED))
         {
            this.selfBg.visible = this.isSelected;
         }
         if(isInvalid(PlayersPanelInvalidationType.ALIVE))
         {
            this.bg.visible = this.isAlive && !this._isHpBarsVisible;
            this.deadBg.visible = !this.isAlive && !this._isHpBarsVisible;
            this.normAltBg.visible = this.isAlive && this._isHpBarsVisible;
            this.deadAltBg.visible = !this.isAlive && this._isHpBarsVisible;
            this.playerNameFullTF.alpha = this.fragsTF.alpha = this.playerNameCutTF.alpha = this.vehicleTF.alpha = !!this.deadAltBg.visible ? Number(DEAD_ALT_TEXT_ALPHA) : Number(this._originalTFAlpha);
         }
         if(isInvalid(PlayersPanelInvalidationType.PLAYER_SCHEME))
         {
            this.badge.alpha = this._isOffline || !this.isAlive ? Number(BADGE_ALPHA_NOT_ACTIVE) : Number(BADGE_ALPHA);
            if(this.dogTag)
            {
               this.dogTag.alpha = this.badge.alpha;
            }
            this.updateColors();
         }
         if(isInvalid(PlayersPanelInvalidationType.IGR_CHANGED))
         {
            this.icoIGR.visible = this._isIGR;
         }
         if(isInvalid(InvalidationType.STATE))
         {
            this.applyState();
         }
         if(isInvalid(PlayersPanelInvalidationType.HP_BAR_VISIBILITY))
         {
            this.hpBarPlayersPanelListItem.visible = this._isHpBarsVisible && this.isAlive;
         }
      }
      
      public function getDynamicSquad() : PlayersPanelDynamicSquad
      {
         return null;
      }
      
      public function getIsIgnoredTmp() : Boolean
      {
         return this._isIgnoredTmp;
      }
      
      public function getPlayerNameFullWidth() : uint
      {
         return (this.playerNameFullTF.textWidth | 0) + PLAYER_NAME_MARGIN;
      }
      
      public function isIgnoredTmp(param1:Boolean) : void
      {
         if(this._isIgnoredTmp == param1 || this.disableCommunication == null)
         {
            return;
         }
         this._isIgnoredTmp = param1;
         invalidate(PlayersPanelInvalidationType.MUTE);
      }
      
      public function isSquadPersonal() : Boolean
      {
         return false;
      }
      
      public function setBadge(param1:BadgeVisualVO, param2:Boolean) : void
      {
         if(this._badgeVO == null || !this._badgeVO.isEquals(param1) && this.hasBadge != param2)
         {
            this._badgeVO = param1;
            this.hasBadge = param2;
            invalidate(PlayersPanelInvalidationType.BADGE_CHANGED);
         }
      }
      
      public function setChatCommand(param1:String, param2:uint) : void
      {
         this.chatCommandState.setActiveChatCommand(param1,param2);
      }
      
      public function setChatCommandVisibility(param1:Boolean) : void
      {
         this.chatCommandState.setChatCommandVisibility(param1);
      }
      
      public function setFrags(param1:int) : void
      {
         if(this._frags == param1)
         {
            return;
         }
         this._frags = param1;
         invalidate(PlayersPanelInvalidationType.FRAGS);
      }
      
      public function setIsAlive(param1:Boolean) : void
      {
         if(this.isAlive == param1)
         {
            return;
         }
         this.isAlive = param1;
         invalidate(PlayersPanelInvalidationType.ALIVE | PlayersPanelInvalidationType.PLAYER_SCHEME | PlayersPanelInvalidationType.HP_BAR_VISIBILITY);
      }
      
      public function setIsCurrentPlayer(param1:Boolean) : void
      {
         if(this._isCurrentPlayer == param1)
         {
            return;
         }
         this._isCurrentPlayer = param1;
         invalidate(PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      public function setIsIGR(param1:Boolean) : void
      {
         if(this._isIGR == param1)
         {
            return;
         }
         this._isIGR = param1;
         invalidate(PlayersPanelInvalidationType.IGR_CHANGED);
      }
      
      public function setIsInteractive(param1:Boolean) : void
      {
      }
      
      public function setIsInviteShown(param1:Boolean) : void
      {
      }
      
      public function setIsMute(param1:Boolean) : void
      {
         if(this.isMute == param1)
         {
            return;
         }
         this.isMute = param1;
         invalidate(PlayersPanelInvalidationType.MUTE);
      }
      
      public function setIsOffline(param1:Boolean) : void
      {
         if(this._isOffline == param1)
         {
            return;
         }
         this._isOffline = param1;
         invalidate(PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      public function setIsRightAligned(param1:Boolean) : void
      {
         if(this._isRightAligned == param1)
         {
            return;
         }
         this._isRightAligned = param1;
         this.hpBarPlayersPanelListItem.setRightAligned(param1);
         this.initializeRightAligned(param1);
         invalidateState();
      }
      
      public function setIsSelected(param1:Boolean) : void
      {
         if(this.isSelected == param1)
         {
            return;
         }
         this.isSelected = param1;
         invalidate(PlayersPanelInvalidationType.SELECTED);
      }
      
      public function setIsSpeaking(param1:Boolean) : void
      {
         if(this._isSpeaking == param1)
         {
            return;
         }
         this._isSpeaking = param1;
         invalidate(PlayersPanelInvalidationType.IS_SPEAKING);
      }
      
      public function setIsTeamKiller(param1:Boolean) : void
      {
         if(this._isTeamKiller == param1)
         {
            return;
         }
         this._isTeamKiller = param1;
         invalidate(PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      public function setOverrideExInfo(param1:Boolean) : void
      {
         this._isHpBarsVisible = this._hpSettingValue == PLAYERS_PANEL_STATE.ALWAYS_SHOW_HP || param1 && this._hpSettingValue == PLAYERS_PANEL_STATE.SHOW_HP_ON_ALT;
         invalidate(PlayersPanelInvalidationType.HP_BAR_VISIBILITY | PlayersPanelInvalidationType.ALIVE | PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      public function setPanelHPBarVisibilityState(param1:uint) : void
      {
         this._hpSettingValue = param1;
         this._isHpBarsVisible = param1 == PLAYERS_PANEL_STATE.ALWAYS_SHOW_HP;
         invalidate(PlayersPanelInvalidationType.HP_BAR_VISIBILITY | PlayersPanelInvalidationType.ALIVE | PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      public function setPlayerNameFullWidth(param1:uint) : void
      {
         param1 = Math.min(this.maxPlayerNameWidth,param1);
         if(this.playerNameFullTF.width == param1)
         {
            return;
         }
         this.playerNameFullTF.width = param1;
         if(this.userProps)
         {
            this._commons.truncateTextFieldText(this.playerNameCutTF,this.userProps.userName);
            this._commons.formatPlayerName(this.playerNameFullTF,this.userProps,!this._isCurrentPlayer,this._isCurrentPlayer);
         }
         this.updatePositions();
      }
      
      public function setPlayerNameProps(param1:IUserProps) : void
      {
         this.userProps = param1;
         this._commons.truncateTextFieldText(this.playerNameCutTF,this.userProps.userName);
         this._commons.formatPlayerName(this.playerNameFullTF,this.userProps,!this._isCurrentPlayer,this._isCurrentPlayer);
      }
      
      public function setPrestige(param1:int, param2:int) : void
      {
         this.prestigeLevel.markId = param1;
         this.prestigeLevel.level = param2;
      }
      
      public function setSpottedStatus(param1:uint) : void
      {
         this.spottedIndicator.updateSpottedStatus(param1);
      }
      
      public function setState(param1:uint) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         this.applyState();
      }
      
      public function setVehicleAction(param1:uint) : void
      {
         this.actionMarker.imageName = BATTLEATLAS.getVehicleActionMarker(VehicleActions.getActionName(param1));
         this.actionMarker.visible = true;
      }
      
      public function setVehicleHealth(param1:int) : void
      {
         this.hpBarPlayersPanelListItem.updateHP(param1);
      }
      
      public function setVehicleIcon(param1:String) : void
      {
         if(this._vehicleImage == param1)
         {
            return;
         }
         this._vehicleImage = param1;
         this.vehicleIcon.setImageNames(param1,BATTLEATLAS.UNKNOWN);
      }
      
      public function setVehicleLevel(param1:int) : void
      {
         if(this._vehicleLevel == param1 || param1 == UNKNOWN_VEHICLE_LEVEL)
         {
            return;
         }
         this._vehicleLevel = param1;
         this.vehicleLevel.isCentralizeByX = true;
         this.vehicleLevel.imageName = BATTLEATLAS.level(this._vehicleLevel.toString());
      }
      
      public function setVehicleLevelVisible(param1:Boolean) : void
      {
         this.vehicleLevel.visible = param1;
      }
      
      public function setVehicleName(param1:String) : void
      {
         if(this._vehicleName == param1)
         {
            return;
         }
         this._vehicleName = param1;
         invalidate(PlayersPanelInvalidationType.VEHILCE_NAME);
      }
      
      public function showDogTag() : void
      {
         this._showDogTag = true;
         invalidate(PlayersPanelInvalidationType.DOG_TAG_CHANGED);
      }
      
      public function triggerChatCommand(param1:String) : void
      {
         this.chatCommandState.playCommandAnimation(param1);
      }
      
      public function updateColorBlind() : void
      {
         invalidate(PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      protected function getState() : uint
      {
         return this._state;
      }
      
      protected function updateDogTag() : void
      {
         this.dogTag.visible = true;
         this.dynamicSquad.visible = false;
      }
      
      protected function initializeRightAligned(param1:Boolean) : void
      {
      }
      
      protected function updatePositionsLeft() : void
      {
         this.vehicleLevel.x = this.vehicleIcon.x + VEHICLE_LEVEL_LEFT_OFFSET;
         this.speakAnimation.x = this.vehicleIcon.x + SPEAK_ANIMATION_LEFT_OFFSET;
         this.spottedIndicator.x = this.vehicleIcon.x + SPOTTED_INDICATOR_LEFT_OFFSET;
         this.actionMarker.x = this.vehicleIcon.x + ACTION_MARKER_LEFT_OFFSET;
      }
      
      protected function updatePositionsRight() : void
      {
         this.vehicleLevel.x = this.vehicleIcon.x + VEHICLE_LEVEL_RIGHT_OFFSET;
         this.speakAnimation.x = this.vehicleIcon.x + SPEAK_ANIMATION_RIGHT_OFFSET;
         this.spottedIndicator.x = this.vehicleIcon.x + SPOTTED_INDICATOR_RIGHT_OFFSET;
         this.actionMarker.x = this.vehicleIcon.x + ACTION_MARKER_RIGHT_OFFSET;
      }
      
      protected function getOffset() : int
      {
         return 0;
      }
      
      protected function getOffsetVehicleIcon() : int
      {
         return 0;
      }
      
      protected function updatePositions() : void
      {
         var _loc1_:int = 0;
         var _loc3_:int = 0;
         if(this._isRightAligned)
         {
            switch(this._state)
            {
               case PLAYERS_PANEL_STATE.FULL:
                  this.vehicleTF.x = VEHICLE_TF_RIGHT_X;
                  _loc1_ = this.vehicleTF.x + this.vehicleTF.width;
                  this.playerNameFullTF.x = _loc1_;
                  _loc1_ = this.playerNameFullTF.x + this.playerNameFullTF.width + BADGE_OFFSET;
                  this.badge.x = _loc1_;
                  _loc1_ = this.badge.x + BADGE_ICON_AREA_WIDTH;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this.prestigeLevel.x + VEHICLE_ICON_RIGHT_OFFSET;
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x + HP_BAR_PRESTIGE_RIGHT_OFFSET);
                  break;
               case PLAYERS_PANEL_STATE.FULL_NO_BADGES:
                  this.vehicleTF.x = VEHICLE_TF_RIGHT_X;
                  _loc1_ = this.vehicleTF.x + this.vehicleTF.width;
                  this.playerNameFullTF.x = _loc1_;
                  _loc1_ = this.playerNameFullTF.x + this.playerNameFullTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this.prestigeLevel.x + VEHICLE_ICON_RIGHT_OFFSET;
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x + HP_BAR_PRESTIGE_RIGHT_OFFSET);
                  break;
               case PLAYERS_PANEL_STATE.LONG:
               case PLAYERS_PANEL_STATE.LONG_NO_BADGES:
                  this.vehicleTF.x = VEHICLE_TF_RIGHT_X;
                  _loc1_ = this.vehicleTF.x + this.vehicleTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this.prestigeLevel.x + VEHICLE_ICON_RIGHT_OFFSET;
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x + HP_BAR_PRESTIGE_RIGHT_OFFSET);
                  break;
               case PLAYERS_PANEL_STATE.MEDIUM:
                  this.playerNameCutTF.x = VEHICLE_TF_RIGHT_X;
                  _loc1_ = this.playerNameCutTF.x + this.playerNameCutTF.width + BADGE_OFFSET;
                  this.badge.x = _loc1_;
                  _loc1_ = this.badge.x + BADGE_ICON_AREA_WIDTH;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this._vehicleIconDefaultX;
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x);
                  break;
               case PLAYERS_PANEL_STATE.MEDIUM_NO_BADGES:
                  this.playerNameCutTF.x = VEHICLE_TF_RIGHT_X;
                  _loc1_ = this.playerNameCutTF.x + this.playerNameCutTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this._vehicleIconDefaultX;
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x);
                  break;
               case PLAYERS_PANEL_STATE.SHORT:
               case PLAYERS_PANEL_STATE.SHORT_NO_BADGES:
                  this.fragsTF.x = VEHICLE_TF_RIGHT_X;
                  this.vehicleIcon.x = this._vehicleIconDefaultX;
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x);
            }
            if(this.dogTag)
            {
               this.dogTag.x = this.fragsTF.x + this.fragsTF.width + DOG_TAG_OFFSET;
            }
            this.chatCommandState.iconOffset(this.vehicleIcon.x + CHAT_COMMAND_RIGHT_ICON_OFFSET);
            this.chatCommandState.x = 0;
            this.updatePositionsRight();
         }
         else
         {
            switch(this._state)
            {
               case PLAYERS_PANEL_STATE.FULL:
                  _loc1_ = VEHICLE_TF_LEFT_X - this.vehicleTF.width;
                  this.vehicleTF.x = _loc1_ + this.getOffset();
                  _loc1_ = this.vehicleTF.x - this.playerNameFullTF.width - this.getOffset();
                  this.playerNameFullTF.x = _loc1_;
                  _loc1_ = this.playerNameFullTF.x - (BADGE_ICON_AREA_WIDTH + BADGE_OFFSET);
                  this.badge.x = _loc1_;
                  _loc1_ = this.badge.x - this.fragsTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this.prestigeLevel.x + VEHICLE_ICON_LEFT_OFFSET + this.getOffsetVehicleIcon();
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x + HP_BAR_PRESTIGE_LEFT_OFFSET);
                  break;
               case PLAYERS_PANEL_STATE.FULL_NO_BADGES:
                  _loc1_ = VEHICLE_TF_LEFT_X - this.vehicleTF.width;
                  this.vehicleTF.x = _loc1_ + this.getOffset();
                  _loc1_ = this.vehicleTF.x - this.playerNameFullTF.width - this.getOffset();
                  this.playerNameFullTF.x = _loc1_;
                  _loc1_ = this.playerNameFullTF.x - this.fragsTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this.prestigeLevel.x + VEHICLE_ICON_LEFT_OFFSET + this.getOffsetVehicleIcon();
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x + HP_BAR_PRESTIGE_LEFT_OFFSET);
                  break;
               case PLAYERS_PANEL_STATE.LONG:
               case PLAYERS_PANEL_STATE.LONG_NO_BADGES:
                  _loc1_ = VEHICLE_TF_LEFT_X - this.vehicleTF.width;
                  this.vehicleTF.x = _loc1_;
                  _loc1_ = this.vehicleTF.x - this.fragsTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this.prestigeLevel.x + VEHICLE_ICON_LEFT_OFFSET + this.getOffsetVehicleIcon();
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x + HP_BAR_PRESTIGE_LEFT_OFFSET);
                  break;
               case PLAYERS_PANEL_STATE.MEDIUM:
                  _loc1_ = VEHICLE_TF_LEFT_X - this.playerNameCutTF.width;
                  this.playerNameCutTF.x = _loc1_;
                  _loc1_ = this.playerNameCutTF.x - (BADGE_ICON_AREA_WIDTH + BADGE_OFFSET);
                  this.badge.x = _loc1_;
                  _loc1_ = this.badge.x - this.fragsTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this._vehicleIconDefaultX + this.getOffset();
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x);
                  break;
               case PLAYERS_PANEL_STATE.MEDIUM_NO_BADGES:
                  _loc1_ = VEHICLE_TF_LEFT_X - this.playerNameCutTF.width;
                  this.playerNameCutTF.x = _loc1_;
                  _loc1_ = this.playerNameCutTF.x - this.fragsTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this._vehicleIconDefaultX + this.getOffset();
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x);
                  break;
               case PLAYERS_PANEL_STATE.SHORT:
               case PLAYERS_PANEL_STATE.SHORT_NO_BADGES:
                  _loc1_ = VEHICLE_TF_LEFT_X - this.fragsTF.width;
                  this.fragsTF.x = _loc1_;
                  this.vehicleIcon.x = this._vehicleIconDefaultX + this.getOffset();
                  this.hpBarPlayersPanelListItem.setVehicleIconX(this.vehicleIcon.x);
            }
            _loc3_ = this.fragsTF.x - CHAT_COMMAND_LEFT_OFFSET;
            this.chatCommandState.iconOffset(this.vehicleIcon.x - _loc3_ + CHAT_COMMAND_LEFT_ICON_OFFSET);
            this.chatCommandState.x = _loc3_;
            this.updatePositionsLeft();
         }
         var _loc2_:int = -x;
         this.hit.x = _loc2_;
         this.hit.width = !!this._isRightAligned ? Number(WIDTH + _loc2_) : Number(WIDTH - _loc2_);
         this.hpBarPlayersPanelListItem.setParentX(this.x);
      }
      
      protected function updateColors() : void
      {
         var _loc4_:uint = 0;
         var _loc1_:String = PlayerStatusSchemeName.getSchemeNameForVehicle(this._isCurrentPlayer,this.isSquadPersonal(),this._isTeamKiller,!this.isAlive,this._isOffline);
         var _loc2_:IColorScheme = App.colorSchemeMgr.getScheme(_loc1_);
         if(_loc2_)
         {
            this.vehicleIcon.transform.colorTransform = _loc2_.colorTransform;
         }
         this.prestigeLevel.alpha = !!this.isAlive ? Number(PRESTIGE_LEVEL_DEFAULT_ALPHA) : Number(PRESTIGE_LEVEL_DEAD_ALPHA);
         _loc1_ = PlayerStatusSchemeName.getSchemeForVehicleLevel(!this.isAlive);
         _loc2_ = App.colorSchemeMgr.getScheme(_loc1_);
         if(_loc2_)
         {
            this.vehicleLevel.transform.colorTransform = _loc2_.colorTransform;
         }
         _loc1_ = PlayerStatusSchemeName.getSchemeNameForPlayer(this._isCurrentPlayer,this.isSquadPersonal(),this._isTeamKiller,!this.isAlive,this._isOffline);
         _loc2_ = App.colorSchemeMgr.getScheme(_loc1_);
         if(_loc2_)
         {
            _loc4_ = this._isHpBarsVisible && !this._isCurrentPlayer && !this.isSquadPersonal() && !this._isTeamKiller ? uint(ALT_TEXT_COLOR) : uint(_loc2_.rgb);
            this.fragsTF.textColor = this.playerNameFullTF.textColor = this.playerNameCutTF.textColor = this.vehicleTF.textColor = _loc4_;
         }
         var _loc3_:Boolean = App.colorSchemeMgr.getIsColorBlindS();
         this.chatCommandState.updateColors(_loc3_);
         this.hpBarPlayersPanelListItem.updateBarColor(_loc3_);
      }
      
      private function applyState() : void
      {
         switch(this._state)
         {
            case PLAYERS_PANEL_STATE.FULL_NO_BADGES:
            case PLAYERS_PANEL_STATE.FULL:
               this.vehicleTF.visible = true;
               this.prestigeLevel.visible = true;
               this.playerNameFullTF.visible = true;
               this.playerNameCutTF.visible = false;
               this.badge.visible = this._state != PLAYERS_PANEL_STATE.FULL_NO_BADGES;
               break;
            case PLAYERS_PANEL_STATE.LONG_NO_BADGES:
            case PLAYERS_PANEL_STATE.LONG:
               this.vehicleTF.visible = true;
               this.prestigeLevel.visible = true;
               this.playerNameFullTF.visible = false;
               this.playerNameCutTF.visible = false;
               this.badge.visible = false;
               break;
            case PLAYERS_PANEL_STATE.MEDIUM_NO_BADGES:
            case PLAYERS_PANEL_STATE.MEDIUM:
               this.vehicleTF.visible = false;
               this.prestigeLevel.visible = false;
               this.playerNameFullTF.visible = false;
               this.playerNameCutTF.visible = true;
               this.badge.visible = this._state != PLAYERS_PANEL_STATE.MEDIUM_NO_BADGES;
               break;
            case PLAYERS_PANEL_STATE.SHORT_NO_BADGES:
            case PLAYERS_PANEL_STATE.SHORT:
               this.vehicleTF.visible = false;
               this.prestigeLevel.visible = false;
               this.playerNameFullTF.visible = false;
               this.playerNameCutTF.visible = false;
               this.badge.visible = false;
               break;
            case PLAYERS_PANEL_STATE.HIDDEN:
               visible = false;
               return;
         }
         visible = true;
         this.updatePositions();
         invalidate();
      }
      
      public function get holderItemID() : uint
      {
         return this._holderItemID;
      }
      
      public function set holderItemID(param1:uint) : void
      {
         this._holderItemID = param1;
      }
      
      public function get state() : int
      {
         return this._state;
      }
      
      protected function get isOffline() : Boolean
      {
         return this._isOffline;
      }
      
      protected function onMouseOver(param1:MouseEvent) : void
      {
         var _loc2_:PlayersPanelItemEvent = new PlayersPanelItemEvent(PlayersPanelItemEvent.ON_ITEM_OVER,this,this.holderItemID,param1);
         dispatchEvent(_loc2_);
      }
      
      protected function onMouseOut(param1:MouseEvent) : void
      {
         var _loc2_:PlayersPanelItemEvent = new PlayersPanelItemEvent(PlayersPanelItemEvent.ON_ITEM_OUT,this,this.holderItemID,param1);
         dispatchEvent(_loc2_);
      }
      
      protected function onMouseClick(param1:MouseEvent) : void
      {
         if(this.dynamicSquad && this.dynamicSquad.hitTestPoint(param1.stageX,param1.stageY))
         {
            return;
         }
         var _loc2_:PlayersPanelItemEvent = new PlayersPanelItemEvent(PlayersPanelItemEvent.ON_ITEM_CLICK,this,this.holderItemID,param1);
         dispatchEvent(_loc2_);
      }
      
      private function onMouseOverHandler(param1:MouseEvent) : void
      {
         this.onMouseOver(param1);
      }
      
      private function onMouseOutHandler(param1:MouseEvent) : void
      {
         this.onMouseOut(param1);
      }
      
      private function onMouseClickHandler(param1:MouseEvent) : void
      {
         this.onMouseClick(param1);
      }
   }
}
