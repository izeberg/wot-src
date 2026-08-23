package net.wg.gui.battle.views.widgetsPanel.autoreloaderSurge
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class AutoreloaderSurgeSector extends MovieClip implements IDisposable
   {
      
      private static const TOTAL_FRAMES:Number = 150;
      
      private static const LABEL_ACTIVE:String = "active";
      
      private static const LABEL_SHOW:String = "show";
      
      private static const LABEL_HIDE:String = "hide";
      
      private static const LABEL_COOLDOWN:String = "cooldown";
      
      private static const LABEL_RECHARGE:String = "recharge";
       
      
      public var reload:MovieClip = null;
      
      public var activation:MovieClip = null;
      
      public var progress:MovieClip = null;
      
      private var _disposed:Boolean = false;
      
      private var _reloadShown:Boolean = false;
      
      public function AutoreloaderSurgeSector()
      {
         super();
      }
      
      public function setProgress(param1:Number) : void
      {
         this.progress.gotoAndStop(param1 * TOTAL_FRAMES);
      }
      
      public function playActivation() : void
      {
         this.activation.gotoAndPlay(LABEL_ACTIVE);
      }
      
      public function setCharging(param1:Boolean) : void
      {
         if(param1 && !this._reloadShown)
         {
            this._reloadShown = true;
            this.reload.gotoAndPlay(LABEL_SHOW);
         }
         else if(!param1 && this._reloadShown)
         {
            this._reloadShown = false;
            this.reload.gotoAndPlay(LABEL_HIDE);
         }
      }
      
      public function playCooldown() : void
      {
         gotoAndPlay(LABEL_COOLDOWN);
      }
      
      public function playRecharge() : void
      {
         gotoAndPlay(LABEL_RECHARGE);
      }
      
      public function dispose() : void
      {
         this._disposed = true;
         this.reload = null;
         this.progress = null;
         this.activation = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
