package net.wg.gui.components.crosshairPanel.components.shared
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class ShellProgressBar extends MovieClip implements IDisposable
   {
      
      public static const EMPTY_STATE:String = "empty";
      
      public static const READY_STATE:String = "ready";
      
      protected static const STATE_INSTANTLY_POSTFIX:String = "_instantly";
      
      private static const ACTIVE_MC_STATE_NORMAL:String = "normal";
      
      private static const ACTIVE_MC_STATE_CRITICAL:String = "critical";
      
      private static const PROGRESS_MC_FRAMES_COUNT:uint = 26;
       
      
      public var progressMC:MovieClip;
      
      public var activeMC:MovieClip;
      
      private var _state:String = "empty";
      
      private var _isCritical:Boolean = false;
      
      private var _baseDisposed:Boolean = false;
      
      public function ShellProgressBar()
      {
         super();
      }
      
      protected function onDispose() : void
      {
         this.progressMC = this.activeMC = null;
      }
      
      public final function dispose() : void
      {
         if(this._baseDisposed)
         {
            return;
         }
         this.onDispose();
         this._baseDisposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._baseDisposed;
      }
      
      public function setState(param1:String, param2:Boolean = false) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         if(param2)
         {
            this.gotoAndStop(param1 + STATE_INSTANTLY_POSTFIX);
         }
         else
         {
            this.gotoAndPlay(param1);
         }
      }
      
      public function set isCritical(param1:Boolean) : void
      {
         if(this._isCritical == param1)
         {
            return;
         }
         this._isCritical = param1;
         if(param1)
         {
            this.activeMC.gotoAndPlay(ACTIVE_MC_STATE_CRITICAL);
         }
         else
         {
            this.activeMC.gotoAndStop(ACTIVE_MC_STATE_NORMAL);
         }
      }
      
      public function set reloadingPercent(param1:Number) : void
      {
         this.progressMC.gotoAndStop(1 + param1 * PROGRESS_MC_FRAMES_COUNT | 0);
      }
   }
}
