package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PenetrationFX extends MovieClip implements IDisposable
   {
      
      private static const FRAME_LABEL_PENETRATE_FX:String = "penetrateFX";
       
      
      private var _disposed:Boolean = false;
      
      public function PenetrationFX()
      {
         super();
      }
      
      public final function dispose() : void
      {
         stop();
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function showPenetrationFX() : void
      {
         gotoAndPlay(FRAME_LABEL_PENETRATE_FX);
      }
   }
}
