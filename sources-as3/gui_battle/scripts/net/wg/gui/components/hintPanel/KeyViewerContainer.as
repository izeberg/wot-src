package net.wg.gui.components.hintPanel
{
   import flash.display.Sprite;
   import net.wg.gui.battle.windows.vo.IngameDetailsKeyVO;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class KeyViewerContainer extends Sprite implements IDisposable
   {
       
      
      public var keyViewer:KeyViewer = null;
      
      private var _disposed:Boolean = false;
      
      public function KeyViewerContainer()
      {
         super();
         this.keyViewer.cacheAsBitmap = true;
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.keyViewer.dispose();
         this.keyViewer = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setKey(param1:IngameDetailsKeyVO) : void
      {
         this.keyViewer.setKey(param1);
         this.keyViewer.x = -(this.keyViewer.width >> 1);
         this.keyViewer.y = -(this.keyViewer.height >> 1);
      }
   }
}
