package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BitmapData;
   import flash.display.BlendMode;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.temperatureGun.TemperatureGunScaleCursor;
   import net.wg.gui.battle.views.widgetsPanel.temperatureGun.TemperatureGunScaleSector;
   import net.wg.infrastructure.base.meta.ITemperatureGunHeatZonesWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.TemperatureGunHeatZonesWidgetMeta;
   import net.wg.utils.IClassFactory;
   
   public class TemperatureGunHeatZonesWidget extends TemperatureGunHeatZonesWidgetMeta implements ITemperatureGunHeatZonesWidgetMeta
   {
      
      private static const LOW_ZONE_INDEX:int = 0;
      
      private static const MEDIUM_ZONE_INDEX:int = 1;
      
      private static const HIGH_ZONE_INDEX:int = 2;
      
      private static const ZONE_SECTOR_GAP:Number = 0.015;
      
      private static const ZONE_HIGHLIGHT_SHOW_STATE:String = "show";
      
      private static const ZONE_HIGHLIGHT_HIDE_STATE:String = "hide";
      
      private static const ZONE_PATH_BITMAP_LINKAGE:String = "TemperatureGunZonePathUI";
      
      private static const LOW_ZONE_PROGRESS_1_BITMAP_LINKAGE:String = "TemperatureGunLowZoneProgress1UI";
      
      private static const LOW_ZONE_PROGRESS_2_BITMAP_LINKAGE:String = "TemperatureGunLowZoneProgress2UI";
      
      private static const LOW_ZONE_PROGRESS_3_BITMAP_LINKAGE:String = "TemperatureGunLowZoneProgress3UI";
      
      private static const MEDIUM_ZONE_PROGRESS_1_BITMAP_LINKAGE:String = "TemperatureGunMediumZoneProgress1UI";
      
      private static const MEDIUM_ZONE_PROGRESS_2_BITMAP_LINKAGE:String = "TemperatureGunMediumZoneProgress2UI";
      
      private static const HIGH_ZONE_PROGRESS_BITMAP_LINKAGE:String = "TemperatureGunHighZoneProgressUI";
      
      private static const MEDIUM_ZONE_HIGHLIGHT_BITMAP_LINKAGE:String = "TemperatureGunMediumZoneHighlightUI";
      
      private static const HIGH_ZONE_HIGHLIGHT_BITMAP_LINKAGE:String = "TemperatureGunHighZoneHighlightUI";
      
      private static const TEMPERATURE_INVALID:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
       
      
      public var scaleCursor:TemperatureGunScaleCursor;
      
      public var lowZonePathSector:TemperatureGunScaleSector;
      
      public var mediumZonePathSector:TemperatureGunScaleSector;
      
      public var highZonePathSector:TemperatureGunScaleSector;
      
      public var lowZoneProgressSector:TemperatureGunScaleSector;
      
      public var mediumZoneProgressSector:TemperatureGunScaleSector;
      
      public var highZoneProgressSector:TemperatureGunScaleSector;
      
      public var mediumZoneHighlightSector:TemperatureGunScaleSector;
      
      public var highZoneHighlightSector:TemperatureGunScaleSector;
      
      private var _temperature:Number = 0;
      
      private var _lowZoneMax:Number = 1;
      
      private var _mediumZoneMax:Number = 1;
      
      private var _zonePathBitmap:BitmapData = null;
      
      private var _lowZoneProgress1Bitmap:BitmapData = null;
      
      private var _lowZoneProgress2Bitmap:BitmapData = null;
      
      private var _lowZoneProgress3Bitmap:BitmapData = null;
      
      private var _mediumZoneProgress1Bitmap:BitmapData = null;
      
      private var _mediumZoneProgress2Bitmap:BitmapData = null;
      
      private var _highZoneProgressBitmap:BitmapData = null;
      
      private var _mediumZoneHighlightBitmap:BitmapData = null;
      
      private var _highZoneHighlightBitmap:BitmapData = null;
      
      public function TemperatureGunHeatZonesWidget()
      {
         super();
         this.blendMode = BlendMode.SCREEN;
         var _loc1_:IClassFactory = App.utils.classFactory;
         this._zonePathBitmap = _loc1_.getObject(ZONE_PATH_BITMAP_LINKAGE) as BitmapData;
         this._lowZoneProgress1Bitmap = _loc1_.getObject(LOW_ZONE_PROGRESS_1_BITMAP_LINKAGE) as BitmapData;
         this._lowZoneProgress2Bitmap = _loc1_.getObject(LOW_ZONE_PROGRESS_2_BITMAP_LINKAGE) as BitmapData;
         this._lowZoneProgress3Bitmap = _loc1_.getObject(LOW_ZONE_PROGRESS_3_BITMAP_LINKAGE) as BitmapData;
         this._mediumZoneProgress1Bitmap = _loc1_.getObject(MEDIUM_ZONE_PROGRESS_1_BITMAP_LINKAGE) as BitmapData;
         this._mediumZoneProgress2Bitmap = _loc1_.getObject(MEDIUM_ZONE_PROGRESS_2_BITMAP_LINKAGE) as BitmapData;
         this._highZoneProgressBitmap = _loc1_.getObject(HIGH_ZONE_PROGRESS_BITMAP_LINKAGE) as BitmapData;
         this._mediumZoneHighlightBitmap = _loc1_.getObject(MEDIUM_ZONE_HIGHLIGHT_BITMAP_LINKAGE) as BitmapData;
         this._highZoneHighlightBitmap = _loc1_.getObject(HIGH_ZONE_HIGHLIGHT_BITMAP_LINKAGE) as BitmapData;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.lowZonePathSector.bitmapData = this.mediumZonePathSector.bitmapData = this.highZonePathSector.bitmapData = this._zonePathBitmap;
         this.highZoneProgressSector.bitmapData = this._highZoneProgressBitmap;
         this.mediumZoneHighlightSector.bitmapData = this._mediumZoneHighlightBitmap;
         this.highZoneHighlightSector.bitmapData = this._highZoneHighlightBitmap;
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         super.draw();
         if(isInvalid(TEMPERATURE_INVALID))
         {
            _loc1_ = this._temperature <= this._mediumZoneMax ? (this._temperature <= this._lowZoneMax ? int(LOW_ZONE_INDEX) : int(MEDIUM_ZONE_INDEX)) : int(HIGH_ZONE_INDEX);
            this.scaleCursor.cursorType = _loc1_;
            switch(_loc1_)
            {
               case LOW_ZONE_INDEX:
                  this.lowZoneProgressSector.bitmapData = this._lowZoneProgress1Bitmap;
                  break;
               case MEDIUM_ZONE_INDEX:
                  this.lowZoneProgressSector.bitmapData = this._lowZoneProgress2Bitmap;
                  this.mediumZoneProgressSector.bitmapData = this._mediumZoneProgress1Bitmap;
                  break;
               case HIGH_ZONE_INDEX:
                  this.lowZoneProgressSector.bitmapData = this._lowZoneProgress3Bitmap;
                  this.mediumZoneProgressSector.bitmapData = this._mediumZoneProgress2Bitmap;
            }
            this.lowZonePathSector.maxThreshold = this.lowZoneProgressSector.maxThreshold = this._lowZoneMax;
            this.mediumZonePathSector.minThreshold = this.mediumZoneProgressSector.minThreshold = this.mediumZoneHighlightSector.minThreshold = this._lowZoneMax + ZONE_SECTOR_GAP;
            this.mediumZonePathSector.maxThreshold = this.mediumZoneProgressSector.maxThreshold = this.mediumZoneHighlightSector.maxThreshold = this._mediumZoneMax;
            this.highZonePathSector.minThreshold = this.highZoneProgressSector.minThreshold = this.highZoneHighlightSector.minThreshold = this._mediumZoneMax + ZONE_SECTOR_GAP;
            this.scaleCursor.progress = this.lowZoneProgressSector.currProgress = this.mediumZoneProgressSector.currProgress = this.highZoneProgressSector.currProgress = this._temperature;
            this.mediumZoneHighlightSector.state = _loc1_ == MEDIUM_ZONE_INDEX ? ZONE_HIGHLIGHT_SHOW_STATE : ZONE_HIGHLIGHT_HIDE_STATE;
            this.highZoneHighlightSector.state = _loc1_ == HIGH_ZONE_INDEX ? ZONE_HIGHLIGHT_SHOW_STATE : ZONE_HIGHLIGHT_HIDE_STATE;
         }
      }
      
      override protected function onDispose() : void
      {
         this.highZoneHighlightSector.dispose();
         this.highZoneHighlightSector = null;
         this.mediumZoneHighlightSector.dispose();
         this.mediumZoneHighlightSector = null;
         this.highZoneProgressSector.dispose();
         this.highZoneProgressSector = null;
         this.mediumZoneProgressSector.dispose();
         this.mediumZoneProgressSector = null;
         this.lowZoneProgressSector.dispose();
         this.lowZoneProgressSector = null;
         this.highZonePathSector.dispose();
         this.highZonePathSector = null;
         this.mediumZonePathSector.dispose();
         this.mediumZonePathSector = null;
         this.lowZonePathSector.dispose();
         this.lowZonePathSector = null;
         this.scaleCursor.dispose();
         this.scaleCursor = null;
         this._highZoneHighlightBitmap.dispose();
         this._highZoneHighlightBitmap = null;
         this._mediumZoneHighlightBitmap.dispose();
         this._mediumZoneHighlightBitmap = null;
         this._highZoneProgressBitmap.dispose();
         this._highZoneProgressBitmap = null;
         this._mediumZoneProgress2Bitmap.dispose();
         this._mediumZoneProgress2Bitmap = null;
         this._mediumZoneProgress1Bitmap.dispose();
         this._mediumZoneProgress1Bitmap = null;
         this._lowZoneProgress3Bitmap.dispose();
         this._lowZoneProgress3Bitmap = null;
         this._lowZoneProgress2Bitmap.dispose();
         this._lowZoneProgress2Bitmap = null;
         this._lowZoneProgress1Bitmap.dispose();
         this._lowZoneProgress1Bitmap = null;
         this._zonePathBitmap.dispose();
         this._zonePathBitmap = null;
         super.onDispose();
      }
      
      public function as_setHeatZonesValues(param1:Number, param2:Number) : void
      {
         if(param1 == this._lowZoneMax && param2 == this._mediumZoneMax)
         {
            return;
         }
         this._lowZoneMax = param1;
         this._mediumZoneMax = param2;
         invalidate(TEMPERATURE_INVALID);
      }
      
      public function as_setTemperature(param1:Number) : void
      {
         if(param1 == this._temperature)
         {
            return;
         }
         this._temperature = param1;
         invalidate(TEMPERATURE_INVALID);
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.DISABLE;
      }
   }
}
