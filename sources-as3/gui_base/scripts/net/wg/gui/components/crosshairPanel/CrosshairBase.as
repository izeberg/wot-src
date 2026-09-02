package net.wg.gui.components.crosshairPanel
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CROSSHAIR_CASSETTE_TYPES;
   import net.wg.data.constants.generated.CROSSHAIR_CONSTANTS;
   import net.wg.gui.components.crosshairPanel.VO.GunMarkerIndicatorVO;
   import net.wg.gui.components.crosshairPanel.components.AbilityModifierIndicator;
   import net.wg.gui.components.crosshairPanel.components.ClipQuantityIndicator;
   import net.wg.gui.components.crosshairPanel.components.CrosshairClipQuantityBarContainer;
   import net.wg.gui.components.crosshairPanel.components.GunCoolingIndicator;
   import net.wg.gui.components.crosshairPanel.components.ShotDamageInd;
   import net.wg.gui.components.crosshairPanel.components.ShotFlyTimeInd;
   import net.wg.gui.components.crosshairPanel.components.autoloader.AutoloaderIndicator;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorStateParamsVO;
   import net.wg.gui.components.crosshairPanel.components.coolantAbility.CoolantAbilityIndicator;
   import net.wg.gui.components.crosshairPanel.components.overheatBar.OverheatBar;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   
   public class CrosshairBase extends MovieClip implements ICrosshair
   {
      
      private static const NET_MC_SHORT_LABEL:String = "short";
      
      private static const TYPE_PREFIX:String = "type";
      
      private static const FRACTIONAL_FORMAT_CMD:String = "getFractionalFormat";
      
      private static const TF_LEFT_MARGIN:int = 2;
      
      private static const COOLANT_ABILITY_INDICATOR_OFFSET:int = -60;
      
      private static const GUN_COOLING_INDICATOR_OFFSET:int = -13;
       
      
      public var timerProgressTextField:TextField = null;
      
      public var timerCompleteTextField:TextField = null;
      
      public var reloadTimeBlink:MovieClip = null;
      
      public var quickReloadingTimerTextField:TextField = null;
      
      public var reloadingBar:MovieClip = null;
      
      public var reloadingAnimationMC:MovieClip = null;
      
      public var healthBarMC:MovieClip = null;
      
      public var cassetteMC:CrosshairClipQuantityBarContainer = null;
      
      public var autogunCassetteMC:CrosshairClipQuantityBarContainer = null;
      
      public var mbCassetteMC:CrosshairClipQuantityBarContainer = null;
      
      public var centerMC:MovieClip = null;
      
      public var netMC:MovieClip = null;
      
      public var netSeparator:Sprite = null;
      
      public var distance:CrosshairDistanceContainer = null;
      
      public var autoloaderComponent:AutoloaderIndicator = null;
      
      public var mbAutoloaderComponent:AutoloaderIndicator = null;
      
      public var shotFlyTimeInd:ShotFlyTimeInd = null;
      
      public var shotDamageInd:ShotDamageInd = null;
      
      protected var health:Number = 0;
      
      protected var reloadingTime:Number = 0;
      
      protected var netType:Number = 0;
      
      protected var centerType:Number = 0;
      
      protected var reloadingState:String = "";
      
      protected var centerAlpha:Number = 1.0;
      
      protected var netAlpha:Number = 1.0;
      
      protected var reloadingBarAlpha:Number = 1.0;
      
      protected var healthBarAlpha:Number = 1.0;
      
      protected var cassetteAlpha:Number = 1.0;
      
      protected var reloadingTimeFieldAlpha:Number = 1.0;
      
      private var _overheatBar:OverheatBar = null;
      
      private var _coolantAbilityIndicator:CoolantAbilityIndicator = null;
      
      private var _abilityModifierIndicator:AbilityModifierIndicator = null;
      
      private var _gunCoolingIndicator:GunCoolingIndicator = null;
      
      private var _prevReloadingState:String = "";
      
      private var _clipsByType:Vector.<ClipQuantityIndicator> = null;
      
      private var _clipType:int = 0;
      
      private var _currentTimerTextField:TextField = null;
      
      private var _currentReloadingTime:Number = -1;
      
      private var _isReloadInProgress:Boolean = false;
      
      private var _isUseFrameAnimation:Boolean = true;
      
      private var _netSeparatorVisible:Boolean = true;
      
      private var _visibleNetMask:int = 3;
      
      private var _quickReloadingTime:Number = -1;
      
      private var _quickReloadingTimerActive:Boolean = false;
      
      private var _quickReloadingTimerVisible:Boolean = true;
      
      private var _disposed:Boolean = false;
      
      private var _shotFlyTimeIndVisible:Boolean = false;
      
      private var _shotDamageIndVisible:Boolean = false;
      
      public function CrosshairBase()
      {
         super();
         this.cassetteMC.isUseFrameAnimation = this._isUseFrameAnimation;
         this.autogunCassetteMC.isUseFrameAnimation = this._isUseFrameAnimation;
         this.mbCassetteMC.isUseFrameAnimation = this._isUseFrameAnimation;
         this.timerProgressTextField.visible = false;
         this.reloadTimeBlink.visible = false;
         this.updateQuickReloadingTimer();
         addEventListener(CrosshairPanelEvent.SOUND,this.onCrosshairPanelSoundHandler);
         this._clipsByType = new Vector.<ClipQuantityIndicator>(0);
         this._clipsByType.length = CROSSHAIR_CASSETTE_TYPES.CASSETTE_TYPES.length;
         this._clipsByType[CROSSHAIR_CASSETTE_TYPES.CASSETTE] = this.cassetteMC;
         this._clipsByType[CROSSHAIR_CASSETTE_TYPES.AUTOLOADER] = this.autoloaderComponent;
         this._clipsByType[CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_CASSETTE] = this.mbCassetteMC;
         this._clipsByType[CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_AUTOLOADER] = this.mbAutoloaderComponent;
         this._clipsByType[CROSSHAIR_CASSETTE_TYPES.AUTO_GUN_CASSETTE] = this.autogunCassetteMC;
      }
      
      public function addOverheat(param1:Vector.<Number>) : void
      {
         var _loc2_:Class = null;
         if(!this._overheatBar)
         {
            _loc2_ = Class(getDefinitionByName(Linkages.OVERHEAT_WIDGET));
            this._overheatBar = OverheatBar(new _loc2_());
            addChild(this._overheatBar);
            this._overheatBar.x = OverheatBar.X_OFFSET;
            this._overheatBar.y = OverheatBar.Y_OFFSET;
         }
         this._overheatBar.setOverheatMarkers(param1);
         this._overheatBar.visible = true;
         this.updateNetMC();
      }
      
      private function addCoolantAbilityIndicator() : void
      {
         var _loc1_:Class = Class(getDefinitionByName(Linkages.COOLANT_ABILITY_INDICATOR));
         this._coolantAbilityIndicator = CoolantAbilityIndicator(new _loc1_());
         addChild(this._coolantAbilityIndicator);
         this._coolantAbilityIndicator.x = this.timerProgressTextField.x + COOLANT_ABILITY_INDICATOR_OFFSET;
         this._coolantAbilityIndicator.y = this.timerProgressTextField.y;
         this._coolantAbilityIndicator.addEventListener(CoolantAbilityIndicator.ACTIVATED,this.onCoolantAbilityActivatedHandler);
         this._coolantAbilityIndicator.addEventListener(CoolantAbilityIndicator.DEACTIVATED,this.onCoolantAbilityDeactivatedHandler);
      }
      
      private function addGunCoolingIndicator() : void
      {
         var _loc1_:Class = null;
         if(!this._gunCoolingIndicator)
         {
            _loc1_ = Class(getDefinitionByName(Linkages.GUN_COOLING_INDICATOR));
            this._gunCoolingIndicator = GunCoolingIndicator(new _loc1_());
            addChild(this._gunCoolingIndicator);
            this._gunCoolingIndicator.x = GUN_COOLING_INDICATOR_OFFSET;
            this._gunCoolingIndicator.y = this.getGunCoolingIndicatorYOffset();
         }
      }
      
      private function onCoolantAbilityDeactivatedHandler(param1:Event) : void
      {
         this.blinkReloadTime(CROSSHAIR_CONSTANTS.CROSSHAIR_BLINK_ORANGE_HORIZONTAL);
      }
      
      private function onCoolantAbilityActivatedHandler(param1:Event) : void
      {
         this.blinkReloadTime(CROSSHAIR_CONSTANTS.CROSSHAIR_BLINK_GREEN_HORIZONTAL);
      }
      
      public function autoloaderBoostUpdate(param1:BoostIndicatorStateParamsVO, param2:Number, param3:Boolean = false) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].autoloaderBoostUpdate(param1,param2,param3);
         }
      }
      
      public function autoloaderBoostUpdateAsPercent(param1:Number, param2:Number) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].autoloaderBoostUpdateAsPercent(param1,param2);
         }
      }
      
      public function showShot() : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].autoloaderShowShot();
         }
      }
      
      public function autoloaderUpdate(param1:Number, param2:Number, param3:Boolean, param4:Boolean) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].autoloaderUpdate(param1,param2,param3,param4);
         }
      }
      
      public function blinkReloadTime(param1:int) : void
      {
         var _loc2_:Boolean = param1 > 0;
         this.reloadTimeBlink.visible = _loc2_;
         if(_loc2_)
         {
            this.arrangeReloadTimeBlink();
            this.reloadTimeBlink.blink.gotoAndStop(param1);
            this.reloadTimeBlink.gotoAndPlay(1);
         }
      }
      
      public function clearDistance(param1:Boolean) : void
      {
         this.distance.clearDistance(param1);
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.onDispose();
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function removeOverheat() : void
      {
         if(this._overheatBar)
         {
            this._overheatBar.visible = false;
         }
      }
      
      public function setAmmoStock(param1:Number, param2:String, param3:Boolean = false) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].updateCurrentAmmo(param1);
         }
         else if(this._clipType != CROSSHAIR_CASSETTE_TYPES.NO_CASSETTE)
         {
            this._clipsByType[this._clipType].updateInfo(param1,param2,param3);
         }
      }
      
      public function setAutoloaderReloadingAsPercent(param1:Number, param2:Boolean) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].setGunReloadingPercent(param1);
         }
      }
      
      public function setCenterType(param1:Number) : void
      {
         if(this.centerType != param1)
         {
            this.centerType = param1;
            this.updateCenterMC();
         }
      }
      
      public function setClipsParam(param1:Number, param2:Number, param3:int = 0) : void
      {
         this._clipType = param3;
         this.updateNetSeparatorVisibility();
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].updateTotalAmmo(param1);
         }
         else if(this._clipType != CROSSHAIR_CASSETTE_TYPES.NO_CASSETTE)
         {
            this._clipsByType[this._clipType].setClipsParam(param1,param2,this._clipType);
         }
         this.autoloaderComponent.visible = param3 == CROSSHAIR_CASSETTE_TYPES.AUTOLOADER;
         this.mbAutoloaderComponent.visible = param3 == CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_AUTOLOADER;
         this.cassetteMC.visible = param3 == CROSSHAIR_CASSETTE_TYPES.CASSETTE;
         this.autogunCassetteMC.visible = param3 == CROSSHAIR_CASSETTE_TYPES.AUTO_GUN_CASSETTE;
         this.mbCassetteMC.visible = param3 == CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_CASSETTE;
      }
      
      public function setComponentsAlpha(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : void
      {
         this.netAlpha = param1;
         this.centerAlpha = param2;
         this.reloadingBarAlpha = param3;
         this.healthBarAlpha = param4;
         this.cassetteAlpha = param5;
         this.setReloadingAlpha(param6);
         this.updateComponentsAlpha();
      }
      
      public function setDistance(param1:String) : void
      {
         this.distance.setDistance(param1);
      }
      
      public function setDistanceVisibility(param1:Boolean) : void
      {
      }
      
      public function setFlameDistanceVisibility(param1:Boolean, param2:String) : void
      {
         if(this._overheatBar)
         {
            this._overheatBar.updateDistance(param1,param2);
         }
      }
      
      public function setGunMarkersData(param1:Vector.<GunMarkerIndicatorVO>, param2:Boolean) : void
      {
      }
      
      public function setHealth(param1:Number) : void
      {
         if(this.health == param1)
         {
            return;
         }
         this.health = param1;
         this.updateHealthBarMC();
      }
      
      public function setInfo(param1:Number, param2:String, param3:String, param4:Boolean, param5:Boolean, param6:String, param7:String, param8:Number, param9:Number, param10:String, param11:Number, param12:String, param13:Boolean = false, param14:int = 0, param15:Boolean = false) : void
      {
         this.setClipsParam(param8,param9,param14);
         this.setHealth(param1);
         this.setZoom(param2);
         this.setReloadingState(param3);
         this.showReloadingTimeField(param4);
         this.setDistanceVisibility(param5);
         this.setDistance(param6);
         this.updatePlayerInfo(param7);
         this.setAmmoStock(param11,param12,param13);
         this.updateAmmoState(param10);
         this.updateAutoloaderState(param8,param11,param15);
      }
      
      public function setNetSeparatorVisible(param1:Boolean) : void
      {
         this._netSeparatorVisible = param1;
         this.updateNetSeparatorVisibility();
      }
      
      public function setNetType(param1:Number) : void
      {
         if(this.netType != param1)
         {
            this.netType = param1;
            this.updateNetType();
            this.updateNetMC();
            this.updateCenterMC();
            this.updateComponentsAlpha();
            this.updateHealthBarMC();
            this.setReloadingBarFrame();
            this.updateNetSeparatorVisibility();
            this.updateQuickReloadingTimer();
            this.updateShotIndicatorsVisibility();
         }
      }
      
      public function setOverheatProgress(param1:Number, param2:Number, param3:Boolean = false, param4:Boolean = false) : void
      {
         if(this._overheatBar)
         {
            if(param3)
            {
               this._overheatBar.onChangeCrosshair(param1,param2);
            }
            else
            {
               this._overheatBar.updateInfo(param1,param2,param4);
            }
         }
      }
      
      public function setOverheatState(param1:Number) : void
      {
         if(this._overheatBar)
         {
            this._overheatBar.state = param1;
         }
      }
      
      public function setOverheatStatus(param1:Boolean) : void
      {
         if(this._overheatBar)
         {
            this._overheatBar.isOverheated = param1;
         }
      }
      
      public function setQuickReloadingTime(param1:Boolean, param2:Number) : void
      {
         if(this._quickReloadingTimerActive != param1 || this._quickReloadingTime != param2)
         {
            this._quickReloadingTimerActive = param1;
            this._quickReloadingTime = param2;
            this.updateQuickReloadingTimer();
         }
      }
      
      public function setReloadingAsPercent(param1:Number) : void
      {
         if(this.reloadingTime == param1)
         {
            return;
         }
         this.reloadingTime = param1;
         this.setReloadingBarFrame();
      }
      
      public function setReloadingState(param1:String) : void
      {
         if(this.reloadingState != param1)
         {
            this.reloadingState = param1;
            this.updateReloadingState();
            if(this._clipType != CROSSHAIR_CASSETTE_TYPES.NO_CASSETTE)
            {
               this._clipsByType[this._clipType].setReloadingState(param1);
            }
         }
         this._prevReloadingState = param1;
      }
      
      public function setReloadingTime(param1:Number) : void
      {
         if(this._currentReloadingTime != param1)
         {
            this._currentReloadingTime = param1 < 0 ? Number(0) : Number(param1);
            this.applyReloadingData();
         }
      }
      
      public function setShotDamageIndValue(param1:int) : void
      {
         if(this.shotDamageInd)
         {
            this.shotDamageInd.setValue(param1);
         }
      }
      
      public function setShotDamageIndVisibility(param1:Boolean) : void
      {
         if(this.shotDamageInd)
         {
            this._shotDamageIndVisible = param1;
            this.shotDamageInd.visible = this._shotDamageIndVisible;
         }
      }
      
      public function setShotFlyTimeIndValue(param1:Number) : void
      {
         if(this.shotFlyTimeInd)
         {
            this.shotFlyTimeInd.setValue(param1);
         }
      }
      
      public function setShotFlyTimeIndVisibility(param1:Boolean) : void
      {
         if(this.shotFlyTimeInd)
         {
            this._shotFlyTimeIndVisible = param1;
            this.shotFlyTimeInd.visible = this._shotFlyTimeIndVisible;
         }
      }
      
      public function setCoolantAbilityReloadingPenalty(param1:Number, param2:Number) : void
      {
         if(!this._coolantAbilityIndicator)
         {
            this.addCoolantAbilityIndicator();
            this._coolantAbilityIndicator.validateNow();
         }
         this._coolantAbilityIndicator.updateReloadingPenalty(param1,param2);
      }
      
      public function addCoolantAbilityReloadingPenalty(param1:Number) : void
      {
         if(!this._coolantAbilityIndicator)
         {
            this.addCoolantAbilityIndicator();
            this._coolantAbilityIndicator.validateNow();
         }
         this._coolantAbilityIndicator.addReloadingPenalty(param1);
      }
      
      public function setAbilityModifier(param1:int, param2:Boolean) : void
      {
         var _loc3_:Class = null;
         if(!this._abilityModifierIndicator)
         {
            _loc3_ = Class(getDefinitionByName(Linkages.ABILITY_MODIFIER_INDICATOR));
            this._abilityModifierIndicator = AbilityModifierIndicator(new _loc3_());
            this._abilityModifierIndicator.y = AbilityModifierIndicator.Y_OFFSET;
            this.arrangeAbilityModifier();
            addChild(this._abilityModifierIndicator);
         }
         if(param1 <= Values.ZERO)
         {
            this._abilityModifierIndicator.hide(param2);
         }
         else
         {
            this._abilityModifierIndicator.show(param1,param2);
         }
      }
      
      public function setTimerReloadingState() : void
      {
         var _loc1_:Boolean = !(this.reloadingState == CrosshairConsts.RELOADING_ENDED || this.reloadingState == CrosshairConsts.RELOADING_END);
         var _loc2_:Boolean = this._currentTimerTextField == this.timerProgressTextField;
         var _loc3_:Boolean = this._currentTimerTextField == this.timerCompleteTextField;
         if(this._isReloadInProgress == _loc1_ && this._currentTimerTextField && (_loc2_ || _loc3_))
         {
            return;
         }
         this._isReloadInProgress = _loc1_;
         if(this._currentTimerTextField)
         {
            this.setComponentVisibility(this.timerProgressTextField,false);
            this.setComponentVisibility(this.timerCompleteTextField,false);
         }
         this._currentTimerTextField = !!this._isReloadInProgress ? this.timerProgressTextField : this.timerCompleteTextField;
         this.setComponentVisibility(this._currentTimerTextField,true);
         this.applyReloadingData();
         this.applyReloadingAlpha();
      }
      
      public function setVisibleNet(param1:int) : void
      {
         this._visibleNetMask = param1;
         this.updateNetVisibility();
         this.updateNetSeparatorVisibility();
      }
      
      public function setZoom(param1:String) : void
      {
      }
      
      public function showReloadingTimeField(param1:Boolean) : void
      {
         if(param1)
         {
            if(this._currentTimerTextField)
            {
               this.setComponentVisibility(this.timerCompleteTextField,this.timerCompleteTextField == this._currentTimerTextField);
               this.setComponentVisibility(this.timerProgressTextField,this.timerProgressTextField == this._currentTimerTextField);
            }
            else
            {
               this.setComponentVisibility(this.timerCompleteTextField,true);
               this.setComponentVisibility(this.timerProgressTextField,false);
            }
            this._quickReloadingTimerVisible = true;
         }
         else
         {
            this.setComponentVisibility(this.timerCompleteTextField,false);
            this.setComponentVisibility(this.timerProgressTextField,false);
            this._quickReloadingTimerVisible = false;
         }
         this.updateQuickReloadingTimer();
      }
      
      public function updateAmmoState(param1:String) : void
      {
      }
      
      public function updateAutoloaderState(param1:Number, param2:Number, param3:Boolean) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].updateQuantityInClip(param2,param1);
            this._clipsByType[this._clipType].updateCritical(param3);
         }
      }
      
      public function updateCritical(param1:Boolean) : void
      {
         if(this.isAutoloader)
         {
            this._clipsByType[this._clipType].updateCritical(param1);
         }
      }
      
      public function updatePlayerInfo(param1:String) : void
      {
      }
      
      public function updateScaleSteps(param1:int) : void
      {
      }
      
      public function updateScaleWidget(param1:Number) : void
      {
      }
      
      public function animShotHitMarker(param1:String) : void
      {
      }
      
      public function setShotHitMarkerVisibility(param1:Boolean) : void
      {
      }
      
      public function setGunCoolingTime(param1:Boolean, param2:Number) : void
      {
         this.addGunCoolingIndicator();
         this._gunCoolingIndicator.updateTime(param1,param2);
      }
      
      public function setGunCoolingVisibility(param1:Boolean) : void
      {
         if(this._gunCoolingIndicator)
         {
            this._gunCoolingIndicator.visible = param1;
         }
      }
      
      protected function onDispose() : void
      {
         removeEventListener(CrosshairPanelEvent.SOUND,this.onCrosshairPanelSoundHandler);
         this._clipsByType.splice(0,this._clipsByType.length);
         this._clipsByType = null;
         this.reloadTimeBlink = null;
         this.timerProgressTextField = null;
         this.timerCompleteTextField = null;
         this._currentTimerTextField = null;
         this.quickReloadingTimerTextField = null;
         this.reloadingBar = null;
         this.reloadingAnimationMC = null;
         this.healthBarMC = null;
         this.centerMC = null;
         this.netMC = null;
         this.netSeparator = null;
         this.autoloaderComponent.dispose();
         this.autoloaderComponent = null;
         this.mbAutoloaderComponent.dispose();
         this.mbAutoloaderComponent = null;
         this.distance.dispose();
         this.distance = null;
         this.cassetteMC.dispose();
         this.cassetteMC = null;
         this.autogunCassetteMC.dispose();
         this.autogunCassetteMC = null;
         this.mbCassetteMC.dispose();
         this.mbCassetteMC = null;
         if(this._coolantAbilityIndicator)
         {
            this._coolantAbilityIndicator.removeEventListener(CoolantAbilityIndicator.ACTIVATED,this.onCoolantAbilityActivatedHandler);
            this._coolantAbilityIndicator.removeEventListener(CoolantAbilityIndicator.DEACTIVATED,this.onCoolantAbilityDeactivatedHandler);
            this._coolantAbilityIndicator.dispose();
            this._coolantAbilityIndicator = null;
         }
         if(this._abilityModifierIndicator)
         {
            this._abilityModifierIndicator.dispose();
            this._abilityModifierIndicator = null;
         }
         if(this.shotFlyTimeInd)
         {
            this.shotFlyTimeInd.dispose();
            this.shotFlyTimeInd = null;
         }
         if(this.shotDamageInd)
         {
            this.shotDamageInd.dispose();
            this.shotDamageInd = null;
         }
         if(this._overheatBar)
         {
            this._overheatBar.dispose();
            this._overheatBar = null;
         }
         if(this._gunCoolingIndicator)
         {
            this._gunCoolingIndicator.dispose();
            this._gunCoolingIndicator = null;
         }
      }
      
      protected function arrangeReloadTimeBlink() : void
      {
         var _loc1_:Array = this.getReloadTimeBlinkYPos();
         if(_loc1_ && this.reloadTimeBlink && this._currentTimerTextField)
         {
            this.reloadTimeBlink.x = this._currentTimerTextField.x + (this._currentTimerTextField.textWidth >> 1) + TF_LEFT_MARGIN;
            this.reloadTimeBlink.y = _loc1_[this.netType];
         }
      }
      
      protected function arrangeAbilityModifier() : void
      {
         var _loc1_:Array = this.getAbilityModifierXPos();
         if(this._abilityModifierIndicator && _loc1_)
         {
            this._abilityModifierIndicator.x = _loc1_[this.netType];
         }
      }
      
      protected function updateNetType() : void
      {
         gotoAndStop(TYPE_PREFIX + this.netType);
         this.arrangeAbilityModifier();
      }
      
      protected function updateReloadingState() : void
      {
         this.setTimerReloadingState();
         if(this.reloadingState == CrosshairConsts.RELOADING_END)
         {
            this.setComponentVisibility(this.reloadingAnimationMC,true);
            this.reloadingAnimationMC.play();
         }
         else if(this.reloadingState == CrosshairConsts.RELOADING_ENDED)
         {
            this.setComponentVisibility(this.reloadingAnimationMC,true);
            this.reloadingAnimationMC.gotoAndStop(1);
         }
         else
         {
            this.setComponentVisibility(this.reloadingAnimationMC,false);
         }
         if(this._coolantAbilityIndicator && (this.reloadingState == CrosshairConsts.RELOADING_PROGRESS && this._prevReloadingState == CrosshairConsts.RELOADING_ENDED || this.reloadingState == CrosshairConsts.RELOADING_IMPOSSIBLE_AMMO_ENDED))
         {
            this._coolantAbilityIndicator.hideAbilityMod();
         }
      }
      
      protected function getReloadTimeBlinkYPos() : Array
      {
         return null;
      }
      
      protected function getAbilityModifierXPos() : Array
      {
         return null;
      }
      
      protected function getGunCoolingIndicatorYOffset() : int
      {
         return Values.ZERO;
      }
      
      private function updateQuickReloadingTimer() : void
      {
         var _loc1_:String = null;
         if(this.quickReloadingTimerTextField)
         {
            if(this._quickReloadingTimerVisible && this._quickReloadingTimerActive && this._quickReloadingTime > 0)
            {
               _loc1_ = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,this._quickReloadingTime]);
               this.quickReloadingTimerTextField.text = _loc1_;
               this.quickReloadingTimerTextField.visible = true;
            }
            else
            {
               this.quickReloadingTimerTextField.visible = false;
            }
         }
      }
      
      private function updateNetSeparatorVisibility() : void
      {
         if(this.netSeparator)
         {
            this.setComponentVisibility(this.netSeparator,!this.isAutoloader && this._netSeparatorVisible);
         }
      }
      
      private function updateNetVisibility() : void
      {
         this.setComponentVisibility(this.netMC,(this._visibleNetMask & CROSSHAIR_CONSTANTS.VISIBLE_NET) != 0);
      }
      
      private function setReloadingAlpha(param1:Number) : void
      {
         if(this.reloadingTimeFieldAlpha != param1)
         {
            this.reloadingTimeFieldAlpha = param1;
            this.applyReloadingAlpha();
         }
      }
      
      private function applyReloadingAlpha() : void
      {
         if(this._currentTimerTextField)
         {
            this._currentTimerTextField.alpha = this.reloadingTimeFieldAlpha;
         }
         if(this.quickReloadingTimerTextField)
         {
            this.quickReloadingTimerTextField.alpha = this.reloadingTimeFieldAlpha;
         }
      }
      
      private function applyReloadingData() : void
      {
         if(this._currentTimerTextField && this._currentReloadingTime != Values.DEFAULT_INT)
         {
            this._currentTimerTextField.text = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,Number(this._currentReloadingTime)]);
         }
      }
      
      private function updateCenterMC() : void
      {
         this.centerMC.gotoAndStop(TYPE_PREFIX + this.centerType);
      }
      
      private function updateNetMC() : void
      {
         this.netMC.gotoAndStop(this._overheatBar && this._overheatBar.visible ? NET_MC_SHORT_LABEL : 1);
      }
      
      private function updateHealthBarMC() : void
      {
         if(this.healthBarMC)
         {
            this.healthBarMC.gotoAndStop(CrosshairConsts.PROGRESS_TOTAL_FRAMES_COUNT * this.health);
         }
      }
      
      private function setReloadingBarFrame() : void
      {
         if(this.reloadingBar)
         {
            this.updateReloadingState();
            this.reloadingBar.gotoAndStop(CrosshairConsts.PROGRESS_TOTAL_FRAMES_COUNT * this.reloadingTime);
         }
      }
      
      private function updateComponentsAlpha() : void
      {
         this.centerMC.alpha = this.centerAlpha;
         if(this.netSeparator)
         {
            this.netSeparator.alpha = this.netAlpha;
         }
         this.netMC.alpha = this.netAlpha;
         this.healthBarMC.alpha = this.healthBarAlpha;
         this.reloadingBar.alpha = this.reloadingBarAlpha;
         this.reloadingAnimationMC.alpha = this.reloadingBarAlpha;
         this.cassetteMC.alpha = this.cassetteAlpha;
         this.autogunCassetteMC.alpha = this.cassetteAlpha;
         this.mbCassetteMC.alpha = this.cassetteAlpha;
         this.autoloaderComponent.alpha = this.cassetteAlpha;
         this.mbAutoloaderComponent.alpha = this.cassetteAlpha;
      }
      
      private function onCrosshairPanelSoundHandler(param1:CrosshairPanelEvent) : void
      {
         if(!visible)
         {
            param1.stopImmediatePropagation();
         }
      }
      
      private function updateShotIndicatorsVisibility() : void
      {
         if(this.shotDamageInd)
         {
            this.shotDamageInd.visible = this._shotDamageIndVisible;
         }
         if(this.shotFlyTimeInd)
         {
            this.shotFlyTimeInd.visible = this._shotFlyTimeIndVisible;
         }
      }
      
      public function get autoloaderBoostParams() : BoostIndicatorStateParamsVO
      {
         if(this.isAutoloader)
         {
            return this._clipsByType[this._clipType].autoloaderBoostParams;
         }
         return null;
      }
      
      public function set isUseFrameAnimation(param1:Boolean) : void
      {
         this._isUseFrameAnimation = param1;
      }
      
      public function set scaleWidgetEnabled(param1:Boolean) : void
      {
      }
      
      public function get isAutoloader() : Boolean
      {
         return this._clipType == CROSSHAIR_CASSETTE_TYPES.AUTOLOADER || this._clipType == CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_AUTOLOADER;
      }
      
      protected function setComponentVisibility(param1:DisplayObject, param2:Boolean) : void
      {
         param1.visible = param2;
      }
   }
}
