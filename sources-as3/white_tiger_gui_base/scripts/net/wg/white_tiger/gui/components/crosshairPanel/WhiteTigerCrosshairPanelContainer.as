package net.wg.white_tiger.gui.components.crosshairPanel
{
   import flash.display.DisplayObject;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.crosshairPanel.ICrosshair;
   import net.wg.gui.components.crosshairPanel.VO.CrosshairSettingsVO;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WhiteTigerCrosshairPanelContainerMeta;
   
   public class WhiteTigerCrosshairPanelContainer extends WhiteTigerCrosshairPanelContainerMeta
   {
      
      private static const EXPLOSIVE_SHOT_MARKER_TYPE:Number = 6;
       
      
      private var _gunMarkerSettings:CrosshairSettingsVO;
      
      public function WhiteTigerCrosshairPanelContainer()
      {
         super();
      }
      
      override protected function initCrosshairs() : void
      {
         var _loc1_:Object = null;
         var _loc2_:String = null;
         var _loc3_:Boolean = false;
         crosshairs = new Vector.<ICrosshair>(0);
         for each(_loc2_ in CROSSHAIRS_LINAKGES)
         {
            _loc3_ = _loc2_ == Linkages.CROSSHAIR_ARCADE_UI || _loc2_ == Linkages.CROSSHAIR_SNIPER_UI;
            _loc1_ = !!_loc3_ ? IWhiteTigerCrosshair(createComponent(_loc2_)) : ICrosshair(createComponent(_loc2_));
            crosshairs.push(_loc1_ as ICrosshair);
            addChild(DisplayObject(_loc1_));
         }
         currentCrosshair = crosshairs[0];
      }
      
      override public function as_setSettings(param1:Object) : void
      {
         super.as_setSettings(param1);
         this._gunMarkerSettings = gunMarkersContainer.markerSettings;
      }
      
      public function as_showPlasmaIndicator(param1:Number, param2:Boolean, param3:String) : void
      {
         var _loc4_:IWhiteTigerCrosshair = null;
         if(currentCrosshair is IWhiteTigerCrosshair)
         {
            _loc4_ = currentCrosshair as IWhiteTigerCrosshair;
            _loc4_.showPlasmaIndicator(param1,param2,param3);
         }
      }
      
      public function as_showExplosiveShotIndicator(param1:Boolean) : void
      {
         var _loc2_:IWhiteTigerCrosshair = null;
         if(param1)
         {
            gunMarkersContainer.updateSettings(new CrosshairSettingsVO({
               "gunTagType":this._gunMarkerSettings.gunTagType,
               "gunTagAlpha":this._gunMarkerSettings.gunTagAlpha,
               "mixingType":EXPLOSIVE_SHOT_MARKER_TYPE,
               "mixingAlpha":this._gunMarkerSettings.mixingAlpha
            }));
         }
         else
         {
            gunMarkersContainer.updateSettings(this._gunMarkerSettings);
         }
         if(currentCrosshair is IWhiteTigerCrosshair)
         {
            _loc2_ = currentCrosshair as IWhiteTigerCrosshair;
            _loc2_.setExplosiveShotVisible(param1);
         }
      }
   }
}
