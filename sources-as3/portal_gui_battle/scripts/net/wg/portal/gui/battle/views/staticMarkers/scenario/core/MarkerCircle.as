package net.wg.portal.gui.battle.views.staticMarkers.scenario.core
{
   import flash.display.MovieClip;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.vehicleMarkers.IMarkerManagerHandler;
   import net.wg.gui.battle.views.vehicleMarkers.VehicleMarkersManager;
   import net.wg.gui.battle.views.vehicleMarkers.events.VehicleMarkersManagerEvent;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class MarkerCircle extends BattleUIComponent implements IMarkerManagerHandler
   {
      
      private static const INV_FRAME:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
       
      
      public var icon:MovieClip = null;
      
      public var highlight:MovieClip = null;
      
      private var _colorblindMode:Boolean = false;
      
      private var _vmManager:VehicleMarkersManager = null;
      
      private var _iconType:String = null;
      
      private var _iconTypeColorblind:String = null;
      
      private var _backIcon:String = null;
      
      public function MarkerCircle()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         this._vmManager = VehicleMarkersManager.getInstance();
         this._vmManager.addEventListener(VehicleMarkersManagerEvent.UPDATE_COLORS,this.onUpdateColorsHandler);
         this.updateColorBlind();
         this._vmManager.addReadyHandler(this);
         invalidate(INV_FRAME);
         super.initialize();
      }
      
      override protected function onDispose() : void
      {
         this._vmManager.removeEventListener(VehicleMarkersManagerEvent.UPDATE_COLORS,this.onUpdateColorsHandler);
         this._vmManager = null;
         this.icon.graphics.clear();
         this.icon = null;
         this.highlight.graphics.clear();
         this.highlight = null;
         super.onDispose();
      }
      
      public function managerReadyHandler() : void
      {
         this.drawIconType();
         this.drawBackIcon();
      }
      
      private function setColorBlindMode(param1:Boolean) : void
      {
         if(this._colorblindMode != param1)
         {
            this._colorblindMode = param1;
            invalidateState();
         }
      }
      
      private function updateColorBlind() : void
      {
         this.setColorBlindMode(this._vmManager.isColorBlind);
      }
      
      private function drawIconType() : void
      {
         var _loc1_:String = null;
         if(StringUtils.isEmpty(this._iconType))
         {
            return;
         }
         if(this._vmManager.isAtlasInited)
         {
            _loc1_ = this._iconType;
            if(this._colorblindMode && StringUtils.isNotEmpty(this._iconTypeColorblind))
            {
               _loc1_ = this._iconTypeColorblind;
            }
            this.icon.graphics.clear();
            this._vmManager.drawWithCenterAlign(_loc1_,this.icon.graphics,true,true);
         }
      }
      
      private function drawBackIcon() : void
      {
         if(StringUtils.isEmpty(this._backIcon))
         {
            return;
         }
         this.highlight.graphics.clear();
         if(this._vmManager.isAtlasInited)
         {
            this._vmManager.drawWithCenterAlign(this._backIcon,this.highlight.graphics,true,true);
         }
      }
      
      public function set iconType(param1:String) : void
      {
         this._iconType = param1;
         this.drawIconType();
      }
      
      public function set iconTypeColorblind(param1:String) : void
      {
         this._iconTypeColorblind = param1;
         this.drawIconType();
      }
      
      public function set backIcon(param1:String) : void
      {
         this._backIcon = param1;
         this.drawBackIcon();
      }
      
      private function onUpdateColorsHandler(param1:VehicleMarkersManagerEvent) : void
      {
         this.updateColorBlind();
      }
   }
}
