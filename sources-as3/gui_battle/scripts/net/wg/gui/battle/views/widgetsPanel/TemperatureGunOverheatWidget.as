package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BitmapData;
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.temperatureGun.TemperatureGunScaleCursor;
   import net.wg.gui.battle.views.widgetsPanel.temperatureGun.TemperatureGunScaleSector;
   import net.wg.infrastructure.base.meta.ITemperatureGunOverheatWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.TemperatureGunOverheatWidgetMeta;
   import net.wg.utils.IClassFactory;
   
   public class TemperatureGunOverheatWidget extends TemperatureGunOverheatWidgetMeta implements ITemperatureGunOverheatWidgetMeta
   {
      
      private static const SCALE_SECTOR_GAP:Number = 0.01;
      
      private static const WARN_HIGHLIGHT_SHOW_STATE:String = "show";
      
      private static const WARN_HIGHLIGHT_HIDE_STATE:String = "hide";
      
      private static const DEFAULT_COLOR_FRAME_LABEL:String = "normal";
      
      private static const COLOR_BLIND_FRAME_LABEL:String = "colorBlind";
      
      private static const WARN_PATH_BITMAP_LINKAGE:String = "TemperatureGunWarnPathUI";
      
      private static const WARN_HIGHLIGHT_BITMAP_LINKAGE:String = "TemperatureGunWarnHighlightUI";
      
      private static const HEAT_PROGRESS_BITMAP_LINKAGE:String = "TemperatureGunHeatProgressUI";
      
      private static const WARN_PROGRESS_BITMAP_LINKAGE:String = "TemperatureGunWarnProgressUI";
      
      private static const COOL_PROGRESS_BITMAP_LINKAGE:String = "TemperatureGunCoolProgressUI";
      
      private static const COOL_PROGRESS_ALT_BITMAP_LINKAGE:String = "TemperatureGunCoolProgressAltUI";
      
      private static const OVERHEAT_PROGRESS_BITMAP_LINKAGE:String = "TemperatureGunOverheatProgressUI";
      
      private static const OVERHEAT_PROGRESS_ALT_BITMAP_LINKAGE:String = "TemperatureGunOverheatProgressAltUI";
      
      private static const TEMPERATURE_INVALID:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
       
      
      public var overheatIcon:MovieClip;
      
      public var overheatScale:MovieClip;
      
      public var scaleCursor:TemperatureGunScaleCursor;
      
      public var warnPathSector:TemperatureGunScaleSector;
      
      public var warnPathEffectSector:TemperatureGunScaleSector;
      
      public var warnHighlightSector:TemperatureGunScaleSector;
      
      public var heatProgressSector:TemperatureGunScaleSector;
      
      public var warnProgressSector:TemperatureGunScaleSector;
      
      public var coolProgressSector:TemperatureGunScaleSector;
      
      public var overheatProgressSector:TemperatureGunScaleSector;
      
      public var overheatPathEffectSector1:TemperatureGunScaleSector;
      
      public var overheatPathEffectSector2:TemperatureGunScaleSector;
      
      private var _temperature:Number = 0;
      
      private var _warnThreshold:Number = 1;
      
      private var _overheatThreshold:Number = 0;
      
      private var _warnPathBitmap:BitmapData = null;
      
      private var _warnHighlightBitmap:BitmapData = null;
      
      private var _heatProgressBitmap:BitmapData = null;
      
      private var _warnProgressBitmap:BitmapData = null;
      
      private var _coolProgressBitmap:BitmapData = null;
      
      private var _coolProgressAltBitmap:BitmapData = null;
      
      private var _overheatProgressBitmap:BitmapData = null;
      
      private var _overheatProgressAltBitmap:BitmapData = null;
      
      public function TemperatureGunOverheatWidget()
      {
         super();
         this.blendMode = BlendMode.SCREEN;
         var _loc1_:IClassFactory = App.utils.classFactory;
         this._warnPathBitmap = _loc1_.getObject(WARN_PATH_BITMAP_LINKAGE) as BitmapData;
         this._warnHighlightBitmap = _loc1_.getObject(WARN_HIGHLIGHT_BITMAP_LINKAGE) as BitmapData;
         this._heatProgressBitmap = _loc1_.getObject(HEAT_PROGRESS_BITMAP_LINKAGE) as BitmapData;
         this._warnProgressBitmap = _loc1_.getObject(WARN_PROGRESS_BITMAP_LINKAGE) as BitmapData;
         this._coolProgressBitmap = _loc1_.getObject(COOL_PROGRESS_BITMAP_LINKAGE) as BitmapData;
         this._coolProgressAltBitmap = _loc1_.getObject(COOL_PROGRESS_ALT_BITMAP_LINKAGE) as BitmapData;
         this._overheatProgressBitmap = _loc1_.getObject(OVERHEAT_PROGRESS_BITMAP_LINKAGE) as BitmapData;
         this._overheatProgressAltBitmap = _loc1_.getObject(OVERHEAT_PROGRESS_ALT_BITMAP_LINKAGE) as BitmapData;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.warnPathSector.bitmapData = this.warnPathEffectSector.bitmapData = this._warnPathBitmap;
         this.warnHighlightSector.bitmapData = this._warnHighlightBitmap;
         this.heatProgressSector.bitmapData = this._heatProgressBitmap;
         this.warnProgressSector.bitmapData = this._warnProgressBitmap;
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            _loc1_ = !!isColorBlind ? COLOR_BLIND_FRAME_LABEL : DEFAULT_COLOR_FRAME_LABEL;
            timer.gotoAndStop(_loc1_);
            this.overheatIcon.gotoAndStop(_loc1_);
            this.overheatScale.gotoAndStop(_loc1_);
            this.coolProgressSector.bitmapData = !!isColorBlind ? this._coolProgressAltBitmap : this._coolProgressBitmap;
            this.overheatProgressSector.bitmapData = this.overheatPathEffectSector1.bitmapData = this.overheatPathEffectSector2.bitmapData = !!isColorBlind ? this._overheatProgressAltBitmap : this._overheatProgressBitmap;
         }
         if(isInvalid(TEMPERATURE_INVALID))
         {
            this.scaleCursor.progress = this._temperature;
            this.warnHighlightSector.state = this._temperature > this._warnThreshold ? WARN_HIGHLIGHT_SHOW_STATE : WARN_HIGHLIGHT_HIDE_STATE;
            this.heatProgressSector.maxThreshold = this._warnThreshold < 1 ? Number(this._warnThreshold - SCALE_SECTOR_GAP) : Number(this._warnThreshold);
            this.warnPathSector.minThreshold = this.warnPathEffectSector.minThreshold = this.warnProgressSector.minThreshold = this.warnHighlightSector.minThreshold = this._warnThreshold;
            this.coolProgressSector.maxThreshold = this._overheatThreshold;
            this.overheatProgressSector.minThreshold = this.overheatPathEffectSector1.minThreshold = this.overheatPathEffectSector2.minThreshold = this._overheatThreshold > 0 ? Number(this._overheatThreshold + SCALE_SECTOR_GAP) : Number(this._overheatThreshold);
            this.heatProgressSector.currProgress = this.warnProgressSector.currProgress = this.coolProgressSector.currProgress = this.overheatProgressSector.currProgress = this._temperature;
         }
      }
      
      override protected function onDispose() : void
      {
         this.overheatPathEffectSector2.dispose();
         this.overheatPathEffectSector2 = null;
         this.overheatPathEffectSector1.dispose();
         this.overheatPathEffectSector1 = null;
         this.overheatProgressSector.dispose();
         this.overheatProgressSector = null;
         this.coolProgressSector.dispose();
         this.coolProgressSector = null;
         this.warnProgressSector.dispose();
         this.warnProgressSector = null;
         this.heatProgressSector.dispose();
         this.heatProgressSector = null;
         this.warnHighlightSector.dispose();
         this.warnHighlightSector = null;
         this.warnPathEffectSector.dispose();
         this.warnPathEffectSector = null;
         this.warnPathSector.dispose();
         this.warnPathSector = null;
         this.scaleCursor.dispose();
         this.scaleCursor = null;
         this._overheatProgressAltBitmap.dispose();
         this._overheatProgressAltBitmap = null;
         this._overheatProgressBitmap.dispose();
         this._overheatProgressBitmap = null;
         this._coolProgressAltBitmap.dispose();
         this._coolProgressAltBitmap = null;
         this._coolProgressBitmap.dispose();
         this._coolProgressBitmap = null;
         this._warnProgressBitmap.dispose();
         this._warnProgressBitmap = null;
         this._heatProgressBitmap.dispose();
         this._heatProgressBitmap = null;
         this._warnHighlightBitmap.dispose();
         this._warnHighlightBitmap = null;
         this._warnPathBitmap.dispose();
         this._warnPathBitmap = null;
         this.overheatScale = null;
         this.overheatIcon = null;
         super.onDispose();
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
      
      public function as_setupThresholds(param1:Number, param2:Number) : void
      {
         if(param1 == this._warnThreshold && param2 == this._overheatThreshold)
         {
            return;
         }
         this._warnThreshold = param1;
         this._overheatThreshold = param2;
         invalidate(TEMPERATURE_INVALID);
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.DISABLE;
      }
   }
}
