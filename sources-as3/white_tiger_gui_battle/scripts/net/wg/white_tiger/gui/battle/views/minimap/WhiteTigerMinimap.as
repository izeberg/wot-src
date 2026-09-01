package net.wg.white_tiger.gui.battle.views.minimap
{
   import flash.filters.ColorMatrixFilter;
   import flash.geom.Rectangle;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.views.minimap.Minimap;
   import net.wg.gui.battle.views.minimap.events.MinimapEvent;
   import net.wg.infrastructure.events.LifeCycleEvent;
   
   public class WhiteTigerMinimap extends Minimap
   {
      
      private static const SATURATION_FILTER:Array = [new ColorMatrixFilter([0.3,0.6,0.3,0,0,0.3,0.6,0.3,0,0,0.3,0.6,0.6,0,0,0,0,0,1,0])];
      
      private static const MESSAGE_OFFSET_Y:int = 8;
       
      
      private var _isDeploymentMode:Boolean = false;
      
      private var _entriesContainer:WhiteTigerDeploymentMapEntriesContainer = null;
      
      private var _savedSizeIndex:int = 0;
      
      private var _savedEntriesContIndex:int = -1;
      
      public function WhiteTigerMinimap()
      {
         super();
         foreground0.imageName = BATTLEATLAS.WT_MINIMAP_B1;
         foreground1.imageName = BATTLEATLAS.WT_MINIMAP_B2;
         foreground2.imageName = BATTLEATLAS.WT_MINIMAP_B3;
         foreground3.imageName = BATTLEATLAS.WT_MINIMAP_B4;
         foreground4.imageName = BATTLEATLAS.WT_MINIMAP_B5;
         foreground5.imageName = BATTLEATLAS.WT_MINIMAP_B6;
         this._entriesContainer = WhiteTigerDeploymentMapEntriesContainer(entriesContainer);
         this._savedEntriesContIndex = getChildIndex(this._entriesContainer);
      }
      
      override protected function onDispose() : void
      {
         background.filters = null;
         super.onDispose();
         this._entriesContainer = null;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         background.filters = SATURATION_FILTER;
      }
      
      override public function getRectangles() : Vector.<Rectangle>
      {
         if(!visible || this._isDeploymentMode)
         {
            return null;
         }
         return new <Rectangle>[mapHit.getBounds(App.stage)];
      }
      
      public function set isDeploymentMode(param1:Boolean) : void
      {
         if(this._isDeploymentMode == param1)
         {
            return;
         }
         this._isDeploymentMode = param1;
         setChildIndex(this._entriesContainer,!!this._isDeploymentMode ? int(numChildren - 1) : int(this._savedEntriesContIndex));
         this._entriesContainer.isDeploymentMode = this._isDeploymentMode;
         if(param1)
         {
            this._savedSizeIndex = currentSizeIndex;
         }
         else
         {
            this.checkNewSize(this._savedSizeIndex);
         }
         updateSizeIndex(true);
      }
      
      private function checkNewSize(param1:int) : void
      {
         dispatchEvent(new MinimapEvent(MinimapEvent.TRY_SIZE_CHANGED,false,false,param1));
         dispatchEvent(new LifeCycleEvent(LifeCycleEvent.ON_GRAPHICS_RECTANGLES_UPDATE));
      }
      
      public function get isDeploymentMode() : Boolean
      {
         return this._isDeploymentMode;
      }
      
      override public function getMessageCoordinate() : Number
      {
         return super.getMessageCoordinate() + MESSAGE_OFFSET_Y;
      }
   }
}
