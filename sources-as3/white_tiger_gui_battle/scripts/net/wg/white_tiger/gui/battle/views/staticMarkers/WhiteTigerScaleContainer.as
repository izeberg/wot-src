package net.wg.white_tiger.gui.battle.views.staticMarkers
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class WhiteTigerScaleContainer extends MovieClip implements IDisposable
   {
       
      
      public var content:WhiteTigerIndexedContent = null;
      
      private var _disposed:Boolean = false;
      
      public function WhiteTigerScaleContainer()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.content.dispose();
         this.content = null;
      }
      
      public function setScale(param1:Number) : void
      {
         this.content.scaleX = param1;
         this.content.scaleY = param1;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
