package net.wg.gui.battle.eventBattle.views.loading.containers
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class LoadingContainer extends MovieClip implements IDisposable
   {
       
      
      public var gradientBg:MovieClip;
      
      private var _disposed:Boolean = false;
      
      public function LoadingContainer()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.gradientBg = null;
      }
      
      public function setWidth(param1:int) : void
      {
         this.gradientBg.width = param1;
         this.gradientBg.x = -param1 >> 1;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
