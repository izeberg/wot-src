package net.wg.gui.components.crosshairPanel.components
{
   import flash.geom.Rectangle;
   import net.wg.data.constants.Errors;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorStateParamsVO;
   import net.wg.infrastructure.base.SimpleContainer;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class ClipQuantityIndicator extends SimpleContainer
   {
       
      
      public function ClipQuantityIndicator()
      {
         super();
      }
      
      public function setReloadingState(param1:String) : void
      {
         throw new AbstractException("setReloadingState" + Errors.ABSTRACT_INVOKE);
      }
      
      public function autoloaderBoostUpdate(param1:BoostIndicatorStateParamsVO, param2:Number, param3:Boolean = false) : void
      {
         throw new AbstractException("autoloaderBoostUpdate" + Errors.ABSTRACT_INVOKE);
      }
      
      public function autoloaderBoostUpdateAsPercent(param1:Number, param2:Number) : void
      {
         throw new AbstractException("autoloaderBoostUpdateAsPercent" + Errors.ABSTRACT_INVOKE);
      }
      
      public function autoloaderShowShot() : void
      {
         throw new AbstractException("autoloaderShowShot" + Errors.ABSTRACT_INVOKE);
      }
      
      public function autoloaderUpdate(param1:Number, param2:Number, param3:Boolean, param4:Boolean) : void
      {
         throw new AbstractException("autoloaderUpdate" + Errors.ABSTRACT_INVOKE);
      }
      
      public function getTimerRect() : Rectangle
      {
         return null;
      }
      
      public function setClipsParam(param1:Number, param2:Number, param3:int) : void
      {
         throw new AbstractException("setClipsParam" + Errors.ABSTRACT_INVOKE);
      }
      
      public function setGunReloadingPercent(param1:Number) : void
      {
         throw new AbstractException("setGunReloadingPercent" + Errors.ABSTRACT_INVOKE);
      }
      
      public function updateCritical(param1:Boolean) : void
      {
         throw new AbstractException("updateCritical" + Errors.ABSTRACT_INVOKE);
      }
      
      public function updateCurrentAmmo(param1:int) : void
      {
         throw new AbstractException("updateCurrentAmmo" + Errors.ABSTRACT_INVOKE);
      }
      
      public function updateInfo(param1:Number, param2:String, param3:Boolean) : void
      {
         throw new AbstractException("updateInfo" + Errors.ABSTRACT_INVOKE);
      }
      
      public function updateQuantityInClip(param1:int, param2:int) : void
      {
         throw new AbstractException("updateQuantityInClip" + Errors.ABSTRACT_INVOKE);
      }
      
      public function updateTotalAmmo(param1:int) : void
      {
         throw new AbstractException("updateTotalAmmo" + Errors.ABSTRACT_INVOKE);
      }
      
      public function get autoloaderBoostParams() : BoostIndicatorStateParamsVO
      {
         return null;
      }
   }
}
