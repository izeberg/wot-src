package net.wg.gui.lobby.settings
{
   import flash.events.Event;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormatAlign;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.CheckBox;
   import net.wg.gui.components.controls.DropdownMenu;
   import net.wg.gui.components.controls.InfoIcon;
   import net.wg.gui.components.controls.LabelControl;
   import net.wg.gui.components.controls.Slider;
   import net.wg.gui.lobby.settings.components.RadioButtonBar;
   import net.wg.gui.lobby.settings.config.SettingsConfigHelper;
   import net.wg.gui.lobby.settings.events.SettingsSubVewEvent;
   import net.wg.gui.lobby.settings.vo.SettingsControlProp;
   import net.wg.gui.lobby.settings.vo.base.SettingsDataVo;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterProps;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.IndexEvent;
   import scaleform.clik.events.ListEvent;
   import scaleform.clik.events.SliderEvent;
   
   public class SettingsArmorFlashlightForm extends SettingsNewCountersForm implements ISettingsAimForm
   {
      
      private static const INFO_ICON_X_PADDING:int = 8;
      
      private static const CHECKBOX_COUNTER_OFFSET_X:int = -7;
      
      private static const MAX_TOOLTIP_WIDTH:uint = 270;
      
      private static const OPACITY_VISUAL_MAX:uint = 100;
       
      
      public var armorFlashlightPerformanceImpactLabel:TextField = null;
      
      public var armorFlashlightPerformanceImpactInfoIcon:InfoIcon = null;
      
      public var armorFlashlightResolutionScalingLabel:TextField = null;
      
      public var armorFlashlightResolutionScalingInfoIcon:InfoIcon = null;
      
      public var armorFlashlightResolutionScalingDropDown:DropdownMenu = null;
      
      public var armorFlashlightEnabledCheckbox:CheckBox = null;
      
      public var armorFlashlightColorSchemaLabel:TextField = null;
      
      public var armorFlashlightColorSchemaButtonBar:RadioButtonBar = null;
      
      public var armorFlashlightFillLabel:TextField = null;
      
      public var armorFlashlightFillButtonBar:RadioButtonBar = null;
      
      public var armorFlashlightOpacityLabel:TextField = null;
      
      public var armorFlashlightOpacitySlider:Slider = null;
      
      public var armorFlashlightOpacityValue:LabelControl = null;
      
      private var _data:Object = null;
      
      private var _formId:String = null;
      
      public function SettingsArmorFlashlightForm()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.armorFlashlightPerformanceImpactLabel.text = SETTINGS.AIM_ARMORFLASHLIGHT_PERFORMANCEIMPACT;
         this.armorFlashlightPerformanceImpactInfoIcon.icoType = InfoIcon.TYPE_WARNING;
         this.armorFlashlightPerformanceImpactInfoIcon.tooltip = TOOLTIPS.ARMORFLASHLIGHT_PERFORMANCEIMPACTINFO;
         this.armorFlashlightPerformanceImpactInfoIcon.tooltipMaxWidth = MAX_TOOLTIP_WIDTH;
         this.armorFlashlightPerformanceImpactInfoIcon.x = this.armorFlashlightPerformanceImpactLabel.x + this.armorFlashlightPerformanceImpactLabel.textWidth + INFO_ICON_X_PADDING;
         this.armorFlashlightResolutionScalingLabel.text = SETTINGS.AIM_ARMORFLASHLIGHT_RESOLUTIONSCALING;
         this.armorFlashlightResolutionScalingInfoIcon.icoType = InfoIcon.TYPE_INFO;
         this.armorFlashlightResolutionScalingInfoIcon.tooltip = TOOLTIPS.ARMORFLASHLIGHT_RESOLUTIONSCALINGINFO;
         this.armorFlashlightResolutionScalingInfoIcon.tooltipMaxWidth = MAX_TOOLTIP_WIDTH;
         this.armorFlashlightResolutionScalingInfoIcon.x = this.armorFlashlightResolutionScalingLabel.x + this.armorFlashlightResolutionScalingLabel.textWidth + INFO_ICON_X_PADDING;
         this.armorFlashlightColorSchemaLabel.text = SETTINGS.AIM_ARMORFLASHLIGHT_COLORSCHEMAS;
         this.armorFlashlightOpacityLabel.text = SETTINGS.AIM_ARMORFLASHLIGHT_OPACITY;
         this.armorFlashlightFillLabel.text = SETTINGS.AIM_ARMORFLASHLIGHT_FILL_LABEL;
         this.armorFlashlightEnabledCheckbox.multiline = true;
         this.armorFlashlightEnabledCheckbox.wordWrap = true;
         this.armorFlashlightEnabledCheckbox.addEventListener(Event.SELECT,this.onCheckBoxSelectHandler);
         this.armorFlashlightColorSchemaButtonBar.setInfoIconTooltipWidth(MAX_TOOLTIP_WIDTH);
         this.armorFlashlightColorSchemaButtonBar.autoSize = TextFieldAutoSize.LEFT;
         this.armorFlashlightColorSchemaButtonBar.addEventListener(IndexEvent.INDEX_CHANGE,this.onButtonBarIndexChangeHandler);
         this.armorFlashlightFillButtonBar.autoSize = TextFieldAutoSize.LEFT;
         this.armorFlashlightFillButtonBar.addEventListener(IndexEvent.INDEX_CHANGE,this.onButtonBarIndexChangeHandler);
         this.armorFlashlightOpacitySlider.addEventListener(SliderEvent.VALUE_CHANGE,this.onSliderValueChangeHandler);
      }
      
      override protected function onDispose() : void
      {
         this.armorFlashlightPerformanceImpactLabel = null;
         this.armorFlashlightPerformanceImpactInfoIcon.dispose();
         this.armorFlashlightPerformanceImpactInfoIcon = null;
         this.armorFlashlightResolutionScalingLabel = null;
         this.armorFlashlightResolutionScalingInfoIcon.dispose();
         this.armorFlashlightResolutionScalingInfoIcon = null;
         this.armorFlashlightResolutionScalingDropDown.removeEventListener(ListEvent.INDEX_CHANGE,this.onDropDownIndexChangeHandler);
         this.armorFlashlightResolutionScalingDropDown.dispose();
         this.armorFlashlightResolutionScalingDropDown = null;
         this.armorFlashlightEnabledCheckbox.dispose();
         this.armorFlashlightEnabledCheckbox.removeEventListener(Event.SELECT,this.onCheckBoxSelectHandler);
         this.armorFlashlightEnabledCheckbox = null;
         this.armorFlashlightColorSchemaButtonBar.dispose();
         this.armorFlashlightColorSchemaButtonBar.removeEventListener(ListEvent.INDEX_CHANGE,this.onButtonBarIndexChangeHandler);
         this.armorFlashlightColorSchemaButtonBar = null;
         this.armorFlashlightFillButtonBar.dispose();
         this.armorFlashlightFillButtonBar.removeEventListener(ListEvent.INDEX_CHANGE,this.onButtonBarIndexChangeHandler);
         this.armorFlashlightFillButtonBar = null;
         this.armorFlashlightOpacitySlider.dispose();
         this.armorFlashlightOpacitySlider.removeEventListener(SliderEvent.VALUE_CHANGE,this.onSliderValueChangeHandler);
         this.armorFlashlightOpacitySlider = null;
         super.onDispose();
      }
      
      private function getSelectedIndex(param1:SettingsControlProp) : int
      {
         var _loc2_:int = param1.options.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            if(param1.options[_loc3_].data == param1.current)
            {
               return _loc3_;
            }
            _loc3_++;
         }
         return Values.DEFAULT_INT;
      }
      
      override protected function getControlPropsByKey(param1:String) : SettingsControlProp
      {
         if(this._data && this._data[param1])
         {
            return this._data[param1];
         }
         return super.getControlPropsByKey(param1);
      }
      
      override public function get formId() : String
      {
         return this._formId;
      }
      
      public function get data() : SettingsDataVo
      {
         return this._data as SettingsDataVo;
      }
      
      public function setData(param1:String, param2:Object) : void
      {
         var _loc3_:Vector.<String> = null;
         var _loc4_:Vector.<Object> = null;
         var _loc5_:int = 0;
         var _loc6_:String = null;
         var _loc7_:SettingsControlProp = null;
         var _loc8_:int = 0;
         var _loc9_:DropdownMenu = null;
         var _loc10_:CheckBox = null;
         var _loc11_:RadioButtonBar = null;
         var _loc12_:int = 0;
         var _loc13_:Slider = null;
         var _loc14_:LabelControl = null;
         var _loc15_:int = 0;
         this._formId = param1;
         if(param2 != null)
         {
            this._data = param2;
            _loc3_ = param2.keys;
            _loc4_ = param2.values;
            _loc5_ = _loc3_.length;
            _loc6_ = Values.EMPTY_STR;
            _loc7_ = null;
            _loc8_ = 0;
            for(; _loc8_ < _loc5_; _loc8_++)
            {
               _loc6_ = _loc3_[_loc8_];
               _loc7_ = _loc4_[_loc8_] as SettingsControlProp;
               App.utils.asserter.assertNotNull(_loc7_,"values[i] must be SettingsControlProp");
               if(!this[_loc6_ + _loc7_.type])
               {
                  continue;
               }
               switch(_loc7_.type)
               {
                  case SettingsConfigHelper.TYPE_DROPDOWN:
                     _loc9_ = this[_loc6_ + _loc7_.type];
                     _loc9_.dataProvider = new DataProvider(_loc7_.options);
                     _loc9_.menuRowCount = _loc7_.options is Array ? Number(_loc7_.options.length) : Number(0);
                     _loc9_.selectedIndex = this.getSelectedIndex(_loc7_);
                     _loc9_.enabled = _loc7_.extraData.enabled;
                     _loc9_.addEventListener(ListEvent.INDEX_CHANGE,this.onDropDownIndexChangeHandler);
                     break;
                  case SettingsConfigHelper.TYPE_CHECKBOX:
                     _loc10_ = this[_loc6_ + _loc7_.type];
                     _loc10_.selected = _loc7_.current;
                     _loc10_.enabled = _loc7_.extraData.enabled;
                     _loc10_.label = _loc7_.extraData.label;
                     _loc10_.toolTip = _loc7_.extraData.tooltip;
                     if(_loc10_.toolTip != null)
                     {
                        _loc10_.infoIcoType = InfoIcon.TYPE_INFO;
                        _loc10_.infoIcoFixedY = true;
                     }
                     _loc10_.validateNow();
                     break;
                  case SettingsConfigHelper.TYPE_BUTTON_BAR:
                     _loc11_ = this[_loc6_ + _loc7_.type];
                     _loc12_ = _loc7_.options.length;
                     _loc11_.dataProvider = new DataProvider(_loc7_.options);
                     _loc15_ = 0;
                     while(_loc15_ < _loc12_)
                     {
                        _loc11_.setInfoButton(_loc7_.options[_loc15_].tooltip,_loc15_);
                        _loc15_++;
                     }
                     _loc11_.selectedIndex = int(_loc7_.current);
                     _loc11_.enabled = _loc7_.extraData.enabled;
                     _loc11_.validateNow();
                     break;
                  case SettingsConfigHelper.TYPE_SLIDER:
                     _loc13_ = Slider(this[_loc6_ + _loc7_.type]);
                     _loc13_.value = Number(_loc7_.current) * OPACITY_VISUAL_MAX;
                     _loc13_.enabled = _loc7_.extraData.enabled;
                     _loc13_.validateNow();
                     _loc14_ = this[_loc6_ + SettingsConfigHelper.TYPE_VALUE] as LabelControl;
                     if(_loc14_ != null)
                     {
                        _loc14_.text = _loc13_.value.toString();
                     }
                     _loc14_.validateNow();
                     break;
               }
            }
         }
         else
         {
            this.disableAllControls();
         }
         invalidate();
      }
      
      private function disableAllControls() : void
      {
         this.armorFlashlightEnabledCheckbox.enabled = false;
         this.armorFlashlightColorSchemaButtonBar.enabled = false;
         this.armorFlashlightResolutionScalingDropDown.enabled = false;
         this.armorFlashlightFillButtonBar.enabled = false;
         this.armorFlashlightOpacitySlider.enabled = false;
         this.armorFlashlightOpacityValue.enabled = false;
      }
      
      private function onCheckBoxSelectHandler(param1:Event) : void
      {
         var _loc2_:CheckBox = CheckBox(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_CHECKBOX);
         dispatchEvent(new SettingsSubVewEvent(SettingsSubVewEvent.ON_CONTROL_CHANGE,this.formId,_loc3_,_loc2_.selected));
      }
      
      private function onButtonBarIndexChangeHandler(param1:IndexEvent) : void
      {
         var _loc2_:RadioButtonBar = RadioButtonBar(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_BUTTON_BAR);
         dispatchEvent(new SettingsSubVewEvent(SettingsSubVewEvent.ON_CONTROL_CHANGE,this.formId,_loc3_,_loc2_.selectedIndex));
      }
      
      private function onSliderValueChangeHandler(param1:SliderEvent) : void
      {
         var _loc2_:Slider = Slider(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_SLIDER);
         var _loc4_:LabelControl = this[_loc3_ + SettingsConfigHelper.TYPE_VALUE] as LabelControl;
         _loc4_.text = _loc2_.value.toString();
         dispatchEvent(new SettingsSubVewEvent(SettingsSubVewEvent.ON_CONTROL_CHANGE,this.formId,_loc3_,_loc2_.value / OPACITY_VISUAL_MAX));
      }
      
      override protected function getCounterProps(param1:String) : ICounterProps
      {
         if(param1 == SettingsConfigHelper.TYPE_CHECKBOX)
         {
            return new CounterProps(CHECKBOX_COUNTER_OFFSET_X,CounterProps.DEFAULT_OFFSET_Y,TextFormatAlign.LEFT,false,Linkages.COUNTER_LINE_UI);
         }
         return super.getCounterProps(param1);
      }
      
      private function onDropDownIndexChangeHandler(param1:ListEvent) : void
      {
         var _loc2_:DropdownMenu = DropdownMenu(param1.target);
         var _loc3_:String = SettingsConfigHelper.instance.getControlIdByControlNameAndType(_loc2_.name,SettingsConfigHelper.TYPE_DROPDOWN);
         dispatchEvent(new SettingsSubVewEvent(SettingsSubVewEvent.ON_CONTROL_CHANGE,this._formId,_loc3_,_loc2_.dataProvider[_loc2_.selectedIndex].data));
      }
   }
}
