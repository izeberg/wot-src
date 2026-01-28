package net.wg.gui.lobby.vehicleCustomization
{
   import flash.display.DisplayObject;
   import flash.display.InteractiveObject;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.ListDAAPIDataProvider;
   import net.wg.data.VO.TankCarouselFilterInitVO;
   import net.wg.data.constants.Values;
   import net.wg.data.managers.impl.ToolTipParams;
   import net.wg.gui.components.carousels.HorizontalScroller;
   import net.wg.gui.components.carousels.ScrollCarousel;
   import net.wg.gui.components.carousels.interfaces.IFilterCounter;
   import net.wg.gui.components.controls.BitmapFill;
   import net.wg.gui.components.controls.ScrollBarBookmarked;
   import net.wg.gui.components.controls.events.RendererEvent;
   import net.wg.gui.events.FiltersEvent;
   import net.wg.gui.interfaces.IMagneticClickHandler;
   import net.wg.gui.interfaces.ISoundButtonEx;
   import net.wg.gui.lobby.vehicleCustomization.controls.CarouselItemRenderer;
   import net.wg.gui.lobby.vehicleCustomization.controls.ShopEntryPoint;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationCarouselFilters;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationCarouselFilterSelectedVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselBookmarkVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselDataVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselFilterVO;
   import net.wg.gui.lobby.vehicleCustomization.data.customizationPanel.CustomizationCarouselRendererVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.interfaces.IFocusChainContainer;
   import net.wg.utils.IClassFactory;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class CustomizationCarousel extends ScrollCarousel implements IFocusChainContainer, IMagneticClickHandler
   {
      
      private static const NORMAL_ITEM_GAP:Number = 20;
      
      private static const MIN_RES_ITEM_GAP:Number = 16;
      
      private static const MASK_SIDE_OFFSET:int = -10;
      
      private static const MASK_TOP_OFFSET:int = -25;
      
      private static const BOOKMARKS_COEFFICIENT:int = 4;
      
      private static const VIEPORT_EXTRA_OFFSET:int = 79;
      
      private static const SCROLL_X_OFFSET:int = 23;
      
      private static const SCROLL_Y_OFFSET:int = 10;
      
      private static const SCROLL_EXTRA_WIDTH:int = 8;
      
      private static const MIN_RESOLUTION:int = 900;
      
      private static const FILTERS_GAP_OFFSET:int = -5;
      
      private static const BOOK_MARK_BACK_MOVIE:String = "BookmarkBackingUI";
      
      private static const SHOP_ENTRY_POINT_BUTTON_SMALL_UI:String = "ShopEntryPointButtonSmallUI";
      
      private static const SHOP_ENTRY_POINT_BUTTON_BIG_UI:String = "ShopEntryPointButtonBigUI";
      
      private static const GO_TO_OFFSET:Number = 0.5;
      
      private static const GO_TO_DURATION:Number = 1;
      
      private static const BOOKMARK_START_OFFSET:int = 5;
      
      private static const HIT_AREA_HEIGHT:int = 116;
      
      private static const HIT_AREA_HEIGHT_MIN:int = 95;
      
      private static const FILTERS_COUNTER_OFFSET:int = 3;
      
      private static const SHOP_ENTRY_Y_SMALL:int = 64;
      
      private static const SHOP_ENTRY_Y_BIG:int = 26;
      
      private static const SHOP_ENTRY_X:int = 0;
      
      private static const BG_OFFSET_Y:int = 25;
      
      private static const BG_HEIGHT:int = 160;
      
      private static const BG_HEIGHT_SMALL:int = 139;
      
      private static const LBL_MESSAGE_OFFSET_Y:uint = 2;
      
      private static const BTN_DEFAULT_OFFSET_Y:uint = 10;
      
      private static const FADE_MASK_LABEL_SMALL:String = "small";
      
      private static const FADE_MASK_LABEL_LARGE:String = "large";
      
      private static const FADE_MASK_Y_OFFSET:int = 28;
      
      private static const SCROLL_MARGIN:int = 38;
      
      private static const PADDING_LEFT_SMALL:int = 232;
      
      private static const PADDING_LEFT_MEDIUM:int = 252;
      
      private static const PADDING_LEFT_LARGE:int = 296;
      
      private static const FADE_ALPHA_DEFAULT:Number = 1;
      
      private static const FADE_ALPHA_NOSCROLL:Number = 0.5;
      
      private static const TILE_BG_ALPHA:Number = 0.6;
      
      private static const INVALID_GO_TO_ITEM:String = "INVALID_GO_TO_ITEM";
       
      
      public var lblMessage:TextField = null;
      
      public var btnDefault:ISoundButtonEx = null;
      
      public var scrollBar:ScrollBarBookmarked = null;
      
      public var filterCounter:IFilterCounter = null;
      
      public var dragBlocker:MovieClip = null;
      
      public var carouselFilters:CustomizationCarouselFilters = null;
      
      public var shopEntryPointBtn:ShopEntryPoint = null;
      
      public var tiledBackgroundCenter:BitmapFill = null;
      
      public var projectionDecalHint:UIComponentEx = null;
      
      public var editableStyleHint:UIComponentEx = null;
      
      public var progressionDecalHint:UIComponentEx = null;
      
      private var _layoutController:CustomizationCarouselLayoutController = null;
      
      private var _layoutRenderer:CustomizationCarouselLayoutRenderer = null;
      
      private var _bookmarkBackings:Vector.<MovieClip>;
      
      private var _dataProvider:ListDAAPIDataProvider = null;
      
      private var _data:CustomizationCarouselDataVO = null;
      
      private var _oldWidth:Number = 0;
      
      private var _isMinResolution:Boolean;
      
      private var _classFactory:IClassFactory;
      
      private var _tabBarOffset:int = 0;
      
      private var _paddingLeft:int = 0;
      
      private var _scrollToIndex:int = 0;
      
      public function CustomizationCarousel()
      {
         this._bookmarkBackings = new Vector.<MovieClip>();
         this._classFactory = App.utils.classFactory;
         super();
         roundCountRenderer = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         scrollList.hasHorizontalElasticEdges = true;
         scrollList.snapScrollPositionToItemRendererSize = false;
         scrollList.horizontalGap = NORMAL_ITEM_GAP;
         scrollList.snapToPages = true;
         scrollList.goToOffset = GO_TO_OFFSET;
         scrollList.goToDuration = GO_TO_DURATION;
         scrollList.cropContent = true;
         scrollList.maskOffsetLeft = scrollList.maskOffsetRight = MASK_SIDE_OFFSET;
         scrollList.maskOffsetTop = MASK_TOP_OFFSET;
         scrollList.showRendererOnlyIfDataExists = true;
         this.lblMessage.autoSize = TextFieldAutoSize.LEFT;
         this.btnDefault.label = VEHICLE_CUSTOMIZATION.CAROUSEL_RESETFILTERSBTN_LABEL;
         this.btnDefault.focusable = false;
         this.btnDefault.addEventListener(ButtonEvent.CLICK,this.onBtnDefaultClickHandler);
         this.btnDefault.addEventListener(MouseEvent.ROLL_OVER,this.onBtnDefaultRollOverHandler);
         this.btnDefault.addEventListener(MouseEvent.ROLL_OUT,this.onBtnDefaultRollOutHandler);
         this.filterCounter.setCloseButtonSimpleTooltip(VEHICLE_CUSTOMIZATION.CAROUSEL_RESETFILTERSBTN_TOOLTIP);
         this._layoutController = new CustomizationCarouselLayoutController(scrollList);
         this._layoutRenderer = new CustomizationCarouselLayoutRenderer(scrollList,this._layoutController);
         scrollList.setLayoutController(this._layoutController);
         scrollList.setScrollbar(this.scrollBar);
         this.scrollBar.setBookmarkStartOffset(BOOKMARK_START_OFFSET);
         this.carouselFilters.addEventListener(RendererEvent.ITEM_CLICK,this.onCarouselFiltersItemClickHandler);
         this.carouselFilters.addEventListener(Event.RESIZE,this.onCarouselFiltersResizeHandler);
         endFadeMask.mouseEnabled = false;
         startFadeMask.mouseEnabled = false;
         this.tiledBackgroundCenter.mouseEnabled = this.tiledBackgroundCenter.mouseChildren = false;
         this.tiledBackgroundCenter.alpha = TILE_BG_ALPHA;
         App.utils.commons.addEmptyHitArea(this.tiledBackgroundCenter);
         this.createShopEntryPoint();
      }
      
      override protected function onDispose() : void
      {
         this._dataProvider.removeEventListener(Event.CHANGE,this.onDataProviderChangeHandler);
         this.btnDefault.removeEventListener(ButtonEvent.CLICK,this.onBtnDefaultClickHandler);
         this.btnDefault.removeEventListener(MouseEvent.ROLL_OVER,this.onBtnDefaultRollOverHandler);
         this.btnDefault.removeEventListener(MouseEvent.ROLL_OUT,this.onBtnDefaultRollOutHandler);
         this.carouselFilters.removeEventListener(Event.RESIZE,this.onCarouselFiltersResizeHandler);
         this.carouselFilters.removeEventListener(RendererEvent.ITEM_CLICK,this.onCarouselFiltersItemClickHandler);
         this._bookmarkBackings.splice(0,this._bookmarkBackings.length);
         this._bookmarkBackings = null;
         this._layoutRenderer.dispose();
         this._layoutRenderer = null;
         this.scrollBar.dispose();
         this.scrollBar = null;
         this.carouselFilters.dispose();
         this.carouselFilters = null;
         this.lblMessage = null;
         this.btnDefault.dispose();
         this.btnDefault = null;
         this.filterCounter.dispose();
         this.filterCounter = null;
         this.projectionDecalHint.dispose();
         this.projectionDecalHint = null;
         this.editableStyleHint.dispose();
         this.editableStyleHint = null;
         this.progressionDecalHint.dispose();
         this.progressionDecalHint = null;
         this._dataProvider.cleanUp();
         this._dataProvider = null;
         this._layoutController.dispose();
         this._layoutController = null;
         this._data = null;
         this.dragBlocker = null;
         this._classFactory = null;
         this.tiledBackgroundCenter.hitArea = null;
         this.tiledBackgroundCenter.dispose();
         this.tiledBackgroundCenter = null;
         this.removeShopEntryPoint();
         super.onDispose();
      }
      
      override protected function updateLayout(param1:int, param2:int = 0) : void
      {
         var _loc9_:Rectangle = null;
         var _loc3_:int = this.paddingLeft - SCROLL_X_OFFSET;
         var _loc4_:int = param1 - this.paddingLeft + SCROLL_EXTRA_WIDTH;
         var _loc5_:int = this.scrollList.viewPort.width + VIEPORT_EXTRA_OFFSET;
         var _loc6_:int = Math.min(_loc5_,_loc4_);
         var _loc7_:int = Math.max(param1 - _loc6_ >> 1,_loc3_);
         var _loc8_:int = _loc6_ + leftArrowOffset - rightArrowOffset;
         if(this.shopEntryPointBtn)
         {
            this.shopEntryPointBtn.x = SHOP_ENTRY_X;
            this.shopEntryPointBtn.y = !!this._isMinResolution ? Number(SHOP_ENTRY_Y_SMALL) : Number(SHOP_ENTRY_Y_BIG);
         }
         this.carouselFilters.x = this.paddingLeft - this.carouselFilters.width - SCROLL_MARGIN;
         this.filterCounter.x = this.carouselFilters.x + (this.carouselFilters.width - this.filterCounter.width >> 1) - FILTERS_COUNTER_OFFSET;
         super.updateLayout(_loc6_,(_loc6_ - _loc8_ >> 1) + _loc7_);
         this.scrollBar.setVisibleBookmarks(scrollList.viewPort.width / _loc6_ > BOOKMARKS_COEFFICIENT);
         this.dragBlocker.width = param1;
         if(hasScrollButtons)
         {
            _loc9_ = CustomizationShared.computeItemSize(false,this._isMinResolution);
            leftArrow.height = _loc9_.height;
            rightArrow.height = _loc9_.height;
         }
         this.scrollBar.width = scrollList.width;
         this.scrollBar.x = scrollList.x;
         this.scrollBar.y = leftArrow.y + leftArrow.height + SCROLL_Y_OFFSET;
         this.projectionDecalHint.x = this.editableStyleHint.x = this.progressionDecalHint.x = scrollList.x;
         this.projectionDecalHint.y = this.editableStyleHint.y = this.progressionDecalHint.y = scrollList.y;
         this.projectionDecalHint.width = this.editableStyleHint.width = this.progressionDecalHint.width = scrollList.width;
         this.projectionDecalHint.height = this.editableStyleHint.height = this.progressionDecalHint.height = !!this._isMinResolution ? Number(HIT_AREA_HEIGHT_MIN) : Number(HIT_AREA_HEIGHT);
         this.carouselFilters.gapOffset = int(this._isMinResolution) * FILTERS_GAP_OFFSET;
         leftArrow.x = this.paddingLeft - leftArrow.width;
         rightArrow.x = _width - SCROLL_MARGIN + rightArrow.width;
         startFadeMask.x = this.paddingLeft;
         endFadeMask.x = _width - SCROLL_MARGIN;
         endFadeMask.y = startFadeMask.y = scrollList.y - FADE_MASK_Y_OFFSET;
         this.tiledBackgroundCenter.widthFill = param1;
         this.tiledBackgroundCenter.y = scrollList.y - BG_OFFSET_Y;
         this.tiledBackgroundCenter.heightFill = !!this._isMinResolution ? Number(BG_HEIGHT_SMALL) : Number(BG_HEIGHT);
         this.updateLblMessagePosition();
         this.updateBtnDefaultPosition();
      }
      
      override protected function updateAvailableScroll(param1:Boolean, param2:Boolean) : void
      {
         super.updateAvailableScroll(param1,param2);
         leftArrow.visible = rightArrow.visible = param1 || param2;
         endFadeMask.alpha = startFadeMask.alpha = param1 || param2 ? Number(FADE_ALPHA_DEFAULT) : Number(FADE_ALPHA_NOSCROLL);
         if(!param1 && !param2)
         {
            this.scrollBar.clearBookmarks();
         }
      }
      
      override protected function scrollListResizeComplete() : void
      {
         super.scrollListResizeComplete();
         invalidateSize();
         this._layoutController.invalidateData();
      }
      
      override protected function draw() : void
      {
         var _loc3_:String = null;
         var _loc4_:Vector.<Rectangle> = null;
         var _loc5_:Vector.<Rectangle> = null;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:MovieClip = null;
         var _loc9_:CustomizationCarouselBookmarkVO = null;
         var _loc10_:CustomizationCarouselBookmarkVO = null;
         var _loc11_:int = 0;
         var _loc12_:int = 0;
         var _loc13_:Rectangle = null;
         var _loc14_:Boolean = false;
         var _loc15_:int = 0;
         var _loc1_:Boolean = isInvalid(InvalidationType.SIZE);
         if(_loc1_)
         {
            if(App.appHeight < StageSizeBoundaries.HEIGHT_900)
            {
               this._paddingLeft = App.appWidth < StageSizeBoundaries.WIDTH_1366 ? int(PADDING_LEFT_SMALL) : int(PADDING_LEFT_MEDIUM);
            }
            else
            {
               this._paddingLeft = PADDING_LEFT_LARGE;
            }
         }
         super.draw();
         var _loc2_:Boolean = App.appHeight < MIN_RESOLUTION;
         if((this._oldWidth != _width || this._isMinResolution != _loc2_) && _loc1_)
         {
            this._oldWidth = _width;
            if(this._isMinResolution != _loc2_)
            {
               this._isMinResolution = _loc2_;
               this.createShopEntryPoint();
            }
            _loc3_ = !!this._isMinResolution ? FADE_MASK_LABEL_SMALL : FADE_MASK_LABEL_LARGE;
            startFadeMask.gotoAndStop(_loc3_);
            endFadeMask.gotoAndStop(_loc3_);
            scrollList.horizontalGap = !!_loc2_ ? int(MIN_RES_ITEM_GAP) : int(NORMAL_ITEM_GAP);
            this._dataProvider.dispatchEvent(new Event(Event.CHANGE));
         }
         if(this._data != null && scrollList.viewPort != null && isInvalid(InvalidationType.DATA))
         {
            this.scrollBar.clearBookmarks();
            _loc4_ = this._layoutController.getLayout();
            _loc5_ = this._layoutController.getBookmarksLayout();
            _loc6_ = Math.min(_loc5_.length,this._data.bookmarks.length);
            _loc7_ = _loc4_.length;
            for each(_loc8_ in this._bookmarkBackings)
            {
               HorizontalScroller(scrollList).removeUnmanagedChild(_loc8_);
               _loc8_.visible = false;
            }
            this._bookmarkBackings.splice(0,this._bookmarkBackings.length);
            _loc13_ = null;
            _loc14_ = false;
            _loc15_ = 0;
            while(_loc15_ < _loc6_)
            {
               _loc9_ = this._data.bookmarks[_loc15_];
               _loc11_ = _loc9_.bookmarkIndex;
               if(_loc11_ < 0)
               {
                  _loc11_ = _loc7_ - 1;
               }
               if(_loc11_ < _loc7_)
               {
                  _loc13_ = _loc4_[_loc11_];
                  if(_loc15_ + 1 < _loc6_)
                  {
                     _loc10_ = this._data.bookmarks[_loc15_ + 1];
                     if(_loc10_)
                     {
                        _loc12_ = _loc10_.bookmarkIndex;
                     }
                  }
                  _loc14_ = Boolean(_loc12_ == _loc11_ + 1);
                  this.addBookmarkItem(_loc5_[_loc15_],_loc9_,_loc14_);
                  this.scrollBar.addBookmark(_loc13_.right,TOOLTIPS.CUSTOMIZATION_SCROLLBAR_BOOKMARK,new ToolTipParams({"bookmark":_loc9_.bookmarkName}));
               }
               _loc12_ = _loc11_;
               _loc15_++;
            }
            this.scrollBar.validateNow();
            if(_loc7_ > 0)
            {
               pageWidth = _loc4_[0].width + horizontalGap;
            }
            this.lblMessage.visible = _loc7_ == 0;
            this.btnDefault.visible = this.lblMessage.visible;
            scrollList.visible = true;
            this.carouselFilters.updateHotFilterSelectedFromData = false;
            this._layoutRenderer.render();
         }
         if(INVALID_GO_TO_ITEM)
         {
            this.scrollToItem();
         }
      }
      
      override public function goToItem(param1:int, param2:Boolean = false, param3:Boolean = false) : void
      {
         this._scrollToIndex = param1;
         invalidate(INVALID_GO_TO_ITEM);
      }
      
      public function itemIsOutOfView(param1:int) : Boolean
      {
         var _loc2_:Vector.<Rectangle> = null;
         var _loc3_:Rectangle = null;
         var _loc4_:Boolean = false;
         var _loc5_:Boolean = false;
         if(this._layoutController)
         {
            _loc2_ = this._layoutController.getLayout();
            if(_loc2_.length > param1)
            {
               _loc3_ = _loc2_[param1];
               _loc4_ = scrollList.horizontalScrollPosition > _loc3_.x;
               _loc5_ = scrollList.horizontalScrollPosition + scrollList.width < _loc3_.x + _loc3_.width;
               return _loc4_ || _loc5_;
            }
         }
         return false;
      }
      
      public function clearSelected() : void
      {
         selectedIndex = Values.DEFAULT_INT;
      }
      
      public function getDataProvider() : Object
      {
         if(this._dataProvider == null)
         {
            this._dataProvider = new ListDAAPIDataProvider(CustomizationCarouselRendererVO);
            scrollList.dataProvider = this._dataProvider;
            this._dataProvider.addEventListener(Event.CHANGE,this.onDataProviderChangeHandler);
         }
         return this._dataProvider;
      }
      
      public function getFocusChain() : Vector.<InteractiveObject>
      {
         var _loc1_:Vector.<InteractiveObject> = new Vector.<InteractiveObject>();
         if(visible)
         {
            _loc1_.push(this.carouselFilters,scrollList);
         }
         return _loc1_;
      }
      
      public function playFilterBlink() : void
      {
         this.filterCounter.blink();
      }
      
      public function selectSlot(param1:int, param2:Boolean = false) : CustomizationCarouselRendererVO
      {
         var _loc3_:CustomizationCarouselRendererVO = null;
         var _loc4_:int = this._dataProvider.length;
         var _loc5_:int = 0;
         while(_loc5_ < _loc4_)
         {
            _loc3_ = CustomizationCarouselRendererVO(this._dataProvider.requestItemAt(_loc5_));
            if(_loc3_.intCD == param1)
            {
               selectedIndex = _loc5_;
               this.goToItem(selectedIndex,param2);
               return _loc3_;
            }
            _loc5_++;
         }
         selectedIndex = -1;
         return _loc3_;
      }
      
      public function setCarouselFiltersData(param1:CustomizationCarouselFilterSelectedVO) : void
      {
         this.carouselFilters.setSelectedData(param1);
         this.updatePopoverData();
      }
      
      public function setCarouselFiltersInitData(param1:TankCarouselFilterInitVO) : void
      {
         this.carouselFilters.initData(param1);
         this.updatePopoverData();
      }
      
      public function setData(param1:CustomizationCarouselDataVO) : void
      {
         if(param1 != null && this._data != param1)
         {
            this._data = param1;
            if(this._layoutController)
            {
               this._layoutController.setData(param1);
               invalidateData();
               invalidateSize();
            }
            if(this._data.shouldShow)
            {
               this.filterCounter.setCount(param1.displayString,param1.isZeroCount);
            }
            else
            {
               this.filterCounter.hide();
            }
            this.updatePopoverData();
         }
      }
      
      public function setFilterData(param1:CustomizationCarouselFilterVO) : void
      {
         var _loc2_:Object = {
            "purchasedEnabled":param1.purchasedEnabled,
            "historicEnabled":param1.historicEnabled,
            "nonHistoricEnabled":param1.nonHistoricEnabled,
            "fantasticalEnabled":param1.fantasticalEnabled,
            "appliedEnabled":param1.appliedEnabled,
            "favoriteEnabled":param1.favoriteEnabled,
            "groups":param1.groups,
            "selectedGroup":param1.selectedGroup,
            "groupCount":param1.groupCount,
            "formfactorGroups":param1.formfactorGroups,
            "displayGroups":param1.displayGroups,
            "hideOnAnotherVehEnabled":param1.hideOnAnotherVehEnabled,
            "showOnlyProgressionDecalsEnabled":param1.showOnlyProgressionDecalsEnabled,
            "showOnlyEditableStylesEnabled":param1.showOnlyEditableStylesEnabled,
            "showOnlyNonEditableStylesEnabled":param1.showOnlyNonEditableStylesEnabled,
            "showOnlyProgressionStylesEnabled":param1.showOnlyProgressionStylesEnabled,
            "isInit":true
         };
         this.carouselFilters.popoverData = _loc2_;
      }
      
      public function setFilterMessage(param1:String) : void
      {
         this.lblMessage.htmlText = param1;
      }
      
      public function setTabBarOffset(param1:int) : void
      {
         this._tabBarOffset = param1;
         this.updateLblMessagePosition();
         this.updateBtnDefaultPosition();
      }
      
      private function scrollToItem() : void
      {
         var _loc1_:Vector.<Rectangle> = null;
         var _loc2_:Rectangle = null;
         var _loc3_:int = 0;
         if(this._layoutController && this._scrollToIndex > Values.DEFAULT_INT)
         {
            _loc1_ = this._layoutController.getLayout();
            if(_loc1_.length > this._scrollToIndex)
            {
               _loc2_ = _loc1_[this._scrollToIndex];
               _loc3_ = -1;
               if(_loc2_.x < scrollList.horizontalScrollPosition)
               {
                  _loc3_ = _loc2_.x;
               }
               else if(_loc2_.x + _loc2_.width - scrollList.width > scrollList.horizontalScrollPosition)
               {
                  _loc3_ = _loc2_.x + _loc2_.width - scrollList.width;
               }
               if(_loc3_ != -1)
               {
                  if(_loc3_ > scrollList.maxHorizontalScrollPosition)
                  {
                     _loc3_ = scrollList.maxHorizontalScrollPosition;
                  }
                  else if(_loc3_ < scrollList.minHorizontalScrollPosition)
                  {
                     _loc3_ = scrollList.minHorizontalScrollPosition;
                  }
                  scrollList.horizontalScrollPosition = _loc3_;
                  return;
               }
            }
         }
         this._scrollToIndex = Values.DEFAULT_INT;
      }
      
      private function updateLblMessagePosition() : void
      {
         this.lblMessage.x = this._tabBarOffset - (this.lblMessage.width >> 1);
         this.lblMessage.y = this.tiledBackgroundCenter.y + (this.tiledBackgroundCenter.heightFill - this.lblMessage.height - this.btnDefault.height - BTN_DEFAULT_OFFSET_Y >> 1) - LBL_MESSAGE_OFFSET_Y;
      }
      
      private function updateBtnDefaultPosition() : void
      {
         this.btnDefault.x = this.lblMessage.x + (this.lblMessage.width - this.btnDefault.width >> 1);
         this.btnDefault.y = this.lblMessage.y + this.lblMessage.height + BTN_DEFAULT_OFFSET_Y;
      }
      
      private function removeShopEntryPoint() : void
      {
         if(this.shopEntryPointBtn)
         {
            removeChild(this.shopEntryPointBtn);
            this.shopEntryPointBtn.dispose();
            this.shopEntryPointBtn = null;
         }
      }
      
      private function createShopEntryPoint() : void
      {
         this.removeShopEntryPoint();
         this.shopEntryPointBtn = this._classFactory.getComponent(!!this._isMinResolution ? SHOP_ENTRY_POINT_BUTTON_SMALL_UI : SHOP_ENTRY_POINT_BUTTON_BIG_UI,ShopEntryPoint);
         this.shopEntryPointBtn.label = VEHICLE_CUSTOMIZATION.SHOP_ENTRYPOINT;
         addChild(this.shopEntryPointBtn);
      }
      
      private function addBookmarkItem(param1:Rectangle, param2:CustomizationCarouselBookmarkVO, param3:Boolean) : void
      {
         var _loc4_:Class = App.instance.utils.classFactory.getClass(BOOK_MARK_BACK_MOVIE);
         var _loc5_:CustomizationCarouselBookmark = new _loc4_() as CustomizationCarouselBookmark;
         if(_loc5_ != null)
         {
            _loc5_.visible = true;
            HorizontalScroller(scrollList).addUnmanagedChild(_loc5_,0);
            _loc5_.width = param1.width;
            _loc5_.x = param1.x;
            _loc5_.y = param1.y;
            _loc5_.setBookmarkNameText(param2.bookmarkName,param3);
            this._bookmarkBackings.push(_loc5_);
         }
      }
      
      private function updateSelectedIndex() : void
      {
         selectedIndex = this._dataProvider.getDAAPIselectedIdx();
      }
      
      private function updatePopoverData() : void
      {
         dispatchEvent(new CustomizationEvent(CustomizationEvent.REFRESH_FILTER_DATA,false));
      }
      
      private function get paddingLeft() : int
      {
         return this._paddingLeft;
      }
      
      public function handleLeftClick(param1:MouseEvent) : Boolean
      {
         return DisplayObject(param1.target) is CarouselItemRenderer;
      }
      
      private function onCarouselFiltersItemClickHandler(param1:RendererEvent) : void
      {
         dispatchEvent(new CustomizationEvent(CustomizationEvent.SELECT_HOT_FILTER,this.carouselFilters.listHotFilter.getRendererAt(param1.index).selectable,param1.index));
         this.updatePopoverData();
         scrollList.moveToHorizontalScrollPosition(0);
      }
      
      private function onCarouselFiltersResizeHandler(param1:Event) : void
      {
         this.carouselFilters.y = leftArrow.y + (leftArrow.height - this.carouselFilters.height >> 1);
      }
      
      private function onDataProviderChangeHandler(param1:Event) : void
      {
         invalidateData();
         if(this._layoutController != null)
         {
            this._layoutController.invalidateData();
         }
         this.updateSelectedIndex();
         this.updatePopoverData();
      }
      
      private function onBtnDefaultClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new FiltersEvent(FiltersEvent.RESET_ALL_FILTERS,0,true));
      }
      
      private function onBtnDefaultRollOverHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.show(VEHICLE_CUSTOMIZATION.CAROUSEL_RESETFILTERSBTN_TOOLTIP);
      }
      
      private function onBtnDefaultRollOutHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.hide();
      }
   }
}
