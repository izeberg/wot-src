package net.wg.gui.lobby.vehicleCustomization
{
   import flash.display.InteractiveObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.geom.Point;
   import mx.effects.easing.Linear;
   import net.wg.gui.components.containers.HorizontalGroupLayout;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationBottomPanelTabBar;
   import net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel.CustomizationModalLine;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationBottomPanelNotificationVO;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationTabNavigatorVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationTabEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.interfaces.IFocusChainContainer;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.controls.Button;
   import scaleform.clik.motion.Tween;
   
   public class CustomizationTabNavigator extends UIComponentEx implements IFocusChainContainer
   {
      
      private static const BUTTON_LINKAGE:String = "CustomizationBottomPanelTabButtonUI";
      
      private static const MIN_RESOLUTION:int = 1000;
      
      private static const MIN_OFFSET:int = -50;
      
      private static const ANIMATION_DURATION:int = 300;
      
      private static const MODAL_INVALID:String = "modalFrameInvalid";
       
      
      public var overlay:MovieClip = null;
      
      public var tabBar:CustomizationBottomPanelTabBar = null;
      
      public var selector:MovieClip = null;
      
      public var modalLine:CustomizationModalLine = null;
      
      private var _selectedId:int = -1;
      
      private var _isMinResolution:Boolean;
      
      private var _tween:Tween = null;
      
      private var _tmpPoint:Point;
      
      public function CustomizationTabNavigator()
      {
         this._tmpPoint = new Point();
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.tabBar.layout = new HorizontalGroupLayout(-3,false);
         this.tabBar.buttonLinkage = BUTTON_LINKAGE;
         this.tabBar.allowedKeyboard = false;
         this.tabBar.toggleResolutions(App.appWidth < MIN_RESOLUTION);
      }
      
      override protected function configUI() : void
      {
         var _loc1_:Sprite = null;
         super.configUI();
         _loc1_ = new Sprite();
         this.selector.hitArea = _loc1_;
         this.overlay.hitArea = _loc1_;
         addChild(_loc1_);
         this.tabBar.addEventListener(Event.CHANGE,this.onTabBarChangeHandler);
         this.tabBar.addEventListener(Event.RESIZE,this.onTabBarResizeHandler);
         this.updateLayout();
      }
      
      override protected function onDispose() : void
      {
         App.utils.scheduler.cancelTask(this.animModal);
         this.clearTween();
         this.tabBar.removeEventListener(Event.CHANGE,this.onTabBarChangeHandler);
         this.tabBar.removeEventListener(Event.RESIZE,this.onTabBarResizeHandler);
         this.tabBar.dispose();
         this.tabBar = null;
         this.modalLine.dispose();
         this.modalLine = null;
         this.selector = null;
         this.overlay = null;
         this._tmpPoint = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.overlay.width = _width;
            this.updateLayout();
         }
         if(isInvalid(MODAL_INVALID))
         {
            this.validateModalAnim();
         }
      }
      
      public function clearTween() : void
      {
         if(this._tween != null)
         {
            this._tween.paused = true;
            this._tween.dispose();
            this._tween = null;
         }
      }
      
      public function getFocusChain() : Vector.<InteractiveObject>
      {
         var _loc1_:Vector.<InteractiveObject> = new Vector.<InteractiveObject>();
         _loc1_.push(this.tabBar);
         return _loc1_;
      }
      
      public function setData(param1:CustomizationTabNavigatorVO) : void
      {
         this._selectedId = param1.selectedTab;
         this.tabBar.setData(param1.tabsDP,param1.selectedTab);
      }
      
      public function setNotificationCounters(param1:CustomizationBottomPanelNotificationVO) : void
      {
         this.tabBar.setNotificationCounters(param1);
      }
      
      public function switchState(param1:Boolean) : void
      {
         this.tabBar.visible = param1;
         this.selector.visible = param1;
         this.tabBar.focusable = param1;
      }
      
      public function updateBorders(param1:int, param2:int) : void
      {
         this.tabBar.updateBorders(param1,param2);
      }
      
      public function updateStage(param1:int, param2:int) : void
      {
         this.width = param1;
         var _loc3_:Boolean = param1 < MIN_RESOLUTION;
         if(this._isMinResolution != _loc3_)
         {
            this.toggleResolutions(_loc3_);
         }
         this.updateCollapsing();
         this.updateLayout();
      }
      
      private function updateCollapsing() : void
      {
         var _loc1_:Boolean = this.tabBar.checkCollapsing();
         if(_loc1_ != this.tabBar.isBarCollapsed)
         {
            this.tabBar.collapseBar(_loc1_);
         }
      }
      
      private function updateSelector(param1:Button) : void
      {
         if(!param1)
         {
            return;
         }
         param1.validateNow();
         this._tmpPoint.x = param1.x;
         this._tmpPoint.y = param1.y;
         var _loc2_:Point = param1.parent.localToGlobal(this._tmpPoint);
         _loc2_ = globalToLocal(_loc2_);
         this.selector.x = _loc2_.x + (param1.width >> 1);
      }
      
      private function updateLayout() : void
      {
         this.tabBar.x = _width - this.tabBar.width >> 1;
         if(this.tabBar.isBarCollapsed)
         {
            this.tabBar.x += MIN_OFFSET;
         }
         this.updateSelector(this.tabBar.getButtonAt(this.tabBar.selectedIndex));
         invalidate(MODAL_INVALID);
      }
      
      private function validateModalAnim() : void
      {
         App.utils.scheduler.scheduleOnNextFrame(this.animModal);
      }
      
      private function animModal() : void
      {
         this.clearTween();
         var _loc1_:Point = this.tabBar.getBound();
         this._tween = new Tween(ANIMATION_DURATION,this.modalLine,{"x":this.tabBar.x + _loc1_.x},{"ease":Linear.easeIn});
         this.modalLine.update(_loc1_);
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
         this.updateSelector(_loc2_);
         dispatchEvent(new CustomizationTabEvent(CustomizationTabEvent.TAB_CHANGED,this._selectedId,true));
      }
      
      private function onTabBarResizeHandler(param1:Event) : void
      {
         this.updateCollapsing();
         this.updateLayout();
         dispatchEvent(new Event(Event.RESIZE));
      }
   }
}
