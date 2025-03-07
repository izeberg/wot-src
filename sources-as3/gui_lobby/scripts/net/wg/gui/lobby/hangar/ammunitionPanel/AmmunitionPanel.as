package net.wg.gui.lobby.hangar.ammunitionPanel
{
   import flash.display.InteractiveObject;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.gui.components.vehicleStatus.VehicleStatus;
   import net.wg.gui.components.vehicleStatus.data.VehicleStatusVO;
   import net.wg.gui.components.vehicleStatus.events.VehicleStatusEvent;
   import net.wg.gui.lobby.hangar.ammunitionPanel.data.AmmunitionPanelBtnVO;
   import net.wg.gui.lobby.hangar.ammunitionPanel.data.AmmunitionPanelVO;
   import net.wg.infrastructure.base.meta.impl.AmmunitionPanelMeta;
   import net.wg.infrastructure.events.ChildVisibilityEvent;
   import net.wg.infrastructure.events.FocusRequestEvent;
   import net.wg.infrastructure.interfaces.IUniversalBtn;
   import net.wg.infrastructure.managers.ITooltipFormatter;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.infrastructure.managers.counter.CounterManager;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   import net.wg.utils.IUtils;
   import net.wg.utils.StageSizeBoundaries;
   import net.wg.utils.helpLayout.HelpLayoutVO;
   import scaleform.clik.events.ButtonEvent;
   
   public class AmmunitionPanel extends AmmunitionPanelMeta implements IAmmunitionPanel
   {
      
      private static const DEFAULT_BUTTON_WIDTH:int = 132;
      
      private static const REDUCED_BUTTON_WIDTH:int = 35;
      
      public static const SLOTS_HEIGHT_AND_OFFSET:int = 30;
      
      private static const VEHICLE_STATUS_INVALID:String = "vehicleStatusInvalid";
      
      private static const TO_RENT_LEFT_MARGIN:int = 5;
      
      private static const INV_MAINTENANCE_STATE:String = "InvMaintenanceState";
      
      private static const INV_HIGHLIGHT_ETE:String = "InvHighlightETE";
      
      private static const INV_BUTTONS:String = "invButtons";
      
      private static const INV_BUTTONS_LAYOUT:String = "invButtonsLayout";
      
      private static const INV_SIZE:String = "invSize";
      
      private static const OFFSET_BTN_TO_RENT:int = 3;
      
      private static const INDENT_BETWEEN_BUTTONS:int = 11;
      
      private static const COUNTER_PROPS:CounterProps = new CounterProps(3,-1);
      
      private static const VEHICLE_STATUS_TO_BUTTONS_OFFSET_Y:int = -6;
      
      private static const VEHICLE_STATUS_TO_SLOTS_OFFSET_Y:int = 0;
      
      private static const SOUND_MAINTENANCE_BTN:String = "maitenanceBtn";
      
      private static const SOUND_TUNING_BTN:String = "customizationBtn";
      
      private static const SOUND_BTN_TYPE:String = "iconTextButton";
      
      private static const BTN_TEXT_FIELD_PADDING:int = 10;
      
      private static const SHINE_REPEAT_COUNT:int = 4;
      
      private static const SHINE_DELAY:int = 1000;
       
      
      public var vehicleStatus:VehicleStatus = null;
      
      public var maintenanceBtn:UniversalBtn = null;
      
      public var easyTankEquipBtn:UniversalBtn = null;
      
      public var customizationBtn:UniversalBtn = null;
      
      public var changeNationBtn:UniversalBtn = null;
      
      public var toRent:SoundButtonEx = null;
      
      private var _maintenanceStateWarning:Boolean = false;
      
      private var _isEasyTankEquipHighlight:Boolean = false;
      
      private var _toolTipMgr:ITooltipMgr;
      
      private var _utils:IUtils;
      
      private var _statusVo:VehicleStatusVO = null;
      
      private var _screenWidth:int = 0;
      
      private var _counterManager:ICounterManager;
      
      private var _buttonWidth:int = 132;
      
      private var _buttonsOrder:Vector.<IUniversalBtn>;
      
      private var _buttonsData:AmmunitionPanelVO = null;
      
      private var _disableAllBtns:Boolean = false;
      
      private var _btnToID:Dictionary = null;
      
      public function AmmunitionPanel()
      {
         this._toolTipMgr = App.toolTipMgr;
         this._utils = App.utils;
         super();
         this._btnToID = new Dictionary();
         this._btnToID[this.maintenanceBtn] = AmmunitionPanelVO.MAINTENANCE;
         this._btnToID[this.customizationBtn] = AmmunitionPanelVO.CUSTOMIZATION;
         this._btnToID[this.changeNationBtn] = AmmunitionPanelVO.CHANGE_NATION;
         this._btnToID[this.easyTankEquipBtn] = AmmunitionPanelVO.EASY_TANK_EQUIP;
         this._buttonsOrder = new <IUniversalBtn>[this.easyTankEquipBtn,this.customizationBtn,this.changeNationBtn,this.maintenanceBtn];
         this._counterManager = App.utils.counterManager;
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.customizationBtn.enabled = false;
         App.waiting.addEventListener(ChildVisibilityEvent.CHILD_SHOWN,this.onChildShownHandler);
         App.waiting.addEventListener(ChildVisibilityEvent.CHILD_HIDDEN,this.onChildHiddenHandler);
      }
      
      override protected function onBeforeDispose() : void
      {
         var _loc1_:IUniversalBtn = null;
         for each(_loc1_ in this._buttonsOrder)
         {
            _loc1_.removeEventListener(MouseEvent.ROLL_OVER,this.onBtnRollOverHandler);
            _loc1_.removeEventListener(MouseEvent.ROLL_OUT,this.onBtnRollOutHandler);
            _loc1_.removeEventListener(Event.RESIZE,this.onResizeHandler);
            _loc1_.removeEventListener(ButtonEvent.CLICK,this.onBtnClickHandler);
         }
         App.waiting.removeEventListener(ChildVisibilityEvent.CHILD_SHOWN,this.onChildShownHandler);
         App.waiting.removeEventListener(ChildVisibilityEvent.CHILD_HIDDEN,this.onChildHiddenHandler);
         this.vehicleStatus.removeEventListener(VehicleStatusEvent.RESIZE,this.onVehicleStatusResizeHandler);
         this.toRent.removeEventListener(MouseEvent.ROLL_OVER,this.onBtnRollOverHandler);
         this.toRent.removeEventListener(MouseEvent.ROLL_OUT,this.onBtnRollOutHandler);
         this.toRent.removeEventListener(ButtonEvent.CLICK,this.onToRentClickHandler);
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         var _loc2_:* = null;
         var _loc1_:UniversalBtn = null;
         for(_loc2_ in this._btnToID)
         {
            _loc1_ = UniversalBtn(_loc2_);
            this._counterManager.removeCounter(_loc1_);
            _loc1_.dispose();
         }
         _loc1_ = null;
         App.instance.utils.data.cleanupDynamicObject(this._btnToID);
         this._btnToID = null;
         this._counterManager = null;
         this.maintenanceBtn = null;
         this.easyTankEquipBtn = null;
         this.customizationBtn = null;
         this.changeNationBtn = null;
         this.vehicleStatus.dispose();
         this.vehicleStatus = null;
         this.toRent.dispose();
         this.toRent = null;
         this._buttonsData = null;
         this._statusVo = null;
         this._toolTipMgr = null;
         this._utils = null;
         this._buttonsOrder.splice(0,this._buttonsOrder.length);
         this._buttonsOrder = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:AmmunitionPanelBtnVO = null;
         super.draw();
         if(this._statusVo != null && isInvalid(VEHICLE_STATUS_INVALID))
         {
            this.setVehicleStatus();
         }
         if(isInvalid(INV_MAINTENANCE_STATE))
         {
            this.maintenanceBtn.switchAlertIndicatorVisible(this._maintenanceStateWarning);
         }
         if(isInvalid(INV_HIGHLIGHT_ETE))
         {
            _loc1_ = false;
            if(this._buttonsData)
            {
               _loc2_ = this._buttonsData.getBtnData(AmmunitionPanelVO.EASY_TANK_EQUIP);
               _loc1_ = _loc2_ && _loc2_.visible && _loc2_.enabled;
            }
            if(_loc1_ && this._isEasyTankEquipHighlight)
            {
               this.easyTankEquipBtn.shine(SHINE_REPEAT_COUNT,SHINE_DELAY);
            }
            else
            {
               this.easyTankEquipBtn.stopShine();
            }
         }
         if(this._buttonsData && isInvalid(INV_BUTTONS))
         {
            this.doUpdateButtons();
            invalidate(INV_SIZE);
         }
         if(isInvalid(INV_SIZE))
         {
            this.resizeBtn(this.changeNationBtn);
            invalidate(INV_BUTTONS_LAYOUT);
         }
         if(isInvalid(INV_BUTTONS_LAYOUT))
         {
            this.layoutItems();
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.configureButton(this.maintenanceBtn,MENU.HANGAR_AMMUNITIONPANEL_MAITENANCEBTN,SOUND_MAINTENANCE_BTN);
         this.configureButton(this.easyTankEquipBtn,MENU.HANGAR_AMMUNITIONPANEL_EASYTANKEQUIPBTN,SOUND_TUNING_BTN);
         this.configureButton(this.customizationBtn,MENU.HANGAR_AMMUNITIONPANEL_TUNINGBTN,SOUND_TUNING_BTN);
         this.configureButton(this.changeNationBtn,MENU.HANGAR_AMMUNITIONPANEL_NATIONCHANGEBTN,SOUND_TUNING_BTN,true);
         this.toRent.addEventListener(MouseEvent.ROLL_OVER,this.onBtnRollOverHandler);
         this.toRent.addEventListener(MouseEvent.ROLL_OUT,this.onBtnRollOutHandler);
         this.toRent.addEventListener(ButtonEvent.CLICK,this.onToRentClickHandler);
         this.vehicleStatus.addEventListener(VehicleStatusEvent.RESIZE,this.onVehicleStatusResizeHandler);
         this._utils.helpLayout.registerComponent(this);
         _deferredDispose = true;
      }
      
      override protected function updateVehicleStatus(param1:VehicleStatusVO) : void
      {
         this._statusVo = param1;
         invalidate(VEHICLE_STATUS_INVALID);
      }
      
      public function as_highlightEasyTankEquip(param1:Boolean) : void
      {
         if(this._isEasyTankEquipHighlight != param1)
         {
            this._isEasyTankEquipHighlight = param1;
            invalidate(INV_HIGHLIGHT_ETE);
         }
      }
      
      public function as_setCustomizationBtnCounter(param1:int) : void
      {
         if(param1 > 0)
         {
            this._counterManager.setCounter(this.customizationBtn,param1.toString());
         }
         else
         {
            this._counterManager.removeCounter(this.customizationBtn);
         }
      }
      
      public function as_setMaintenanceWarningState(param1:Boolean) : void
      {
         if(this._maintenanceStateWarning != param1)
         {
            this._maintenanceStateWarning = param1;
            invalidate(INV_MAINTENANCE_STATE);
         }
      }
      
      public function getComponentForFocus() : InteractiveObject
      {
         return this.toRent;
      }
      
      public function getLayoutProperties() : Vector.<HelpLayoutVO>
      {
         return new <HelpLayoutVO>[this.vehicleStatus.createHelpLayoutData()];
      }
      
      public function updateButtons(param1:AmmunitionPanelVO) : void
      {
         this._buttonsData = param1;
         invalidate(INV_BUTTONS);
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         if(this._screenWidth != param1)
         {
            this._screenWidth = param1;
            invalidate(INV_SIZE);
         }
      }
      
      private function placeVehicleStatus() : void
      {
         this.vehicleStatus.x = this.width >> 1;
         var _loc1_:int = Boolean(this._buttonsData) && this._buttonsData.isAnyButtonVisible ? int(VEHICLE_STATUS_TO_BUTTONS_OFFSET_Y) : int(this.maintenanceBtn.height + VEHICLE_STATUS_TO_SLOTS_OFFSET_Y);
         this.vehicleStatus.y = this.maintenanceBtn.y - this.vehicleStatus.height + _loc1_ | 0;
      }
      
      private function configureButton(param1:UniversalBtn, param2:String, param3:String, param4:Boolean = false) : void
      {
         param1.mouseEnabledOnDisabled = true;
         param1.soundType = SOUND_BTN_TYPE;
         param1.soundId = param3;
         param1.changeSizeOnlyUpwards = true;
         param1.paddingHorizontal = BTN_TEXT_FIELD_PADDING;
         if(param4)
         {
            this.resizeBtn(param1,param2);
         }
         else
         {
            param1.width = this._buttonWidth;
            param1.label = param2;
         }
         param1.addEventListener(ButtonEvent.CLICK,this.onBtnClickHandler);
         param1.addEventListener(MouseEvent.ROLL_OVER,this.onBtnRollOverHandler);
         param1.addEventListener(MouseEvent.ROLL_OUT,this.onBtnRollOutHandler);
         param1.addEventListener(Event.RESIZE,this.onResizeHandler);
         App.utils.universalBtnStyles.setStyle(param1,UniversalBtnStylesConst.STYLE_SLIM_GREEN);
      }
      
      private function setVehicleStatus() : void
      {
         this.vehicleStatus.setData(this._statusVo);
         if(this._statusVo.rentAvailable)
         {
            dispatchEvent(new FocusRequestEvent(FocusRequestEvent.REQUEST_FOCUS,this));
         }
      }
      
      private function doUpdateButtons() : void
      {
         var _loc2_:* = null;
         var _loc1_:UniversalBtn = null;
         for(_loc2_ in this._btnToID)
         {
            _loc1_ = UniversalBtn(_loc2_);
            this.updateBtn(_loc1_,this._buttonsData.getBtnData(this._btnToID[_loc1_]));
         }
      }
      
      private function updateBtn(param1:UniversalBtn, param2:AmmunitionPanelBtnVO) : void
      {
         if(param2 == null)
         {
            return;
         }
         if(param2.visible)
         {
            param1.enabled = param2.enabled && !this._disableAllBtns;
            param1.tooltip = param2.tooltip;
            if(param2.isNew)
            {
               this._counterManager.setCounter(param1,CounterManager.EXCLAMATION_COUNTER_VALUE,null,COUNTER_PROPS);
            }
         }
         if(!param2.isNew || !param2.visible)
         {
            this._counterManager.removeCounter(param1);
         }
         param1.visible = param2.visible;
      }
      
      private function layoutItems() : void
      {
         var _loc2_:IUniversalBtn = null;
         var _loc1_:int = 0;
         for each(_loc2_ in this._buttonsOrder)
         {
            if(_loc2_.visible)
            {
               _loc2_.x = _loc1_;
               _loc1_ += _loc2_.width + INDENT_BETWEEN_BUTTONS;
            }
            else
            {
               _loc2_.x = 0;
            }
         }
         this.placeVehicleStatus();
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      private function resizeBtn(param1:UniversalBtn, param2:String = "#menu:hangar/ammunitionPanel/nationChangeBtn") : void
      {
         if(this._screenWidth < StageSizeBoundaries.WIDTH_1366)
         {
            param1.width = REDUCED_BUTTON_WIDTH;
            param1.iconSource = RES_ICONS.MAPS_ICONS_BUTTONS_NC_ICON_19X22;
            param1.label = Values.EMPTY_STR;
         }
         else
         {
            param1.width = this._buttonWidth;
            param1.iconSource = Values.EMPTY_STR;
            param1.label = param2;
         }
      }
      
      override public function get width() : Number
      {
         var _loc4_:* = null;
         if(this._buttonsData == null)
         {
            return Values.ZERO;
         }
         var _loc1_:int = -INDENT_BETWEEN_BUTTONS;
         var _loc2_:AmmunitionPanelBtnVO = null;
         var _loc3_:UniversalBtn = null;
         for(_loc4_ in this._btnToID)
         {
            _loc3_ = UniversalBtn(_loc4_);
            _loc2_ = this._buttonsData.getBtnData(this._btnToID[_loc3_]);
            if(_loc2_ && _loc2_.visible)
            {
               _loc1_ += _loc3_.width + INDENT_BETWEEN_BUTTONS;
            }
         }
         return _loc1_ > Values.ZERO ? Number(_loc1_) : Number(Values.ZERO);
      }
      
      private function onVehicleStatusResizeHandler(param1:VehicleStatusEvent) : void
      {
         if(this._statusVo != null)
         {
            this.placeVehicleStatus();
            this.toRent.x = this.vehicleStatus.statusEndX + TO_RENT_LEFT_MARGIN;
            this.toRent.y = this.vehicleStatus.statusStartY + OFFSET_BTN_TO_RENT;
            this.toRent.visible = this._statusVo.rentAvailable;
         }
      }
      
      private function onBtnClickHandler(param1:ButtonEvent) : void
      {
         if(param1.target == this.easyTankEquipBtn)
         {
            showEasyTankEquipS();
         }
         else if(param1.target == this.customizationBtn)
         {
            showCustomizationS();
         }
         else if(param1.target == this.changeNationBtn)
         {
            showChangeNationS();
         }
         else if(param1.target == this.maintenanceBtn)
         {
            showRepairDialogS();
         }
      }
      
      private function onBtnRollOverHandler(param1:MouseEvent) : void
      {
         var _loc2_:String = null;
         var _loc3_:ITooltipFormatter = null;
         var _loc4_:AmmunitionPanelBtnVO = null;
         if(param1.target == this.toRent)
         {
            _loc3_ = this._toolTipMgr.getNewFormatter();
            _loc3_.addBody(TOOLTIPS.HANGAR_STATUS_TORENT,true);
            _loc2_ = _loc3_.make();
         }
         else if(param1.target in this._btnToID && this._buttonsData)
         {
            _loc4_ = this._buttonsData.getBtnData(this._btnToID[param1.target]);
            _loc2_ = Boolean(_loc4_) ? _loc4_.tooltip : Values.EMPTY_STR;
         }
         this._toolTipMgr.showComplex(_loc2_);
      }
      
      private function onBtnRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onToRentClickHandler(param1:ButtonEvent) : void
      {
         if(this._statusVo.rentAvailable)
         {
            toRentContinueS();
         }
      }
      
      private function onChildShownHandler(param1:ChildVisibilityEvent) : void
      {
         this._disableAllBtns = true;
         invalidate(INV_BUTTONS,INV_HIGHLIGHT_ETE);
      }
      
      private function onChildHiddenHandler(param1:ChildVisibilityEvent) : void
      {
         this._disableAllBtns = false;
         invalidate(INV_BUTTONS);
      }
      
      private function onResizeHandler(param1:Event) : void
      {
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         var _loc5_:IUniversalBtn = null;
         var _loc2_:int = param1.currentTarget.width;
         if(_loc2_ > this._buttonWidth)
         {
            _loc3_ = this._buttonsOrder.length;
            this._buttonWidth = _loc2_;
            _loc4_ = 0;
            while(_loc4_ < _loc3_)
            {
               _loc5_ = this._buttonsOrder[_loc4_];
               if(!(this._screenWidth < StageSizeBoundaries.WIDTH_1366 && _loc5_ == this.changeNationBtn))
               {
                  if(_loc5_.width != _loc2_)
                  {
                     _loc5_.width = _loc2_;
                  }
               }
               _loc4_++;
            }
         }
         invalidate(INV_SIZE);
      }
   }
}
