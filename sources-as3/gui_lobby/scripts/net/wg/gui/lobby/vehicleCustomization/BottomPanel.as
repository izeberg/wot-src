package net.wg.gui.lobby.vehicleCustomization
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.InteractiveObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Point;
   import net.wg.data.ListDAAPIDataProvider;
   import net.wg.data.VO.TankCarouselFilterSelectedVO;
   import net.wg.data.constants.SoundTypes;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CUSTOMIZATION_ALIASES;
   import net.wg.data.constants.generated.CUSTOMIZATION_CONSTS;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.gui.events.FiltersEvent;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationCarouselInfoLabel;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationCarouselOverlay;
   import net.wg.gui.lobby.vehicleCustomization.data.BottomPanelVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationBottomPanelInitVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationBottomPanelNotificationVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationTabNavigatorVO;
   import net.wg.gui.lobby.vehicleCustomization.data.FilterFallbackDataVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselDataVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselFilterVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationItemEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationTabEvent;
   import net.wg.gui.lobby.vehicleCustomization.progressionStyles.StageSwitcher;
   import net.wg.gui.notification.events.NotificationLayoutEvent;
   import net.wg.infrastructure.base.meta.ICustomizationBottomPanelMeta;
   import net.wg.infrastructure.base.meta.impl.CustomizationBottomPanelMeta;
   import net.wg.infrastructure.interfaces.IFocusChainContainer;
   import net.wg.infrastructure.interfaces.IPopOverCaller;
   import net.wg.infrastructure.managers.IPopoverManager;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.utils.IUtils;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   import scaleform.gfx.MouseEventEx;
   
   public class BottomPanel extends CustomizationBottomPanelMeta implements ICustomizationBottomPanelMeta, IFocusChainContainer, IPopOverCaller
   {
      
      private static const TABS_BACKGROUND_HEIGHT:int = 42;
      
      private static const TABS_BACKGROUND_HEIGHT_MIN_RESOLUTION:int = 38;
      
      private static const SM_PADDING_X:int = 5;
      
      private static const SM_PADDING_Y:int = 20;
      
      private static const SM_BILL_ADDITIONAL_HEIGHT:int = 26;
      
      private static const INVALID_SCROLL_POS:String = "InvalidScrollPos";
      
      private static const BUY_OFFSET_VERTICAL:int = 26;
      
      private static const BUY_OFFSET_HORIZONTAL:int = 15;
      
      private static const PRICE_OFFSET_VERTICAL:int = -20;
      
      private static const PRICE_OFFSET_HORIZONTAL:int = 13;
      
      private static const STAGE_SWITCHER_Y:int = -85;
      
      private static const CAROUSEL_Y:int = -75;
      
      private static const CAROUSEL_Y_SMALL:int = -94;
      
      private static const ITEMS_BUTTON_OFFSET:int = 5;
      
      private static const NON_HISTORIC_ICON_OFFSET_X:int = 25;
      
      private static const NON_HISTORIC_FIX_ICON_WIDTH:int = 60;
      
      private static const TOP_SMALL_OFFSET:int = 6;
      
      private static const BUY_BACKGROUND_Y:int = 4;
      
      private static const NON_HISTORIC_ICON_Y:int = 12;
      
      private static const ITEMS_INFO_BTN_ALPHA:Number = 0.6;
      
      private static const POPOVER_BUTTON_STATE_INVALID:String = "popoverBtnStateInvalid";
      
      private static const RIGHT_BTNS_VISIBILITY_INVALID:String = "rightBtnsVisibilityInvalid";
       
      
      public var tabBg:MovieClip = null;
      
      public var carousel:CustomizationCarousel = null;
      
      public var buyBtn:UniversalBtn = null;
      
      public var background:Sprite = null;
      
      public var buyBackground:Sprite = null;
      
      public var tabGlow:Sprite = null;
      
      public var customizationContentTypeIcon:CustomizationFadeInFadeOutMovieClip = null;
      
      public var infoLabel:CustomizationCarouselInfoLabel = null;
      
      public var bill:CustomizationBill = null;
      
      public var tabNavigator:CustomizationTabNavigator;
      
      public var itemsPopoverBtn:UniversalBtn = null;
      
      public var vehiclesSidebarBtn:UniversalBtn = null;
      
      public var overlay:CustomizationCarouselOverlay = null;
      
      public var helpMessage:CustomizationHelpMessage = null;
      
      private var _rightSideBtns:Vector.<UniversalBtn> = null;
      
      private var _buyDisabledTooltip:String = "";
      
      private var _popoverBtnDisabledTooltip:String = "";
      
      private var _smPadding:int = 0;
      
      private var _bottomOffset:uint = 0;
      
      private var _isNonHistoric:Boolean = false;
      
      private var _isMinResolution:Boolean = false;
      
      private var _intCDToScroll:int = -1;
      
      private var _scrollImmediately:Boolean = false;
      
      private var _popoverAlias:String = "";
      
      private var _popoverBtnState:Boolean = true;
      
      private var _popoverIsOpen:Boolean = false;
      
      private var _projectionDecalNotificationShow:Boolean = false;
      
      private var _stageSwitcher:StageSwitcher = null;
      
      private var _popoverMgr:IPopoverManager;
      
      private var _utils:IUtils;
      
      private var _tooltipMgr:ITooltipMgr;
      
      private var _systemMessages:DisplayObjectContainer;
      
      public function BottomPanel()
      {
         this._popoverMgr = App.popoverMgr;
         this._utils = App.utils;
         this._tooltipMgr = App.toolTipMgr;
         this._systemMessages = App.systemMessages;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._rightSideBtns = new <UniversalBtn>[this.vehiclesSidebarBtn,this.itemsPopoverBtn,this.buyBtn];
         this.buyBtn.soundType = SoundTypes.CUSTOMIZATION_DEFAULT;
         this.buyBtn.mouseEnabledOnDisabled = true;
         this.bill.visible = false;
         this.bill.addEventListener(Event.RESIZE,this.onBillResizeHandler);
         this.buyBackground.visible = false;
         this.background.mouseEnabled = this.background.mouseChildren = false;
         this.buyBackground.mouseEnabled = this.buyBackground.mouseChildren = false;
         this.tabGlow.mouseEnabled = this.tabGlow.mouseChildren = false;
         var _loc1_:Sprite = new Sprite();
         this.background.hitArea = _loc1_;
         addChild(_loc1_);
         App.stage.addEventListener(CustomizationItemEvent.SELECT_ITEM,this.onBottomPanelCarouselSelectItemHandler);
         App.stage.addEventListener(CustomizationItemEvent.EDIT_ITEM,this.onBottomPanelCarouselEditItemHandler);
         this.buyBtn.addEventListener(ButtonEvent.CLICK,this.onBuyBtnClickHandler);
         this.buyBtn.addEventListener(MouseEvent.MOUSE_OUT,this.onBtnBuyMouseOutHandler);
         this.buyBtn.addEventListener(MouseEvent.MOUSE_OVER,this.onBtnBuyMouseOverHandler);
         this.tabNavigator.addEventListener(CustomizationTabEvent.TAB_CHANGED,this.onNavigatorTabChangedHandler);
         this.tabNavigator.addEventListener(Event.RESIZE,this.onTabNavigatorResizeHandler);
         this.itemsPopoverBtn.mouseEnabledOnDisabled = true;
         this.itemsPopoverBtn.addEventListener(ButtonEvent.CLICK,this.onItemsPopoverBtnClickHandler);
         this.itemsPopoverBtn.addEventListener(MouseEvent.ROLL_OVER,this.onItemsPopoverBtnRollOverHandler);
         this.vehiclesSidebarBtn.iconSource = RES_ICONS.MAPS_ICONS_CUSTOMIZATION_ICON_BUTTON_TECHNIC_FILTER;
         this.vehiclesSidebarBtn.mouseEnabledOnDisabled = true;
         this.vehiclesSidebarBtn.addEventListener(ButtonEvent.CLICK,this.onVehiclesSidebarBtnClickHandler);
         this.vehiclesSidebarBtn.addEventListener(MouseEvent.ROLL_OVER,this.onVehiclesSidebarBtnRollOverHandler);
         this.carousel.addEventListener(CustomizationEvent.REFRESH_FILTER_DATA,this.onRefreshFilterDataHandler);
         this.carousel.addEventListener(CustomizationEvent.RESET_FILTER,this.onResetFilterHandler);
         this.carousel.addEventListener(FiltersEvent.RESET_ALL_FILTERS,this.onBottomPanelCarouselFilterCounterResetAllFiltersHandler);
         this.carousel.addEventListener(CustomizationEvent.SELECT_HOT_FILTER,this.onBottomPanelCarouselSelectHotFilterHandler);
         this.carousel.addEventListener(CustomizationEvent.NEW_ANIMATION_SHOWN,this.onBottomPanelCarouselNewAnimationShownHandler);
         this.carousel.addEventListener(CustomizationEvent.SHOW_ATTACHMENTS_VIDEO,this.onShowAttachmentsVideoHandler);
         this.carousel.addEventListener(CustomizationEvent.SHOW_VEHICLES_SIDEBAR,this.onShowVehiclesSideBaHandler);
         App.stage.addEventListener(CustomizationEvent.ITEMS_POPOVER_CLOSED,this.onStageItemsPopoverClosedHandler);
         this.overlay.addEventListener(MouseEvent.CLICK,this.onOverlayClickHandler);
         this.overlay.visible = false;
         this._utils.universalBtnStyles.setStyle(this.itemsPopoverBtn,UniversalBtnStylesConst.STYLE_HEAVY_GREEN);
         this._utils.universalBtnStyles.setStyle(this.vehiclesSidebarBtn,UniversalBtnStylesConst.STYLE_HEAVY_GREEN);
         this._utils.universalBtnStyles.setStyle(this.buyBtn,UniversalBtnStylesConst.STYLE_HEAVY_ORANGE);
         this.itemsPopoverBtn.disabledImageAlpha = ITEMS_INFO_BTN_ALPHA;
         this.vehiclesSidebarBtn.disabledImageAlpha = ITEMS_INFO_BTN_ALPHA;
      }
      
      override protected function onBeforeDispose() : void
      {
         this.tabNavigator.removeEventListener(CustomizationTabEvent.TAB_CHANGED,this.onNavigatorTabChangedHandler);
         this.tabNavigator.removeEventListener(Event.RESIZE,this.onTabNavigatorResizeHandler);
         this.carousel.removeEventListener(CustomizationEvent.RESET_FILTER,this.onResetFilterHandler);
         this.carousel.removeEventListener(CustomizationEvent.REFRESH_FILTER_DATA,this.onRefreshFilterDataHandler);
         App.stage.removeEventListener(CustomizationItemEvent.SELECT_ITEM,this.onBottomPanelCarouselSelectItemHandler);
         App.stage.removeEventListener(CustomizationItemEvent.EDIT_ITEM,this.onBottomPanelCarouselEditItemHandler);
         this.buyBtn.removeEventListener(ButtonEvent.CLICK,this.onBuyBtnClickHandler);
         this.buyBtn.removeEventListener(MouseEvent.MOUSE_OUT,this.onBtnBuyMouseOutHandler);
         this.buyBtn.removeEventListener(MouseEvent.MOUSE_OVER,this.onBtnBuyMouseOverHandler);
         this.carousel.removeEventListener(FiltersEvent.RESET_ALL_FILTERS,this.onBottomPanelCarouselFilterCounterResetAllFiltersHandler);
         this.carousel.removeEventListener(CustomizationEvent.SELECT_HOT_FILTER,this.onBottomPanelCarouselSelectHotFilterHandler);
         this.carousel.removeEventListener(CustomizationEvent.NEW_ANIMATION_SHOWN,this.onBottomPanelCarouselNewAnimationShownHandler);
         this.itemsPopoverBtn.removeEventListener(ButtonEvent.CLICK,this.onItemsPopoverBtnClickHandler);
         this.itemsPopoverBtn.removeEventListener(MouseEvent.ROLL_OVER,this.onItemsPopoverBtnRollOverHandler);
         this.vehiclesSidebarBtn.removeEventListener(ButtonEvent.CLICK,this.onVehiclesSidebarBtnClickHandler);
         this.vehiclesSidebarBtn.removeEventListener(MouseEvent.ROLL_OVER,this.onVehiclesSidebarBtnRollOverHandler);
         this.overlay.removeEventListener(MouseEvent.CLICK,this.onOverlayClickHandler);
         App.stage.removeEventListener(CustomizationEvent.ITEMS_POPOVER_CLOSED,this.onStageItemsPopoverClosedHandler);
         this.carousel.removeEventListener(CustomizationEvent.SHOW_ATTACHMENTS_VIDEO,this.onShowAttachmentsVideoHandler);
         this.carousel.removeEventListener(CustomizationEvent.SHOW_VEHICLES_SIDEBAR,this.onShowVehiclesSideBaHandler);
         if(this._stageSwitcher != null)
         {
            this._stageSwitcher.removeEventListener(Event.RESIZE,this.onStageSwitcherResizeHandler);
         }
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this._rightSideBtns.splice(0,this._rightSideBtns.length);
         this._rightSideBtns = null;
         this.overlay.dispose();
         this.overlay = null;
         this.itemsPopoverBtn.dispose();
         this.itemsPopoverBtn = null;
         this.helpMessage.dispose();
         this.helpMessage = null;
         this.vehiclesSidebarBtn.dispose();
         this.vehiclesSidebarBtn = null;
         this.tabNavigator.dispose();
         this.tabNavigator = null;
         this.bill.removeEventListener(Event.RESIZE,this.onBillResizeHandler);
         this.bill.dispose();
         this.bill = null;
         this.carousel.dispose();
         this.carousel = null;
         this.buyBtn.dispose();
         this.buyBtn = null;
         this.customizationContentTypeIcon.dispose();
         this.customizationContentTypeIcon = null;
         this.infoLabel.dispose();
         this.infoLabel = null;
         this._stageSwitcher = null;
         this._utils = null;
         this.buyBackground = null;
         this.background = null;
         this.tabBg = null;
         this._popoverMgr = null;
         this._tooltipMgr = null;
         this._systemMessages = null;
         this.tabGlow = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:UniversalBtn = null;
         super.draw();
         var _loc1_:Boolean = App.appHeight < StageSizeBoundaries.HEIGHT_1080;
         if(isInvalid(InvalidationType.SIZE))
         {
            this.background.width = _width;
            this.background.height = App.appHeight - (y + this.background.y);
            this.carousel.width = _width;
            this.carousel.y = !!_loc1_ ? Number(CAROUSEL_Y_SMALL) : Number(CAROUSEL_Y);
            this.carousel.invalidateSize();
            this.overlay.updateSize(_width,_height,_loc1_);
            this.tabNavigator.updateStage(_width,App.appHeight);
            if(this._isMinResolution != _loc1_)
            {
               this._isMinResolution = _loc1_;
               this._utils.universalBtnStyles.setStyle(this.itemsPopoverBtn,!!_loc1_ ? UniversalBtnStylesConst.STYLE_SLIM_GREEN : UniversalBtnStylesConst.STYLE_HEAVY_GREEN);
               this._utils.universalBtnStyles.setStyle(this.vehiclesSidebarBtn,!!_loc1_ ? UniversalBtnStylesConst.STYLE_SLIM_GREEN : UniversalBtnStylesConst.STYLE_HEAVY_GREEN);
               this._utils.universalBtnStyles.setStyle(this.buyBtn,!!_loc1_ ? UniversalBtnStylesConst.STYLE_SLIM_ORANGE : UniversalBtnStylesConst.STYLE_HEAVY_ORANGE);
            }
            invalidateLayout();
         }
         if(isInvalid(INVALID_SCROLL_POS))
         {
            _loc2_ = 0;
            if(this._intCDToScroll != Values.DEFAULT_INT)
            {
               _loc2_ = this.getItemIndexByIndCD(this._intCDToScroll);
            }
            if(_loc2_ != Values.DEFAULT_INT)
            {
               this.carousel.validateNow();
               this.carousel.goToItem(_loc2_,true,this._scrollImmediately);
               if(this._scrollImmediately)
               {
                  this.carousel.scrollList.validateNow();
               }
            }
            this._intCDToScroll = Values.DEFAULT_INT;
         }
         if(isInvalid(POPOVER_BUTTON_STATE_INVALID))
         {
            this.itemsPopoverBtn.enabled = this._popoverIsOpen || this._popoverBtnState;
         }
         if(isInvalid(InvalidationType.LAYOUT))
         {
            _loc3_ = !!_loc1_ ? int(TOP_SMALL_OFFSET) : int(0);
            _loc4_ = App.appWidth - this.buyBtn.width - BUY_OFFSET_VERTICAL ^ 0;
            this.buyBtn.x = _loc4_;
            this.buyBackground.x = _loc4_ - BUY_OFFSET_HORIZONTAL ^ 0;
            this.buyBackground.y = BUY_BACKGROUND_Y + _loc3_;
            _loc5_ = this.itemsPopoverBtn.width;
            _loc6_ = _loc4_ - ITEMS_BUTTON_OFFSET - _loc5_ ^ 0;
            this.itemsPopoverBtn.x = _loc6_;
            this.customizationContentTypeIcon.x = _loc6_ + _loc5_ - (NON_HISTORIC_FIX_ICON_WIDTH >> 1) + NON_HISTORIC_ICON_OFFSET_X ^ 0;
            this.vehiclesSidebarBtn.x = _loc6_ - ITEMS_BUTTON_OFFSET - this.vehiclesSidebarBtn.width ^ 0;
            this.customizationContentTypeIcon.y = NON_HISTORIC_ICON_Y + _loc3_;
            this.bill.x = _width - this.bill.width - PRICE_OFFSET_HORIZONTAL ^ 0;
            this.bill.y = -this.bill.height + _loc3_ + PRICE_OFFSET_VERTICAL;
            this.infoLabel.x = _width >> 1;
            this.tabBg.x = _width - this.tabBg.width >> 1;
            this.tabGlow.x = _width - this.tabGlow.width >> 1;
            if(this.helpMessage.visible)
            {
               this.helpMessage.x = _width - this.helpMessage.width >> 1;
            }
            invalidate(RIGHT_BTNS_VISIBILITY_INVALID);
         }
         if(isInvalid(RIGHT_BTNS_VISIBILITY_INVALID))
         {
            _loc7_ = App.appWidth;
            for each(_loc8_ in this._rightSideBtns)
            {
               if(_loc8_.visible && _loc8_.x < _loc7_)
               {
                  _loc7_ = _loc8_.x;
               }
            }
            this.tabNavigator.updateBorders(Values.ZERO,_loc7_);
         }
      }
      
      override protected function setBottomPanelInitData(param1:CustomizationBottomPanelInitVO) : void
      {
         this.carousel.setCarouselFiltersInitData(param1.filtersVO);
         invalidateSize();
      }
      
      override protected function setBottomPanelTabsData(param1:CustomizationTabNavigatorVO) : void
      {
         this.tabNavigator.setData(param1);
         var _loc2_:Boolean = param1.selectedTab == Values.DEFAULT_INT;
         this.infoLabel.visible = _loc2_;
         this.tabNavigator.switchState(!_loc2_);
      }
      
      override protected function setCarouselData(param1:CustomizationCarouselDataVO) : void
      {
         this.carousel.setData(param1);
      }
      
      override protected function setCarouselFiltersData(param1:TankCarouselFilterSelectedVO) : void
      {
         this.carousel.setCarouselFiltersData(param1);
      }
      
      override protected function setFilterData(param1:CustomizationCarouselFilterVO) : void
      {
         this.carousel.setFilterData(param1);
      }
      
      override protected function setBottomPanelPriceState(param1:BottomPanelVO) : void
      {
         this.buyBtn.label = param1.buyBtnLabel;
         this._buyDisabledTooltip = param1.buyBtnTooltip;
         this.buyBtn.enabled = param1.buyBtnEnabled;
         this.bill.setData(param1.billVO);
         var _loc2_:int = param1.customizationDisplayType;
         this._isNonHistoric = _loc2_ != CUSTOMIZATION_CONSTS.HISTORICAL_TYPE;
         this.customizationContentTypeIcon.setType(_loc2_);
         if(this._isNonHistoric)
         {
            this.customizationContentTypeIcon.fadeIn();
         }
         else
         {
            this.customizationContentTypeIcon.fadeOut();
         }
         invalidateSize();
      }
      
      override protected function setNotificationCounters(param1:CustomizationBottomPanelNotificationVO) : void
      {
         this.tabNavigator.setNotificationCounters(param1);
      }
      
      override protected function setFilterFallbackData(param1:FilterFallbackDataVO) : void
      {
         this.carousel.setFilterFallbackData(param1);
      }
      
      public function as_getDataProvider() : Object
      {
         return this.carousel.getDataProvider();
      }
      
      public function as_hideBill() : void
      {
         this.setBillVisibility(false);
      }
      
      public function as_playFilterBlink() : void
      {
         this.carousel.playFilterBlink();
      }
      
      public function as_scrollToSlot(param1:int, param2:Boolean) : void
      {
         this._intCDToScroll = param1;
         this._scrollImmediately = param2;
         invalidate(INVALID_SCROLL_POS);
      }
      
      public function as_setCarouselInfoLabelData(param1:String, param2:String) : void
      {
         this.infoLabel.text = param1;
         this.infoLabel.tooltip = param2;
         this.infoLabel.validateNow();
         this.updateVerticalPositions();
      }
      
      public function as_setItemsPopoverBtnEnabled(param1:Boolean) : void
      {
         this._popoverBtnState = param1;
         invalidate(POPOVER_BUTTON_STATE_INVALID);
      }
      
      public function as_setProjectionDecalHintVisibility(param1:Boolean) : void
      {
         this._projectionDecalNotificationShow = param1;
         this.updateProjectionDecalNotificationState();
      }
      
      public function as_setStageSwitcherVisibility(param1:Boolean) : void
      {
         if(this._stageSwitcher != null)
         {
            this._stageSwitcher.visible = param1;
         }
         else if(param1)
         {
            this._stageSwitcher = new StageSwitcher();
            this._stageSwitcher.y = STAGE_SWITCHER_Y;
            addChildAt(this._stageSwitcher,0);
            registerFlashComponentS(this._stageSwitcher,CUSTOMIZATION_ALIASES.PROGRESSION_STYLES_STAGE_SWITCHER);
            this._stageSwitcher.addEventListener(Event.RESIZE,this.onStageSwitcherResizeHandler);
            this._stageSwitcher.visible = true;
         }
         if(param1)
         {
            invalidateLayout();
         }
      }
      
      public function as_setVehiclesSidebarBtnVisibility(param1:Boolean) : void
      {
         this.vehiclesSidebarBtn.visible = param1;
         invalidate(RIGHT_BTNS_VISIBILITY_INVALID);
      }
      
      public function as_showBill() : void
      {
         this.setBillVisibility(true);
      }
      
      public function as_showPopoverBtn(param1:String, param2:String, param3:String) : void
      {
         this._popoverAlias = param1;
         this.itemsPopoverBtn.iconSource = param2;
         this._popoverBtnDisabledTooltip = param3;
      }
      
      public function as_updateEscHelpMessage(param1:Boolean) : void
      {
         this.helpMessage.visible = param1;
      }
      
      public function getFocusChain() : Vector.<InteractiveObject>
      {
         var _loc1_:Vector.<InteractiveObject> = new Vector.<InteractiveObject>();
         if(this.tabNavigator.visible)
         {
            _loc1_ = _loc1_.concat(this.tabNavigator.getFocusChain(),this.carousel.getFocusChain());
         }
         return _loc1_;
      }
      
      public function getHitArea() : DisplayObject
      {
         return this.itemsPopoverBtn;
      }
      
      public function getItemIndexByIndCD(param1:int) : int
      {
         var _loc2_:ListDAAPIDataProvider = this.carousel.dataProvider as ListDAAPIDataProvider;
         return Boolean(_loc2_) ? int(_loc2_.getItemIndex("intCD",param1)) : int(Values.DEFAULT_INT);
      }
      
      public function getTargetButton() : DisplayObject
      {
         return this.itemsPopoverBtn;
      }
      
      public function hideOverlay() : void
      {
         this.overlay.hide();
      }
      
      public function setCarouselNotificationsVisibility(param1:Boolean) : void
      {
         var _loc2_:Boolean = !param1;
         this.updateProjectionDecalNotificationState(_loc2_);
      }
      
      public function showOverlay(param1:String, param2:Boolean = false) : void
      {
         this.overlay.show(param1,param2);
      }
      
      private function setBillVisibility(param1:Boolean) : void
      {
         this.bill.visible = param1;
         this.buyBackground.visible = param1;
         this.updateSysMessagePosition();
      }
      
      private function updateSysMessagePosition() : void
      {
         var _loc1_:int = this.background.height - this._bottomOffset;
         if(this.bill.visible)
         {
            _loc1_ += this.bill.height + SM_BILL_ADDITIONAL_HEIGHT;
         }
         if(this._smPadding != _loc1_)
         {
            this._smPadding = _loc1_;
            this._systemMessages.dispatchEvent(new NotificationLayoutEvent(NotificationLayoutEvent.UPDATE_LAYOUT,new Point(SM_PADDING_X,this._smPadding + SM_PADDING_Y)));
         }
      }
      
      private function updateVerticalPositions() : void
      {
         var _loc1_:int = !!this._isMinResolution ? int(TABS_BACKGROUND_HEIGHT_MIN_RESOLUTION) : int(TABS_BACKGROUND_HEIGHT);
         this.infoLabel.y = this.tabNavigator.y + (_loc1_ - this.infoLabel.height >> 1);
         this.itemsPopoverBtn.y = this.tabNavigator.y + (_loc1_ - this.itemsPopoverBtn.height >> 1);
         this.vehiclesSidebarBtn.y = this.itemsPopoverBtn.y;
         this.buyBtn.y = this.tabNavigator.y + (_loc1_ - this.buyBtn.height >> 1);
         this.updateSysMessagePosition();
      }
      
      private function updateProjectionDecalNotificationState(param1:Boolean = false) : void
      {
         this.carousel.projectionDecalHint.visible = !!param1 ? Boolean(false) : Boolean(this._projectionDecalNotificationShow);
      }
      
      public function set bottomOffset(param1:uint) : void
      {
         this._bottomOffset = param1;
      }
      
      private function onBottomPanelCarouselNewAnimationShownHandler(param1:CustomizationEvent) : void
      {
         onItemIsNewAnimationShownS(param1.index);
      }
      
      private function onBillResizeHandler(param1:Event) : void
      {
         invalidateLayout();
      }
      
      private function onOverlayClickHandler(param1:MouseEvent) : void
      {
         this.hideOverlay();
      }
      
      private function onBtnBuyMouseOutHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.hide();
      }
      
      private function onBtnBuyMouseOverHandler(param1:MouseEvent) : void
      {
         if(!this.buyBtn.enabled)
         {
            this._tooltipMgr.show(this._buyDisabledTooltip);
         }
      }
      
      private function onNavigatorTabChangedHandler(param1:CustomizationTabEvent) : void
      {
         this.carousel.scrollList.moveToHorizontalScrollPosition(0);
         this.carousel.playFilterBlink();
         if(param1.groupId != Values.DEFAULT_INT)
         {
            showGroupFromTabS(param1.groupId);
         }
      }
      
      private function onItemsPopoverBtnClickHandler(param1:ButtonEvent) : void
      {
         if(param1.buttonIdx == MouseEventEx.LEFT_BUTTON)
         {
            this._popoverIsOpen = true;
            this._popoverMgr.show(this,this._popoverAlias,null);
         }
      }
      
      private function onVehiclesSidebarBtnClickHandler(param1:ButtonEvent) : void
      {
         showVehiclesSideBarS();
      }
      
      private function onBuyBtnClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new CustomizationEvent(CustomizationEvent.SHOW_BUY_WINDOW,false));
      }
      
      private function onBottomPanelCarouselSelectItemHandler(param1:CustomizationItemEvent) : void
      {
         onSelectItemS(param1.itemId,param1.groupId,param1.progressionLevel);
      }
      
      private function onBottomPanelCarouselEditItemHandler(param1:CustomizationItemEvent) : void
      {
         onEditItemS(param1.itemId);
      }
      
      private function onRefreshFilterDataHandler(param1:CustomizationEvent) : void
      {
         refreshFilterDataS();
      }
      
      private function onResetFilterHandler(param1:CustomizationEvent) : void
      {
         resetFilterS();
      }
      
      private function onShowAttachmentsVideoHandler(param1:CustomizationEvent) : void
      {
         showVideoS();
      }
      
      private function onShowVehiclesSideBaHandler(param1:CustomizationEvent) : void
      {
         showVehiclesSideBarS();
      }
      
      private function onStageItemsPopoverClosedHandler(param1:CustomizationEvent) : void
      {
         this._popoverIsOpen = false;
         invalidate(POPOVER_BUTTON_STATE_INVALID);
      }
      
      private function onBottomPanelCarouselSelectHotFilterHandler(param1:CustomizationEvent) : void
      {
         onSelectHotFilterS(param1.index,param1.select);
         this.carousel.playFilterBlink();
      }
      
      private function onBottomPanelCarouselFilterCounterResetAllFiltersHandler(param1:FiltersEvent) : void
      {
         resetFilterS();
      }
      
      private function onItemsPopoverBtnRollOverHandler(param1:MouseEvent) : void
      {
         if(this.itemsPopoverBtn.enabled)
         {
            this._tooltipMgr.showSpecial(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_POPOVER_ITEM,null,this._isNonHistoric);
         }
         else
         {
            this._tooltipMgr.show(this._popoverBtnDisabledTooltip);
         }
      }
      
      private function onVehiclesSidebarBtnRollOverHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.show(VEHICLE_CUSTOMIZATION.CUSTOMIZATION_VEHICLELIST);
      }
      
      private function onTabNavigatorResizeHandler(param1:Event) : void
      {
         this.updateVerticalPositions();
      }
      
      private function onStageSwitcherResizeHandler(param1:Event) : void
      {
         if(this._stageSwitcher != null)
         {
            this._stageSwitcher.x = _width - this._stageSwitcher.width >> 1;
         }
         invalidateLayout();
      }
   }
}
