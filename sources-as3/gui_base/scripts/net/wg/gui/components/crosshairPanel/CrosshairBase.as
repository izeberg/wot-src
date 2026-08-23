package net.wg.gui.components.crosshairPanel
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.external.ExternalInterface;
   import flash.filters.BevelFilter;
   import flash.filters.BitmapFilterType;
   import flash.geom.ColorTransform;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CLIP_RELOADING_TYPES;
   import net.wg.data.constants.generated.CROSSHAIR_CONSTANTS;
   import net.wg.gui.components.crosshairPanel.VO.GunMarkerIndicatorVO;
   import net.wg.gui.components.crosshairPanel.components.CrosshairClipQuantityBarContainer;
   import net.wg.gui.components.crosshairPanel.components.autoloader.AutoloaderIndicator;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorStateParamsVO;
   import net.wg.gui.components.crosshairPanel.components.controllableLoader.ControllableReloadCassette;
   import net.wg.gui.components.crosshairPanel.components.extraShotClip.ExtraShotClipPanel;
   import net.wg.gui.components.crosshairPanel.components.gunStack.ReloadBoostBorder;
   import net.wg.gui.components.crosshairPanel.components.shellCalibrationClip.ShellCalibrationClipPanel;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class CrosshairBase extends MovieClip implements ICrosshair
   {
      
      private static const TYPE_PREFIX:String = "type";
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
      
      private static const RELOAD_TIME_BLINK_DURATION:Number = 0.5;
      
      private static const RELOAD_TIME_COLOR_TRANSFORM_BLINK_VALUES:Object = {
         "redOffset":255,
         "greenOffset":255,
         "blueOffset":255
      };
      
      private static const TF_LEFT_MARGIN:int = 2;
      
      private static const RELOAD_BORDER_OFFSET:int = 91;
      
      private static const SIEGE_PILLBOX_NET_TYPES:Vector.<int> = new <int>[4,5];
      
      private static const BOOSTED_TEXT_COLOR:uint = 14286645;
      
      private static const BOOSTED_TEXT_COLOR_RELOAD:uint = 15356485;
      
      private static const RELOAD_SWITCH_ICON_COMPLETE:String = "green";
      
      private static const RELOAD_SWITCH_ICON_PROGRESS:String = "red";
       
      
      public var timerProgressTextField:TextField = null;
      
      public var timerCompleteTextField:TextField = null;
      
      public var reloadTimeBlink:MovieClip = null;
      
      public var quickReloadingTimerTextField:TextField = null;
      
      public var reloadingBar:MovieClip = null;
      
      public var reloadingAnimationMC:MovieClip = null;
      
      public var reloadSwitchIcon:MovieClip = null;
      
      public var healthBarMC:MovieClip = null;
      
      public var cassetteMC:CrosshairClipQuantityBarContainer = null;
      
      public var centerMC:MovieClip = null;
      
      public var netMC:Sprite = null;
      
      public var netSeparator:CrosshairNetSeparator = null;
      
      public var distance:CrosshairDistanceContainer = null;
      
      public var averageDamage:CrosshairAverageDamageContainer = null;
      
      public var autoloaderComponent:AutoloaderIndicator = null;
      
      public var extraShotClipPanel:ExtraShotClipPanel = null;
      
      public var controllableReloadCassette:ControllableReloadCassette = null;
      
      public var shellCalibrationClipPanel:ShellCalibrationClipPanel = null;
      
      public var reloadBoostBorder:ReloadBoostBorder = null;
      
      protected var health:Number = 0;
      
      protected var reloadingTime:Number = 0;
      
      protected var netType:int = 0;
      
      protected var centerType:int = 0;
      
      protected var reloadingState:String = "";
      
      protected var centerAlpha:Number = 1.0;
      
      protected var netAlpha:Number = 1.0;
      
      protected var reloadingBarAlpha:Number = 1.0;
      
      protected var healthBarAlpha:Number = 1.0;
      
      protected var cassetteAlpha:Number = 1.0;
      
      protected var reloadingTimeFieldAlpha:Number = 1.0;
      
      private var _netSeparatorType:String = "default";
      
      private var _timerProgressTextFieldColor:uint = 0;
      
      private var _timerCompleteTextFieldColor:uint = 0;
      
      private var _timerProgressTextFieldFilter:Array;
      
      private var _timerCompleteTextFieldFilter:Array;
      
      private var _timerBoostedFilter:Array;
      
      private var _reloadTimeColorTransform:ColorTransform;
      
      private var _clipReloadingType:int = 0;
      
      private var _currentTimerTextField:TextField = null;
      
      private var _currentReloadingTime:Number = -1;
      
      private var _isReloadInProgress:Boolean = false;
      
      private var _netSeparatorVisible:Boolean = true;
      
      private var _visibleNetMask:int = 3;
      
      private var _intuitionCooldown:String = "";
      
      private var _quickReloadingTimerActive:Boolean = false;
      
      private var _quickReloadingTimerVisible:Boolean = true;
      
      private var _reloadTimeBlinkYPos:Array = null;
      
      private var _disposed:Boolean = false;
      
      private var _width:Number = 0;
      
      private var _height:Number = 0;
      
      private var _isShownReloading:Boolean = true;
      
      private var _isReloadBoostBorder:Boolean = false;
      
      private var _isReloadBoostBorderActive:Boolean = false;
      
      public function CrosshairBase()
      {
         this._timerProgressTextFieldFilter = [];
         this._timerCompleteTextFieldFilter = [];
         this._timerBoostedFilter = [];
         this._reloadTimeColorTransform = new ColorTransform();
         super();
         this.timerProgressTextField.visible = false;
         this.reloadSwitchIcon.visibile = false;
         this.reloadTimeBlink.visible = false;
         this.updateQuickReloadingTimer();
         addEventListener(CrosshairPanelEvent.SOUND,this.onCrosshairPanelSoundHandler);
         this._reloadTimeBlinkYPos = this.getReloadTimeBlinkYPos();
         this._timerProgressTextFieldColor = this.timerProgressTextField.textColor;
         this._reloadTimeColorTransform.color = this._timerProgressTextFieldColor;
         this._timerProgressTextFieldFilter = this.timerProgressTextField.filters;
         this._timerCompleteTextFieldColor = this.timerCompleteTextField.textColor;
         this._timerCompleteTextFieldFilter = this.timerCompleteTextField.filters;
         var _loc1_:BevelFilter = new BevelFilter();
         _loc1_.blurX = 2;
         _loc1_.blurY = 2;
         _loc1_.distance = 1.5;
         _loc1_.highlightColor = 16711680;
         _loc1_.shadowColor = 1461759;
         _loc1_.type = BitmapFilterType.OUTER;
         this._timerBoostedFilter = [_loc1_];
      }
      
      public function autoloaderBoostUpdate(param1:BoostIndicatorStateParamsVO, param2:Number, param3:Boolean = false) : void
      {
         this.autoloaderComponent.autoloaderBoostUpdate(param1,param2,param3);
      }
      
      public function autoloaderBoostUpdateAsPercent(param1:Number, param2:Number) : void
      {
         this.autoloaderComponent.autoloaderBoostUpdateAsPercent(param1,param2);
      }
      
      public function autoloaderUpdate(param1:Number, param2:Number, param3:Boolean, param4:Boolean, param5:Boolean, param6:Boolean = false) : void
      {
         switch(this._clipReloadingType)
         {
            case CLIP_RELOADING_TYPES.AUTO_LOADER_CLIP:
               this.autoloaderComponent.autoloaderUpdate(param1,param2,param4,param5);
               this.autoloaderComponent.updateCritical(param3);
               break;
            case CLIP_RELOADING_TYPES.CONTROLLABLE_RELOAD:
               this.controllableReloadCassette.reloadingPercent = param1;
               this.controllableReloadCassette.setTimer(param4,param2,param3);
               if(param6)
               {
                  this.controllableReloadCassette.applyNow();
               }
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
      
      public function clearAverageDamage(param1:Boolean) : void
      {
         this.averageDamage.clearAverageDamage(param1);
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
      
      public function setAmmoStock(param1:uint, param2:Number, param3:String, param4:Boolean = false) : void
      {
         switch(this._clipReloadingType)
         {
            case CLIP_RELOADING_TYPES.CASSETTE_CLIP:
               this.cassetteMC.updateInfo(param2,param3,param4);
               break;
            case CLIP_RELOADING_TYPES.AUTO_LOADER_CLIP:
               this.autoloaderComponent.updateCurrentAmmo(param2);
               break;
            case CLIP_RELOADING_TYPES.EXTRA_SHOT_CLIP:
               this.extraShotClipPanel.totalAmmo = param1;
               this.extraShotClipPanel.shellCount = param2;
               this.extraShotClipPanel.clipState = param3;
               break;
            case CLIP_RELOADING_TYPES.CONTROLLABLE_RELOAD:
               this.controllableReloadCassette.updateInfo(param2,param3);
               break;
            case CLIP_RELOADING_TYPES.SHELL_CALIBRATION_CLIP:
               this.shellCalibrationClipPanel.totalAmmo = param1;
               this.shellCalibrationClipPanel.shellCount = param2;
               this.shellCalibrationClipPanel.clipState = param3;
         }
      }
      
      public function setAutoloaderReloadingAsPercent(param1:Number) : void
      {
         if(this.isAutoloader)
         {
            this.autoloaderComponent.setGunReloadingPercent(param1);
         }
      }
      
      public function setAverageDamage(param1:String) : void
      {
         this.averageDamage.setAverageDamage(param1);
      }
      
      public function setCenterType(param1:Number) : void
      {
         if(this.centerType != param1)
         {
            this.centerType = param1;
            this.updateCenterMC();
         }
      }
      
      public function setClipsParam(param1:Number, param2:Number, param3:int) : void
      {
         this._clipReloadingType = param3;
         this.updateNetSeparatorVisibility();
         switch(this._clipReloadingType)
         {
            case CLIP_RELOADING_TYPES.CASSETTE_CLIP:
               this.cassetteMC.setClipsParam(param1,param2);
               break;
            case CLIP_RELOADING_TYPES.AUTO_LOADER_CLIP:
               this.autoloaderComponent.updateTotalAmmo(param1);
               break;
            case CLIP_RELOADING_TYPES.EXTRA_SHOT_CLIP:
               this.extraShotClipPanel.clipCapacity = param1;
               break;
            case CLIP_RELOADING_TYPES.CONTROLLABLE_RELOAD:
               this.controllableReloadCassette.setClipsParam(param1);
               break;
            case CLIP_RELOADING_TYPES.SHELL_CALIBRATION_CLIP:
               this.shellCalibrationClipPanel.clipCapacity = param1;
         }
         this.cassetteMC.visible = this.isCassette;
         this.autoloaderComponent.visible = this.isAutoloader;
         this.extraShotClipPanel.visible = this.isExtraShot;
         this.controllableReloadCassette.visible = this.isControllableReload;
         this.reloadSwitchIcon.visible = this.isUnlimitedClip;
         if(this.shellCalibrationClipPanel)
         {
            this.shellCalibrationClipPanel.visible = this.isShellCalibration;
         }
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
      
      public function setExtraShotClipReloading(param1:String, param2:Number, param3:Boolean, param4:Boolean = false) : void
      {
         this.extraShotClipPanel.setReloading(param1,param2,param3);
         if(param4)
         {
            this.extraShotClipPanel.applyNow();
         }
      }
      
      public function setShellCalibrationState(param1:uint) : void
      {
         if(this.shellCalibrationClipPanel)
         {
            this.shellCalibrationClipPanel.calibrationState = param1;
         }
      }
      
      public function setShellCalibrationClipReloading(param1:String, param2:Number, param3:Boolean = false) : void
      {
         this.shellCalibrationClipPanel.setReloading(param1,param2);
         if(param3)
         {
            this.shellCalibrationClipPanel.applyNow();
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
      
      public function setInfo(param1:Number, param2:String, param3:String, param4:Boolean, param5:Boolean, param6:String, param7:String, param8:Number, param9:Number, param10:int, param11:String, param12:uint, param13:Number, param14:String, param15:String, param16:uint, param17:Boolean = false, param18:Boolean = false, param19:Boolean = false, param20:Boolean = false, param21:Boolean = false, param22:Boolean = false) : void
      {
         this.setClipsParam(param8,param9,param10);
         this.setHealth(param1);
         this.setZoom(param2);
         this.setReloadingState(param3);
         this.showReloadingTimeField(param4);
         this.setDistanceVisibility(param5);
         this.setDistance(param6);
         this.setAverageDamage(param15);
         this.updatePlayerInfo(param7);
         this.setAmmoStock(param12,param13,param14,param17);
         this.updateAmmoState(param11);
         this.updateAutoloaderState(param8,param13);
         this.reloadBoost = param19;
         this.setReloadBoostBorderVisible(param20,param21,true);
         this.isUseAlternateZoomPosition = param22;
         this.setIsInControllableReload(param18);
         this.setShellCalibrationState(param16);
      }
      
      public function setIsInControllableReload(param1:Boolean) : void
      {
         if(this.isControllableReload)
         {
            this.controllableReloadCassette.isReloading = param1;
         }
      }
      
      public function setNetSeparatorType(param1:String) : void
      {
         this._netSeparatorType = param1;
         this.updateNetSeparatorType();
      }
      
      public function setAutoreloaderSurgeState(param1:Boolean) : void
      {
         if(this._clipReloadingType == CLIP_RELOADING_TYPES.AUTO_LOADER_CLIP)
         {
            this.autoloaderComponent.setAutoreloaderSurgeState(param1);
         }
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
            this.updateNetSeparatorType();
            this.updateCenterMC();
            this.updateComponentsAlpha();
            this.updateHealthBarMC();
            this.setReloadingBarFrame();
            this.updateNetSeparatorVisibility();
            this.updateQuickReloadingTimer();
            this.setReloadBoostBorderVisible(this._isReloadBoostBorder,this._isReloadBoostBorderActive,true);
         }
      }
      
      public function setQuickReloadingTime(param1:Boolean, param2:String) : void
      {
         if(this._quickReloadingTimerActive != param1 || this._intuitionCooldown != param2)
         {
            this._quickReloadingTimerActive = param1;
            this._intuitionCooldown = param2;
            this.updateQuickReloadingTimer();
         }
      }
      
      public function setReloadBoostBorderBlink() : void
      {
         if(this.reloadBoostBorder)
         {
            this.reloadBoostBorder.blink();
         }
      }
      
      public function setReloadBoostBorderVisible(param1:Boolean, param2:Boolean, param3:Boolean) : void
      {
         this._isReloadBoostBorder = param1;
         this._isReloadBoostBorderActive = param2;
         if(this.reloadBoostBorder)
         {
            this.reloadBoostBorder.visible = this._isReloadBoostBorder;
            this.reloadBoostBorder.updateState(this._isReloadBoostBorderActive,param3);
            this.reloadBoostBorder.x = this.timerProgressTextField.x - RELOAD_BORDER_OFFSET;
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
         }
      }
      
      public function setReloadingTime(param1:Number) : void
      {
         param1 = param1 < 0 ? Number(0) : Number(param1);
         if(this._currentReloadingTime != param1)
         {
            this._currentReloadingTime = param1;
            this.applyReloadingData();
         }
      }
      
      public function setSize(param1:Number, param2:Number) : void
      {
         this._width = param1;
         this._height = param2;
         this.updateNetSize();
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
            this.timerProgressTextField.visible = false;
            this.timerCompleteTextField.visible = false;
         }
         this._currentTimerTextField = !!this._isReloadInProgress ? this.timerProgressTextField : this.timerCompleteTextField;
         this._currentTimerTextField.visible = this._isShownReloading;
         this.reloadSwitchIcon.gotoAndStop(!!this._isReloadInProgress ? RELOAD_SWITCH_ICON_PROGRESS : RELOAD_SWITCH_ICON_COMPLETE);
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
               this.timerCompleteTextField.visible = this.timerCompleteTextField == this._currentTimerTextField;
               this.timerProgressTextField.visible = this.timerProgressTextField == this._currentTimerTextField;
            }
            else
            {
               this.timerCompleteTextField.visible = true;
               this.timerProgressTextField.visible = false;
            }
            this._quickReloadingTimerVisible = true;
         }
         else
         {
            this.timerCompleteTextField.visible = false;
            this.timerProgressTextField.visible = false;
            this._quickReloadingTimerVisible = false;
         }
         this._isShownReloading = param1;
         this.updateQuickReloadingTimer();
      }
      
      public function showShot() : void
      {
         if(this.isAutoloader)
         {
            this.autoloaderComponent.autoloaderShowShot();
         }
         else if(this.isExtraShot)
         {
            this.extraShotClipPanel.showShot();
            if(this._isReloadInProgress)
            {
               GTweener.removeTweens(this._reloadTimeColorTransform);
               this._reloadTimeColorTransform.color = this._timerProgressTextFieldColor;
               GTweener.from(this._reloadTimeColorTransform,RELOAD_TIME_BLINK_DURATION,RELOAD_TIME_COLOR_TRANSFORM_BLINK_VALUES,{
                  "ease":Cubic.easeIn,
                  "onChange":this.onReloadTimeColorTransformChange
               });
            }
         }
      }
      
      public function updateAmmoState(param1:String) : void
      {
      }
      
      public function updateAutoloaderState(param1:Number, param2:Number) : void
      {
         if(this.isAutoloader)
         {
            this.autoloaderComponent.updateQuantityInClip(param2,param1);
         }
      }
      
      public function updatePlayerInfo(param1:String) : void
      {
      }
      
      public function updateScaleWidget(param1:Number) : void
      {
      }
      
      protected function getSiegeNetScale(param1:Number, param2:Number) : Number
      {
         return Values.DEFAULT_SCALE;
      }
      
      protected function onDispose() : void
      {
         removeEventListener(CrosshairPanelEvent.SOUND,this.onCrosshairPanelSoundHandler);
         GTweener.removeTweens(this._reloadTimeColorTransform);
         this.reloadTimeBlink = null;
         this.reloadSwitchIcon = null;
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
         this.reloadBoostBorder = null;
         this._timerProgressTextFieldFilter.length = 0;
         this._timerProgressTextFieldFilter = null;
         this._timerCompleteTextFieldFilter.length = 0;
         this._timerCompleteTextFieldFilter = null;
         this._timerBoostedFilter.length = 0;
         this._timerBoostedFilter = null;
         this.autoloaderComponent.dispose();
         this.autoloaderComponent = null;
         this.extraShotClipPanel.dispose();
         this.extraShotClipPanel = null;
         this.controllableReloadCassette.dispose();
         this.controllableReloadCassette = null;
         if(this.shellCalibrationClipPanel)
         {
            this.shellCalibrationClipPanel.dispose();
            this.shellCalibrationClipPanel = null;
         }
         if(this.averageDamage)
         {
            this.averageDamage.dispose();
            this.averageDamage = null;
         }
         this.netSeparator = null;
         this.distance.dispose();
         this.distance = null;
         this.cassetteMC.dispose();
         this.cassetteMC = null;
         if(this._reloadTimeBlinkYPos)
         {
            this._reloadTimeBlinkYPos.length = 0;
            this._reloadTimeBlinkYPos = null;
         }
      }
      
      protected function arrangeReloadTimeBlink() : void
      {
         this.reloadTimeBlink.x = this._currentTimerTextField.x + (this._currentTimerTextField.textWidth >> 1) + TF_LEFT_MARGIN;
         this.reloadTimeBlink.y = this._reloadTimeBlinkYPos[this.netType];
      }
      
      protected function updateNetType() : void
      {
         gotoAndStop(TYPE_PREFIX + this.netType);
         this.updateNetSize();
      }
      
      protected function updateReloadingState() : void
      {
         this.setTimerReloadingState();
         if(this.reloadingState == CrosshairConsts.RELOADING_END)
         {
            this.reloadingAnimationMC.visible = true;
            this.reloadingAnimationMC.play();
         }
         else if(this.reloadingState == CrosshairConsts.RELOADING_ENDED)
         {
            this.reloadingAnimationMC.visible = true;
            this.reloadingAnimationMC.gotoAndStop(1);
         }
         else
         {
            this.reloadingAnimationMC.visible = false;
         }
      }
      
      protected function getReloadTimeBlinkYPos() : Array
      {
         return null;
      }
      
      private function onReloadTimeColorTransformChange() : void
      {
         this.timerProgressTextField.textColor = this._reloadTimeColorTransform.color;
      }
      
      private function updateNetSize() : void
      {
         var _loc1_:Number = Values.DEFAULT_SCALE;
         if(SIEGE_PILLBOX_NET_TYPES.indexOf(this.netType) >= 0)
         {
            _loc1_ = this.getSiegeNetScale(this._width,this._height);
         }
         this.netMC.scaleX = this.netMC.scaleY = _loc1_;
      }
      
      private function updateQuickReloadingTimer() : void
      {
         if(this.quickReloadingTimerTextField)
         {
            if(this._quickReloadingTimerVisible && this._quickReloadingTimerActive && StringUtils.isNotEmpty(this._intuitionCooldown))
            {
               this.quickReloadingTimerTextField.text = this._intuitionCooldown;
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
            this.netSeparator.visible = this._netSeparatorVisible && !this.isExtraShot;
         }
      }
      
      private function updateNetVisibility() : void
      {
         this.netMC.visible = (this._visibleNetMask & CROSSHAIR_CONSTANTS.VISIBLE_NET) != 0;
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
      
      private function updateHealthBarMC() : void
      {
         if(this.healthBarMC)
         {
            this.healthBarMC.gotoAndStop((this.healthBarMC.totalFrames - 1) * this.health + 1);
         }
      }
      
      private function setReloadingBarFrame() : void
      {
         if(this.reloadingBar)
         {
            this.updateReloadingState();
            this.reloadingBar.gotoAndStop((this.reloadingBar.totalFrames - 1) * this.reloadingTime + 1);
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
         this.autoloaderComponent.alpha = this.cassetteAlpha;
         this.extraShotClipPanel.alpha = this.cassetteAlpha;
         this.controllableReloadCassette.alpha = this.cassetteAlpha;
         if(this.shellCalibrationClipPanel)
         {
            this.shellCalibrationClipPanel.alpha = this.cassetteAlpha;
         }
      }
      
      private function updateNetSeparatorType() : void
      {
         if(this.netSeparator)
         {
            this.netSeparator.updateType(this._netSeparatorType);
         }
      }
      
      public function set reloadBoost(param1:Boolean) : void
      {
         this.timerProgressTextField.textColor = !!param1 ? uint(BOOSTED_TEXT_COLOR_RELOAD) : uint(this._timerProgressTextFieldColor);
         this.timerProgressTextField.filters = !!param1 ? this._timerBoostedFilter : this._timerProgressTextFieldFilter;
         this.timerCompleteTextField.textColor = !!param1 ? uint(BOOSTED_TEXT_COLOR) : uint(this._timerCompleteTextFieldColor);
         this.timerCompleteTextField.filters = !!param1 ? this._timerBoostedFilter : this._timerCompleteTextFieldFilter;
      }
      
      public function get autoloaderBoostParams() : BoostIndicatorStateParamsVO
      {
         return this.autoloaderComponent.autoloaderBoostParams;
      }
      
      public function set isUseFrameAnimation(param1:Boolean) : void
      {
         this.cassetteMC.isUseFrameAnimation = param1;
      }
      
      public function set isUseAlternateZoomPosition(param1:Boolean) : void
      {
      }
      
      public function set scaleWidgetEnabled(param1:Boolean) : void
      {
      }
      
      protected function get isCassette() : Boolean
      {
         return this._clipReloadingType == CLIP_RELOADING_TYPES.CASSETTE_CLIP;
      }
      
      protected function get isAutoloader() : Boolean
      {
         return this._clipReloadingType == CLIP_RELOADING_TYPES.AUTO_LOADER_CLIP;
      }
      
      protected function get isExtraShot() : Boolean
      {
         return this._clipReloadingType == CLIP_RELOADING_TYPES.EXTRA_SHOT_CLIP;
      }
      
      protected function get isControllableReload() : Boolean
      {
         return this._clipReloadingType == CLIP_RELOADING_TYPES.CONTROLLABLE_RELOAD;
      }
      
      protected function get isUnlimitedClip() : Boolean
      {
         return this._clipReloadingType == CLIP_RELOADING_TYPES.UNLIMITED_CLIP;
      }
      
      protected function get isShellCalibration() : Boolean
      {
         return this._clipReloadingType == CLIP_RELOADING_TYPES.SHELL_CALIBRATION_CLIP;
      }
      
      private function onCrosshairPanelSoundHandler(param1:CrosshairPanelEvent) : void
      {
         if(!visible)
         {
            param1.stopImmediatePropagation();
         }
      }
   }
}
