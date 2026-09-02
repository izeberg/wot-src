package net.wg.gui.battle.views.minimap
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.gui.battle.views.minimap.containers.MinimapEntriesContainer;
   import net.wg.gui.battle.views.minimap.events.MinimapEvent;
   import net.wg.gui.battle.views.minimap.interfaces.IHoverableEntity;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.infrastructure.events.LifeCycleEvent;
   import scaleform.gfx.MouseEventEx;
   
   public class Minimap extends BaseMinimap
   {
      
      private static const OPTIMIZE_OFFSET:int = 10;
      
      private static const ANIM_FADE_IN:String = "fadeIn";
      
      private static const ANIM_FADE_OUT:String = "fadeOut";
      
      private static const NAME_CLICK_AREA:String = "clickAreaSpr";
       
      
      public var mapHit:Sprite = null;
      
      public var fakePixel:MovieClip = null;
      
      public var foreground0:BattleAtlasSprite = null;
      
      public var foreground1:BattleAtlasSprite = null;
      
      public var foreground2:BattleAtlasSprite = null;
      
      public var foreground3:BattleAtlasSprite = null;
      
      public var foreground4:BattleAtlasSprite = null;
      
      public var foreground5:BattleAtlasSprite = null;
      
      public var entriesContainerMask:Sprite = null;
      
      public var entriesContainer:MinimapEntriesContainer = null;
      
      public var background:UILoaderAlt = null;
      
      public var minimapHint:MinimapHint = null;
      
      private var _scenarioLayer:ScenarioLayer = null;
      
      private var _foregrounds:Vector.<Sprite> = null;
      
      private var _currForeground:Sprite = null;
      
      private var _currentSizeIndex:int = 0;
      
      private var _updateSizeIndexForce:Boolean = false;
      
      private var _clickAreaSpr:Sprite;
      
      private var _bIsHintPanelEnabled:Boolean = false;
      
      private var _containers:Vector.<Sprite> = null;
      
      private var _hoverableEntities:Vector.<IHoverableEntity> = null;
      
      private var _hoverableActive:Boolean = false;
      
      private var _hoveredEntity:IHoverableEntity = null;
      
      private var _lastContainerChildCount:int = -1;
      
      public function Minimap()
      {
         this._clickAreaSpr = new Sprite();
         super();
         this._foregrounds = new <Sprite>[this.foreground0,this.foreground1,this.foreground2,this.foreground3,this.foreground4,this.foreground5];
         this.foreground0.visible = this.foreground1.visible = this.foreground2.visible = this.foreground3.visible = this.foreground4.visible = this.foreground5.visible = false;
         this.foreground0.imageName = BATTLEATLAS.MINIMAP_B1;
         this.foreground1.imageName = BATTLEATLAS.MINIMAP_B2;
         this.foreground2.imageName = BATTLEATLAS.MINIMAP_B3;
         this.foreground3.imageName = BATTLEATLAS.MINIMAP_B4;
         this.foreground4.imageName = BATTLEATLAS.MINIMAP_B5;
         this.foreground5.imageName = BATTLEATLAS.MINIMAP_B6;
         this._currForeground = this.foreground0;
         this.entriesContainer.mask = this.entriesContainerMask;
         this._containers = new <Sprite>[this.entriesContainer.points,this.entriesContainer.icons,this.entriesContainer.equipments,this.entriesContainer.flags];
         this._hoverableEntities = new Vector.<IHoverableEntity>();
         this._clickAreaSpr.name = NAME_CLICK_AREA;
         addChildAt(this._clickAreaSpr,getChildIndex(this.mapHit));
         this.mapHit.visible = false;
         this._clickAreaSpr.hitArea = this.mapHit;
         removeChild(this.fakePixel);
         this.fakePixel = null;
         this.updateIntenalHintPanelData(false,false);
         this.minimapHint.gotoAndStop(ANIM_FADE_IN);
      }
      
      override public function as_clearScenarioEvent(param1:String) : void
      {
         this._scenarioLayer.clearScenarioEvent(param1);
      }
      
      override public function as_disableHintPanel() : void
      {
         this._bIsHintPanelEnabled = false;
         this.minimapHint.gotoAndPlay(ANIM_FADE_OUT);
      }
      
      override public function as_enableHintPanelWithData(param1:Boolean, param2:Boolean) : void
      {
         this.updateIntenalHintPanelData(param1,param2);
         this._bIsHintPanelEnabled = true;
         this.minimapHint.gotoAndPlay(ANIM_FADE_IN);
      }
      
      override public function as_initPrebattleSize(param1:int) : void
      {
         dispatchEvent(new MinimapEvent(MinimapEvent.TRY_INIT_PREBATTLE_SIZE,false,false,param1));
      }
      
      override public function as_setAlpha(param1:Number) : void
      {
         alpha = param1;
      }
      
      override public function as_setBackground(param1:String) : void
      {
         this.background.source = param1;
      }
      
      override public function as_setScenarioEvent(param1:String, param2:String, param3:String) : void
      {
         if(this._scenarioLayer == null)
         {
            this.createScenarioLayer();
         }
         this._scenarioLayer.setScenarioEvent(param1,param2,param3);
      }
      
      override public function as_setScenarioEventVisible(param1:String, param2:Boolean) : void
      {
         if(this._scenarioLayer != null)
         {
            this._scenarioLayer.setScenarioEventVisible(param1,param2);
         }
      }
      
      override public function as_setSize(param1:int) : void
      {
         if(initialized)
         {
            this.checkNewSize(param1);
         }
         else
         {
            this._currentSizeIndex = param1;
         }
      }
      
      override public function as_setVisible(param1:Boolean) : void
      {
         this.visible = param1;
         dispatchEvent(new MinimapEvent(MinimapEvent.VISIBILITY_CHANGED));
      }
      
      override public function as_updateHintPanelData(param1:Boolean, param2:Boolean) : void
      {
         this.updateIntenalHintPanelData(param1,param2);
      }
      
      override public function getMessageCoordinate() : Number
      {
         return initedHeight - this.currentTopLeftPoint.y + messageCoordinateOffset;
      }
      
      override public function getMinimapRectBySizeIndex(param1:int) : Rectangle
      {
         var _loc2_:int = this._currentSizeIndex;
         var _loc3_:Vector.<Rectangle> = MinimapSizeConst.MAP_SIZE;
         if(param1 >= 0 && param1 < _loc3_.length)
         {
            _loc2_ = param1;
         }
         return new Rectangle(0,0,initedWidth - _loc3_[_loc2_].x,initedHeight - _loc3_[_loc2_].y);
      }
      
      override public function getMinimapTotalWidthByIndex(param1:uint) : int
      {
         var _loc2_:Boolean = param1 >= this._foregrounds.length;
         if(_loc2_)
         {
            App.utils.asserter.assert(_loc2_,Errors.WRONG_VALUE + Values.SPACE_STR + param1);
            return 0;
         }
         return this._foregrounds[param1].width;
      }
      
      override public function getRectangles() : Vector.<Rectangle>
      {
         if(!visible)
         {
            return null;
         }
         var _loc1_:Rectangle = this._currForeground.getBounds(App.stage);
         _loc1_.x += OPTIMIZE_OFFSET;
         _loc1_.y += OPTIMIZE_OFFSET;
         _loc1_.width -= OPTIMIZE_OFFSET;
         _loc1_.height -= OPTIMIZE_OFFSET;
         return new <Rectangle>[_loc1_];
      }
      
      override public function setAllowedSizeIndex(param1:Number) : void
      {
         if(initialized && (this._currentSizeIndex != param1 || this._updateSizeIndexForce))
         {
            this._currentSizeIndex = param1;
            dispatchEvent(new MinimapEvent(MinimapEvent.SIZE_CHANGED));
            this.updateContent();
            dispatchEvent(new LifeCycleEvent(LifeCycleEvent.ON_GRAPHICS_RECTANGLES_UPDATE));
            applyNewSizeS(param1);
         }
         else
         {
            this._currentSizeIndex = param1;
         }
         this._updateSizeIndexForce = false;
      }
      
      override public function updateSizeIndex(param1:Boolean) : void
      {
         this._updateSizeIndexForce = param1;
         this.checkNewSize(this._currentSizeIndex);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.updateSizeIndex(true);
         this._clickAreaSpr.addEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         this._clickAreaSpr.addEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         this._clickAreaSpr.addEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
      }
      
      override protected function onDispose() : void
      {
         this.clearHoverableEntities();
         this._hoverableEntities = null;
         this._hoveredEntity = null;
         this._containers.length = 0;
         this._containers = null;
         this.foreground0 = null;
         this.foreground1 = null;
         this.foreground2 = null;
         this.foreground3 = null;
         this.foreground4 = null;
         this.foreground5 = null;
         this._currForeground = null;
         this.fakePixel = null;
         if(this._scenarioLayer)
         {
            this._scenarioLayer.dispose();
            this._scenarioLayer = null;
         }
         if(this._foregrounds)
         {
            this._foregrounds.fixed = false;
            this._foregrounds.splice(0,this._foregrounds.length);
            this._foregrounds = null;
         }
         this._clickAreaSpr.removeEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         this._clickAreaSpr.removeEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         this._clickAreaSpr.removeEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
         this._clickAreaSpr = null;
         this.entriesContainer.dispose();
         this.entriesContainer = null;
         this.entriesContainerMask = null;
         this.mapHit = null;
         this.background.dispose();
         this.background = null;
         this.minimapHint.stop();
         this.minimapHint.dispose();
         this.minimapHint = null;
         super.onDispose();
      }
      
      private function createScenarioLayer() : void
      {
         this._scenarioLayer = App.utils.classFactory.getComponent(Linkages.MINIMAP_SCENARIO_LAYOUT,ScenarioLayer);
         addChildAt(this._scenarioLayer,getChildIndex(this.background) + 1);
         this._scenarioLayer.x = this.background.x;
         this._scenarioLayer.y = this.background.y;
         this._scenarioLayer.updateSize(this.background.width,this.background.height);
      }
      
      private function updateContent() : void
      {
         this._currForeground.visible = false;
         this._currForeground = this._foregrounds[this._currentSizeIndex];
         this._currForeground.visible = true;
         this.updateContainersSize();
      }
      
      private function updateContainersSize() : void
      {
         var _loc1_:Rectangle = MinimapSizeConst.MAP_SIZE[this._currentSizeIndex];
         var _loc2_:int = _loc1_.width;
         var _loc3_:int = _loc1_.height;
         var _loc4_:int = _loc1_.x;
         var _loc5_:int = _loc1_.y;
         this.background.width = _loc2_;
         this.background.height = _loc3_;
         this.background.x = _loc4_;
         this.background.y = _loc5_;
         if(this._scenarioLayer)
         {
            this._scenarioLayer.x = _loc4_;
            this._scenarioLayer.y = _loc5_;
            this._scenarioLayer.updateSize(_loc2_,_loc3_);
         }
         var _loc6_:Point = MinimapSizeConst.ENTRY_CONTAINER_POINT[this._currentSizeIndex];
         this.entriesContainer.scaleX = this.background.scaleX;
         this.entriesContainer.scaleY = this.background.scaleY;
         MinimapEntryController.instance.updateScale(this._currentSizeIndex,this);
         this.entriesContainer.x = _loc6_.x;
         this.entriesContainer.y = _loc6_.y;
         this.entriesContainerMask.width = _loc2_;
         this.entriesContainerMask.height = _loc3_;
         this.entriesContainerMask.x = _loc6_.x;
         this.entriesContainerMask.y = _loc6_.y;
         this.mapHit.width = _loc2_;
         this.mapHit.height = _loc3_;
         this.mapHit.x = _loc4_;
         this.mapHit.y = _loc5_;
         this.minimapHint.x = _loc4_;
         this.minimapHint.y = _loc5_;
      }
      
      private function checkNewSize(param1:int) : void
      {
         dispatchEvent(new MinimapEvent(MinimapEvent.TRY_SIZE_CHANGED,false,false,param1));
      }
      
      private function updateIntenalHintPanelData(param1:Boolean, param2:Boolean) : void
      {
         this.minimapHint.setLeftMinimapHintIconType(MinimapIconCollection.ICON_ATTENTION);
         if(param2)
         {
            this.minimapHint.setRightMinimapHintIconType(MinimapIconCollection.ICON_REPOSITION_VIEW);
            if(param1)
            {
               this.minimapHint.setLeftMinimapHintIconType(MinimapIconCollection.ICON_SPG);
            }
            return;
         }
         this.minimapHint.setRightMinimapHintIconType(MinimapIconCollection.ICON_WAYPOINT);
      }
      
      private function quitHover(param1:Point) : void
      {
         if(this._hoveredEntity && !this._hoveredEntity.isDisposed())
         {
            this._hoveredEntity.onRollOut(param1);
            this._hoveredEntity = null;
         }
      }
      
      private function invalidateHoverableEntities() : void
      {
         var _loc2_:Sprite = null;
         var _loc5_:Sprite = null;
         var _loc6_:int = 0;
         var _loc1_:int = 0;
         for each(_loc2_ in this._containers)
         {
            _loc1_ += _loc2_.numChildren;
         }
         if(_loc1_ == this._lastContainerChildCount && this._hoverableEntities.length > 0)
         {
            return;
         }
         this._lastContainerChildCount = _loc1_;
         this.clearHoverableEntities();
         var _loc3_:IHoverableEntity = null;
         var _loc4_:int = Values.ZERO;
         for each(_loc5_ in this._containers)
         {
            _loc4_ = _loc5_.numChildren;
            _loc6_ = 0;
            while(_loc6_ < _loc4_)
            {
               _loc3_ = _loc5_.getChildAt(_loc6_) as IHoverableEntity;
               if(_loc3_)
               {
                  _loc3_.addEventListener(LifeCycleEvent.ON_DISPOSE,this.onEntityDisposeHandler);
                  this._hoverableEntities.push(_loc3_);
               }
               _loc6_++;
            }
         }
      }
      
      private function clearHoverableEntities() : void
      {
         var _loc1_:IHoverableEntity = null;
         for each(_loc1_ in this._hoverableEntities)
         {
            _loc1_.removeEventListener(LifeCycleEvent.ON_DISPOSE,this.onEntityDisposeHandler);
         }
         this._hoverableEntities.length = 0;
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(super.visible == param1)
         {
            return;
         }
         super.visible = param1;
         dispatchEvent(new LifeCycleEvent(LifeCycleEvent.ON_GRAPHICS_RECTANGLES_UPDATE));
      }
      
      override public function get currentTopLeftPoint() : Point
      {
         var _loc1_:Rectangle = MinimapSizeConst.MAP_SIZE[this._currentSizeIndex];
         return _loc1_.topLeft;
      }
      
      override public function get currentSizeIndex() : Number
      {
         return this._currentSizeIndex;
      }
      
      private function onMouseClickHandler(param1:MouseEvent) : void
      {
         var _loc2_:Point = null;
         if(param1 is MouseEventEx && param1.target == this._clickAreaSpr)
         {
            onMinimapClickedS(this.mapHit.mouseX,this.mapHit.mouseY,MouseEventEx(param1).buttonIdx,this._currentSizeIndex);
         }
         if(this._hoveredEntity != null)
         {
            _loc2_ = this.mapHit.localToGlobal(new Point(this.mapHit.mouseX,this.mapHit.mouseY));
            this._hoveredEntity.onClick(this._hoveredEntity.globalToLocal(_loc2_));
         }
      }
      
      private function onMouseOverHandler(param1:MouseEvent) : void
      {
         if(this._bIsHintPanelEnabled && param1 is MouseEventEx && param1.target == this._clickAreaSpr)
         {
            this.minimapHint.gotoAndPlay(ANIM_FADE_OUT);
         }
         this.invalidateHoverableEntities();
         this._hoverableActive = this._hoverableEntities.length > 0;
         this._clickAreaSpr.addEventListener(MouseEvent.MOUSE_MOVE,this.onMouseMoveHandler);
      }
      
      private function onMouseOutHandler(param1:MouseEvent) : void
      {
         if(this._bIsHintPanelEnabled && param1 is MouseEventEx && param1.target == this._clickAreaSpr)
         {
            this.minimapHint.gotoAndPlay(ANIM_FADE_IN);
         }
         this._hoverableActive = false;
         this._clickAreaSpr.removeEventListener(MouseEvent.MOUSE_MOVE,this.onMouseMoveHandler);
         this.quitHover(new Point(0,0));
      }
      
      private function onMouseMoveHandler(param1:MouseEvent) : void
      {
         var _loc4_:DisplayObject = null;
         var _loc5_:IHoverableEntity = null;
         if(!this._hoverableActive)
         {
            return;
         }
         var _loc2_:Point = this.mapHit.localToGlobal(new Point(this.mapHit.mouseX,this.mapHit.mouseY));
         _loc2_.x = _loc2_.x / App.appScale >> 0;
         _loc2_.y = _loc2_.y / App.appScale >> 0;
         var _loc3_:Boolean = false;
         for each(_loc5_ in this._hoverableEntities)
         {
            _loc4_ = _loc5_.hitTestTarget;
            if(_loc4_.hitTestPoint(_loc2_.x,_loc2_.y,false) && _loc4_.hitTestPoint(_loc2_.x,_loc2_.y,true))
            {
               if(this._hoveredEntity != _loc5_)
               {
                  if(this._hoveredEntity != null)
                  {
                     this._hoveredEntity.onRollOut(this._hoveredEntity.globalToLocal(_loc2_));
                  }
                  _loc5_.onRollOver(_loc5_.globalToLocal(_loc2_));
                  this._hoveredEntity = _loc5_;
               }
               _loc3_ = true;
               continue;
               _loc3_ = true;
               break;
            }
         }
         if(!_loc3_ && this._hoveredEntity)
         {
            this.quitHover(this._hoveredEntity.globalToLocal(_loc2_));
         }
      }
      
      private function onEntityDisposeHandler(param1:LifeCycleEvent) : void
      {
         var _loc2_:IHoverableEntity = param1.currentTarget as IHoverableEntity;
         var _loc3_:int = this._hoverableEntities.indexOf(_loc2_);
         if(_loc3_ > -1)
         {
            _loc2_.removeEventListener(LifeCycleEvent.ON_DISPOSE,this.onEntityDisposeHandler);
            this._hoverableEntities.splice(_loc3_,1);
            this._lastContainerChildCount = -1;
         }
      }
   }
}
