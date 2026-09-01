package net.wg.gui.battle.windows
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.geom.Point;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.windows.components.IngameDetailsRoleActionContainer;
   import net.wg.gui.battle.windows.vo.IngameDetailsPageVO;
   import net.wg.gui.battle.windows.vo.IngameDetailsRoleActionVO;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.hintPanel.KeyViewersList;
   import net.wg.gui.components.interfaces.IPaginatorArrowsController;
   import net.wg.gui.components.paginator.PaginationDetailsNumButton;
   import net.wg.gui.components.paginator.PaginationGroup;
   import net.wg.gui.components.paginator.PaginatorArrowBtn;
   import net.wg.gui.components.paginator.PaginatorArrowsController;
   import net.wg.gui.components.paginator.vo.PaginatorPageNumVO;
   import net.wg.gui.components.windows.WindowEvent;
   import net.wg.gui.interfaces.ISoundButtonEx;
   import net.wg.infrastructure.base.meta.IIngameDetailsHelpWindowMeta;
   import net.wg.infrastructure.base.meta.impl.IngameDetailsHelpWindowMeta;
   import net.wg.infrastructure.constants.WindowViewInvalidationType;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.ButtonEvent;
   
   public class IngameDetailsHelpWindow extends IngameDetailsHelpWindowMeta implements IIngameDetailsHelpWindowMeta
   {
      
      private static const DETAILS_HELP_PAGE_GROUP:String = "DetailsHelpPageGroup";
      
      private static const INV_PAGE:String = "InvPage";
      
      private static const INV_PAGE_SIZE:String = "InvPageSize";
      
      private static const MIN_PAGES:int = 1;
      
      private static const WINDOW_HEIGHT:int = 732;
      
      private static const FOOTER_HEIGHT:int = 60;
      
      private static const DESCRIPTION_PADDING_BOTTOM:int = 30;
      
      private static const TEXT_BASELINE_PADDING:int = 6;
      
      private static const KEYS_PADDING:int = 63;
      
      private static const WARNING_MARGIN_TOP:int = 27;
      
      private static const KEY_BOTTOM:int = 65;
      
      private static const PAGE_TITLE_BOTTOM:int = 15;
      
      private static const ARROWS_PADDING_TOP:int = 85;
      
      private static const PAGINATOR_HEIGHT:int = 20;
      
      private static const ARROW_HORIZONTAL_LEFT_PADDING:int = 66;
      
      private static const ARROW_HORIZONTAL_RIGHT_PADDING:int = 91;
      
      private static const ROLE_ACTION_BOTTOM:int = 139;
      
      private static const ROLE_ACTION_PADDING_TOP:int = -17;
      
      private static const ROLE_IMAGE_Y_SHIFT:int = -53;
      
      private static const ROLE_PADDING_BOTTOM:int = 22;
       
      
      public var pgBackground:Sprite = null;
      
      public var background:Sprite = null;
      
      public var arrowLeftBtn:PaginatorArrowBtn = null;
      
      public var arrowRightBtn:PaginatorArrowBtn = null;
      
      public var pageButtons:PaginationGroup = null;
      
      public var btnClose:ISoundButtonEx = null;
      
      public var pageBg:UILoaderAlt = null;
      
      public var headerTitle:TextField = null;
      
      public var title:TextField = null;
      
      public var description:TextField = null;
      
      public var warning:TextField = null;
      
      public var roleImage:Image = null;
      
      private var _currentIndex:int = 0;
      
      private var _pagesDP:DataProvider = null;
      
      private var _pageData:IngameDetailsPageVO = null;
      
      private var _pageController:IPaginatorArrowsController = null;
      
      private var _keyViewersList:KeyViewersList = null;
      
      private var _roleActionContainer:IngameDetailsRoleActionContainer = null;
      
      private var _paginatorPos:Point;
      
      public function IngameDetailsHelpWindow()
      {
         this._paginatorPos = new Point();
         super();
         showWindowBgForm = false;
         showWindowBg = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         updateStage(App.appWidth,App.appHeight);
         window.addEventListener(WindowEvent.SCALE_Y_CHANGED,this.onWindowScaleYChangedHandler);
         this.btnClose.label = INGAME_HELP.BATTLECONTROLS_CLOSEBTNLABEL;
         this._pageController = this.createPaginatorController();
         this.btnClose.addEventListener(ButtonEvent.CLICK,this.onBtnCloseClickHandler);
         this._pageController.addEventListener(Event.CHANGE,this.onPageControllerChangeHandler);
         this.warning.text = INGAME_HELP.DETAILSHELP_NOKEYSWARNING;
         this.warning.visible = false;
         this.arrowLeftBtn.focusable = false;
         this.arrowRightBtn.focusable = false;
         this.pageButtons.focusable = false;
         this.btnClose.focusable = false;
         this.roleImage.addEventListener(Event.CHANGE,this.onRoleImageChangeHandler);
         this._keyViewersList = new KeyViewersList();
         addChild(this._keyViewersList);
         this._keyViewersList.y = this.background.height - KEY_BOTTOM - KEYS_PADDING >> 0;
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         var _loc2_:PaginatorPageNumVO = null;
         super.draw();
         if(geometry && window && isInvalid(WindowViewInvalidationType.POSITION_INVALID))
         {
            window.x = App.appWidth - window.getBackground().width >> 1;
            window.y = App.appHeight - window.getBackground().height >> 1;
         }
         if(this._pagesDP != null)
         {
            _loc1_ = this._pagesDP.length;
            if(isInvalid(InvalidationType.DATA))
            {
               if(_loc1_ > MIN_PAGES)
               {
                  this._pageController.setPages(this._pagesDP);
                  for each(_loc2_ in this._pagesDP)
                  {
                     if(_loc2_.selected)
                     {
                        this._pageController.setPageIndex(_loc2_.pageIndex);
                        break;
                     }
                  }
               }
               requestPageDataS(this._currentIndex);
               invalidateSize();
            }
            if(this._pageData != null && _loc1_ > this._currentIndex && isInvalid(INV_PAGE))
            {
               this.setData(this._pageData);
               invalidate(INV_PAGE_SIZE);
            }
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.updateLayout();
         }
         if(isInvalid(INV_PAGE_SIZE))
         {
            this.updatePageLayout();
         }
      }
      
      override protected function onDispose() : void
      {
         this.btnClose.removeEventListener(ButtonEvent.CLICK,this.onBtnCloseClickHandler);
         this._pageController.removeEventListener(Event.CHANGE,this.onPageControllerChangeHandler);
         window.removeEventListener(WindowEvent.SCALE_Y_CHANGED,this.onWindowScaleYChangedHandler);
         this.pgBackground = null;
         this.background = null;
         this._paginatorPos = null;
         this.pageBg.dispose();
         this.pageBg = null;
         this.btnClose.dispose();
         this.btnClose = null;
         this.headerTitle = null;
         this.title = null;
         this.description = null;
         this.warning = null;
         this.roleImage.removeEventListener(Event.CHANGE,this.onRoleImageChangeHandler);
         this.roleImage.dispose();
         this.roleImage = null;
         this._pagesDP = null;
         this._pageData = null;
         removeChild(this._keyViewersList);
         this._keyViewersList.dispose();
         this._keyViewersList = null;
         if(this._roleActionContainer)
         {
            removeChild(this._roleActionContainer);
            this._roleActionContainer.dispose();
            this._roleActionContainer = null;
         }
         this._pageController.dispose();
         this._pageController = null;
         this.arrowLeftBtn.dispose();
         this.arrowLeftBtn = null;
         this.arrowRightBtn.dispose();
         this.arrowRightBtn = null;
         this.pageButtons.dispose();
         this.pageButtons = null;
         super.onDispose();
      }
      
      override protected function setPaginatorData(param1:DataProvider) : void
      {
         this._pagesDP = param1;
         invalidateData();
      }
      
      override protected function setPageData(param1:IngameDetailsPageVO) : void
      {
         this._pageData = param1;
         invalidate(INV_PAGE);
      }
      
      override protected function getIngameDetailsPageVOForData(param1:Object) : IngameDetailsPageVO
      {
         return new IngameDetailsPageVO(param1);
      }
      
      public function createPaginatorController() : IPaginatorArrowsController
      {
         return new PaginatorArrowsController(this,this.pageButtons,this.arrowLeftBtn,this.arrowRightBtn,DETAILS_HELP_PAGE_GROUP,Values.ZERO,true);
      }
      
      private function updateLayout() : void
      {
         this.arrowLeftBtn.x = x - this.arrowLeftBtn.width + ARROW_HORIZONTAL_LEFT_PADDING >> 0;
         this.arrowRightBtn.x = x + width + this.arrowRightBtn.width - ARROW_HORIZONTAL_RIGHT_PADDING >> 0;
         this.arrowLeftBtn.y = this.arrowRightBtn.y = this.background.y + ARROWS_PADDING_TOP;
         var _loc1_:Number = this.pgBackground.height;
         this.pgBackground.y = this.background.height - _loc1_;
         this._paginatorPos.x = x + (this.background.width >> 1);
         this._paginatorPos.y = this.pgBackground.y + (_loc1_ - PAGINATOR_HEIGHT >> 1);
         this._pageController.setPositions(this._paginatorPos);
      }
      
      private function updatePageLayout() : void
      {
         App.utils.commons.updateTextFieldSize(this.description,false,true);
         var _loc1_:int = WINDOW_HEIGHT - FOOTER_HEIGHT - DESCRIPTION_PADDING_BOTTOM;
         if(this._keyViewersList.visible || this.warning.visible)
         {
            _loc1_ -= KEYS_PADDING;
         }
         if(this._roleActionContainer && this._roleActionContainer.visible)
         {
            this._roleActionContainer.x = width - this._roleActionContainer.width >> 1;
            this._roleActionContainer.y = height - ROLE_ACTION_BOTTOM >> 0;
            _loc1_ -= this._roleActionContainer.height + ROLE_ACTION_PADDING_TOP - ROLE_PADDING_BOTTOM;
         }
         if(this.roleImage.visible)
         {
            _loc1_ -= ROLE_PADDING_BOTTOM;
            this.roleImage.x = width - this.roleImage.width >> 1;
            this.roleImage.y = _loc1_ - this.roleImage.height + ROLE_IMAGE_Y_SHIFT;
         }
         this.description.y = _loc1_ - this.description.height + TEXT_BASELINE_PADDING >> 0;
         this.title.y = this.description.y - this.headerTitle.height - PAGE_TITLE_BOTTOM >> 0;
         this.warning.y = this.description.y + this.description.height + WARNING_MARGIN_TOP >> 0;
      }
      
      private function setData(param1:IngameDetailsPageVO) : void
      {
         this.headerTitle.text = param1.headerTitle;
         this.title.htmlText = param1.title;
         this.description.htmlText = param1.descr;
         this.pageBg.source = param1.image;
         var _loc2_:Boolean = param1.hasEmptyKey;
         this._keyViewersList.clearKeys();
         this._keyViewersList.visible = param1.keys.length > 0;
         this.warning.visible = _loc2_;
         if(!_loc2_)
         {
            this._keyViewersList.setKeys(param1.keys);
            this._keyViewersList.x = width - this._keyViewersList.width >> 1;
         }
         var _loc3_:Boolean = StringUtils.isNotEmpty(param1.roleImage);
         this.roleImage.visible = _loc3_;
         if(_loc3_)
         {
            this.roleImage.source = param1.roleImage;
         }
         var _loc4_:Vector.<IngameDetailsRoleActionVO> = param1.roleActions;
         if(_loc4_)
         {
            if(!this._roleActionContainer)
            {
               this._roleActionContainer = new IngameDetailsRoleActionContainer();
               addChild(this._roleActionContainer);
            }
            this._roleActionContainer.setRolesData(_loc4_);
            this._roleActionContainer.visible = true;
         }
         else if(this._roleActionContainer)
         {
            this._roleActionContainer.visible = false;
         }
      }
      
      private function onWindowScaleYChangedHandler(param1:WindowEvent) : void
      {
         invalidate(WindowViewInvalidationType.POSITION_INVALID);
      }
      
      private function onBtnCloseClickHandler(param1:ButtonEvent) : void
      {
         handleWindowClose();
      }
      
      private function onPageControllerChangeHandler(param1:Event) : void
      {
         this._currentIndex = PaginationDetailsNumButton(this._pageController.getSelectedButton()).pageIndex;
         requestPageDataS(this._currentIndex);
      }
      
      private function onRoleImageChangeHandler(param1:Event) : void
      {
         invalidate(INV_PAGE_SIZE);
      }
   }
}
