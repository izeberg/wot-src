package net.wg.gui.lobby
{
   import fl.motion.easing.Quadratic;
   import flash.display.Bitmap;
   import flash.display.DisplayObject;
   import flash.display.InteractiveObject;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import net.wg.data.Aliases;
   import net.wg.data.constants.Cursors;
   import net.wg.data.constants.DragType;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.LAYER_NAMES;
   import net.wg.gui.components.common.waiting.Waiting;
   import net.wg.gui.components.containers.LobbyPageSubContainer;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.gui.components.vehicleHitArea.VehicleHitAreaComponent;
   import net.wg.gui.events.LobbyEvent;
   import net.wg.gui.lobby.interfaces.ILobbyPage;
   import net.wg.gui.lobby.post.TeaserEvent;
   import net.wg.gui.lobby.settings.config.ControlsFactory;
   import net.wg.gui.notification.NotificationPopUpViewer;
   import net.wg.infrastructure.base.meta.impl.LobbyPageMeta;
   import net.wg.infrastructure.interfaces.ILobbyPageSubContainer;
   import net.wg.utils.IAssertable;
   import net.wg.utils.IClassFactory;
   import scaleform.clik.constants.ConstrainMode;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   import scaleform.clik.utils.Constraints;
   
   public class LobbyPage extends LobbyPageMeta implements ILobbyPage
   {
      
      private static const TEASER_ANIMATION_SCALE:Number = 0.05;
      
      private static const TEASER_ANIMATION_ALPHA:Number = 0.5;
      
      private static const TEASER_ANIM_SPEED_TIME:int = 600;
      
      private static const TOP_SUB_VIEW_POSITION:Number = 53;
      
      private static const WARNING_EMPTY_HIT_AREA:String = "vehicleHitArea is null!";
       
      
      public var vehicleHitArea:VehicleHitAreaComponent = null;
      
      public var subTopContainer:ILobbyPageSubContainer = null;
      
      public var subViewContainer:ILobbyPageSubContainer = null;
      
      public var notificationPopupViewer:NotificationPopUpViewer;
      
      public var waiting:Waiting = null;
      
      private var _subContainers:Array;
      
      private var _asserter:IAssertable;
      
      private var _classFactory:IClassFactory;
      
      private var _header:GFInjectComponent;
      
      private var _footer:GFInjectComponent;
      
      private var _headerOffset:uint = 0;
      
      private var _footerOffset:uint = 0;
      
      private var _dragOffsetX:Number = 0;
      
      private var _dragOffsetY:Number = 0;
      
      private var _resetDragParams:Boolean;
      
      private var _teaserOverlay:Sprite = null;
      
      private var _teaserTween:Tween;
      
      private var _teaser:Bitmap;
      
      private var _requiresFramedMode:Boolean = false;
      
      public function LobbyPage()
      {
         this._subContainers = [];
         super();
         this._classFactory = App.utils.classFactory;
         this._asserter = App.utils.asserter;
      }
      
      override public function getSubContainers() : Array
      {
         return this._subContainers;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         _originalWidth = param1;
         _originalHeight = param2;
         setSize(param1,param2);
         this.vehicleHitArea.width = param1;
         this.vehicleHitArea.height = param2 - this.vehicleHitArea.y;
         this.waiting.setSize(param1,param2);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.stage.addEventListener(LobbyEvent.REGISTER_DRAGGING,this.onRegisterDraggingHandler);
         App.stage.addEventListener(LobbyEvent.UNREGISTER_DRAGGING,this.onUnregisterDraggingHandler);
         addEventListener(TeaserEvent.HIDE,this.onTeaserHideHandler,true);
         constraints = new Constraints(this,ConstrainMode.COUNTER_SCALE);
         this.updateStage(App.appWidth,App.appHeight);
         this.vehicleHitArea.addEventListener(MouseEvent.ROLL_OVER,this.onVehicleHitAreaRollOverHandler);
         this.vehicleHitArea.addEventListener(MouseEvent.ROLL_OUT,this.onVehicleHitAreaRollOutHandler);
      }
      
      override protected function allowHandleInput() : Boolean
      {
         return false;
      }
      
      override protected function onSetModalFocus(param1:InteractiveObject) : void
      {
         this.tryToFocusContent();
         super.onSetModalFocus(param1);
      }
      
      override protected function onInitModalFocus(param1:InteractiveObject) : void
      {
         super.onInitModalFocus(param1);
         this.tryToFocusContent();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            constraints.update(width,height);
            invalidateLayout();
         }
         if(isInvalid(InvalidationType.LAYOUT))
         {
            this.updateInnerLayersSize(width,height);
            this.updateHeaderLayout();
            this.updateFooterLayout();
            if(this.notificationPopupViewer)
            {
               this.notificationPopupViewer.updateStage(width,height - this._footerOffset);
            }
         }
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         if(!this.notificationPopupViewer)
         {
            this.notificationPopupViewer = new NotificationPopUpViewer(this._classFactory.getClass(Linkages.SERVICE_MESSAGES_POPUP));
            addChild(this.notificationPopupViewer);
            registerFlashComponentS(this.notificationPopupViewer,Aliases.SYSTEM_MESSAGES);
         }
         var _loc1_:uint = this.getChildIndex(this.waiting) + 1;
         this.subViewContainer = this.addSubContainer(LAYER_NAMES.SUBVIEW,_loc1_);
         this.subTopContainer = this.addSubContainer(LAYER_NAMES.TOP_SUB_VIEW,_loc1_ + 1);
         this._subContainers = [this.subViewContainer,this.subTopContainer];
         this.createPanels();
      }
      
      override protected function onDispose() : void
      {
         App.stage.removeEventListener(LobbyEvent.REGISTER_DRAGGING,this.onRegisterDraggingHandler);
         App.stage.removeEventListener(LobbyEvent.UNREGISTER_DRAGGING,this.onUnregisterDraggingHandler);
         removeEventListener(TeaserEvent.HIDE,this.onTeaserHideHandler,true);
         removeChild(this.notificationPopupViewer);
         this.vehicleHitArea.hit.removeEventListener(MouseEvent.MOUSE_WHEEL,this.onHitAreaMouseWheelHandler);
         this.vehicleHitArea.removeEventListener(MouseEvent.ROLL_OVER,this.onVehicleHitAreaRollOverHandler);
         this.vehicleHitArea.removeEventListener(MouseEvent.ROLL_OUT,this.onVehicleHitAreaRollOutHandler);
         this.vehicleHitArea.dispose();
         this.vehicleHitArea = null;
         this.removePanels();
         this.subViewContainer = null;
         this.subTopContainer = null;
         this._subContainers.splice(0,this._subContainers.length);
         this._subContainers = null;
         this.waiting.dispose();
         this.waiting = null;
         if(this._teaserTween)
         {
            this._teaserTween.paused = true;
            this._teaserTween.dispose();
            this._teaserTween = null;
         }
         if(this._teaser)
         {
            this._teaserOverlay.removeChild(this._teaser);
            this._teaser.bitmapData.dispose();
            this._teaser = null;
         }
         this.notificationPopupViewer = null;
         this._teaserOverlay = null;
         this._asserter = null;
         this._classFactory = null;
         ControlsFactory.instance.dispose();
         super.onDispose();
      }
      
      public function as_closeHelpLayout() : void
      {
         var _loc1_:InteractiveObject = InteractiveObject(this.subViewContainer.getTopmostView(true));
         if(_loc1_)
         {
            setFocus(_loc1_);
         }
      }
      
      public function as_hideWaiting() : void
      {
         this.waiting.hide();
      }
      
      public function as_setSubContainerItemsVisibility(param1:Boolean) : void
      {
         var _loc4_:ILobbyPageSubContainer = null;
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc2_:InteractiveObject = null;
         var _loc3_:DisplayObject = null;
         for each(_loc4_ in this.getSubContainers())
         {
            _loc5_ = _loc4_.numChildren;
            _loc6_ = 0;
            while(_loc6_ < _loc5_)
            {
               _loc3_ = _loc4_.getChildAt(_loc6_);
               _loc3_.visible = param1;
               _loc2_ = _loc3_ as InteractiveObject;
               _loc6_++;
            }
         }
         if(param1 && _loc2_)
         {
            setFocus(_loc2_);
         }
      }
      
      public function as_setWalletStatus(param1:Object) : void
      {
         App.utils.voMgr.walletStatusVO.update(param1);
      }
      
      public function as_showHelpLayout() : void
      {
      }
      
      public function as_showWaiting(param1:String) : void
      {
         this.waiting.setMessage(param1);
         this.waiting.setSize(_width,_height);
         this.waiting.show();
      }
      
      public function getDragType() : String
      {
         return DragType.SOFT;
      }
      
      public function getHitArea() : InteractiveObject
      {
         if(this.vehicleHitArea == null)
         {
            DebugUtils.LOG_WARNING(WARNING_EMPTY_HIT_AREA);
            return this;
         }
         return this.vehicleHitArea.hit;
      }
      
      public function onDragging(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = !!this._resetDragParams ? Number(0) : Number(-(this._dragOffsetX - stage.mouseX));
         var _loc4_:Number = !!this._resetDragParams ? Number(0) : Number(-(this._dragOffsetY - stage.mouseY));
         this._resetDragParams = false;
         this._dragOffsetX = stage.mouseX;
         this._dragOffsetY = stage.mouseY;
         dispatchEvent(new LobbyEvent(LobbyEvent.DRAGGING));
         moveSpaceS(_loc3_,_loc4_,0);
      }
      
      public function onEndDrag() : void
      {
         dispatchEvent(new LobbyEvent(LobbyEvent.DRAGGING_END));
         notifyCursorDraggingS(false);
      }
      
      public function onStartDrag() : void
      {
         dispatchEvent(new LobbyEvent(LobbyEvent.DRAGGING_START));
         notifyCursorDraggingS(true);
         this._dragOffsetX = stage.mouseX;
         this._dragOffsetY = stage.mouseY;
      }
      
      private function tryToFocusContent() : void
      {
         var _loc4_:Boolean = false;
         var _loc1_:ILobbyPageSubContainer = null;
         var _loc2_:Array = this.getSubContainers();
         var _loc3_:int = _loc2_.length - 1;
         while(_loc3_ >= 0)
         {
            _loc1_ = ILobbyPageSubContainer(_loc2_[_loc3_]);
            if(_loc1_.getTopmostView(true))
            {
               _loc4_ = true;
               _loc1_.tryToSetFocus(false,_loc4_);
               return;
            }
            _loc3_--;
         }
         setFocus(this);
      }
      
      private function createPanels() : void
      {
         this._asserter.assertNull(this._header,Errors.MUST_NULL);
         this._asserter.assertNull(this._footer,Errors.MUST_NULL);
         var _loc1_:int = getChildIndex(this.notificationPopupViewer);
         this._header = new GFInjectComponent();
         this._header.name = Aliases.LOBBY_HEADER_OVERLAPPING;
         this._footer = new GFInjectComponent();
         this._footer.name = Aliases.LOBBY_FOOTER_OVERLAPPING;
         this._header.addEventListener(Event.RESIZE,this.onHeaderResizeHandler);
         this._footer.addEventListener(Event.RESIZE,this.onFooterResizeHandler);
         addChildAt(this._footer,_loc1_);
         addChildAt(this._header,_loc1_);
         registerFlashComponentS(this._header,Aliases.LOBBY_HEADER_OVERLAPPING);
         registerFlashComponentS(this._footer,Aliases.LOBBY_FOOTER_OVERLAPPING);
         this._headerOffset = this.getHeaderOffset();
         this._footerOffset = this.getFooterOffset();
         invalidateLayout();
      }
      
      private function removePanels() : void
      {
         if(this._header)
         {
            this._header.removeEventListener(Event.RESIZE,this.onHeaderResizeHandler);
            if(isFlashComponentRegisteredS(Aliases.LOBBY_HEADER_OVERLAPPING))
            {
               unregisterFlashComponentS(Aliases.LOBBY_HEADER_OVERLAPPING);
            }
            this._header = null;
         }
         if(this._footer)
         {
            this._footer.removeEventListener(Event.RESIZE,this.onFooterResizeHandler);
            if(isFlashComponentRegisteredS(Aliases.LOBBY_FOOTER_OVERLAPPING))
            {
               unregisterFlashComponentS(Aliases.LOBBY_FOOTER_OVERLAPPING);
            }
            this._footer = null;
         }
      }
      
      private function updateInnerLayersSize(param1:Number, param2:Number) : void
      {
         var _loc3_:ILobbyPageSubContainer = null;
         for each(_loc3_ in this.getSubContainers())
         {
            _loc3_.updateStage(param1,param2,new Rectangle(0,this._headerOffset,0,this._footerOffset));
         }
      }
      
      private function updateHeaderLayout() : void
      {
         var _loc1_:int = 0;
         if(this._header)
         {
            _loc1_ = this._header.width > 0 ? int(this._header.width) : int(width);
            this._header.scaleX = width / _loc1_;
         }
      }
      
      private function updateFooterLayout() : void
      {
         var _loc1_:int = 0;
         if(this._footer)
         {
            this._footer.y = height - this._footer.height;
            _loc1_ = this._header.width > 0 ? int(this._header.width) : int(width);
            this._footer.scaleX = width / _loc1_;
         }
      }
      
      private function getFooterOffset() : uint
      {
         return Boolean(this._footer) ? uint(this._footer.height - this._footer.hitRect.y) : uint(0);
      }
      
      private function getHeaderOffset() : uint
      {
         return Boolean(this._header) ? uint(this._header.hitRect.y + this._header.hitRect.height) : uint(TOP_SUB_VIEW_POSITION);
      }
      
      private function createHintTween(param1:Point, param2:DisplayObject) : Tween
      {
         return new Tween(TEASER_ANIM_SPEED_TIME,param2,{
            "x":param1.x,
            "y":param1.y,
            "scaleX":TEASER_ANIMATION_SCALE,
            "scaleY":TEASER_ANIMATION_SCALE,
            "alpha":TEASER_ANIMATION_ALPHA
         },{
            "paused":false,
            "onComplete":this.animationFinished,
            "ease":Quadratic.easeInOut
         });
      }
      
      private function animationFinished() : void
      {
         this._teaserOverlay.removeChild(this._teaser);
         this._teaser.bitmapData.dispose();
         this._teaser = null;
         this._teaserTween = null;
         this._teaserOverlay = null;
      }
      
      private function addSubContainer(param1:String, param2:int) : ILobbyPageSubContainer
      {
         var _loc3_:LobbyPageSubContainer = new LobbyPageSubContainer(param1);
         _loc3_.addEventListener(LobbyPageSubContainer.FRAMED_MODE_CHANGED,this.onSubContainerFramedModeChangedHandler,false,0,true);
         addChildAt(_loc3_,param2);
         return _loc3_;
      }
      
      private function registerDragging() : void
      {
         this.vehicleHitArea.hit.addEventListener(MouseEvent.MOUSE_WHEEL,this.onHitAreaMouseWheelHandler);
         App.cursor.registerDragging(this,Cursors.ROTATE);
      }
      
      private function unregisterDragging() : void
      {
         this.vehicleHitArea.hit.removeEventListener(MouseEvent.MOUSE_WHEEL,this.onHitAreaMouseWheelHandler);
         App.cursor.unRegisterDragging(this);
      }
      
      private function onSubContainerFramedModeChangedHandler(param1:Event) : void
      {
         var _loc4_:ILobbyPageSubContainer = null;
         var _loc2_:Array = this.getSubContainers();
         var _loc3_:Boolean = false;
         for each(_loc4_ in _loc2_)
         {
            if(_loc4_.isFramedMode)
            {
               _loc3_ = true;
               break;
            }
         }
         if(this._requiresFramedMode != _loc3_)
         {
            this._requiresFramedMode = _loc3_;
            setRequiresOldStyleS(this._requiresFramedMode);
            invalidateLayout();
         }
      }
      
      private function onHeaderResizeHandler(param1:Event) : void
      {
         this.updateHeaderLayout();
         var _loc2_:uint = this.getHeaderOffset();
         if(this._headerOffset == _loc2_)
         {
            return;
         }
         this._headerOffset = _loc2_;
         invalidateLayout();
      }
      
      private function onFooterResizeHandler(param1:Event) : void
      {
         this.updateFooterLayout();
         var _loc2_:uint = this.getFooterOffset();
         if(this._footerOffset == _loc2_)
         {
            return;
         }
         this._footerOffset = _loc2_;
         invalidateLayout();
      }
      
      private function onTeaserHideHandler(param1:TeaserEvent) : void
      {
         addChildAt(this._teaserOverlay = new Sprite(),getChildIndex(this._header) + 1);
         this._teaser = param1.teaser.drawToBitmap();
         var _loc2_:Point = new Point(this._teaser.x,this._teaser.y);
         _loc2_ = this._teaserOverlay.globalToLocal(_loc2_);
         this._teaser.x = _loc2_.x;
         this._teaser.y = _loc2_.y;
         this._teaserOverlay.addChild(this._teaser);
         if(this._header)
         {
            _loc2_.x = this._header.x + this._header.width >> 1;
            _loc2_.y = this._header.y + this._header.height >> 1;
            _loc2_ = this._header.localToGlobal(_loc2_);
         }
         _loc2_.offset(this._teaser.width * -TEASER_ANIMATION_SCALE >> 1,this._teaser.height * -TEASER_ANIMATION_SCALE >> 1);
         if(!this._teaserTween)
         {
            this._teaserTween = this.createHintTween(_loc2_,this._teaser);
         }
      }
      
      private function onVehicleHitAreaRollOverHandler(param1:MouseEvent) : void
      {
         notifyCursorOver3dSceneS(true);
      }
      
      private function onVehicleHitAreaRollOutHandler(param1:MouseEvent) : void
      {
         this._resetDragParams = true;
         notifyCursorOver3dSceneS(false);
      }
      
      private function onHitAreaMouseWheelHandler(param1:MouseEvent) : void
      {
         moveSpaceS(0,0,param1.delta * 200);
      }
      
      private function onRegisterDraggingHandler(param1:LobbyEvent) : void
      {
         this.registerDragging();
      }
      
      private function onUnregisterDraggingHandler(param1:LobbyEvent) : void
      {
         this.unregisterDragging();
      }
   }
}
