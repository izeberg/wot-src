package net.wg.gui.lobby.vehicleCustomization
{
   import flash.display.InteractiveObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Point;
   import net.wg.data.constants.SoundTypes;
   import net.wg.gui.components.advanced.collapsingBar.ResizableButton;
   import net.wg.gui.interfaces.ISoundButtonEx;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationBottomPanelTabBar;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationBottomPanelTabButton;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationTabLayout;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationTabNavigatorVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationTabEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.interfaces.IFocusChainContainer;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.controls.Button;
   
   public class CustomizationTabNavigator extends UIComponentEx implements IFocusChainContainer
   {
      
      private static const BUTTON_LINKAGE:String = "CustomizationBottomPanelTabButtonUI";
      
      private static const SELECTOR_OFFSET_Y:int = -3;
      
      private static const TABS_GAP:int = -3;
      
      private static const RETURN_BTN_OFFSET_X:int = 5;
      
      private static const CANCEL_EDIT_STYLE_BTN_NAME:String = "cancelEditStyleBtn";
       
      
      public var overlay:MovieClip = null;
      
      public var tabBar:CustomizationBottomPanelTabBar = null;
      
      public var cancelEditStylePanel:MovieClip = null;
      
      public var selector:MovieClip = null;
      
      public var firstHighlight:MovieClip = null;
      
      public var lastHighlight:MovieClip = null;
      
      private var _cancelEditStyleBtn:ISoundButtonEx;
      
      private var _selectedId:int = -1;
      
      private var _isMinResolution:Boolean;
      
      private var _paddingRight:int = 0;
      
      public function CustomizationTabNavigator()
      {
         super();
         this._cancelEditStyleBtn = ISoundButtonEx(this.cancelEditStylePanel.getChildByName(CANCEL_EDIT_STYLE_BTN_NAME));
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.tabBar.layout = new CustomizationTabLayout(TABS_GAP);
         this.tabBar.buttonLinkage = BUTTON_LINKAGE;
         this.tabBar.allowedKeyboard = false;
         this.tabBar.toggleResolutions(App.appHeight < StageSizeBoundaries.HEIGHT_900);
      }
      
      override protected function configUI() : void
      {
         var _loc1_:Sprite = null;
         super.configUI();
         this.firstHighlight.mouseEnabled = this.lastHighlight.mouseEnabled = false;
         this.firstHighlight.mouseChildren = this.lastHighlight.mouseChildren = false;
         _loc1_ = new Sprite();
         this.selector.hitArea = _loc1_;
         this.overlay.hitArea = _loc1_;
         addChild(_loc1_);
         this.tabBar.addEventListener(Event.CHANGE,this.onTabBarChangeHandler);
         this.tabBar.addEventListener(Event.RESIZE,this.onTabBarResizeHandler);
         this._cancelEditStyleBtn.soundType = SoundTypes.FITTING_BUTTON;
         this._cancelEditStyleBtn.addEventListener(MouseEvent.CLICK,this.onReturnClickHandler);
      }
      
      override protected function onDispose() : void
      {
         this.tabBar.removeEventListener(Event.CHANGE,this.onTabBarChangeHandler);
         this.tabBar.removeEventListener(Event.RESIZE,this.onTabBarResizeHandler);
         this.tabBar.dispose();
         this.tabBar = null;
         this.firstHighlight = null;
         this.lastHighlight = null;
         this.selector = null;
         this.overlay = null;
         this._cancelEditStyleBtn.removeEventListener(MouseEvent.CLICK,this.onReturnClickHandler);
         this._cancelEditStyleBtn.dispose();
         this._cancelEditStyleBtn = null;
         this.cancelEditStylePanel = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.overlay.width = _width;
         }
      }
      
      public function getFocusChain() : Vector.<InteractiveObject>
      {
         var _loc1_:Vector.<InteractiveObject> = new Vector.<InteractiveObject>();
         _loc1_.push(this.tabBar);
         return _loc1_;
      }
      
      public function getTabBarOffset() : int
      {
         return this.tabBar.x + (this.tabBar.width >> 1);
      }
      
      public function setData(param1:CustomizationTabNavigatorVO) : void
      {
         this.tabBar.setData(param1.tabsDP,param1.selectedTab);
         this.cancelEditStylePanel.visible = param1.isEditable;
      }
      
      public function setNotificationCounters(param1:Array) : void
      {
         this.tabBar.setNotificationCounters(param1);
      }
      
      public function setPaddingRight(param1:Number) : void
      {
         this._paddingRight = param1;
         this.updateLayout();
      }
      
      public function setTabsPluses(param1:Array) : void
      {
         var _loc2_:ResizableButton = null;
         var _loc3_:int = param1.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc3_)
         {
            _loc2_ = CustomizationBottomPanelTabButton(this.tabBar.getButtonAt(_loc4_));
            CustomizationBottomPanelTabButton(_loc2_).showPlus(param1[_loc4_]);
            _loc4_++;
         }
      }
      
      public function switchState(param1:Boolean) : void
      {
         this.tabBar.visible = param1;
         this.firstHighlight.visible = param1;
         this.lastHighlight.visible = param1;
         this.selector.visible = param1;
         this.tabBar.focusable = param1;
      }
      
      public function updateStage(param1:int, param2:int) : void
      {
         this.width = param1;
         var _loc3_:Boolean = param2 < StageSizeBoundaries.HEIGHT_900;
         var _loc4_:Boolean = this.tabBar.checkCollapsing();
         if(this._isMinResolution != _loc3_ || _loc4_ != this.tabBar.isBarCollapsed)
         {
            this.toggleResolutions(_loc3_);
            this.tabBar.collapseBar(_loc4_);
         }
         else
         {
            this.updateLayout();
         }
      }
      
      private function updateSelector(param1:Button) : void
      {
         var _loc2_:Point = null;
         if(!param1)
         {
            return;
         }
         param1.validateNow();
         _loc2_ = param1.parent.localToGlobal(new Point(param1.x,param1.y));
         _loc2_ = globalToLocal(_loc2_);
         this.firstHighlight.x = _loc2_.x;
         this.lastHighlight.x = _loc2_.x + param1.width | 0;
         this.firstHighlight.y = this.lastHighlight.y = _loc2_.y | 0;
         this.selector.x = _loc2_.x + (param1.width >> 1) | 0;
         this.selector.y = _loc2_.y + param1.height + SELECTOR_OFFSET_Y | 0;
      }
      
      private function updateLayout() : void
      {
         this.lastHighlight.height = this.firstHighlight.height = this.tabBar.height;
         var _loc1_:int = _width - this.tabBar.width >> 1;
         this.tabBar.x = _loc1_ + this.tabBar.width + this._paddingRight < _width ? Number(_loc1_) : Number(_width - this._paddingRight - this.tabBar.width);
         this.updateSelector(this.tabBar.getButtonAt(this.tabBar.selectedIndex));
         this.cancelEditStylePanel.x = this.tabBar.x + this.tabBar.width + RETURN_BTN_OFFSET_X;
      }
      
      private function toggleResolutions(param1:Boolean) : void
      {
         this._isMinResolution = param1;
         this.tabBar.toggleResolutions(param1);
      }
      
      private function onTabBarChangeHandler(param1:Event) : void
      {
         var _loc2_:Button = this.tabBar.getButtonAt(this.tabBar.selectedIndex);
         if(!_loc2_)
         {
            return;
         }
         if(this._selectedId == _loc2_.data.id)
         {
            return;
         }
         this._selectedId = _loc2_.data.id;
         this.tabBar.updateGroupSelection(this._selectedId,_loc2_.data.groupId);
         this.updateSelector(_loc2_);
         dispatchEvent(new CustomizationTabEvent(CustomizationTabEvent.TAB_CHANGED,this._selectedId,true));
      }
      
      private function onTabBarResizeHandler(param1:Event) : void
      {
         this.updateLayout();
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      private function onReturnClickHandler(param1:Event) : void
      {
         dispatchEvent(new CustomizationTabEvent(CustomizationTabEvent.RETURN_TO_COMPLETE_STYLE,-1,true));
      }
   }
}
