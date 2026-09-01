package net.wg.gui.lobby.vehicleCustomization
{
   import flash.display.DisplayObject;
   import flash.display.InteractiveObject;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import flash.ui.Keyboard;
   import net.wg.data.Aliases;
   import net.wg.data.constants.Cursors;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CUSTOMIZATION_ALIASES;
   import net.wg.gui.components.advanced.tutorial.TutorialHint;
   import net.wg.gui.events.LobbyEvent;
   import net.wg.gui.interfaces.IMagneticClickHandler;
   import net.wg.gui.lobby.vehicleCustomization.controls.C11nInnerEntryPoint;
   import net.wg.gui.lobby.vehicleCustomization.controls.CarouselItemRenderer;
   import net.wg.gui.lobby.vehicleCustomization.controls.CarouselRendererAttachedBase;
   import net.wg.gui.lobby.vehicleCustomization.controls.magneticTool.MagneticToolController;
   import net.wg.gui.lobby.vehicleCustomization.controls.propertiesSheet.CustomizationPropertiesSheet;
   import net.wg.gui.lobby.vehicleCustomization.controls.seasonBar.CustomizaionSeasonsBar;
   import net.wg.gui.lobby.vehicleCustomization.controls.seasonBar.CustomizationSeasonRenderer;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationAnchorInitVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationAnchorsSetVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationAnchorsStateVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationHeaderVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationInnerEntryPointVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationSlotIdVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationSlotUpdateVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselRendererVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationAnchorEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationAnchorSetEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationButtonEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationCarouselScrollEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationItemEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationItemSwitchEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationSoundEvent;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationStyleInfoEvent;
   import net.wg.infrastructure.base.meta.ICustomizationMainViewMeta;
   import net.wg.infrastructure.base.meta.impl.CustomizationMainViewMeta;
   import net.wg.infrastructure.interfaces.ICursorManager;
   import net.wg.infrastructure.interfaces.IInnerView;
   import net.wg.utils.IGameInputManager;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.IndexEvent;
   import scaleform.clik.events.InputEvent;
   import scaleform.clik.motion.Tween;
   import scaleform.gfx.MouseEventEx;
   
   public class CustomizationMainView extends CustomizationMainViewMeta implements ICustomizationMainViewMeta, IInnerView
   {
      
      private static const BOTTOM_OFFSET:int = 248;
      
      private static const MIN_RES_BOTTOM_OFFSET:int = 295;
      
      private static const INV_FOCUS_CHAIN:String = "InvFocusChain";
      
      private static const INV_ENTRY_POINTS_SIZE:String = "InvEntryPointsSize";
      
      private static const HIDE_CONTAINER_NAME:String = "hideContainer";
      
      private static const SIDEBAR_MIN_SCREEN_SIZE:int = 1367;
      
      private static const SEASON_BAR_DEFAULT_OFFSET_X:int = 50;
      
      private static const SEASON_TOP_SHIFT:int = 54;
      
      private static const SEASON_BAR_SMALL_OFFSET_X:int = -150;
      
      private static const SEASON_BAR_OFFSET_Y:int = -129;
      
      private static const SEASON_BAR_TOP_OFFSET:int = -30;
      
      private static const SEASON_BAR_STYLE_INFO_OFFSET_Y:Number = -60;
      
      private static const SEASON_BAR_SPACING:int = -153;
      
      private static const SEASON_RENDERER_HEIGHT:int = 56;
      
      private static const SHOW_ALPHA:Number = 1;
      
      private static const HIDE_ALPHA:Number = 0;
      
      private static const ANIMATION_DURATION:int = 200;
      
      private static const ANIMATION_DELAY:int = 150;
      
      private static const STYLE_INFO_ANIMATION_DURATION:int = 800;
      
      private static const STYLE_INFO_ANIMATION_DELAY:int = 200;
      
      public static const ENTRY_POINT_SCALE:Number = 1;
      
      private static const ENTRY_POINT_MIN_SCALE:Number = 0.75;
      
      private static const FIRST_ENTRY_POINT_SMALL_GAP:int = 13;
      
      private static const FIRST_ENTRY_POINT_GAP:int = 20;
      
      private static const ENTRY_POINT_SMALL_START_X:int = 40;
      
      private static const ENTRY_POINT_START_X:int = 0;
      
      private static const ENTRY_POINT_SMALL_SHORT_START_X:int = 10;
      
      private static const ENTRY_POINT_SHORT_START_X:int = 0;
      
      private static const SINGLE_ENTRY_POINT_Y_SHIFT:int = 21;
      
      private static const BG_ALPHA:Number = 0.5;
       
      
      public var notification:CustomizationNotification = null;
      
      public var propertiesSheet:CustomizationPropertiesSheet = null;
      
      public var customizationHeader:CustomizationHeader = null;
      
      public var styleInfo:CustomizationStyleInfo = null;
      
      public var bottomPanel:BottomPanel = null;
      
      public var vehicleView:CustomizationVehicleView = null;
      
      public var background:Sprite = null;
      
      public var seasonsBar:CustomizaionSeasonsBar = null;
      
      private var _actualWidth:int = 0;
      
      private var _actualHeight:int = 0;
      
      private var _focusChain:Vector.<InteractiveObject>;
      
      private var _magneticClickHandlers:Vector.<IMagneticClickHandler>;
      
      private var _magneticTool:MagneticToolController = null;
      
      private var _dragOccurred:Boolean = false;
      
      private var _inscriptionControllerShown:Boolean = false;
      
      private var _dragMouseX:Number = 0;
      
      private var _dragMouseY:Number = 0;
      
      private var _gameInputMgr:IGameInputManager = null;
      
      private var _cursor:ICursorManager;
      
      private var _customizationAnchorInitData:CustomizationAnchorInitVO = null;
      
      private var _innerEntriesData:Vector.<CustomizationInnerEntryPointVO> = null;
      
      private var _entries:Vector.<C11nInnerEntryPoint> = null;
      
      private var _tweens:Vector.<Tween>;
      
      private var _hideContainer:Sprite;
      
      private var _topOffset:uint = 0;
      
      private var _bottomOffset:uint = 0;
      
      public function CustomizationMainView()
      {
         this._focusChain = new Vector.<InteractiveObject>();
         this._tweens = new Vector.<Tween>();
         super();
         this._gameInputMgr = App.gameInputMgr;
         this._cursor = App.cursor;
      }
      
      private static function checkClickRightMouse(param1:MouseEvent) : Boolean
      {
         var _loc2_:MouseEventEx = param1 as MouseEventEx;
         var _loc3_:uint = _loc2_ == null ? uint(0) : uint(_loc2_.buttonIdx);
         return _loc3_ == MouseEventEx.RIGHT_BUTTON;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         assertUpdateStageMethod();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:int = 0;
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.customizationHeader.y = this._topOffset;
            this.customizationHeader.updateSize(this._actualWidth);
            this.styleInfo.y = this._topOffset;
            this.vehicleView.updateSize(this._actualWidth,this._actualHeight);
            _loc1_ = App.appHeight < StageSizeBoundaries.HEIGHT_1080;
            _loc2_ = !!_loc1_ ? int(MIN_RES_BOTTOM_OFFSET) : int(BOTTOM_OFFSET);
            this.bottomPanel.y = this._actualHeight - this.bottomPanel.height + _loc2_ - this._bottomOffset ^ 0;
            this.bottomPanel.width = this._actualWidth;
            this.bottomPanel.bottomOffset = this._bottomOffset;
            this.bottomPanel.invalidateSize();
            this.background.y = 0;
            this.background.width = App.appWidth;
            this.background.height = App.appHeight;
            this.bottomPanel.invalidateSize();
            this.updateSeasonsBar();
            invalidate(INV_ENTRY_POINTS_SIZE);
         }
         if(isInvalid(INV_ENTRY_POINTS_SIZE))
         {
            this.updateInnerEntryPoints();
         }
         if(isInvalid(INV_FOCUS_CHAIN))
         {
            this.refreshFocusChain();
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.seasonsBar.spacing = SEASON_BAR_SPACING;
         this._gameInputMgr.setKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler,true);
         this._gameInputMgr.setKeyHandler(Keyboard.LEFT,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler,true);
         this._gameInputMgr.setKeyHandler(Keyboard.RIGHT,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler,true);
         this._gameInputMgr.setKeyHandler(Keyboard.DELETE,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler,true);
         this._gameInputMgr.setKeyHandler(Keyboard.NUMPAD_DECIMAL,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler,true);
         App.stage.dispatchEvent(new LobbyEvent(LobbyEvent.REGISTER_DRAGGING));
         App.stage.addEventListener(LobbyEvent.DRAGGING_START,this.onStageDraggingStartHandler);
         App.stage.addEventListener(LobbyEvent.DRAGGING_END,this.onStageDraggingEndHandler);
         App.stage.addEventListener(LobbyEvent.DRAGGING,this.onLobbyDraggingHandler);
         App.stage.addEventListener(MouseEvent.MOUSE_WHEEL,this.onMouseWheelHandler);
         App.stage.addEventListener(MouseEvent.MOUSE_UP,this.onMouseUpHandler);
         this.customizationHeader.addEventListener(CustomizationEvent.CLOSE_VIEW,this.onCloseViewHandler);
         this.customizationHeader.addEventListener(CustomizationEvent.SHOW_PROGRESSION_INFO,this.onShowProgressionInfoHandler);
         addEventListener(CustomizationEvent.SHOW_BUY_WINDOW,this.onShowBuyWindowHandler);
         addEventListener(CustomizationEvent.ENTRY_POINT_CLICKED,this.onEntryPointClickHandler);
         addEventListener(CustomizationEvent.SHOW_SHOP,this.onShopEntryPointHandler);
         addEventListener(CustomizationItemEvent.SEEN_ITEM,this.onSeenItemHandler);
         addEventListener(CustomizationAnchorEvent.SELECT_ANCHOR,this.onSelectAnchorHandler);
         addEventListener(CustomizationAnchorEvent.LOCKED_ANCHOR,this.onLockedAnchorHandler);
         addEventListener(CustomizationAnchorEvent.OVER_ANCHOR,this.onOverAnchorHandler);
         addEventListener(CustomizationAnchorEvent.OUT_ANCHOR,this.onOutAnchorHandler);
         addEventListener(CustomizationAnchorEvent.DRAG_ANCHOR,this.onDragAnchorHandler);
         addEventListener(CustomizationSoundEvent.PLAY_SOUND,this.onCustomizationPlaySoundHandler);
         addEventListener(CustomizationItemEvent.SELECT_ITEM,this.onCarouselSelectItemHandler);
         this.propertiesSheet.addEventListener(CustomizationEvent.SHOW_PROPERTIES_SHEET,this.onShowPropertiesSheetHandler);
         this.propertiesSheet.addEventListener(CustomizationEvent.CLOSE_PROPERTIES_SHEET,this.onClosePropertiesSheetHandler);
         this.propertiesSheet.addEventListener(CustomizationEvent.SHOW_INSCRIPTION_CONTROLLER,this.onShowInscriptionControllerHandler);
         this.propertiesSheet.addEventListener(CustomizationEvent.HIDE_INSCRIPTION_CONTROLLER,this.onHideInscriptionControllerHandler);
         App.stage.addEventListener(CustomizationStyleInfoEvent.SHOW_STYLE_INFO,this.onShowStyleInfoHandler);
         App.stage.addEventListener(CustomizationStyleInfoEvent.HIDE_STYLE_INFO,this.onHideStyleInfoHandler);
         this.propertiesSheet.addEventListener(CustomizationItemSwitchEvent.SELECT_NEXT_ITEM,this.onSelectNextItemHandler);
         this.vehicleView.anchorsSet.addEventListener(CustomizationAnchorSetEvent.ANCHORS_FILLED,this.onAnchorsFilledHandler);
         this.seasonsBar.addEventListener(Event.COMPLETE,this.onSeasonBarCompleteHandler);
         this.seasonsBar.addEventListener(IndexEvent.INDEX_CHANGE,this.onSeasonBarIndexChangeHandler);
         this.bottomPanel.addEventListener(CustomizationButtonEvent.BUTTON_PRESSED,this.onBottomPanelButtonPressedHandler);
         App.stage.addEventListener(CustomizationCarouselScrollEvent.AVAILABLE_PAGING,this.onAvailablePagingHandler);
         var _loc1_:Sprite = new Sprite();
         addChild(_loc1_);
         this.background.hitArea = _loc1_;
         this.background.alpha = BG_ALPHA;
         this._magneticTool = new MagneticToolController(this,this.getMagneticClickHandlers());
         this.addToHideContainer();
         propertiesSheetSetS(this.propertiesSheet,this.propertiesSheet.width,this.propertiesSheet.height,CustomizationPropertiesSheet.OFFSET_X,CustomizationPropertiesSheet.OFFSET_Y);
         this.styleInfo.visible = false;
         this.invalidateInnerEntriesData();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerFlashComponentS(this.propertiesSheet,Aliases.CUSTOMIZATION_PROPERTIES_SHEET);
         registerFlashComponentS(this.bottomPanel,Aliases.CUSTOMIZATION_BOTTOM_PANEL);
         registerFlashComponentS(this.styleInfo,Aliases.CUSTOMIZATION_STYLE_INFO);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:C11nInnerEntryPoint = null;
         App.popoverMgr.hide();
         App.stage.removeEventListener(LobbyEvent.DRAGGING_START,this.onStageDraggingStartHandler);
         App.stage.removeEventListener(LobbyEvent.DRAGGING_END,this.onStageDraggingEndHandler);
         App.stage.removeEventListener(LobbyEvent.DRAGGING,this.onLobbyDraggingHandler);
         App.stage.dispatchEvent(new LobbyEvent(LobbyEvent.UNREGISTER_DRAGGING));
         App.stage.removeEventListener(MouseEvent.MOUSE_WHEEL,this.onMouseWheelHandler);
         App.stage.removeEventListener(MouseEvent.MOUSE_UP,this.onMouseUpHandler);
         this.customizationHeader.removeEventListener(CustomizationEvent.CLOSE_VIEW,this.onCloseViewHandler);
         this.customizationHeader.removeEventListener(CustomizationEvent.SHOW_PROGRESSION_INFO,this.onShowProgressionInfoHandler);
         removeEventListener(CustomizationEvent.SHOW_BUY_WINDOW,this.onShowBuyWindowHandler);
         removeEventListener(CustomizationEvent.ENTRY_POINT_CLICKED,this.onEntryPointClickHandler);
         removeEventListener(CustomizationEvent.SHOW_SHOP,this.onShopEntryPointHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.LEFT,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.RIGHT,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.DELETE,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.NUMPAD_DECIMAL,KeyboardEvent.KEY_DOWN,this.onKeyDownHandler);
         removeEventListener(CustomizationAnchorEvent.SELECT_ANCHOR,this.onSelectAnchorHandler);
         removeEventListener(CustomizationAnchorEvent.LOCKED_ANCHOR,this.onLockedAnchorHandler);
         removeEventListener(CustomizationAnchorEvent.OVER_ANCHOR,this.onOverAnchorHandler);
         removeEventListener(CustomizationAnchorEvent.OUT_ANCHOR,this.onOutAnchorHandler);
         removeEventListener(CustomizationAnchorEvent.DRAG_ANCHOR,this.onDragAnchorHandler);
         removeEventListener(CustomizationSoundEvent.PLAY_SOUND,this.onCustomizationPlaySoundHandler);
         removeEventListener(CustomizationItemEvent.SEEN_ITEM,this.onSeenItemHandler);
         removeEventListener(CustomizationItemEvent.SELECT_ITEM,this.onCarouselSelectItemHandler);
         this.propertiesSheet.removeEventListener(CustomizationEvent.SHOW_PROPERTIES_SHEET,this.onShowPropertiesSheetHandler);
         this.propertiesSheet.removeEventListener(CustomizationEvent.CLOSE_PROPERTIES_SHEET,this.onClosePropertiesSheetHandler);
         this.propertiesSheet.removeEventListener(CustomizationEvent.SHOW_INSCRIPTION_CONTROLLER,this.onShowInscriptionControllerHandler);
         this.propertiesSheet.removeEventListener(CustomizationEvent.HIDE_INSCRIPTION_CONTROLLER,this.onHideInscriptionControllerHandler);
         App.stage.removeEventListener(CustomizationStyleInfoEvent.SHOW_STYLE_INFO,this.onShowStyleInfoHandler);
         App.stage.removeEventListener(CustomizationStyleInfoEvent.HIDE_STYLE_INFO,this.onHideStyleInfoHandler);
         this.propertiesSheet.removeEventListener(CustomizationItemSwitchEvent.SELECT_NEXT_ITEM,this.onSelectNextItemHandler);
         this.vehicleView.anchorsSet.removeEventListener(CustomizationAnchorSetEvent.ANCHORS_FILLED,this.onAnchorsFilledHandler);
         this.seasonsBar.removeEventListener(Event.COMPLETE,this.onSeasonBarCompleteHandler);
         this.seasonsBar.removeEventListener(IndexEvent.INDEX_CHANGE,this.onSeasonBarIndexChangeHandler);
         this.bottomPanel.removeEventListener(CustomizationButtonEvent.BUTTON_PRESSED,this.onBottomPanelButtonPressedHandler);
         App.stage.removeEventListener(CustomizationCarouselScrollEvent.AVAILABLE_PAGING,this.onAvailablePagingHandler);
         this._magneticTool.dispose();
         this._magneticTool = null;
         this._magneticClickHandlers.splice(0,this._magneticClickHandlers.length);
         this._magneticClickHandlers = null;
         this.removeTweens();
         this._tweens = null;
         this.notification.dispose();
         this.notification = null;
         this._cursor = null;
         this.customizationHeader.dispose();
         this.customizationHeader = null;
         this.styleInfo = null;
         this.bottomPanel = null;
         this.vehicleView.dispose();
         this.vehicleView = null;
         this._focusChain.splice(0,this._focusChain.length);
         this._focusChain = null;
         this.propertiesSheet = null;
         this._gameInputMgr = null;
         this.background = null;
         this.seasonsBar.dispose();
         this.seasonsBar = null;
         if(this._entries)
         {
            for each(_loc1_ in this._entries)
            {
               _loc1_.dispose();
               _loc1_.removeEventListener(Event.RESIZE,this.onEntryPointResizeChanged);
               this._hideContainer.removeChild(_loc1_);
            }
            this._entries.splice(0,this._entries.length);
            this._entries = null;
         }
         this._hideContainer = null;
         this._customizationAnchorInitData = null;
         App.stage.dispatchEvent(new KeyboardEvent(KeyboardEvent.KEY_UP,true,false,0,Keyboard.ESCAPE));
         this._innerEntriesData = null;
         super.onDispose();
      }
      
      override protected function onInitModalFocus(param1:InteractiveObject) : void
      {
         super.onInitModalFocus(param1);
         setFocus(this.bottomPanel.tabNavigator.tabBar);
      }
      
      override protected function onSetModalFocus(param1:InteractiveObject) : void
      {
         if(param1 == null)
         {
            param1 = this;
         }
         super.onSetModalFocus(param1);
      }
      
      override protected function setHeaderData(param1:CustomizationHeaderVO) : void
      {
         this.customizationHeader.setHeaderData(param1);
      }
      
      override protected function setAnchorsData(param1:CustomizationAnchorsSetVO) : void
      {
         this.vehicleView.setAnchorPositions(param1);
      }
      
      override protected function setAnchorInit(param1:CustomizationAnchorInitVO) : void
      {
         this._customizationAnchorInitData = param1;
         this.vehicleView.setAnchorInit(param1);
      }
      
      override protected function updateAnchorData(param1:CustomizationAnchorInitVO) : void
      {
         this.vehicleView.updateAnchorData(param1);
      }
      
      override protected function setSeasonsBarData(param1:DataProvider) : void
      {
         this.seasonsBar.dataProvider = param1;
         if(this.seasonsBar.selectedIndex == Values.DEFAULT_INT && param1.length > 0)
         {
            this.seasonsBar.selectedIndex = 0;
         }
         this.seasonsBar.height = param1.length * SEASON_RENDERER_HEIGHT;
      }
      
      override protected function onRegionHighlighted(param1:CustomizationSlotIdVO, param2:Boolean, param3:Boolean, param4:Boolean) : void
      {
         this.vehicleView.anchorsSet.highlightAnchor(param1);
         if(param4)
         {
            this._cursor.forceSetCursor(!!param3 ? Cursors.BUTTON : Cursors.DRAG_OPEN);
         }
         if(!param2)
         {
            return;
         }
         if(!param1 || param1.slotType == Values.DEFAULT_INT)
         {
            this.resetMagneticTool();
         }
         var _loc5_:CustomizationSlotUpdateVO = this.vehicleView.anchorsSet.getSlotDataById(param1);
         if(_loc5_ != null)
         {
            this.vehicleView.anchorsSet.setSelectedSlot(param1);
         }
      }
      
      override protected function updateSelectedRegions(param1:CustomizationSlotIdVO) : void
      {
         if(param1.isEmpty())
         {
            this.vehicleView.anchorsSet.deselectCurrentAnchor();
         }
         else
         {
            this.vehicleView.anchorsSet.setSelectedSlot(param1);
         }
      }
      
      override protected function setNotificationCounters(param1:Array) : void
      {
         this.seasonsBar.setNotificationCounters(param1);
      }
      
      override protected function setAnchorsState(param1:CustomizationAnchorsStateVO) : void
      {
         this.vehicleView.setAnchorsState(param1);
      }
      
      override protected function attachToCursor(param1:CustomizationCarouselRendererVO) : void
      {
         var _loc2_:int = this.bottomPanel.getItemIndexByIndCD(param1.intCD);
         dispatchEvent(new CustomizationItemEvent(CustomizationItemEvent.SELECT_ITEM,_loc2_,param1.intCD,param1.progressionLevel));
         if(!param1)
         {
            return;
         }
         this._magneticTool.attachDataToCursor(param1);
         this.vehicleView.onStartDrop();
      }
      
      override protected function reselect(param1:CustomizationCarouselRendererVO) : void
      {
         this.bottomPanel.onSelectItemS(this.bottomPanel.carousel.selectedIndex,param1.intCD,param1.progressionLevel);
         this._magneticTool.attachDataToCursor(param1);
      }
      
      override protected function updateInnerEntries(param1:Vector.<CustomizationInnerEntryPointVO>) : void
      {
         this._innerEntriesData = param1;
         this.invalidateInnerEntriesData();
      }
      
      public function as_enableDND(param1:Boolean) : void
      {
         this._magneticTool.enableSelected = param1;
      }
      
      public function as_hide(param1:Boolean) : void
      {
         this.resetMagneticTool();
         this.alpha = !!param1 ? Number(SHOW_ALPHA) : Number(HIDE_ALPHA);
         mouseEnabled = mouseChildren = param1;
      }
      
      public function as_releaseItem(param1:Boolean) : void
      {
         this.resetMagneticTool(param1);
      }
      
      public function as_selectSeason(param1:int) : void
      {
         this.seasonsBar.removeEventListener(IndexEvent.INDEX_CHANGE,this.onSeasonBarIndexChangeHandler);
         this.seasonsBar.selectedIndex = param1;
         this.seasonsBar.addEventListener(IndexEvent.INDEX_CHANGE,this.onSeasonBarIndexChangeHandler);
      }
      
      public function as_showCarouselsArrowsNotification(param1:String) : void
      {
         this.bottomPanel.showOverlay(param1,true);
      }
      
      public function getFocusChain() : Vector.<InteractiveObject>
      {
         var _loc1_:Vector.<InteractiveObject> = new Vector.<InteractiveObject>();
         return _loc1_.concat(this.bottomPanel.getFocusChain());
      }
      
      public function isFullScreenModeSupported() : Boolean
      {
         return true;
      }
      
      public function onLobbyZoomChange(param1:Number) : void
      {
      }
      
      public function updateStageWithPadding(param1:Number, param2:Number, param3:Rectangle) : void
      {
         this._topOffset = param3.y;
         this._bottomOffset = param3.height;
         this.customizationHeader.allowCloseBtnShowing = this._topOffset == 0;
         this._actualWidth = param1;
         this._actualHeight = param2;
         invalidateSize();
         this.styleInfo.invalidateSize();
      }
      
      private function updateInnerEntryPoints() : void
      {
         if(this._entries == null || this._entries.length <= 0)
         {
            return;
         }
         var _loc1_:C11nInnerEntryPoint = this.getFirstVisibleEntry();
         if(_loc1_ == null)
         {
            return;
         }
         var _loc2_:Boolean = App.appWidth < SIDEBAR_MIN_SCREEN_SIZE;
         var _loc3_:Boolean = App.appHeight < StageSizeBoundaries.HEIGHT_1080;
         var _loc4_:Number = !!_loc3_ ? Number(ENTRY_POINT_MIN_SCALE) : Number(ENTRY_POINT_SCALE);
         var _loc5_:int = this.getInnerEntriesCount();
         var _loc6_:Boolean = _loc5_ > 1;
         var _loc7_:int = this.bottomPanel.y - (this.bottomPanel.y >> 2);
         var _loc8_:int = _loc1_.height * _loc4_;
         var _loc9_:int = (!!_loc6_ ? FIRST_ENTRY_POINT_SMALL_GAP : FIRST_ENTRY_POINT_GAP) * _loc4_;
         var _loc10_:int = _loc8_ + _loc9_;
         var _loc11_:int = Values.ZERO;
         if(_loc2_)
         {
            _loc11_ = !!_loc6_ ? int(ENTRY_POINT_SMALL_SHORT_START_X) : int(ENTRY_POINT_SHORT_START_X);
         }
         else
         {
            _loc11_ = !!_loc6_ ? int(ENTRY_POINT_SMALL_START_X) : int(ENTRY_POINT_START_X);
         }
         var _loc12_:int = _loc7_ - (_loc5_ * _loc10_ - _loc9_ >> 1) - _loc1_.hitMc.y * _loc4_ + (!!_loc6_ ? 0 : SINGLE_ENTRY_POINT_Y_SHIFT);
         var _loc13_:C11nInnerEntryPoint = null;
         var _loc14_:int = this._entries.length;
         var _loc15_:int = 0;
         while(_loc15_ < _loc14_)
         {
            _loc13_ = this._entries[_loc15_];
            if(this._innerEntriesData[_loc15_].isVisible)
            {
               _loc13_.setScale(_loc4_);
               _loc13_.x = _loc11_;
               _loc13_.y = _loc12_;
               _loc12_ += _loc10_;
            }
            _loc15_++;
         }
      }
      
      private function getFirstVisibleEntry() : C11nInnerEntryPoint
      {
         var _loc1_:C11nInnerEntryPoint = null;
         for each(_loc1_ in this._entries)
         {
            if(_loc1_.visible)
            {
               return _loc1_;
            }
         }
         return null;
      }
      
      private function getInnerEntriesCount() : uint
      {
         var _loc2_:CustomizationInnerEntryPointVO = null;
         if(!this._innerEntriesData)
         {
            return Values.ZERO;
         }
         var _loc1_:int = Values.ZERO;
         for each(_loc2_ in this._innerEntriesData)
         {
            if(_loc2_.isVisible)
            {
               _loc1_++;
            }
         }
         return _loc1_;
      }
      
      private function invalidateInnerEntriesData() : void
      {
         if(this._innerEntriesData == null)
         {
            return;
         }
         var _loc1_:C11nInnerEntryPoint = null;
         var _loc2_:uint = this._innerEntriesData.length;
         var _loc3_:Boolean = this.getInnerEntriesCount() > 1;
         var _loc4_:int = 0;
         if(this._entries == null)
         {
            this._entries = new Vector.<C11nInnerEntryPoint>();
            this.createHideContainer();
         }
         var _loc5_:int = this._entries.length;
         if(_loc5_ > _loc2_)
         {
            _loc4_ = _loc5_ - _loc2_;
            while(_loc4_ > 0)
            {
               _loc1_ = this._entries.pop();
               this._hideContainer.removeChild(_loc1_);
               _loc1_.dispose();
               _loc1_ = null;
               _loc4_--;
            }
         }
         _loc4_ = 0;
         while(_loc4_ < _loc2_)
         {
            this._innerEntriesData[_loc4_].isSmall = _loc3_;
            if(_loc4_ < _loc5_)
            {
               this._entries[_loc4_].setData(this._innerEntriesData[_loc4_]);
            }
            else
            {
               _loc1_ = App.utils.classFactory.getComponent(CUSTOMIZATION_ALIASES.INNER_ENTRY_POINT,C11nInnerEntryPoint);
               _loc1_.addEventListener(Event.RESIZE,this.onEntryPointResizeChanged);
               this._hideContainer.addChild(_loc1_);
               this._entries.push(_loc1_);
               _loc1_.initData(this._innerEntriesData[_loc4_]);
            }
            _loc4_++;
         }
         invalidateSize();
      }
      
      private function getMagneticClickHandlers() : Vector.<IMagneticClickHandler>
      {
         if(!this._magneticClickHandlers)
         {
            this._magneticClickHandlers = new Vector.<IMagneticClickHandler>();
            this._magneticClickHandlers.push(this.vehicleView.anchorsSet);
            this._magneticClickHandlers.push(this.bottomPanel.carousel);
            this._magneticClickHandlers.push(this.seasonsBar);
         }
         return this._magneticClickHandlers;
      }
      
      private function clearSelectedItem(param1:Boolean = true) : void
      {
         onReleaseItemS();
         if(param1)
         {
            this.vehicleView.anchorsSet.deselectCurrentAnchor();
         }
      }
      
      private function createHideContainer() : void
      {
         if(this._hideContainer == null)
         {
            this._hideContainer = new Sprite();
            this._hideContainer.name = HIDE_CONTAINER_NAME;
            addChild(this._hideContainer);
         }
      }
      
      private function addToHideContainer() : void
      {
         this.createHideContainer();
         removeChild(this.seasonsBar);
         removeChild(this.bottomPanel);
         removeChild(this.vehicleView);
         removeChild(this.propertiesSheet);
         removeChild(this.notification);
         this._hideContainer.addChild(this.vehicleView);
         this._hideContainer.addChild(this.notification);
         this._hideContainer.addChild(this.seasonsBar);
         this._hideContainer.addChild(this.bottomPanel);
         this._hideContainer.addChild(this.propertiesSheet);
      }
      
      private function removeTweens() : void
      {
         var _loc1_:Tween = null;
         for each(_loc1_ in this._tweens)
         {
            _loc1_.paused = true;
            _loc1_.dispose();
            _loc1_ = null;
         }
         this._tweens.splice(0,this._tweens.length);
      }
      
      private function refreshFocusChain() : void
      {
         var _loc1_:InteractiveObject = null;
         for each(_loc1_ in this._focusChain)
         {
            _loc1_.tabIndex = -1;
         }
         this._focusChain.splice(0,this._focusChain.length);
         this._focusChain = this.getFocusChain();
         App.utils.commons.initTabIndex(this._focusChain);
         if(this._focusChain.length > 0)
         {
            setFocus(this._focusChain[0]);
         }
      }
      
      private function closeView(param1:Boolean = false) : void
      {
         App.popoverMgr.hide();
         this.resetMagneticTool();
         if(param1)
         {
            if(this.styleInfo.visible)
            {
               App.stage.dispatchEvent(new CustomizationStyleInfoEvent(CustomizationStyleInfoEvent.CLOSE_STYLE_INFO));
            }
            else
            {
               onPressEscBtnS();
            }
         }
         else
         {
            onCloseWindowS();
         }
      }
      
      private function onHideContainerEnd() : void
      {
         this._hideContainer.visible = false;
      }
      
      private function updateSeasonsBar() : void
      {
         var _loc4_:int = 0;
         var _loc1_:Boolean = this.styleInfo.visible || App.appWidth < SIDEBAR_MIN_SCREEN_SIZE;
         var _loc2_:int = !!_loc1_ ? int(SEASON_BAR_SMALL_OFFSET_X) : int(SEASON_BAR_DEFAULT_OFFSET_X);
         var _loc3_:Boolean = this.getInnerEntriesCount() > 1;
         this.seasonsBar.x = _loc2_;
         if(_loc3_ && !this.styleInfo.visible)
         {
            _loc4_ = this.bottomPanel.y >> 2;
            this.seasonsBar.y = Math.max(Values.ZERO,_loc4_ - (this.seasonsBar.height >> 1)) + SEASON_TOP_SHIFT;
         }
         else
         {
            this.seasonsBar.y = (this._actualHeight - this.seasonsBar.height >> 1) + (!!this.styleInfo.visible ? SEASON_BAR_STYLE_INFO_OFFSET_Y : SEASON_BAR_OFFSET_Y);
         }
         this.seasonsBar.y += this._topOffset > 0 ? SEASON_BAR_TOP_OFFSET : 0;
         this.updateSeasonRenders(_loc1_);
      }
      
      private function updateSeasonRenders(param1:Boolean) : void
      {
         var _loc3_:CustomizationSeasonRenderer = null;
         var _loc2_:int = this.seasonsBar.dataProvider.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc2_)
         {
            _loc3_ = CustomizationSeasonRenderer(this.seasonsBar.getButtonAt(_loc4_));
            if(_loc3_)
            {
               _loc3_.toggleResolution(param1);
            }
            _loc4_++;
         }
      }
      
      private function resetMagneticTool(param1:Boolean = true) : void
      {
         this.vehicleView.anchorsSet.onMagneticReset();
         this._magneticTool.resetSelect();
         this.clearSelectedItem(param1);
      }
      
      private function onEntryPointResizeChanged(param1:Event) : void
      {
         invalidate(INV_ENTRY_POINTS_SIZE);
      }
      
      private function onShopEntryPointHandler(param1:CustomizationEvent) : void
      {
         onShopEntryPointClickS();
      }
      
      private function onShowProgressionInfoHandler(param1:CustomizationEvent) : void
      {
         showQuestProgressionInfoWindowS();
      }
      
      private function onAvailablePagingHandler(param1:CustomizationCarouselScrollEvent) : void
      {
         this.propertiesSheet.anchorSwitchers.updateAvailableScroll(param1.leftScroll,param1.rightScroll);
      }
      
      private function onSeasonBarCompleteHandler(param1:Event) : void
      {
         this.updateSeasonsBar();
      }
      
      private function onSeasonBarIndexChangeHandler(param1:IndexEvent) : void
      {
         var _loc3_:CustomizationCarouselRendererVO = null;
         this.vehicleView.anchorsSet.animatedAnchorStateTransitionsEnabled = false;
         changeSeasonS(param1.index,MagneticToolController.isAllSeasonSelected());
         var _loc2_:CarouselRendererAttachedBase = CarouselRendererAttachedBase(App.cursor.getAttachedSprite());
         if(_loc2_)
         {
            _loc3_ = CustomizationCarouselRendererVO(_loc2_.data);
            if(_loc3_ && !_loc3_.isAllSeasons)
            {
               this._magneticTool.resetSelect();
               this.clearSelectedItem(true);
            }
         }
      }
      
      private function onSeenItemHandler(param1:CustomizationItemEvent) : void
      {
         resetC11nItemsNoveltyS([param1.itemId]);
      }
      
      private function onSelectNextItemHandler(param1:CustomizationItemSwitchEvent) : void
      {
         if(!this.styleInfo.visible)
         {
            onPressSelectNextItemS(param1.reverse);
         }
      }
      
      private function onAnchorsFilledHandler(param1:CustomizationAnchorSetEvent) : void
      {
         onAnchorsShownS(param1.anchors);
      }
      
      private function onShowPropertiesSheetHandler(param1:CustomizationEvent) : void
      {
         this.resetMagneticTool(false);
         this.vehicleView.anchorsSet.deselectCurrentAnchor();
      }
      
      private function onClosePropertiesSheetHandler(param1:CustomizationEvent) : void
      {
         if(this._customizationAnchorInitData && this._customizationAnchorInitData.typeRegions == CUSTOMIZATION_ALIASES.ANCHOR_TYPE_SPECIFIC)
         {
         }
         this.bottomPanel.hideOverlay();
      }
      
      private function onShowStyleInfoHandler(param1:CustomizationStyleInfoEvent) : void
      {
         var _loc2_:int = this._hideContainer.numChildren;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            this._hideContainer.getChildAt(_loc3_).visible = false;
            _loc3_++;
         }
         this.bottomPanel.setCarouselNotificationsVisibility(false);
         this.seasonsBar.visible = true;
         this.removeTweens();
         this.styleInfo.alpha = this.seasonsBar.alpha = HIDE_ALPHA;
         this._tweens.push(new Tween(STYLE_INFO_ANIMATION_DURATION,this.styleInfo,{"alpha":SHOW_ALPHA},{
            "delay":STYLE_INFO_ANIMATION_DELAY,
            "fastTransform":false
         }));
         this._tweens.push(new Tween(STYLE_INFO_ANIMATION_DURATION,this.seasonsBar,{"alpha":SHOW_ALPHA},{
            "delay":STYLE_INFO_ANIMATION_DELAY,
            "fastTransform":false
         }));
         this.updateSeasonsBar();
      }
      
      private function onHideStyleInfoHandler(param1:CustomizationStyleInfoEvent) : void
      {
         var _loc2_:int = this._hideContainer.numChildren;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            this._hideContainer.getChildAt(_loc3_).visible = true;
            _loc3_++;
         }
         this.bottomPanel.setCarouselNotificationsVisibility(true);
         this.removeTweens();
         this.styleInfo.alpha = this.seasonsBar.alpha = SHOW_ALPHA;
         this.updateSeasonsBar();
      }
      
      private function onShowInscriptionControllerHandler(param1:CustomizationEvent) : void
      {
         this._inscriptionControllerShown = true;
         this.resetMagneticTool();
      }
      
      private function onHideInscriptionControllerHandler(param1:CustomizationEvent) : void
      {
         this._inscriptionControllerShown = false;
         if(this._dragOccurred)
         {
            this.propertiesSheet.visible = false;
            this.onStageDraggingStartHandler(new LobbyEvent(LobbyEvent.DRAGGING_START));
         }
      }
      
      private function onLobbyDraggingHandler(param1:LobbyEvent) : void
      {
         this._dragOccurred = stage.mouseX != this._dragMouseX || stage.mouseY != this._dragMouseY;
      }
      
      private function onSelectAnchorHandler(param1:CustomizationAnchorEvent) : void
      {
         var _loc2_:CustomizationSlotIdVO = null;
         if(param1.anchor.id != null)
         {
            _loc2_ = param1.anchor.id;
            this.onRegionHighlighted(_loc2_,false,false,false);
            onSelectAnchorS(_loc2_.areaId,_loc2_.slotType,_loc2_.regionIdx);
            this.notification.hide();
         }
      }
      
      private function onLockedAnchorHandler(param1:CustomizationAnchorEvent) : void
      {
         this.notification.addToAnchor(param1.anchor);
         this.notification.show();
      }
      
      private function onOverAnchorHandler(param1:CustomizationAnchorEvent) : void
      {
         var _loc2_:CustomizationSlotIdVO = null;
         if(param1.anchor.id != null)
         {
            _loc2_ = param1.anchor.id;
            onHoverAnchorS(_loc2_.areaId,_loc2_.slotType,_loc2_.regionIdx,true);
         }
      }
      
      private function onOutAnchorHandler(param1:CustomizationAnchorEvent) : void
      {
         var _loc2_:CustomizationSlotIdVO = null;
         if(param1.anchor.id != null)
         {
            _loc2_ = param1.anchor.id;
            onHoverAnchorS(_loc2_.areaId,_loc2_.slotType,_loc2_.regionIdx,false);
         }
      }
      
      private function onDragAnchorHandler(param1:CustomizationAnchorEvent) : void
      {
         var _loc2_:CustomizationSlotIdVO = param1.anchor.id;
         onDragAnchorS(_loc2_.areaId,_loc2_.slotType,_loc2_.regionIdx);
      }
      
      private function onCustomizationPlaySoundHandler(param1:CustomizationSoundEvent) : void
      {
         playCustomSoundS(param1.sound);
      }
      
      private function onCarouselSelectItemHandler(param1:CustomizationItemEvent) : void
      {
         if(!this._magneticTool.enableSelected)
         {
            return;
         }
         var _loc2_:CarouselItemRenderer = param1.target as CarouselItemRenderer;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:CustomizationCarouselRendererVO = CustomizationCarouselRendererVO(_loc2_.data);
         if(!_loc3_)
         {
            return;
         }
         this._magneticTool.attachDataToCursor(_loc3_);
         this.vehicleView.onStartDrop();
      }
      
      private function onStageDraggingStartHandler(param1:LobbyEvent) : void
      {
         var _loc3_:DisplayObject = null;
         if(this._inscriptionControllerShown)
         {
            return;
         }
         this.vehicleView.onDragStart();
         fadeOutAnchorsS(true);
         this._dragMouseX = stage.mouseX;
         this._dragMouseY = stage.mouseY;
         this.removeTweens();
         this._tweens.push(new Tween(ANIMATION_DURATION,this._hideContainer,{"alpha":HIDE_ALPHA},{
            "delay":ANIMATION_DELAY,
            "onComplete":this.onHideContainerEnd
         }));
         this._hideContainer.mouseEnabled = this._hideContainer.mouseChildren = false;
         this.notification.hide();
         var _loc2_:uint = 0;
         while(_loc2_ < numChildren)
         {
            _loc3_ = getChildAt(_loc2_);
            if(_loc3_ is TutorialHint)
            {
               (_loc3_ as TutorialHint).fadeOut();
            }
            _loc2_++;
         }
      }
      
      private function onStageDraggingEndHandler(param1:LobbyEvent) : void
      {
         var _loc2_:uint = 0;
         var _loc3_:DisplayObject = null;
         this.removeTweens();
         this._hideContainer.visible = true;
         this.propertiesSheet.visible = true;
         if(this._hideContainer.alpha != SHOW_ALPHA)
         {
            this._tweens.push(new Tween(ANIMATION_DURATION,this._hideContainer,{"alpha":SHOW_ALPHA},{}));
         }
         this._hideContainer.mouseEnabled = this._hideContainer.mouseChildren = true;
         this.vehicleView.onDragEnd();
         if(!this._dragOccurred)
         {
            onLobbyClickS();
         }
         this._dragOccurred = false;
         fadeOutAnchorsS(false);
         while(_loc2_ < numChildren)
         {
            _loc3_ = getChildAt(_loc2_);
            if(_loc3_ is TutorialHint)
            {
               (_loc3_ as TutorialHint).fadeIn();
            }
            _loc2_++;
         }
      }
      
      private function onCloseViewHandler(param1:CustomizationEvent) : void
      {
         this.closeView();
      }
      
      private function onShowBuyWindowHandler(param1:CustomizationEvent) : void
      {
         showBuyWindowS();
      }
      
      private function onBottomPanelButtonPressedHandler(param1:CustomizationButtonEvent) : void
      {
         onButtonPressedS(param1.name);
      }
      
      private function onEntryPointClickHandler(param1:CustomizationEvent) : void
      {
         var _loc2_:int = this._innerEntriesData.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            this._innerEntriesData[_loc3_].isSelected = this._innerEntriesData[_loc3_].itemId == param1.group && !this._innerEntriesData[_loc3_].isSelected;
            _loc3_++;
         }
         this.invalidateInnerEntriesData();
         onEntryPointClickS(param1.group);
      }
      
      private function onKeyDownHandler(param1:InputEvent = null) : void
      {
         switch(param1.details.code)
         {
            case Keyboard.ESCAPE:
               if(this._magneticTool.attachedData)
               {
                  this.resetMagneticTool();
               }
               else
               {
                  this.closeView(true);
               }
               break;
            case Keyboard.LEFT:
            case Keyboard.RIGHT:
               this.propertiesSheet.onKeyDownHandler(param1.details);
               this.bottomPanel.hideOverlay();
               break;
            case Keyboard.DELETE:
            case Keyboard.NUMPAD_DECIMAL:
               onRemoveSelectedItem();
         }
      }
      
      private function onMouseWheelHandler(param1:MouseEvent) : void
      {
         this.notification.hide();
      }
      
      private function onMouseUpHandler(param1:MouseEvent) : void
      {
         if(this._dragOccurred)
         {
            return;
         }
         var _loc2_:Boolean = checkClickRightMouse(param1);
         if(this._magneticTool.attachedData)
         {
            if(_loc2_ || this._magneticTool.handleLeftClick(param1))
            {
               this.resetMagneticTool();
            }
         }
      }
   }
}
