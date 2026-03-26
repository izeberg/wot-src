package net.wg.gui.battle.views.widgetsPanel.propellantGun
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PropellantGunScaleCursor extends Sprite implements IDisposable
   {
      
      private static const PROGRESS_START_ANGLE:Number = -74.1;
      
      private static const PROGRESS_LENGTH_ANGLE:Number = -31.8;
       
      
      public var cursorMC:MovieClip;
      
      private var _isDisposed:Boolean = false;
      
      private var _progress:Number = 0;
      
      public function PropellantGunScaleCursor()
      {
         super();
         this.cursorMC.visible = false;
      }
      
      protected function onDispose() : void
      {
         this.cursorMC = null;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.onDispose();
         this._isDisposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function set cursorType(param1:String) : void
      {
         if(param1 == this.cursorMC.currentFrameLabel)
         {
            return;
         }
         this.cursorMC.gotoAndStop(param1);
      }
      
      public function set progress(param1:Number) : void
      {
         param1 = param1 < 0 ? Number(0) : (param1 > 1 ? Number(1) : Number(param1));
         if(param1 == this._progress)
         {
            return;
         }
         this._progress = param1;
         this.cursorMC.visible = param1 != 0;
         if(this.cursorMC.visible)
         {
            this.cursorMC.rotation = PROGRESS_START_ANGLE + param1 * PROGRESS_LENGTH_ANGLE;
         }
      }
   }
}
