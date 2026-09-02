package net.wg.gui.components.crosshairPanel
{
   import net.wg.gui.components.crosshairPanel.VO.GunMarkerIndicatorVO;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorStateParamsVO;
   import net.wg.infrastructure.interfaces.IDisplayObject;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public interface ICrosshair extends IDisposable, IDisplayObject
   {
       
      
      function setHealth(param1:Number) : void;
      
      function setDistance(param1:String) : void;
      
      function setAverageDamage(param1:String) : void;
      
      function clearAverageDamage(param1:Boolean) : void;
      
      function clearDistance(param1:Boolean) : void;
      
      function setDistanceVisibility(param1:Boolean) : void;
      
      function updateAmmoState(param1:String) : void;
      
      function setZoom(param1:String) : void;
      
      function setSize(param1:Number, param2:Number) : void;
      
      function updatePlayerInfo(param1:String) : void;
      
      function setAmmoStock(param1:uint, param2:Number, param3:String, param4:Boolean = false) : void;
      
      function setClipsParam(param1:Number, param2:Number, param3:int) : void;
      
      function setNetType(param1:Number) : void;
      
      function setCenterType(param1:Number) : void;
      
      function setComponentsAlpha(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : void;
      
      function setInfo(param1:Number, param2:String, param3:String, param4:Boolean, param5:Boolean, param6:String, param7:String, param8:Number, param9:Number, param10:int, param11:String, param12:uint, param13:Number, param14:String, param15:String, param16:uint, param17:Boolean = false, param18:Boolean = false, param19:Boolean = false, param20:Boolean = false, param21:Boolean = false, param22:Boolean = false) : void;
      
      function setReloadingState(param1:String) : void;
      
      function setReloadingAsPercent(param1:Number) : void;
      
      function setAutoloaderReloadingAsPercent(param1:Number) : void;
      
      function setExtraShotClipReloading(param1:String, param2:Number, param3:Boolean, param4:Boolean = false) : void;
      
      function setShellCalibrationClipReloading(param1:String, param2:Number, param3:Boolean = false) : void;
      
      function setShellCalibrationState(param1:uint) : void;
      
      function setReloadingTime(param1:Number) : void;
      
      function setQuickReloadingTime(param1:Boolean, param2:String) : void;
      
      function showReloadingTimeField(param1:Boolean) : void;
      
      function setVisibleNet(param1:int) : void;
      
      function setNetSeparatorVisible(param1:Boolean) : void;
      
      function autoloaderUpdate(param1:Number, param2:Number, param3:Boolean, param4:Boolean, param5:Boolean, param6:Boolean = false) : void;
      
      function setIsInControllableReload(param1:Boolean) : void;
      
      function autoloaderBoostUpdate(param1:BoostIndicatorStateParamsVO, param2:Number, param3:Boolean = false) : void;
      
      function autoloaderBoostUpdateAsPercent(param1:Number, param2:Number) : void;
      
      function showShot() : void;
      
      function updateScaleWidget(param1:Number) : void;
      
      function setGunMarkersData(param1:Vector.<GunMarkerIndicatorVO>, param2:Boolean) : void;
      
      function blinkReloadTime(param1:int) : void;
      
      function setReloadBoostBorderBlink() : void;
      
      function setReloadBoostBorderVisible(param1:Boolean, param2:Boolean, param3:Boolean) : void;
      
      function set reloadBoost(param1:Boolean) : void;
      
      function get autoloaderBoostParams() : BoostIndicatorStateParamsVO;
      
      function set isUseFrameAnimation(param1:Boolean) : void;
      
      function set scaleWidgetEnabled(param1:Boolean) : void;
      
      function set isUseAlternateZoomPosition(param1:Boolean) : void;
      
      function setNetSeparatorType(param1:String) : void;
      
      function setAutoreloaderSurgeState(param1:Boolean) : void;
   }
}
