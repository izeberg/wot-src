package net.wg.gui.components.crosshairPanel.components.controllableLoader
{
   import flash.display.MovieClip;
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   
   public class ControllableReloadShellProgressBar extends ShellProgressBar
   {
      
      private static const RELOAD_COMPLETE_PERCENT:Number = 1;
       
      
      public var reloadCompleteMC:MovieClip;
      
      private var _isReloaded:Boolean = false;
      
      public function ControllableReloadShellProgressBar()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.reloadCompleteMC = null;
         super.onDispose();
      }
      
      public function setReloading(param1:Number, param2:Boolean = false) : void
      {
         this.reloadingPercent = param1;
         var _loc3_:Boolean = param1 == RELOAD_COMPLETE_PERCENT;
         if(_loc3_ == this._isReloaded)
         {
            return;
         }
         this._isReloaded = _loc3_;
         if(_loc3_ && !param2)
         {
            this.reloadCompleteMC.play();
         }
      }
   }
}
