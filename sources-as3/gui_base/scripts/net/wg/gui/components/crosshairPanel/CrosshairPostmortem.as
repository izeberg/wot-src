package net.wg.gui.components.crosshairPanel
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.components.crosshairPanel.VO.GunMarkerIndicatorVO;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorStateParamsVO;
   
   public class CrosshairPostmortem extends MovieClip implements ICrosshair
   {
       
      
      public var ammoInfo:TextField = null;
      
      private var _strAmmoState:String = "";
      
      private var _disposed:Boolean = false;
      
      public function CrosshairPostmortem()
      {
         super();
      }
      
      public function set reloadBoost(param1:Boolean) : void
      {
      }
      
      public function autoloaderBoostUpdate(param1:BoostIndicatorStateParamsVO, param2:Number, param3:Boolean = false) : void
      {
      }
      
      public function autoloaderBoostUpdateAsPercent(param1:Number, param2:Number) : void
      {
      }
      
      public function autoloaderUpdate(param1:Number, param2:Number, param3:Boolean, param4:Boolean, param5:Boolean, param6:Boolean = false) : void
      {
      }
      
      public function blinkReloadTime(param1:int) : void
      {
      }
      
      public function clearAverageDamage(param1:Boolean) : void
      {
      }
      
      public function clearDistance(param1:Boolean) : void
      {
      }
      
      public function dispose() : void
      {
         this._disposed = true;
         this.ammoInfo = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setAmmoStock(param1:uint, param2:Number, param3:String, param4:Boolean = false) : void
      {
      }
      
      public function setAutoloaderReloadingAsPercent(param1:Number) : void
      {
      }
      
      public function setAverageDamage(param1:String) : void
      {
      }
      
      public function setCenterType(param1:Number) : void
      {
      }
      
      public function setClipsParam(param1:Number, param2:Number, param3:int) : void
      {
      }
      
      public function setComponentsAlpha(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : void
      {
      }
      
      public function setDistance(param1:String) : void
      {
      }
      
      public function setDistanceVisibility(param1:Boolean) : void
      {
      }
      
      public function setExtraShotClipReloading(param1:String, param2:Number, param3:Boolean, param4:Boolean = false) : void
      {
      }
      
      public function setShellCalibrationClipReloading(param1:String, param2:Number, param3:Boolean = false) : void
      {
      }
      
      public function setShellCalibrationState(param1:uint) : void
      {
      }
      
      public function setGunMarkersData(param1:Vector.<GunMarkerIndicatorVO>, param2:Boolean) : void
      {
      }
      
      public function setHealth(param1:Number) : void
      {
      }
      
      public function setInfo(param1:Number, param2:String, param3:String, param4:Boolean, param5:Boolean, param6:String, param7:String, param8:Number, param9:Number, param10:int, param11:String, param12:uint, param13:Number, param14:String, param15:String, param16:uint, param17:Boolean = false, param18:Boolean = false, param19:Boolean = false, param20:Boolean = false, param21:Boolean = false, param22:Boolean = false) : void
      {
         this.updatePlayerInfo(param7);
         this.updateAmmoState(param11);
      }
      
      public function setIsInControllableReload(param1:Boolean) : void
      {
      }
      
      public function setNetSeparatorType(param1:String) : void
      {
      }
      
      public function setAutoreloaderSurgeState(param1:Boolean) : void
      {
      }
      
      public function setNetSeparatorVisible(param1:Boolean) : void
      {
      }
      
      public function setNetType(param1:Number) : void
      {
      }
      
      public function setQuickReloadingTime(param1:Boolean, param2:String) : void
      {
      }
      
      public function setReloadingAsPercent(param1:Number) : void
      {
      }
      
      public function setReloadingState(param1:String) : void
      {
      }
      
      public function setReloadingTime(param1:Number) : void
      {
      }
      
      public function setVisibleNet(param1:int) : void
      {
      }
      
      public function setZoom(param1:String) : void
      {
      }
      
      public function showReloadingTimeField(param1:Boolean) : void
      {
      }
      
      public function showShot() : void
      {
      }
      
      public function updateAmmoState(param1:String) : void
      {
         if(this._strAmmoState != param1)
         {
            this._strAmmoState = param1;
            this.ammoInfo.text = this._strAmmoState;
         }
      }
      
      public function updatePlayerInfo(param1:String) : void
      {
      }
      
      public function updateScaleWidget(param1:Number) : void
      {
      }
      
      public function set isUseFrameAnimation(param1:Boolean) : void
      {
      }
      
      public function set isUseAlternateZoomPosition(param1:Boolean) : void
      {
      }
      
      public function get autoloaderBoostParams() : BoostIndicatorStateParamsVO
      {
         return null;
      }
      
      public function set scaleWidgetEnabled(param1:Boolean) : void
      {
      }
      
      public function setSize(param1:Number, param2:Number) : void
      {
      }
      
      public function setReloadBoostBorderBlink() : void
      {
      }
      
      public function setReloadBoostBorderVisible(param1:Boolean, param2:Boolean, param3:Boolean) : void
      {
      }
   }
}
