package net.wg.historical_battles.gui.battle.views.minimap
{
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import net.wg.gui.battle.epicBattle.VO.daapi.EpicPlayerStatsVO;
   import net.wg.gui.battle.epicBattle.VO.daapi.EpicVehiclesStatsVO;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.gui.battle.views.minimap.events.MinimapEvent;
   import net.wg.historical_battles.infrastructure.base.meta.IHBMinimapMeta;
   import net.wg.historical_battles.infrastructure.base.meta.impl.HBMinimapMeta;
   import net.wg.infrastructure.events.LifeCycleEvent;
   import net.wg.infrastructure.helpers.statisticsDataController.intarfaces.IEpicBattleStatisticDataController;
   import scaleform.gfx.MouseEventEx;
   
   public class HBMinimap extends HBMinimapMeta implements IEpicBattleStatisticDataController, IHBMinimapMeta
   {
      
      private static const MAP_OFFSET:Number = 0;
      
      private static const BORDER_OFFSET:int = 14;
      
      private static const SCALE_SIZES:Vector.<Number> = new <Number>[1,1.23,1.48,1.86,2.33,2.9,4.5];
      
      private static const MINIMAP_SCALE_SIZES:Vector.<Number> = new <Number>[212,262,312,392,492,622,945];
      
      private static const MINIMAP_MAX_SIZE_INDEX:uint = MINIMAP_SCALE_SIZES.length - 1;
      
      private static const FRAME_WIDTH_MULTIPLIER:int = 2;
      
      private static const FRAME_IMG_OFFSET:int = 24;
      
      private static const MMAP_BASE_SIZE:int = 210;
      
      private static const MESSAGE_COORDINATE_OFFSET:int = -8;
      
      public static const TAB_MODE_SMALL_SCREEN_SIZE_INDEX:int = MINIMAP_SCALE_SIZES.indexOf(492);
      
      public static const TAB_MODE_MEDIUM_SCREEN_SIZE_INDEX:int = MINIMAP_SCALE_SIZES.indexOf(622);
      
      public static const TAB_MODE_LARGE_SCREEN_SIZE_INDEX:int = MINIMAP_SCALE_SIZES.indexOf(945);
       
      
      private var _clickAreaSpr:Sprite = null;
      
      private var _updateSizeIndexForce:Boolean = false;
      
      private var _currentSizeIndex:int = 0;
      
      private var _mapWidth:int = 210;
      
      private var _mapHeight:int = 210;
      
      public function HBMinimap()
      {
         super();
         messageCoordinateOffset = MESSAGE_COORDINATE_OFFSET;
         background = entriesContainer.background;
         bgFrame.visible = false;
         fgFrame.visible = false;
         this._clickAreaSpr = new Sprite();
         addChildAt(this._clickAreaSpr,getChildIndex(mapHit));
         mapHit.visible = true;
         this._clickAreaSpr.hitArea = mapHit;
         mapZoomMode.visible = true;
         mapShortcutLabel.sectorOverview.visible = false;
      }
      
      override public function as_setBackground(param1:String) : void
      {
         background.setOriginalHeight(this._mapHeight);
         background.setOriginalWidth(this._mapWidth);
         background.maintainAspectRatio = false;
         background.source = param1;
      }
      
      override public function as_setMapDimensions(param1:int, param2:int) : void
      {
         this._mapWidth = param1;
         this._mapHeight = param2;
      }
      
      override public function as_setSize(param1:int) : void
      {
         if(!initialized)
         {
            this._currentSizeIndex = this.recalculateCurrentSizeIndexToLimits(param1);
         }
         else
         {
            this.checkNewSize(param1);
         }
      }
      
      override public function as_setZoomMode(param1:Number, param2:String) : void
      {
         mapZoomMode.mapZoomModeContainer.zoomLevelTF.text = param2;
         mapZoomMode.gotoAndPlay(2);
      }
      
      override public function as_updateSectorStateStats(param1:Object) : void
      {
      }
      
      override public function getMinimapRectBySizeIndex(param1:int) : Rectangle
      {
         var _loc2_:int = this._currentSizeIndex;
         if(param1 >= 0 && param1 < MinimapSizeConst.MAP_SIZE.length)
         {
            _loc2_ = param1;
         }
         return new Rectangle(0,0,MINIMAP_SCALE_SIZES[_loc2_],MINIMAP_SCALE_SIZES[_loc2_]);
      }
      
      override public function getRectangles() : Vector.<Rectangle>
      {
         if(!visible)
         {
            return null;
         }
         return new <Rectangle>[mapHit.getBounds(App.stage)];
      }
      
      override public function setAllowedSizeIndex(param1:Number) : void
      {
         if((this._currentSizeIndex != param1 || this._updateSizeIndexForce) && initialized)
         {
            this._currentSizeIndex = this.recalculateCurrentSizeIndexToLimits(param1);
            if(this._currentSizeIndex > MINIMAP_MAX_SIZE_INDEX)
            {
               this._currentSizeIndex = MINIMAP_MAX_SIZE_INDEX;
            }
            this.updateContainersSize();
            dispatchEvent(new MinimapEvent(MinimapEvent.SIZE_CHANGED));
            dispatchEvent(new LifeCycleEvent(LifeCycleEvent.ON_GRAPHICS_RECTANGLES_UPDATE));
            applyNewSizeS(param1);
         }
         else
         {
            this._currentSizeIndex = this.recalculateCurrentSizeIndexToLimits(param1);
         }
         this._updateSizeIndexForce = false;
      }
      
      override public function setEpicVehiclesStats(param1:EpicVehiclesStatsVO) : void
      {
      }
      
      override public function toggleTabMode(param1:Boolean) : void
      {
         super.toggleTabMode(param1);
         mapShortcutLabel.visible = !this.isTabMode;
      }
      
      override public function updateEpicPlayerStats(param1:EpicPlayerStatsVO) : void
      {
      }
      
      override public function updateEpicVehiclesStats(param1:EpicVehiclesStatsVO) : void
      {
      }
      
      override public function updateSizeIndex(param1:Boolean) : void
      {
         this._updateSizeIndexForce = param1;
         this.checkNewSize(this._currentSizeIndex);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.updateContainersSize();
         this._clickAreaSpr.addEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         mapShortcutLabel.mapBtnTF.text = READABLE_KEY_NAMES.KEY_M;
      }
      
      override protected function onDispose() : void
      {
         this._clickAreaSpr.removeEventListener(MouseEvent.CLICK,this.onMouseClickHandler);
         this._clickAreaSpr = null;
         super.onDispose();
      }
      
      public function as_setTabMode(param1:Boolean) : void
      {
         this.toggleTabMode(param1);
      }
      
      private function recalculateCurrentSizeIndexToLimits(param1:int) : uint
      {
         if(param1 > MINIMAP_MAX_SIZE_INDEX)
         {
            return MINIMAP_MAX_SIZE_INDEX;
         }
         if(param1 < MinimapSizeConst.MIN_SIZE_INDEX)
         {
            return MinimapSizeConst.MIN_SIZE_INDEX;
         }
         return param1;
      }
      
      private function updateContainersSize() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         _loc1_ = SCALE_SIZES[this._currentSizeIndex];
         entriesContainer.scaleX = entriesContainer.scaleY = _loc1_;
         _loc2_ = _loc1_ * MMAP_BASE_SIZE;
         var _loc3_:Number = _loc1_ * FRAME_WIDTH_MULTIPLIER;
         var _loc4_:Number = _loc2_ + FRAME_WIDTH_MULTIPLIER * FRAME_IMG_OFFSET;
         fgFrame.width = fgFrame.height = _loc4_;
         bgFrame.width = bgFrame.height = _loc4_ + _loc3_ * FRAME_WIDTH_MULTIPLIER;
         fgFrame.x = fgFrame.y = -FRAME_IMG_OFFSET;
         bgFrame.x = fgFrame.x - _loc3_ | 0;
         bgFrame.y = bgFrame.x;
         fgFrame.visible = true;
         mapShortcutLabel.x = -BORDER_OFFSET - _loc3_ | 0;
         mapHit.scaleX = mapHit.scaleY = _loc1_;
         mapZoomMode.y = -FRAME_IMG_OFFSET - _loc3_ | 0;
      }
      
      private function checkNewSize(param1:int) : void
      {
         dispatchEvent(new MinimapEvent(MinimapEvent.TRY_SIZE_CHANGED,false,false,param1));
         dispatchEvent(new LifeCycleEvent(LifeCycleEvent.ON_GRAPHICS_RECTANGLES_UPDATE));
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
      
      override public function get currentWidth() : int
      {
         return MINIMAP_SCALE_SIZES[this._currentSizeIndex];
      }
      
      override public function get currentHeight() : int
      {
         return MINIMAP_SCALE_SIZES[this._currentSizeIndex];
      }
      
      override public function get currentSizeIndex() : Number
      {
         return this._currentSizeIndex;
      }
      
      private function onMouseClickHandler(param1:MouseEvent) : void
      {
         if(param1 is MouseEventEx && param1.target == this._clickAreaSpr)
         {
            if(mapHit.mouseX < MAP_OFFSET || mapHit.mouseY < MAP_OFFSET || mapHit.mouseX > MAP_OFFSET + background.width || mapHit.mouseY > MAP_OFFSET + background.height)
            {
               return;
            }
            onMinimapClicked(mapHit.mouseX,mapHit.mouseY,MouseEventEx(param1).buttonIdx,this._currentSizeIndex);
         }
      }
   }
}
