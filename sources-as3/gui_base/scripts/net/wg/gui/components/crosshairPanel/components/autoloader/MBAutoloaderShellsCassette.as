package net.wg.gui.components.crosshairPanel.components.autoloader
{
   import net.wg.data.constants.Values;
   
   public class MBAutoloaderShellsCassette extends AutoloaderShellsCassette
   {
       
      
      public function MBAutoloaderShellsCassette()
      {
         super();
      }
      
      override public function autoloadProgress(param1:Number, param2:Number, param3:Boolean, param4:Boolean, param5:Boolean = false) : void
      {
         super.autoloadProgress(param1,param2,param3,param4,true);
      }
      
      override public function reloadingPercent(param1:Number) : void
      {
         if(param1 != _currentReloadingPercent)
         {
            _currentReloadingPercent = param1;
            if(param1 < GUN_RELOADING_COMPLETE_STATE)
            {
               reloadingInProgress(param1);
            }
            else
            {
               reloadingComplete();
            }
         }
      }
      
      override protected function updateCurrentAmmoStates(param1:int) : void
      {
         var _loc2_:int = Values.DEFAULT_INT;
         if(_lastLoadedShell && _lastLoadedShell.currentLabel == SHELL_STATE_RELOADING)
         {
            _loc2_ = _lastLoadedShell.currentFrame;
         }
         super.updateCurrentAmmoStates(param1);
         var _loc3_:int = !!_isAnimationInProgress ? int(param1) : int(_currentAmmo);
         _lastLoadedShell = _shells[_loc3_];
         if(_loc2_ != Values.DEFAULT_INT && _lastLoadedShell.currentLabel == SHELL_STATE_CLEAR)
         {
            _lastLoadedShell.gotoAndStop(_loc2_);
         }
      }
   }
}
