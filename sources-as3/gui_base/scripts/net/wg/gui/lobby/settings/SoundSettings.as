package net.wg.gui.lobby.settings
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import flash.events.IEventDispatcher;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFormatAlign;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Time;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ACOUSTICS;
   import net.wg.gui.components.advanced.ButtonBarEx;
   import net.wg.gui.components.advanced.ContentTabBar;
   import net.wg.gui.components.controls.BorderShadowScrollPane;
   import net.wg.gui.components.controls.CheckBox;
   import net.wg.gui.components.controls.DropdownMenu;
   import net.wg.gui.components.controls.InfoIcon;
   import net.wg.gui.components.controls.LabelControl;
   import net.wg.gui.components.controls.Slider;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.data.Aliases;
   import net.wg.gui.lobby.settings.components.KeyInput;
   import net.wg.gui.lobby.settings.components.SoundDeviceTabButton;
   import net.wg.gui.lobby.settings.components.WarningMessageBlock;
   import net.wg.gui.lobby.settings.components.evnts.KeyInputEvents;
   import net.wg.gui.lobby.settings.components.evnts.WarningMessageEvent;
   import net.wg.gui.lobby.settings.config.SettingsConfigHelper;
   import net.wg.gui.lobby.settings.events.AlternativeVoiceEvent;
   import net.wg.gui.lobby.settings.events.SettingViewEvent;
   import net.wg.gui.lobby.settings.vo.MessageBlockDataVO;
   import net.wg.gui.lobby.settings.vo.SettingsControlProp;
   import net.wg.gui.lobby.settings.vo.SettingsKeyProp;
   import net.wg.gui.lobby.settings.vo.base.SettingsDataVo;
   import net.wg.infrastructure.interfaces.IPopOverCaller;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICommons;
   import net.wg.utils.ICounterProps;
   import net.wg.utils.IUtils;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.ButtonEvent;
   import scaleform.clik.events.IndexEvent;
   import scaleform.clik.events.ListEvent;
   import scaleform.clik.events.SliderEvent;
   import scaleform.clik.interfaces.IDataProvider;
   
   public class SoundSettings extends SettingsBaseView implements IPopOverCaller
   {
      
      private static const VOICE_TEST_DURATION:Number = 10;
      
      private static const VOICE_TEST_UPDATE_RATE:Number = 0.1;
      
      private static const COMMON_TAB_INDEX:int = 0;
      
      private static const VIVOX_TAB_INDEX:int = 1;
      
      private static const SPECIAL_TAB_INDEX:int = 2;
      
      private static const ENABLE_ALPHA:Number = 1;
      
      private static const DISABLE_ALPHA:Number = 0.5;
      
      private static const SOUND_COUNTER_CONTAINER_ID:String = "SOUND_COUNTER_CONTAINER_ID";
      
      private static const COUNTER_CHECKBOX_OFFSET_X:int = -17;
      
      private static const BULB_VOICES_NULL_ERROR:String = "_existsBulbVoices";
      
      private static const ARTY_BULB_VOICES_NULL_ERROR:String = "_existsArtyBulbVoices";
      
      private static const COUNT_SLIDER_MIN_MAX_OPTIONS:int = 2;
      
      private static const PANE_WIDTH:uint = 800;
      
      private static const PANE_HEIGHT:uint = 518;
      
      private static const SHADOW_HEIGHT:uint = 20;
      
      private static const WARNING_MESSAGEM_BLOCK_X:uint = 400;
      
      private static const WARNING_MESSAGEM_BLOCK_PADDING:uint = 80;
      
      private static const PANE_HEIGHT_WITH_WARNING_BLOCK:uint = PANE_HEIGHT - WARNING_MESSAGEM_BLOCK_PADDING;
      
      private static const TOOLTIP_PREFIX:String = "sounds/";
      
      private static const SYSTEM_MIXER_WARNING_DATA:MessageBlockDataVO = new MessageBlockDataVO({
         "message":SETTINGS.SOUNDS_SYSTEMMIXERVOLUMEWARNING,
         "actionName":WarningMessageEvent.FIX_MIXER_SOUND,
         "buttonLabel":SETTINGS.SOUNDS_FIXBUTTON,
         "infoIconType":InfoIcon.TYPE_WARNING,
         "tooltip":TOOLTIPS.SYSTEMMIXERVOLUMEDISABLEDWARNING
      });
       
      
      public var scrollPane:BorderShadowScrollPane;
      
      private var _isVoiceTestStarted:Boolean = false;
      
      private var _vivoxTestTimeLeft:Number = 0;
      
      private var _toolTipMgr:ITooltipMgr;
      
      private var _existsBulbVoices:Array = null;
      
      private var _existsArtyBulbVoices:Array = null;
      
      private var _masterVolumeSelected:Boolean = false;
      
      private var _typeAcousticsSelected:Boolean = false;
      
      private var _isAcousticsAlertVisible:Boolean = false;
      
      private var _isVOIPButtonForceDisabled:Boolean = false;
      
      private var _isSystemMixerVolumeDisabled:Boolean = false;
      
      private var _warningMessageBlock:WarningMessageBlock = null;
      
      public function SoundSettings()
      {
         this._toolTipMgr = App.toolTipMgr;
         super();
      }
      
      override public function toString() : String
      {
         return "[WG SoundSettings " + name + "]";
      }
      
      override public function updateDependentData() : void
      {
         this.updatesPttKeyList();
      }
      
      override protected function getCounterProps(param1:String) : ICounterProps
      {
         if(param1 == SettingsConfigHelper.TYPE_CHECKBOX)
         {
            return new CounterProps(COUNTER_CHECKBOX_OFFSET_X,CounterProps.DEFAULT_OFFSET_Y,TextFormatAlign.LEFT,false,Linkages.COUNTER_LINE_UI);
         }
         return super.getCounterProps(param1);
      }
      
      override protected function getContainerId() : String
      {
         return SOUND_COUNTER_CONTAINER_ID;
      }
      
      override protected function configUI() : void
      {
         this.scrollPane.topShadow.height = this.scrollPane.bottomShadow.height = SHADOW_HEIGHT;
         this.scrollPane.setSize(PANE_WIDTH,PANE_HEIGHT);
         var _loc1_:SoundSettingsBase = this.getContent();
         _loc1_.soundSpeakersTestButton.addEventListener(ButtonEvent.CLICK,this.onSoundSpeakersTestButtonClickHandler);
         _loc1_.btnVivoxTest.addEventListener(ButtonEvent.CLICK,this.onBtnVivoxTestClickHandler);
         _loc1_.btnCaptureDevicesUpdate.addEventListener(ButtonEvent.CLICK,this.onBtnCaptureDevicesUpdateClickHandler);
         _loc1_.PTTKeyInput.addEventListener(KeyInputEvents.DISABLE_OVER,this.onPTTKeyInputDisableOverHandler);
         _loc1_.PTTKeyInput.addEventListener(KeyInputEvents.DISABLE_OUT,this.onPTTKeyInputDisableOutHandler);
         _loc1_.PTTKeyInput.addEventListener(KeyInputEvents.DISABLE_PRESS,this.onPTTKeyInputDisablePressHandler);
         _loc1_.PTTKeyInput.addEventListener(KeyInputEvents.CHANGE,this.onPTTKeyInputChangeHandler);
         _loc1_.PTTKeyInput.alertMessageAlias = TOOLTIPS.SETTING_WINDOW_CONTROLS_KEY_INPUT_PTT_WARNING;
         this.updatesPttKeyList();
         _loc1_.testAlternativeVoicesButton.addEventListener(ButtonEvent.CLICK,this.onTestAlternativeVoicesButtonClickHandler);
         _loc1_.testAlternativeVoicesButton.addEventListener(MouseEvent.MOUSE_OVER,this.onTestAlternativeVoicesButtonMouseOverHandler);
         _loc1_.testAlternativeVoicesButton.addEventListener(MouseEvent.MOUSE_OUT,this.onTestAlternativeVoicesButtonMouseOutHandler);
         _loc1_.bulbVoicesButton.addEventListener(ButtonEvent.CLICK,this.onTestBulbVoicesButtonClickHandler);
         _loc1_.bulbVoicesButton.addEventListener(MouseEvent.MOUSE_OVER,this.onTestBulbVoicesButtonMouseOverHandler);
         _loc1_.bulbVoicesButton.addEventListener(MouseEvent.MOUSE_OUT,this.onTestBulbVoicesButtonMouseOutHandler);
         _loc1_.artyBulbVoicesButton.addEventListener(ButtonEvent.CLICK,this.onArtyBulbVoicesButtonClickHandler);
         _loc1_.artyBulbVoicesButton.addEventListener(MouseEvent.MOUSE_OVER,this.onArtyBulbVoicesButtonMouseOverHandler);
         _loc1_.artyBulbVoicesButton.addEventListener(MouseEvent.MOUSE_OUT,this.onArtyBulbVoicesButtonMouseOutHandler);
         _loc1_.enableVoIPCheckbox.enabled = App.voiceChatMgr.getYY();
         _loc1_.tabs.addEventListener(IndexEvent.INDEX_CHANGE,this.onTabsIndexChangeHandler);
         super.configUI();
         registerToolTip(_loc1_.bulbVoicesDropDown,SettingsConfigHelper.BULB_VOICES);
         registerToolTip(_loc1_.bulbVoicesLabel,SettingsConfigHelper.BULB_VOICES);
         registerToolTip(_loc1_.masterVolumeToggleCheckbox,SettingsConfigHelper.MASTER_VOLUME_TOGGLE);
         registerToolTip(_loc1_.nightModeCheckbox,SettingsConfigHelper.NIGHT_MODE);
         registerToolTip(_loc1_.bassBoostCheckbox,SettingsConfigHelper.BASS_BOOST);
         registerToolTip(_loc1_.soundQualityCheckbox,SettingsConfigHelper.SOUND_QUALITY);
         registerToolTip(_loc1_.artyBulbVoicesIcon,SettingsConfigHelper.ARTY_BULB_VOICES);
         registerToolTip(_loc1_.artyBulbVoicesLabel,SettingsConfigHelper.ARTY_BULB_VOICES);
         registerToolTip(_loc1_.artyBulbVoicesDropDown,SettingsConfigHelper.ARTY_BULB_VOICES);
      }
      
      override protected function getTooltipID(param1:String) : String
      {
         return TOOLTIP_PREFIX + param1;
      }
      
      override protected function setData(param1:SettingsDataVo) : void
      {
         var _loc11_:String = null;
         var _loc13_:String = null;
         var _loc14_:String = null;
         var _loc15_:DisplayObject = null;
         var _loc17_:Boolean = false;
         var _loc18_:KeyInput = null;
         this.controlsUnsubscribe();
         super.setData(param1);
         var _loc2_:SoundSettingsBase = this.getContent();
         var _loc3_:SettingsControlProp = SettingsControlProp(param1.getByKey(SettingsConfigHelper.VOICE_CHAT_SUPPORTED));
         var _loc4_:Boolean = _loc3_.current;
         var _loc5_:Array = [{"label":SETTINGS.SOUNDS_TABCOMMON}];
         var _loc6_:Boolean = App.voiceChatMgr.getYY();
         if(_loc4_ || _loc6_)
         {
            _loc5_.push({"label":SETTINGS.SOUNDS_TABVIVOX});
            _loc2_.enableVoIPCheckbox.visible = true;
            this.showHideVoiceSettings(_loc4_);
         }
         var _loc7_:ContentTabBar = _loc2_.tabs;
         _loc7_.dataProvider = new DataProvider(_loc5_);
         _loc7_.visible = _loc5_.length > 1;
         var _loc8_:Vector.<String> = param1.keys;
         var _loc9_:Vector.<Object> = param1.values;
         var _loc10_:int = _loc8_.length;
         var _loc12_:SettingsControlProp = null;
         var _loc16_:int = 0;
         while(_loc16_ < _loc10_)
         {
            _loc11_ = _loc8_[_loc16_];
            _loc12_ = SettingsControlProp(_loc9_[_loc16_]);
            _loc13_ = _loc12_.type;
            _loc14_ = _loc11_ + _loc13_;
            _loc15_ = _loc2_[_loc14_] as DisplayObject;
            if(_loc15_)
            {
               _loc17_ = _loc12_.current != null;
               if(SettingsConfigHelper.TYPE_CHECKBOX == _loc13_)
               {
                  this.prepareCheckbox(CheckBox(_loc15_),_loc11_,_loc17_,_loc12_);
               }
               else if(SettingsConfigHelper.TYPE_SLIDER == _loc13_)
               {
                  this.prepareSlider(Slider(_loc15_),_loc11_,_loc17_,_loc12_);
               }
               else if(SettingsConfigHelper.TYPE_DROPDOWN == _loc13_)
               {
                  if(_loc11_ == SettingsConfigHelper.BULB_VOICES)
                  {
                     this._existsBulbVoices = _loc12_.extraData as Array;
                     App.utils.asserter.assertNotNull(this._existsBulbVoices,BULB_VOICES_NULL_ERROR + Errors.CANT_NULL);
                  }
                  else if(_loc11_ == SettingsConfigHelper.ARTY_BULB_VOICES)
                  {
                     this._existsArtyBulbVoices = _loc12_.extraData as Array;
                     App.utils.asserter.assertNotNull(this._existsArtyBulbVoices,ARTY_BULB_VOICES_NULL_ERROR + Errors.CANT_NULL);
                  }
                  this.prepareDropdown(DropdownMenu(_loc15_),_loc17_,_loc12_);
               }
               else if(SettingsConfigHelper.TYPE_KEYINPUT == _loc13_)
               {
                  _loc18_ = KeyInput(_loc15_);
                  _loc18_.key = Number(_loc12_.current);
                  _loc18_.validateNow();
               }
               else if(SettingsConfigHelper.TYPE_BUTTON_BAR == _loc13_)
               {
                  this.prepareButtonBar(ButtonBarEx(_loc15_),_loc11_,_loc17_,_loc12_);
               }
               trySetLabel(_loc11_);
            }
            else if(!_loc12_.readOnly)
            {
               App.utils.asserter.assert(false,_loc14_ + Errors.WASNT_FOUND);
            }
            _loc16_++;
         }
         this.updateMasterVolumeEnabled();
         this.updateVoiceChatEnabled();
         App.utils.scheduler.scheduleOnNextFrame(this.dispatchGetSystemOffStatus);
      }
      
      override protected function onDispose() : void
      {
         this.breakSoundCheck();
         this.forceFinishVivoxTest();
         var _loc1_:SoundSettingsBase = this.getContent();
         _loc1_.btnCaptureDevicesUpdate.removeEventListener(ButtonEvent.CLICK,this.onBtnCaptureDevicesUpdateClickHandler);
         _loc1_.soundSpeakersTestButton.removeEventListener(ButtonEvent.CLICK,this.onSoundSpeakersTestButtonClickHandler);
         _loc1_.btnVivoxTest.removeEventListener(ButtonEvent.CLICK,this.onBtnVivoxTestClickHandler);
         _loc1_.testAlternativeVoicesButton.removeEventListener(ButtonEvent.CLICK,this.onTestAlternativeVoicesButtonClickHandler);
         _loc1_.testAlternativeVoicesButton.removeEventListener(MouseEvent.MOUSE_OVER,this.onTestAlternativeVoicesButtonMouseOverHandler);
         _loc1_.testAlternativeVoicesButton.removeEventListener(MouseEvent.MOUSE_OUT,this.onTestAlternativeVoicesButtonMouseOutHandler);
         _loc1_.bulbVoicesButton.removeEventListener(ButtonEvent.CLICK,this.onTestBulbVoicesButtonClickHandler);
         _loc1_.bulbVoicesButton.removeEventListener(MouseEvent.MOUSE_OVER,this.onTestBulbVoicesButtonMouseOverHandler);
         _loc1_.bulbVoicesButton.removeEventListener(MouseEvent.MOUSE_OUT,this.onTestBulbVoicesButtonMouseOutHandler);
         _loc1_.artyBulbVoicesButton.removeEventListener(ButtonEvent.CLICK,this.onArtyBulbVoicesButtonClickHandler);
         _loc1_.artyBulbVoicesButton.removeEventListener(MouseEvent.MOUSE_OVER,this.onArtyBulbVoicesButtonMouseOverHandler);
         _loc1_.artyBulbVoicesButton.removeEventListener(MouseEvent.MOUSE_OUT,this.onArtyBulbVoicesButtonMouseOutHandler);
         _loc1_.PTTKeyInput.removeEventListener(KeyInputEvents.DISABLE_OVER,this.onPTTKeyInputDisableOverHandler);
         _loc1_.PTTKeyInput.removeEventListener(KeyInputEvents.DISABLE_OUT,this.onPTTKeyInputDisableOutHandler);
         _loc1_.PTTKeyInput.removeEventListener(KeyInputEvents.DISABLE_PRESS,this.onPTTKeyInputDisablePressHandler);
         _loc1_.PTTKeyInput.removeEventListener(KeyInputEvents.CHANGE,this.onPTTKeyInputChangeHandler);
         _loc1_.tabs.removeEventListener(IndexEvent.INDEX_CHANGE,this.onTabsIndexChangeHandler);
         this.controlsUnsubscribe();
         if(this._warningMessageBlock)
         {
            this._warningMessageBlock.dispose();
            this._warningMessageBlock = null;
         }
         this._toolTipMgr = null;
         this._existsBulbVoices = null;
         this._existsArtyBulbVoices = null;
         this.scrollPane.dispose();
         this.scrollPane = null;
         super.onDispose();
      }
      
      public function breakSoundCheck() : void
      {
         if(this._isVoiceTestStarted)
         {
            dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_VIVOX_TEST,viewId,null,Values.EMPTY_STR,false));
         }
      }
      
      public function getContent() : SoundSettingsBase
      {
         return this.scrollPane.target as SoundSettingsBase;
      }
      
      public function getHitArea() : DisplayObject
      {
         return this.getContent().soundSpeakersTestButton;
      }
      
      public function getTargetButton() : DisplayObject
      {
         return this.getContent().soundSpeakersTestButton;
      }
      
      public function isCanSelectAcousticType(param1:Boolean) : void
      {
         var _loc2_:SoundSettingsBase = null;
         if(param1)
         {
            _loc2_ = this.getContent();
            this.applyNewSoundSpeakers(_loc2_.soundSpeakersDropDown.selectedIndex);
            _loc2_.soundDeviceAlert.visible = this._isAcousticsAlertVisible = !param1;
         }
      }
      
      public function isPresetApply(param1:Boolean) : void
      {
         var _loc4_:SettingsControlProp = null;
         var _loc2_:SoundSettingsBase = this.getContent();
         var _loc3_:DropdownMenu = _loc2_.soundSpeakersDropDown;
         if(param1)
         {
            this.applyNewSoundSpeakers(_loc3_.selectedIndex);
            _loc2_.soundDeviceAlert.visible = this._isAcousticsAlertVisible = true;
         }
         else
         {
            _loc4_ = SettingsControlProp(data[SettingsConfigHelper.SOUND_SPEAKERS]);
            _loc3_.removeEventListener(ListEvent.INDEX_CHANGE,this.onDropdownIndexChangeHandler);
            _loc3_.selectedIndex = Number(_loc4_.changedVal);
            _loc3_.addEventListener(ListEvent.INDEX_CHANGE,this.onDropdownIndexChangeHandler);
         }
      }
      
      public function onViewChanged() : void
      {
         this.breakSoundCheck();
      }
      
      public function setCaptureDevices(param1:Number, param2:DataProvider) : void
      {
         var _loc3_:DropdownMenu = this.getContent().captureDeviceDropDown;
         _loc3_.dataProvider = param2;
         _loc3_.selectedIndex = param1;
         var _loc4_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc3_.name,SettingsConfigHelper.TYPE_DROPDOWN);
         var _loc5_:SettingsControlProp = SettingsControlProp(data[_loc4_]);
         if(param2.length != _loc5_.options.length)
         {
            _loc5_.current = -1;
         }
         _loc5_.options = param2;
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,_loc4_,param1));
         this.updateVoiceChatEnabled();
      }
      
      public function setSystemMixerVolumeDisabled(param1:Boolean) : void
      {
         this._isSystemMixerVolumeDisabled = param1;
         this.setMasterVolumeToggleCheckboxAdditionalProps();
      }
      
      public function setVOIPButtonState(param1:Boolean) : void
      {
         this._isVOIPButtonForceDisabled = !param1;
         this.getContent().btnVivoxTest.enabled = param1;
      }
      
      public function setVoiceTestReady(param1:Boolean) : void
      {
         var _loc2_:SoundSettingsBase = this.getContent();
         var _loc3_:SoundButtonEx = _loc2_.btnVivoxTest;
         _loc2_.voiceWaiting.visible = false;
         _loc3_.label = SETTINGS.SOUND_VIVOX_BUTTONS_TEST_START;
         if(param1)
         {
            _loc2_.voiceAnimation.speak(true);
            _loc3_.enabled = _loc2_.btnCaptureDevicesUpdate.enabled = false;
            this._vivoxTestTimeLeft = VOICE_TEST_DURATION;
            App.utils.scheduler.scheduleRepeatableTask(this.voiceTimerTest,VOICE_TEST_UPDATE_RATE * Time.MILLISECOND_IN_SECOND,VOICE_TEST_DURATION / VOICE_TEST_UPDATE_RATE + 1);
         }
         else
         {
            this.forceFinishVivoxTest();
         }
      }
      
      public function setVoiceTestStarted(param1:Boolean) : void
      {
         if(this._isVoiceTestStarted == param1)
         {
            return;
         }
         this._isVoiceTestStarted = param1;
         var _loc2_:SoundSettingsBase = this.getContent();
         _loc2_.voiceWaiting.visible = this._isVoiceTestStarted;
         if(!this._isVOIPButtonForceDisabled)
         {
            _loc2_.btnVivoxTest.enabled = !this._isVoiceTestStarted;
         }
         _loc2_.btnCaptureDevicesUpdate.enabled = !this._isVoiceTestStarted;
         _loc2_.btnVivoxTest.label = !!this._isVoiceTestStarted ? SETTINGS.SOUND_VIVOX_BUTTONS_TEST_INIT : SETTINGS.SOUND_VIVOX_BUTTONS_TEST_START;
         if(!this._isVoiceTestStarted)
         {
            this.forceFinishVivoxTest();
         }
      }
      
      public function updateAcousticDeviceByType(param1:String) : void
      {
         var _loc2_:SoundSettingsBase = this.getContent();
         var _loc3_:IDataProvider = _loc2_.soundSpeakersDropDown.dataProvider;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:int = _loc3_.length;
         var _loc5_:int = 0;
         var _loc6_:Object = null;
         _loc5_ = 0;
         while(_loc5_ < _loc4_)
         {
            _loc6_ = _loc3_.requestItemAt(_loc5_);
            if(_loc6_.hasOwnProperty(SettingsConfigHelper.SOUND_SPEAKERS_ID_FIELD) && _loc6_[SettingsConfigHelper.SOUND_SPEAKERS_ID_FIELD] == param1)
            {
               this.updateAcousticDeviceLabel(_loc6_);
               _loc2_.soundSpeakersTestButton.enabled = true;
               break;
            }
            _loc5_++;
         }
      }
      
      public function updatePTTControl(param1:Number) : void
      {
         this.getContent().PTTKeyInput.key = param1;
      }
      
      private function updatesPttKeyList() : void
      {
         var _loc7_:int = 0;
         var _loc8_:String = null;
         var _loc12_:Object = null;
         var _loc1_:KeyInput = this.getContent().PTTKeyInput;
         var _loc2_:SettingsConfigHelper = SettingsConfigHelper.instance;
         var _loc3_:SettingsDataVo = _loc2_.getDataItem(SettingsConfigHelper.CONTROLS_SETTINGS,true);
         var _loc4_:SettingsDataVo = SettingsDataVo(_loc3_.getByKey(SettingsConfigHelper.KEYBOARD));
         var _loc5_:Vector.<Object> = _loc4_.values;
         var _loc6_:Array = this.copyItemsInUpperCase(SettingsConfigHelper.pttKeyRange);
         var _loc9_:IUtils = App.utils;
         var _loc10_:ICommons = _loc9_.commons;
         var _loc11_:String = _loc9_.toUpperOrLowerCase(_loc10_.keyToString(_loc1_.key).keyCommand,true);
         for each(_loc12_ in _loc5_)
         {
            _loc8_ = _loc9_.toUpperOrLowerCase(_loc10_.keyToString(SettingsKeyProp(_loc12_).key).keyCommand,true);
            if(_loc8_ != _loc11_)
            {
               _loc7_ = _loc6_.indexOf(_loc9_.toUpperOrLowerCase(_loc8_,true));
               if(_loc7_ >= 0)
               {
                  _loc6_.splice(_loc7_,1);
               }
            }
         }
         _loc1_.keys = _loc6_;
      }
      
      private function copyItemsInUpperCase(param1:Array) : Array
      {
         var _loc3_:String = null;
         var _loc2_:Array = [];
         for each(_loc3_ in param1)
         {
            _loc2_.push(App.utils.toUpperOrLowerCase(_loc3_,true));
         }
         return _loc2_;
      }
      
      private function controlsUnsubscribe() : void
      {
         var _loc1_:String = null;
         var _loc2_:IEventDispatcher = null;
         var _loc3_:int = 0;
         var _loc4_:SoundSettingsBase = null;
         var _loc5_:String = null;
         var _loc6_:int = 0;
         if(data && data.keys)
         {
            _loc3_ = data.keys.length;
            _loc4_ = this.getContent();
            _loc6_ = 0;
            while(_loc6_ < _loc3_)
            {
               _loc1_ = data.keys[_loc6_];
               _loc5_ = SettingsControlProp(data.values[_loc6_]).type;
               _loc2_ = _loc4_[_loc1_ + _loc5_] as IEventDispatcher;
               if(_loc2_)
               {
                  if(_loc5_ == SettingsConfigHelper.TYPE_CHECKBOX)
                  {
                     _loc2_.removeEventListener(Event.SELECT,this.onCheckboxSelectHandler);
                  }
                  else if(_loc5_ == SettingsConfigHelper.TYPE_SLIDER)
                  {
                     _loc2_.removeEventListener(SliderEvent.VALUE_CHANGE,this.onSliderValueChangeHandler);
                  }
                  else if(_loc5_ == SettingsConfigHelper.TYPE_DROPDOWN)
                  {
                     _loc2_.removeEventListener(ListEvent.INDEX_CHANGE,this.onDropdownIndexChangeHandler);
                  }
                  else if(_loc5_ == SettingsConfigHelper.TYPE_BUTTON_BAR)
                  {
                     _loc2_.removeEventListener(IndexEvent.INDEX_CHANGE,this.onButtonBarIndexChangeHandler);
                  }
               }
               _loc6_++;
            }
         }
      }
      
      private function prepareButtonBar(param1:ButtonBarEx, param2:String, param3:Boolean, param4:SettingsControlProp) : void
      {
         param1.dataProvider = new DataProvider(param4.options);
         param1.selectedIndex = int(param4.current);
         param1.addEventListener(IndexEvent.INDEX_CHANGE,this.onButtonBarIndexChangeHandler);
         param1.enabled = param3;
         if(param2 == SettingsConfigHelper.SOUND_DEVICE)
         {
            this.updateSoundSpeakersDependencies(param1.selectedIndex,true);
         }
      }
      
      private function prepareDropdown(param1:DropdownMenu, param2:Boolean, param3:SettingsControlProp) : void
      {
         param1.dataProvider = new DataProvider(param3.options);
         param1.selectedIndex = int(param3.current);
         param1.addEventListener(ListEvent.INDEX_CHANGE,this.onDropdownIndexChangeHandler);
         param1.enabled = param2;
      }
      
      private function prepareSlider(param1:Slider, param2:String, param3:Boolean, param4:SettingsControlProp) : void
      {
         param1.value = Number(param4.current);
         param1.addEventListener(SliderEvent.VALUE_CHANGE,this.onSliderValueChangeHandler);
         var _loc5_:SoundSettingsBase = this.getContent();
         var _loc6_:LabelControl = _loc5_[param2 + SettingsConfigHelper.TYPE_VALUE] as LabelControl;
         if(_loc6_ && param4.hasValue)
         {
            _loc6_.text = param4.current.toString();
         }
         var _loc7_:Array = param4.options;
         if(_loc7_ && _loc7_.length == COUNT_SLIDER_MIN_MAX_OPTIONS)
         {
            param1.minimum = _loc7_[0];
            param1.maximum = _loc7_[1];
         }
         param1.enabled = param3;
      }
      
      private function prepareCheckbox(param1:CheckBox, param2:String, param3:Boolean, param4:SettingsControlProp) : void
      {
         var _loc5_:Boolean = false;
         param1.selected = param4.current;
         param1.addEventListener(Event.SELECT,this.onCheckboxSelectHandler);
         if(param2 == SettingsConfigHelper.ENABLE_VO_IP)
         {
            param1.enabled = param3 && SettingsControlProp(data[SettingsConfigHelper.VOICE_CHAT_SUPPORTED]).current;
         }
         else if(param2 == SettingsConfigHelper.MASTER_VOLUME_TOGGLE)
         {
            param1.infoIcoType = !!param1.selected ? Values.EMPTY_STR : InfoIcon.TYPE_WARNING;
            param1.toolTip = !!param1.selected ? Values.EMPTY_STR : TOOLTIPS.MASTERVOLUMETOGGLEOFF;
         }
         else if(param2 == SettingsConfigHelper.SOUND_QUALITY)
         {
            param1.visible = SettingsControlProp(data[SettingsConfigHelper.SOUND_QUALITY_VISIBLE]).current;
            _loc5_ = param1.selected && param1.visible;
            param1.infoIcoType = !!_loc5_ ? InfoIcon.TYPE_WARNING : Values.EMPTY_STR;
            param1.toolTip = !!_loc5_ ? TOOLTIPS.SOUNDQUALITYON : Values.EMPTY_STR;
            if(param1.visible)
            {
               param1.enabled = param3 && SettingsControlProp(data[SettingsConfigHelper.MASTER_VOLUME_TOGGLE]).current;
            }
         }
         else
         {
            param1.enabled = param3;
         }
      }
      
      private function voiceTimerTest() : void
      {
         this._vivoxTestTimeLeft -= VOICE_TEST_UPDATE_RATE;
         if(this._vivoxTestTimeLeft > 0)
         {
            this.getContent().voiceAnimationText.text = this._vivoxTestTimeLeft.toFixed(1);
         }
         else
         {
            dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_VIVOX_TEST,viewId,null,Values.EMPTY_STR,false));
         }
      }
      
      private function forceFinishVivoxTest() : void
      {
         App.utils.scheduler.cancelTask(this.voiceTimerTest);
         var _loc1_:SoundSettingsBase = this.getContent();
         this._isVoiceTestStarted = false;
         this._vivoxTestTimeLeft = 0;
         _loc1_.voiceAnimationText.text = Values.EMPTY_STR;
         if(!this._isVOIPButtonForceDisabled)
         {
            _loc1_.btnVivoxTest.enabled = true;
         }
         _loc1_.btnCaptureDevicesUpdate.enabled = true;
         _loc1_.voiceAnimation.speak(false);
         _loc1_.voiceWaiting.visible = false;
      }
      
      private function updateMasterVolumeEnabled() : void
      {
         var _loc1_:SoundSettingsBase = this.getContent();
         this._masterVolumeSelected = _loc1_.masterVolumeToggleCheckbox.selected;
         _loc1_.masterVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.masterVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.masterVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.guiVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.guiVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.guiVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.vehiclesVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.vehiclesVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.vehiclesVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.voiceNotificationVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.voiceNotificationVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.voiceNotificationVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.effectsVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.effectsVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.effectsVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.ambientVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.ambientVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.ambientVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.musicVolumeLabel.enabled = this._masterVolumeSelected;
         _loc1_.musicVolumeSlider.enabled = this._masterVolumeSelected;
         _loc1_.musicVolumeValue.enabled = this._masterVolumeSelected;
         _loc1_.musicHangarLabel.enabled = this._masterVolumeSelected;
         _loc1_.musicHangarSlider.enabled = this._masterVolumeSelected;
         _loc1_.musicHangarValue.enabled = this._masterVolumeSelected;
         if(_loc1_.soundDeviceButtonBar != null)
         {
            _loc1_.soundDeviceButtonBar.enabled = this._masterVolumeSelected;
         }
         _loc1_.bassBoostCheckbox.enabled = this._masterVolumeSelected;
         _loc1_.nightModeCheckbox.enabled = this._masterVolumeSelected;
         _loc1_.testAlternativeVoicesButton.enabled = this._masterVolumeSelected;
         var _loc2_:SoundCommonForm = _loc1_.commonForm;
         var _loc3_:UILoaderAlt = _loc2_.bulbIcon;
         _loc3_.alpha = !!this._masterVolumeSelected ? Number(ENABLE_ALPHA) : Number(DISABLE_ALPHA);
         _loc3_.enabled = this._masterVolumeSelected;
         _loc1_.bulbVoicesLabel.enabled = this._masterVolumeSelected;
         var _loc4_:DropdownMenu = _loc1_.bulbVoicesDropDown;
         _loc4_.enabled = this._masterVolumeSelected;
         _loc1_.bulbVoicesButton.enabled = this._masterVolumeSelected && this._existsBulbVoices[_loc4_.selectedIndex];
         var _loc5_:UILoaderAlt = _loc1_.artyBulbVoicesIcon;
         _loc5_.alpha = !!this._masterVolumeSelected ? Number(ENABLE_ALPHA) : Number(DISABLE_ALPHA);
         _loc5_.enabled = this._masterVolumeSelected;
         _loc1_.artyBulbVoicesLabel.enabled = this._masterVolumeSelected;
         var _loc6_:DropdownMenu = _loc1_.artyBulbVoicesDropDown;
         _loc6_.enabled = this._masterVolumeSelected;
         _loc1_.artyBulbVoicesButton.enabled = this._masterVolumeSelected && this._existsArtyBulbVoices[_loc6_.selectedIndex];
         var _loc7_:UILoaderAlt = _loc2_.alternativeVoicesIcon;
         _loc7_.alpha = !!this._masterVolumeSelected ? Number(ENABLE_ALPHA) : Number(DISABLE_ALPHA);
         _loc7_.enabled = this._masterVolumeSelected;
         _loc1_.alternativeVoicesDropDown.enabled = this._masterVolumeSelected;
         _loc1_.alternativeVoicesLabel.enabled = this._masterVolumeSelected;
         _loc1_.soundQualityCheckbox.enabled = this._masterVolumeSelected;
         _loc1_.subtitlesCheckbox.enabled = this._masterVolumeSelected;
         _loc1_.soundSpeakersTestButton.enabled = this._masterVolumeSelected;
         this.updateSoundSpeakersDropDown();
         this.setMasterVolumeToggleCheckboxAdditionalProps();
      }
      
      private function updateVoiceChatEnabled() : void
      {
         this.breakSoundCheck();
         var _loc1_:SoundSettingsBase = this.getContent();
         var _loc2_:Boolean = _loc1_.enableVoIPCheckbox.selected && SettingsControlProp(data[SettingsConfigHelper.VOICE_CHAT_SUPPORTED]).current;
         _loc1_.btnCaptureDevicesUpdate.enabled = _loc2_;
         _loc1_.masterVivoxVolumeLabel.enabled = _loc2_;
         _loc1_.masterVivoxVolumeSlider.enabled = _loc2_;
         _loc1_.masterFadeVivoxVolumeLabel.enabled = _loc2_;
         _loc1_.masterFadeVivoxVolumeSlider.enabled = _loc2_;
         var _loc3_:DropdownMenu = _loc1_.captureDeviceDropDown;
         var _loc4_:Boolean = _loc2_ && _loc3_.dataProvider.length > 0;
         _loc3_.enabled = _loc4_;
         _loc1_.captureDeviceLabel.enabled = _loc4_;
         _loc1_.micVivoxVolumeLabel.enabled = _loc4_;
         _loc1_.micVivoxVolumeSlider.enabled = _loc4_;
         if(!this._isVOIPButtonForceDisabled)
         {
            _loc1_.btnVivoxTest.enabled = _loc4_;
         }
         _loc1_.micVivoxVolumeValue.enabled = _loc2_;
         _loc1_.masterFadeVivoxVolumeValue.enabled = _loc2_;
         _loc1_.masterVivoxVolumeValue.enabled = _loc2_;
      }
      
      private function showHideVoiceSettings(param1:Boolean) : void
      {
         var _loc2_:SoundSettingsBase = this.getContent();
         _loc2_.voiceConnectFieldSet.visible = param1;
         _loc2_.PTTLabel.visible = param1;
         _loc2_.PTTKeyInput.visible = param1;
         _loc2_.captureDeviceLabel.visible = param1;
         _loc2_.captureDeviceDropDown.visible = param1;
         _loc2_.btnCaptureDevicesUpdate.visible = param1;
         _loc2_.btnVivoxTest.visible = param1;
         _loc2_.voiceAnimation.visible = param1;
         var _loc3_:TextField = _loc2_.voiceAnimationText;
         _loc3_.text = !!param1 ? _loc3_.text : Values.EMPTY_STR;
         _loc2_.masterVivoxVolumeLabel.visible = param1;
         _loc2_.masterVivoxVolumeSlider.visible = param1;
         _loc2_.masterVivoxVolumeValue.visible = param1;
         _loc2_.micVivoxVolumeLabel.visible = param1;
         _loc2_.micVivoxVolumeSlider.visible = param1;
         _loc2_.micVivoxVolumeValue.visible = param1;
         _loc2_.masterFadeVivoxVolumeLabel.visible = param1;
         _loc2_.masterFadeVivoxVolumeSlider.visible = param1;
         _loc2_.masterFadeVivoxVolumeValue.visible = param1;
      }
      
      private function hideTooltip() : void
      {
         this._toolTipMgr.hide();
      }
      
      private function updateAcousticDeviceLabel(param1:Object) : void
      {
         if(param1 && param1.hasOwnProperty(SettingsConfigHelper.SOUND_SPEAKERS_TOOLTIP_FIELD) && param1.hasOwnProperty(SettingsConfigHelper.SOUND_SPEAKERS_ID_FIELD))
         {
            this.updateSoundDeviceLabel(ACOUSTICS.TYPE_ACOUSTICS,param1[SettingsConfigHelper.SOUND_SPEAKERS_TOOLTIP_FIELD],param1[SettingsConfigHelper.SOUND_SPEAKERS_ID_FIELD]);
         }
      }
      
      private function updateSoundDeviceLabel(param1:String, param2:String, param3:String) : void
      {
         this.getContent().soundDeviceButtonBar.updateDataById(param1,param2,param3);
      }
      
      private function applyNewSoundSpeakers(param1:Number) : void
      {
         var _loc2_:SettingsControlProp = SettingsControlProp(data[SettingsConfigHelper.SOUND_SPEAKERS]);
         _loc2_.changedVal = param1;
         var _loc3_:Object = _loc2_.options[param1];
         this.updateAcousticDeviceLabel(_loc3_);
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,SettingsConfigHelper.SOUND_SPEAKERS,param1));
      }
      
      private function updateSoundSpeakersDependencies(param1:Number, param2:Boolean) : void
      {
         var _loc3_:SettingsControlProp = SettingsControlProp(data[SettingsConfigHelper.SOUND_DEVICE]);
         var _loc4_:String = _loc3_.options[param1][SettingsConfigHelper.SOUND_DEVICE_ID_FIELD];
         this._typeAcousticsSelected = _loc4_ == ACOUSTICS.TYPE_ACOUSTICS;
         this.updateSoundSpeakersDropDown();
         var _loc5_:InfoIcon = this.getContent().soundDeviceAlert;
         if(this._typeAcousticsSelected)
         {
            if(param2)
            {
               this._isAcousticsAlertVisible = _loc3_.options[param1][SettingsConfigHelper.SOUND_DEVICE_ALERT_FIELD];
            }
            _loc5_.visible = this._isAcousticsAlertVisible;
         }
         else
         {
            _loc5_.visible = _loc3_.options[param1][SettingsConfigHelper.SOUND_DEVICE_ALERT_FIELD];
         }
      }
      
      private function updateSoundSpeakersDropDown() : void
      {
         this.getContent().soundSpeakersDropDown.enabled = this._masterVolumeSelected && this._typeAcousticsSelected;
      }
      
      private function setMasterVolumeToggleCheckboxAdditionalProps() : void
      {
         var _loc3_:Class = null;
         var _loc1_:CheckBox = this.getContent().masterVolumeToggleCheckbox;
         _loc1_.infoIcoType = !!this._masterVolumeSelected ? Values.EMPTY_STR : InfoIcon.TYPE_WARNING;
         _loc1_.toolTip = !!this._masterVolumeSelected ? Values.EMPTY_STR : TOOLTIPS.MASTERVOLUMETOGGLEOFF;
         var _loc2_:Boolean = this._masterVolumeSelected && this._isSystemMixerVolumeDisabled;
         if(_loc2_ && !this._warningMessageBlock)
         {
            _loc3_ = App.utils.classFactory.getClass(Linkages.WARNING_MESSAGE_SETTING_BLOCK);
            this._warningMessageBlock = new _loc3_();
            this._warningMessageBlock.x = WARNING_MESSAGEM_BLOCK_X;
            this._warningMessageBlock.setData(SYSTEM_MIXER_WARNING_DATA);
            addChild(this._warningMessageBlock);
         }
         this.scrollPane.y = !!_loc2_ ? Number(WARNING_MESSAGEM_BLOCK_PADDING) : Number(0);
         this.scrollPane.setSize(PANE_WIDTH,!!_loc2_ ? Number(PANE_HEIGHT_WITH_WARNING_BLOCK) : Number(PANE_HEIGHT));
         if(this._warningMessageBlock)
         {
            this._warningMessageBlock.visible = _loc2_;
         }
      }
      
      private function dispatchGetSystemOffStatus() : void
      {
         dispatchEvent(new SettingViewEvent(SettingViewEvent.GET_SYSTEM_OFF_STATUS,viewId));
      }
      
      private function onBtnVivoxTestClickHandler(param1:ButtonEvent) : void
      {
         if(this._isVoiceTestStarted)
         {
            return;
         }
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_VIVOX_TEST,viewId,null,Values.EMPTY_STR,true));
      }
      
      private function onPTTKeyInputDisablePressHandler(param1:KeyInputEvents) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onPTTKeyInputDisableOutHandler(param1:KeyInputEvents) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onPTTKeyInputChangeHandler(param1:KeyInputEvents) : void
      {
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,SettingsConfigHelper.CONTROLS_SETTINGS,SettingsConfigHelper.KEYBOARD,SettingsConfigHelper.PUSH_TO_TALK,param1.keyCode));
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_PTT_SOUND_CONTROL_CHANGED,SettingsConfigHelper.CONTROLS_SETTINGS,SettingsConfigHelper.KEYBOARD,SettingsConfigHelper.PUSH_TO_TALK,param1.keyCode));
      }
      
      private function onPTTKeyInputDisableOverHandler(param1:KeyInputEvents) : void
      {
         this._toolTipMgr.showComplex(TOOLTIPS.SETTINGS_DIALOG_SOUND_PTTKEY,null);
      }
      
      private function onTestAlternativeVoicesButtonMouseOutHandler(param1:MouseEvent) : void
      {
         this.hideTooltip();
      }
      
      private function onTestAlternativeVoicesButtonMouseOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.showComplex(TOOLTIPS.SETTINGS_DIALOG_SOUND_ALTERNATIVEVOICES);
      }
      
      private function onTestAlternativeVoicesButtonClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new AlternativeVoiceEvent(AlternativeVoiceEvent.ON_TEST_ALTERNATIVE_VOICES));
      }
      
      private function onTestBulbVoicesButtonMouseOutHandler(param1:MouseEvent) : void
      {
         this.hideTooltip();
      }
      
      private function onTestBulbVoicesButtonMouseOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.showComplex(TOOLTIPS.SETTINGS_DIALOG_SOUND_ALTERNATIVEVOICES);
      }
      
      private function onTestBulbVoicesButtonClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new AlternativeVoiceEvent(AlternativeVoiceEvent.ON_TEST_BULB_VOICES,this.getContent().bulbVoicesDropDown.selectedIndex));
      }
      
      private function onArtyBulbVoicesButtonMouseOutHandler(param1:MouseEvent) : void
      {
         this.hideTooltip();
      }
      
      private function onArtyBulbVoicesButtonMouseOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.showComplex(TOOLTIPS.SETTINGS_DIALOG_SOUND_ALTERNATIVEVOICES);
      }
      
      private function onArtyBulbVoicesButtonClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new AlternativeVoiceEvent(AlternativeVoiceEvent.ON_TEST_ARTY_BULB_VOICES,this.getContent().artyBulbVoicesDropDown.selectedIndex));
      }
      
      private function onBtnCaptureDevicesUpdateClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_UPDATE_CAPTURE_DEVICE,viewId));
      }
      
      private function onSoundSpeakersTestButtonClickHandler(param1:ButtonEvent) : void
      {
         var _loc2_:SoundDeviceTabButton = SoundDeviceTabButton(this.getContent().soundDeviceButtonBar.selectedButton);
         App.popoverMgr.show(this,Aliases.ACOUSTIC_POPOVER,_loc2_.speakerId);
      }
      
      private function onCheckboxSelectHandler(param1:Event) : void
      {
         var _loc2_:CheckBox = CheckBox(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_CHECKBOX);
         if(_loc3_ == SettingsConfigHelper.ENABLE_VO_IP)
         {
            this.updateVoiceChatEnabled();
         }
         else if(_loc3_ == SettingsConfigHelper.MASTER_VOLUME_TOGGLE)
         {
            this.updateMasterVolumeEnabled();
         }
         else if(_loc3_ == SettingsConfigHelper.SOUND_QUALITY)
         {
            _loc2_.toolTip = _loc2_.selected && _loc2_.visible ? TOOLTIPS.SOUNDQUALITYON : Values.EMPTY_STR;
            _loc2_.infoIcoType = _loc2_.selected && _loc2_.visible ? InfoIcon.TYPE_WARNING : Values.EMPTY_STR;
         }
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,_loc3_,_loc2_.selected));
      }
      
      private function onSliderValueChangeHandler(param1:SliderEvent) : void
      {
         var _loc2_:Slider = Slider(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_SLIDER);
         var _loc4_:SoundSettingsBase = this.getContent();
         var _loc5_:SettingsControlProp = SettingsControlProp(data[_loc3_]);
         var _loc6_:LabelControl = _loc4_[_loc3_ + SettingsConfigHelper.TYPE_VALUE] as LabelControl;
         if(_loc6_ && _loc5_.hasValue)
         {
            _loc6_.text = _loc2_.value.toString();
         }
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,_loc3_,_loc2_.value));
      }
      
      private function onDropdownIndexChangeHandler(param1:ListEvent) : void
      {
         var _loc5_:SettingsControlProp = null;
         var _loc6_:Object = null;
         var _loc7_:Boolean = false;
         var _loc2_:DropdownMenu = DropdownMenu(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_DROPDOWN);
         var _loc4_:SoundSettingsBase = this.getContent();
         if(_loc3_ == SettingsConfigHelper.BULB_VOICES)
         {
            _loc4_.bulbVoicesButton.enabled = this._existsBulbVoices[_loc4_.bulbVoicesDropDown.selectedIndex];
         }
         else if(_loc3_ == SettingsConfigHelper.ARTY_BULB_VOICES)
         {
            _loc4_.artyBulbVoicesButton.enabled = this._existsArtyBulbVoices[_loc4_.artyBulbVoicesDropDown.selectedIndex];
         }
         if(_loc3_ == SettingsConfigHelper.SOUND_SPEAKERS)
         {
            _loc5_ = SettingsControlProp(data[SettingsConfigHelper.SOUND_SPEAKERS]);
            _loc6_ = _loc5_.options[_loc2_.selectedIndex];
            _loc7_ = _loc6_[SettingsConfigHelper.SOUND_SPEAKERS_IS_AUTODETECT_FIELD];
            if(_loc7_)
            {
               _loc4_.soundSpeakersTestButton.enabled = false;
               _loc4_.soundDeviceButtonBar.updateDataById(ACOUSTICS.TYPE_ACOUSTICS,Values.EMPTY_STR,Values.EMPTY_STR);
               dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_AUTO_DETECT_ACOUSTIC,viewId));
               dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,_loc3_,_loc2_.selectedIndex));
               _loc5_.changedVal = _loc2_.selectedIndex;
               _loc4_.soundDeviceAlert.visible = this._isAcousticsAlertVisible = false;
            }
            else
            {
               dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_SOUND_SPEAKER_CHANGE,viewId,null,_loc3_,_loc2_.selectedIndex));
            }
         }
         else
         {
            dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,_loc3_,_loc2_.selectedIndex));
         }
      }
      
      private function onButtonBarIndexChangeHandler(param1:IndexEvent) : void
      {
         var _loc2_:ButtonBarEx = ButtonBarEx(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_BUTTON_BAR);
         if(_loc3_ == SettingsConfigHelper.SOUND_DEVICE)
         {
            this.updateSoundSpeakersDependencies(_loc2_.selectedIndex,false);
         }
         dispatchEvent(new SettingViewEvent(SettingViewEvent.ON_CONTROL_CHANGED,viewId,null,_loc3_,_loc2_.selectedIndex));
      }
      
      private function onTabsIndexChangeHandler(param1:IndexEvent) : void
      {
         var _loc2_:SoundSettingsBase = this.getContent();
         var _loc3_:SoundCommonForm = _loc2_.commonForm;
         var _loc4_:SoundVivoxForm = _loc2_.vivoxForm;
         var _loc5_:SoundSpecialForm = _loc2_.specialForm;
         _loc3_.visible = false;
         _loc4_.visible = false;
         _loc5_.visible = false;
         switch(param1.index)
         {
            case COMMON_TAB_INDEX:
               _loc3_.visible = true;
               break;
            case VIVOX_TAB_INDEX:
               _loc4_.visible = true;
               break;
            case SPECIAL_TAB_INDEX:
               _loc5_.visible = true;
         }
      }
   }
}
