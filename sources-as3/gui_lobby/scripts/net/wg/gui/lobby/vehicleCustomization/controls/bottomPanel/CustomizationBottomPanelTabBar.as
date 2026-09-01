package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import flash.events.Event;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.advanced.collapsingBar.CollapsingBar;
   import net.wg.gui.components.advanced.collapsingBar.ResizableButton;
   import net.wg.gui.components.advanced.collapsingBar.data.CollapsingBarButtonVO;
   import net.wg.gui.components.advanced.collapsingBar.interfaces.ICollapseChecker;
   import net.wg.gui.components.containers.GroupLayout;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationBottomPanelNotificationVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationTabButtonVO;
   import scaleform.clik.data.DataProvider;
   
   public class CustomizationBottomPanelTabBar extends CollapsingBar implements ICollapseChecker
   {
      
      private static const PADDING:int = 20;
      
      private static const ICON_SIZE:int = 21;
      
      private static const OFFSET_FROM_ICON:int = 10;
      
      private static const RESOLUTION_OFFSET:int = -4;
      
      private static const BUTTONS_OFFSET:int = 550;
      
      private static const HORIZONTAL_BORDER_MARGIN:int = 0;
      
      private static const MIN_WIDTH:int = 60;
      
      private static const BUTTON_HEIGHT:int = 42;
       
      
      private var _barExpandedWith:int = 0;
      
      private var _leftBorder:int = -1;
      
      private var _rightBorder:int = -1;
      
      private var _boundPoint:Point;
      
      public function CustomizationBottomPanelTabBar()
      {
         this._boundPoint = new Point();
         super();
      }
      
      override protected function onDispose() : void
      {
         this._boundPoint = null;
         super.onDispose();
      }
      
      override protected function calculateExpandedSize(param1:ResizableButton) : Point
      {
         param1.validateNow();
         var _loc2_:Point = super.calculateExpandedSize(param1);
         this._barExpandedWith += _loc2_.x + GroupLayout(layout).gap;
         return _loc2_;
      }
      
      override protected function removeAllButtons() : void
      {
         super.removeAllButtons();
         this._barExpandedWith = 0;
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         setCollapsingButtonSize(MIN_WIDTH,BUTTON_HEIGHT);
         setAutoCollapsed(true,this);
      }
      
      override protected function applyDataToButton(param1:ResizableButton, param2:CollapsingBarButtonVO) : void
      {
         super.applyDataToButton(param1,param2);
         param1.padding = PADDING;
         var _loc3_:CustomizationBottomPanelTabButton = CustomizationBottomPanelTabButton(param1);
         var _loc4_:CustomizationTabButtonVO = CustomizationTabButtonVO(param2);
         _loc3_.iconSource = _loc4_.icon;
         _loc3_.offsetFromIcon = OFFSET_FROM_ICON;
         _loc3_.setIconSize(ICON_SIZE,ICON_SIZE);
         _loc3_.setActive(_loc4_.isInActiveGroup);
         _loc3_.showPlus(_loc4_.showPlus);
         _loc3_.enabled = _loc4_.isEnabled;
      }
      
      override protected function createTabs(param1:DataProvider) : void
      {
         var _loc3_:ResizableButton = null;
         var _loc4_:CollapsingBarButtonVO = null;
         var _loc5_:int = 0;
         var _loc2_:int = param1.length;
         if(_loc2_ > 0 && _loc2_ == buttonGroup.length)
         {
            _loc5_ = 0;
            while(_loc5_ < _loc2_)
            {
               _loc4_ = CollapsingBarButtonVO(param1[_loc5_]);
               _loc3_ = ResizableButton(buttonGroup.getButtonAt(_loc5_));
               this.applyDataToButton(_loc3_,_loc4_);
               _loc3_.selected = _loc4_.id == currentSelectedId;
               _loc5_++;
            }
            return;
         }
         this._barExpandedWith = Values.ZERO;
         super.createTabs(param1);
         if(buttonGroup.length > 0)
         {
            CustomizationBottomPanelTabButton(buttonGroup.getButtonAt(buttonGroup.length - 1)).last = true;
            CustomizationBottomPanelTabButton(buttonGroup.getButtonAt(0)).first = true;
         }
      }
      
      public function checkCollapsing() : Boolean
      {
         var _loc1_:Boolean = false;
         var _loc2_:Boolean = false;
         if(this._leftBorder != Values.DEFAULT_INT || this._rightBorder != Values.DEFAULT_INT)
         {
            _loc1_ = App.appWidth - this._barExpandedWith >> 1 < this._leftBorder + HORIZONTAL_BORDER_MARGIN;
            _loc2_ = App.appWidth + this._barExpandedWith >> 1 > this._rightBorder - HORIZONTAL_BORDER_MARGIN;
            return _loc2_ || _loc1_;
         }
         return App.appWidth - this._barExpandedWith < BUTTONS_OFFSET;
      }
      
      public function getBound() : Point
      {
         var _loc2_:CustomizationBottomPanelTabButton = null;
         var _loc5_:Boolean = false;
         var _loc7_:int = 0;
         var _loc1_:int = buttonGroup.length;
         var _loc3_:int = Values.DEFAULT_INT;
         var _loc4_:int = Values.DEFAULT_INT;
         var _loc6_:int = 0;
         while(_loc6_ < _loc1_)
         {
            _loc2_ = CustomizationBottomPanelTabButton(buttonGroup.getButtonAt(_loc6_));
            _loc5_ = _loc2_.getActive();
            if(_loc5_)
            {
               _loc7_ = _loc2_.x + (_loc2_.width >> 1);
               if(_loc3_ == Values.DEFAULT_INT)
               {
                  _loc3_ = _loc7_;
               }
               _loc4_ = _loc7_;
            }
            _loc6_++;
         }
         this._boundPoint.x = _loc3_;
         this._boundPoint.y = _loc4_;
         return this._boundPoint;
      }
      
      public function setNotificationCounters(param1:CustomizationBottomPanelNotificationVO) : void
      {
         var _loc5_:CustomizationBottomPanelTabButton = null;
         var _loc2_:Array = param1.tabsCounters;
         var _loc3_:Array = param1.unseenTabs;
         var _loc4_:int = buttonGroup.length;
         var _loc6_:int = 0;
         while(_loc6_ < _loc4_)
         {
            _loc5_ = CustomizationBottomPanelTabButton(buttonGroup.getButtonAt(_loc6_));
            _loc5_.setNotification(_loc2_[_loc6_],Boolean(_loc3_.indexOf(_loc5_.data.id) != -1));
            _loc6_++;
         }
      }
      
      public function toggleResolutions(param1:Boolean) : void
      {
         buttonGroup.sizeOffset.y = int(param1) * RESOLUTION_OFFSET;
      }
      
      public function updateBorders(param1:int, param2:int) : void
      {
         if(this._leftBorder != param1 || this._rightBorder != param2)
         {
            this._leftBorder = param1;
            this._rightBorder = param2;
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
   }
}
